# Video Cropper App

This script uses OpenCV and Tkinter to allow users to select a video, define a rectangle by clicking with the middle mouse button, and then save the cropped video based on the defined rectangle. The user can interact with the video processing using keyboard commands.

## Prerequisities 

- Python 3.10
- OpenCV 4.8.1

## Installation

You can use pip install requirements.txt and all the needed libraries will installed.

## Usage

You should run video_cropper.py. Once executed, choose a video, and then select a folder to save the cropped video. When the video loads, the first frame will appear on the screen. At this point, select two points to create a rectangle, determining the area to be saved as a new video. Press the middle mouse button to select a point; after two clicks, a green rectangle will appear, indicating the area to crop.

- To delete the selected area, press the 'r' key. 
- To quit the script, press the 'q' key. 
- After selecting the rectangle, press the 's' key to save the video. Once processing is complete, the script will close everything.
