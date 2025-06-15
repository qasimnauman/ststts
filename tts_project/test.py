import requests

# URL of your running Flask API
API_URL = "http://127.0.0.1:5000/api/speak"

# Payload with text and speaker
payload = {
    "text": "This is a test speech generated from the Flask API. How are you doing today?",
    "speaker": "bob"
}

# Send POST request and save audio output
response = requests.post(API_URL, json=payload)

if response.status_code == 200:
    with open("response_audio.wav", "wb") as f:
        f.write(response.content)
    print("✅ Audio saved as response_audio.wav")
else:
    try:
        print("❌ Error:", response.json())
    except Exception:
        print("❌ Unexpected error:", response.text)
