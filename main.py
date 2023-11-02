import generate_deepfake

def execute(video_location, audio_location):
    generate_deepfake.GenerateDeepFake.generate(video_location, audio_location)
if __name__ == "__main__":
    API_key = input("Enter the API key to cloudsync - ")




