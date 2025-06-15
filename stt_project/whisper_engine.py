import whisper
import os
import tempfile
import ssl
import torch

ssl._create_default_https_context = ssl._create_unverified_context

# Automatically use GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("medium.en").to(device)

def transcribe_audio(audio_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
            temp.write(audio_file.read())
            temp_path = temp.name

        result = model.transcribe(temp_path, fp16=(device=="cuda"))
        os.remove(temp_path)
        return result["text"]
    except Exception as e:
        return f"Error during transcription: {str(e)}"
