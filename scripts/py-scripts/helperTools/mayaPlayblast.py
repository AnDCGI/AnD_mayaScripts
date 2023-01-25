import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

# Define the directory where your Maya files are located
maya_dir = "path/to/maya/files"

# Define the directory where you want to save the playblast
playblast_dir = "path/to/playblast/output"


def generate_playblast(maya_file):
    # Construct the full path to the playblast
    playblast_file = os.path.join(playblast_dir, os.path.basename(maya_file) + ".mp4")
    # Check if the playblast already exists
    if not os.path.exists(playblast_file):
        # Use the subprocess module to call the mayabatch command
        subprocess.call(["mayabatch", "-command", "file -f -open -force " + maya_file])
        subprocess.call([
            "mayabatch", "-command",
            "playblast -format avi -filename " + playblast_file[:-4] + ".avi -forceOverwrite true"
        ])
        # Use FFmpeg to convert the AVI playblast to a more web-friendly format
        subprocess.call(["ffmpeg", "-i", playblast_file[:-4] + ".avi", playblast_file])
        os.remove(playblast_file[:-4] + ".avi")
    else:
        print("Playblast for " + os.path.basename(maya_file) + " already exists, skipping")


# Use os.walk to loop over all files in the directory and its subdirectories
with ThreadPoolExecutor() as executor:
    for root, dirs, files in os.walk(maya_dir):
        for file in files:
            # Check if the file is a Maya file
            if file.endswith(".ma"):
                # Construct the full path to the Maya file
                maya_file = os.path.join(root, file)
                executor.submit(generate_playblast, maya_file)
