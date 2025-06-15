# 🗣️ Flask Text-to-Speech API

This project provides a simple Flask API for **text-to-speech** synthesis using the Coqui TTS model.

---

## 🚀 Features

- Converts any text input into natural-sounding speech.
- Supports multiple speaker voices.
- Returns audio as a downloadable `.wav` file.
- Model is loaded only **once** at server start for efficiency.

---

## 🧠 How It Works

- The TTS model is loaded globally when the server starts.
- A client sends a POST request with:
  - A `text` string to synthesize.
  - A `speaker` name to select the voice.
- The API generates speech and returns it as `output.wav`.

---

## 🗣️ Available Speakers

You can use any of these speaker names in your request:

```json
{
  "Lisa": "p284",
  "bob": "p230",
  "charlie": "p238",
  "Ginny": "p240",
  "eva": "p245",
  "emily": "p263",
  "mark": "p254",
  "susan": "p345",
  "mike": "p254"
}

----------------- Steps to run ------------------

1. Create and Activate a Virtual Environment

create environment: python3 -m venv ttsvenv
activate environment on mac : source ttsvenv/bin/activate  
activate environment On Windows: ttsvenv\Scripts\activate


2. Install Dependencies

pip install -r requirements.txt


3. Install espeak / espeak-ng (Required by Coqui TTS)


Ubuntu / Debian  :  sudo apt install espeak

macOS (using Homebrew) : brew install espeak

Windows : Download and install from: https://espeak.sourceforge.net/


4. Run the API (Two Options)

🔧 Option 1: Development Mode (for testing/debugging)


Run with Flask's built-in development server: python app.py


Best for quick local testing.

Automatically reloads on code changes.

Not recommended for production — slower and not secure for real users.

🚀 Option 2: Production Mode (Recommended)
Run with Gunicorn — a robust WSGI server:


gunicorn -w 4 -b 0.0.0.0:5000 app:app


-w 4 starts 4 worker processes (you can adjust this based on CPU cores).

Much faster and stable for production or heavy usage.

No automatic reloading; restart manually if code changes.

5. First-Time Note
⚠️ On first run, the Coqui TTS model will be downloaded locally, which may take a few minutes.
After that, it will be cached and loaded automatically on future runs for faster performance.

6. Try a Demo
Run the included test script to see how it works:

python test.py

This sends a request to the API and saves the generated output (e.g., output.wav).





---------- Installation ---------

---- Requirements

  - Python 3.8+

  - espeak or espeak-ng (required by Coqui TTS)

  - Recommended: CUDA-compatible GPU for faster processing

---


--------- API Endpoints ----------

  🎤 POST /api/speak
  Request Body (JSON):
  {
    "text": "Hello, this is a test.",
    "speaker": "Lisa"
  }
  Response:

  Returns: audio/wav file (Content-Disposition: attachment)

  Status: 200 OK on success

  Status: 400 or 500 on error

  

  📢 GET /api/speakers
  Response (JSON):
  {
    "available_speakers": [
      "Lisa", "bob", "charlie", "Ginny",
      "eva", "emily", "mark", "susan", "mike"
    ]
  }



---------- Production Deployment ----------
Use Gunicorn to serve the app for production:


gunicorn -w 4 -b 0.0.0.0:5000 app:app    #Run server using this command


-w 4 starts 4 worker processes. Adjust based on your CPU cores.



✅ Notes

-    You must install espeak or espeak-ng on your system for the model to run properly.

-    The first time you run the API, it will download the speech recognition model locally. This  may take some time. After that, the model will be cached and loaded instantly on subsequent runs.

-    A sample usage of the API is provided in test.py to help you get started quickly.








