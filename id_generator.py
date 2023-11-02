import uuid
import os
import json

CWD = os.getcwd()


def write_json(dtype="a/v", uuid=None):
    if dtype == "a":
        with open(os.path.join(CWD, "../JSON", "audio_uploads.json"), "r") as f:
            current_data = json.load(f)

        # Append the new UUID. Note that 'append' doesn't return the modified list; it modifies in-place.
        if "ID" in current_data:
            current_data["ID"].append(str(uuid))  # Assuming uuid is a variable containing your UUID.
        else:
            current_data["ID"] = [str(uuid)]  # If "ID" doesn't exist, create it and add the UUID.

        with open(os.path.join(CWD, "../JSON", "audio_uploads.json"), "w") as f:
            json.dump(current_data, f)

    if dtype == "v":
        with open(os.path.join(CWD, "../JSON", "video_uploads.json"), "r") as f:
            current_data = json.load(f)

        # Append the new UUID. Note that 'append' doesn't return the modified list; it modifies in-place.
        if "ID" in current_data:
            current_data["ID"].append(str(uuid))  # Assuming uuid is a variable containing your UUID.
        else:
            current_data["ID"] = [str(uuid)]  # If "ID" doesn't exist, create it and add the UUID.

        # Write the modified data back to the file
        with open(os.path.join(CWD, "../JSON", "video_uploads.json"), "w") as f:
            json.dump(current_data, f)


def generate_video_id():
    video_id = uuid.uuid4()  # This generates a random UUID.
    write_json("v", uuid=video_id)
    return str(video_id)  # Convert UUID to string to make it easier to work with.


def generate_audio_id():
    # Generate a random UUID for an audio.
    audio_id = uuid.uuid4()  # This generates a random UUID.
    write_json(dtype="a", uuid=audio_id)
    return str(audio_id)  # Convert UUID to string to make it easier to work with.


# Example usage:
if __name__ == "__main__":
    video_id = generate_video_id()
    print(f"Generated Video ID: {video_id}")

    audio_id = generate_audio_id()
    print(f"Generated Audio ID: {audio_id}")
