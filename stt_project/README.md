
## 🧏 Flask Speech-to-Text (STT) API
This project provides a simple Flask API that converts spoken audio into text using an automatic speech recognition (ASR) model.

-----------------------------------------------------------------


## 🚀 Features
Accepts .wav audio input and transcribes it into text.

Returns plain text or JSON response.

Supports a range of audio sample rates (16kHz recommended).

Fast and lightweight API, ideal for real-time applications.

------------------------------------------------------------------

## 🧠 How It Works
The ASR model is loaded once when the server starts for efficiency.

A client sends a POST request with a .wav file.

The API processes the audio and returns the transcribed text.

------------------------------------------------------------------

## 📂 Supported Audio Format
Format: .wav or mp3



## 🛠️ Installation
🔧 Requirements
Python 3.8+

FFmpeg (recommended for audio handling)

CUDA-compatible GPU (optional but improves speed)

Required Python packages listed in requirements.txt

----------------------------------------------------------------

## Steps to run 

1. Create and Activate a Virtual Environment

# Create environment
python3 -m venv sttvenv

# Activate environment on macOS / Linux
source sttvenv/bin/activate

# Activate environment on Windows
sttvenv\Scripts\activate


2. Install Dependencies

pip install -r requirements.txt

3. Install FFmpeg (Required by STT model)
Ubuntu / Debian

sudo apt install ffmpeg


macOS (using Homebrew)

brew install ffmpeg


Windows
Download and install from:
👉 https://ffmpeg.org/download.html
Make sure to add FFmpeg to PATH during installation.

4. Run the API (Two Options)
# 🔧 Option 1: Development Mode (for testing/debugging)


Run with Flask's built-in server:  python app.py

Best for quick local testing.

Auto-reloads on code changes.

Not suitable for production.

# 🚀 Option 2: Production Mode (Recommended)
Use Gunicorn for a production-ready deployment:

gunicorn -w 4 -b 0.0.0.0:5000 app:app


-w 4 runs 4 worker processes.

Designed for handling concurrent requests reliably.

Manual restart required on code updates.

5. First-Time Note

⚠️ On the first run, the STT model may download required files or initialize resources, so the first request might take longer.
Once initialized, it runs from local cache and responds faster.

6. Try a Demo
Run the test script provided with the project:

python test.py


Sends an audio file to the API.

Prints or saves the transcribed text from the audio file.


-------------------------------------------------------------------------------


## 📡 API Endpoints

🎙️ POST /api/transcribe

# Request:
Send a .wav audio file as form-data:
Key: audio
Value: <your-audio.wav>

# Response:
{
  "transcription": "This is the recognized text from audio."
}
Status Codes:

200 OK: Successful transcription

400 Bad Request: Missing or invalid audio

500 Internal Server Error: Unexpected issue during processing

-------------------------------------------------------------------------


## ⚙️ Production Deployment
Use Gunicorn to run the app in production:

**gunicorn -w 4 -b 0.0.0.0:5000 app:app**

-w 4: Number of worker processes (adjust based on CPU cores)


----------------------------------------------------------------------------

## ✅ Notes

-  Make sure your .wav or .mp3 file is properly formatted (PCM, 16-bit, mono, 16kHz).

-  The first time you run the API, it will download the speech recognition model locally. This  may take some time. After that, the model will be cached and loaded instantly on subsequent runs.

-  A sample usage of the API is provided in test.py to help you get started quickly.


