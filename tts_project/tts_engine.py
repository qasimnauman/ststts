import os
import uuid
from TTS.api import TTS
from torch import cuda


use_gpu = cuda.is_available()
tts_model = TTS(model_name="tts_models/en/vctk/vits", gpu=use_gpu)

# Map human-friendly names to speaker IDs
speaker_map = {
    "lisa": "p284",
    "bob": "p230",
    "charlie": "p238",
    "ginny": "p240",
    "eva": "p245",
    "emily": "p263",
    "mark": "p254",
    "susan": "p345",
    "mike": "p254",
}

# Determine base path relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def synthesize_speech(text, speaker_name, output_path=None):
    if output_path is None:
        unique_id = str(uuid.uuid4())
        output_path = os.path.join(OUTPUT_DIR, f"{unique_id}.wav")

    speaker_id = speaker_map.get(speaker_name.lower())
    if not speaker_id:
        raise ValueError(f"Unknown speaker name '{speaker_name}'. Choose from {list(speaker_map.keys())}.")

    tts_model.tts_to_file(
        text=text,
        speaker=speaker_id,
        file_path=output_path
    )
    return output_path
