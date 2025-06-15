import requests

# URL of your running STT Flask API
API_URL = "http://127.0.0.1:5001/transcribe"  # Change port if needed

# Path to the audio file you want to transcribe
AUDIO_FILE_PATH = "response_audio.wav"  # Replace with your actual file

# Open the audio file in binary mode
with open(AUDIO_FILE_PATH, "rb") as audio_file:
    files = {"audio": audio_file}
    response = requests.post(API_URL, files=files)

# Handle response
if response.status_code == 200:
    transcription = response.json().get("transcription", "")
    print("✅ Transcription:", transcription)
else:
    try:
        print("❌ Error:", response.json())
    except Exception:
        print("❌ Unexpected error:", response.text)
