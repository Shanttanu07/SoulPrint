import requests
import cloudinary
import id_generator
import time
import urllib.request
import cloudinary.uploader



cloudinary.config(
    cloud_name="dlc7ou1ci",
    api_key="379825293257185",
    api_secret="6TkK5xGfo8AdPYRWtzhJyah_BtQ"
)
API_URL = "https://api.synclabs.so/"


class GenerateDeepFake():
    def __init__(self, video_location, audio_location):
        self.video_url = video_location
        self.audio_url = audio_location
        self.current_status = None

    def upload_video(self):
        uid = id_generator.generate_video_id()
        data = cloudinary.uploader.upload(
            self.audio_url,
            resource_type='video',
            public_id=uid,
            chunk_size=210000000)

        return data['playback_url']

    def upload_audio(self):
        uid = id_generator.generate_audio_id()
        data = cloudinary.uploader.upload(
            self.audio_url,
            resource_type='video',
            public_id=uid,
            chunk_size=210000000)


        return data['playback_url']

    def generate(self, API_KEY):
        video_url = self.upload_video()
        audio_url = self.upload_audio()

        url = 'https://api.synclabs.so/video'
        headers = {
            'accept': 'application/json',
            'x-api-key': API_KEY,
            'Content-Type': 'application/json',
        }

        data = {
            "audioUrl": video_url,
            "videoUrl": audio_url,
            "synergize": False,  # Note that 'False' is used instead of 'false' in Python
            "maxCredits": 15,
            "webhookUrl": None,  # 'None' is used instead of 'null' in Python
        }

        response = requests.post(url, headers=headers, json=data)
        print(response)

        if response.json()!=403:
            while True:
                print(response.json())
                id = response.json()["id"]
                url = f'https://api.synclabs.so/video/{id}'

                headers = {
                    'accept': 'application/json',
                    'x-api-key':  API_KEY
                }

                response = requests.get(url, headers=headers)

                if 'status' in response.json():
                    if response.json()["status"] == "COMPLETED":
                        url =  response.json()["URL"]
                        urllib.request.urlretrieve(url, 'video_name.mp4')
                        return "vidoe_name.mp4"
                        break

                print("PENDING")
                time.sleep(3)







# GenerateDeepFake("v1.mp4","a1.wav").generate("2da53803-360c-4257-a6e0-eab2f8bd36d5")