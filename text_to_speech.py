import os.path

import elevenlabs
from elevenlabs import clone, generate, play, set_api_key

# add the text from the LLM
# Change the voice to be the voice ID

def generate_audio(text, voice_id):
    audio = generate(text, voice_id)
    play(audio)
    print("Generated Audio")
    elevenlabs.save(audio,"audio_final_output.mp3")
    return os.path.join(".", "audio_final_output.mp3")
