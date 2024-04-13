import os
from dotenv import load_dotenv
import requests

# Texto a voz utiliza ElevenLabs
class TTS():
    def __init__(self):
        load_dotenv()
        self.key = os.getenv('ELEVENLABS_API_KEY')
        self.id_value = os.getenv('ID_VALUE')

    def process(self, text):
        CHUNK_SIZE = 1024
        # Usar format() para insertar el ID
        url = "https://api.elevenlabs.io/v1/text-to-speech/{}/stream".format(self.id_value)

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.key
        }

        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.93,
                "similarity_boost": 0.75,
                "style": 1
            }
        }

        file_name = "response.mp3"
        response = requests.post(url, json=data, headers=headers)
        with open("static/" + file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
                    
        return file_name
