import os
from flask import Flask, request, send_file, jsonify, after_this_request
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.exceptions import RequestEntityTooLarge

from tts_engine import synthesize_speech, speaker_map

app = Flask(__name__)

# Enable CORS
CORS(app)

limiter = Limiter(key_func=get_remote_address, default_limits=["20 per minute"])
limiter.init_app(app)

@app.errorhandler(RequestEntityTooLarge)
def handle_large_request(e):
    return jsonify({"error": "Request size too large. Max 5MB allowed."}), 413

@app.route('/api/speak', methods=['POST'])
@limiter.limit("10 per minute")  # Optional: set tighter limit for this endpoint
def speak():
    data = request.get_json()

    if not data or 'text' not in data or 'speaker' not in data:
        return jsonify({
            "error": "Request must include 'text' and 'speaker'"
        }), 400

    text = data['text']
    speaker = data['speaker']

    try:
        output_path = synthesize_speech(text, speaker)

        @after_this_request
        def remove_file(response):
            try:
                os.remove(output_path)
                app.logger.debug(f"Deleted temporary file: {output_path}")
            except Exception as e:
                app.logger.error(f"Error deleting file {output_path}: {e}")
            return response

        return send_file(output_path, mimetype='audio/wav', as_attachment=True)

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "TTS processing failed", "details": str(e)}), 500

@app.route('/api/speakers', methods=['GET'])
def list_speakers():
    return jsonify({"available_speakers": list(speaker_map.keys())})

if __name__ == '__main__':
    app.run(debug=True)
