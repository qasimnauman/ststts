from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from whisper_engine import transcribe_audio
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import logging
from flask_cors import CORS


app = Flask(__name__)

CORS(app) 

# === Config ===
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024  # 20MB limit
ALLOWED_EXTENSIONS = {"wav", "mp3", "m4a", "ogg", "flac"}

# === Make upload folder ===
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# === Rate limiter ===
limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])

# === Logging ===
logging.basicConfig(level=logging.INFO)

# === File type check ===
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/transcribe", methods=["POST"])
@limiter.limit("5 per minute")  # Apply stricter limit to this route if needed
def transcribe():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']

    if audio_file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(audio_file.filename):
        return jsonify({"error": "Unsupported file type"}), 400

    # Save the file securely
    filename = secure_filename(audio_file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    audio_file.save(file_path)

    try:
        with open(file_path, "rb") as f:
            transcription = transcribe_audio(f)
        os.remove(file_path)  # Clean up after processing
        return jsonify({"transcription": transcription})
    except Exception as e:
        logging.exception("Transcription failed.")
        return jsonify({"error": "Transcription failed", "details": str(e)}), 500

# === Run app ===
if __name__ == "__main__":
    app.run(debug=True, port=5000)
