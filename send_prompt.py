import json
import generate_content
import emotion
import random
import os
from pathlib import Path
import text_to_speech
import generate_deepfake

# Access JSON file and return the voice ID
def choose_tone(analyse_reply):
    try:
        os.chdir("ui")
        os.chdir("Audio")
    except:
        os.chdir("Audio")

    with open("Audio", "r") as voice_IDs :
        data = json.load(voice_IDs)
        for keys in data:
            if analyse_reply == data[keys] :
                return data[keys]

def change_file_path(original_path, new_directory, new_filename):
    """
    Change the directory or filename of a given file path.

    Parameters:
    original_path (str): The original file path.
    new_directory (str): The new directory to move the file to.
    new_filename (str): The new filename for the file.

    Returns:
    str: The updated file path.
    """

    # Break the original path into components (head, tail)
    # 'head' would contain the directory while 'tail' contains the file name
    head, tail = os.path.split(original_path)

    # If a new directory is specified, use it, otherwise keep the original directory
    if new_directory:
        head = new_directory

    # If a new filename is specified, use it, otherwise keep the original file name
    if new_filename:
        tail = new_filename

    # Combine the directory with the new filename
    new_path = os.path.join(head, tail)

    return new_path




def choose_video(analyse_reply):

    try:
        os.chdir("ui")
        os.chdir("Audio")
    except:
        os.chdir("Audio")

    with open("seperate_video.json", "r") as video_emo :
        data = json.load(video_emo)
        for keys in data:
            if keys==analyse_reply:
                array =  data[keys]
                random_video = data[keys][random.randint(0, len(array)-1)]
                path = Path(random_video)
                random_video_path = os.path.join(path.parent.absolute(),"Audio",random_video.split(".\\")[-1])
                return random_video_path


def get_audio(bot_reply, audio_tone):
    return text_to_speech.generate(bot_reply, audio_tone)


def send_prompt(question):
    bot_reply = generate_content.runPrompt(question)
    analyse_reply = emotion.predict([bot_reply])
    audio_tone = choose_tone(analyse_reply)
    audio = get_audio(bot_reply, audio_tone)
    video = choose_video(analyse_reply)
    generate_deepfake.GenerateDeepFake(video, audio).generate(API_KEY="c869492f-80dc-460d-b4f6-e3b87a2da132")

# API_KEY = "c869492f-80dc-460d-b4f6-e3b87a2da132"
#
# choose_video("happiness")