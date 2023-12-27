"""
This script allows the user to select a video and crop it

@author: Deivy Munoz 
"""

import cv2 as cv
import numpy as np
import  tkinter as tk
from tkinter import filedialog
import time

# Gloal variables
square = []
squares = [0]
copy_frame = cv.Mat

# Functions
def adding_points(event, x, y, flags, params):
  """It handles when the frame is clicked to add the points to the correct variable and checks if the coordinates are return correctly"""
  global squares, square
  if event == cv.EVENT_MBUTTONDOWN:
    square.append([x,y])
    if len(square)%2 == 0 and squares[0] == 0:
      if(square[0][0] > square[1][0]):
        temp = square[0][0]
        square[0][0] = square[1][0]
        square[1][0] = temp
      
      if(square[0][1] > square[1][1]):
        temp = square[0][1]
        square[0][1] = square[1][1]
        square[1][1] = temp

      squares[0] = ([square[-2], square[-1]])
      square.clear()
      showRectangle()
      # print(squares)

def imgcrop(frame, rectangle_points):
  """Crops the image to the points given
      params:
      frame: original image to crop
      rectangel_points: points to crop the image"""
  point1 = rectangle_points[0]
  point2 = rectangle_points[1]
  return frame[point1[1]:point2[1], point1[0]:point2[0]]

def showRectangle():
  """Shows the rectangle on the first frame"""
  global copy_frame
  for index, square_to_draw in enumerate(squares):
      cv.rectangle(copy_frame, square_to_draw[0], square_to_draw[1], (0,255,0),2)
  cv.imshow('Frame', copy_frame)

def createProcessingText():
  """It creates an image that says processing..."""
  width, height = 250, 100
  image = np.zeros((height, width, 3), dtype=np.uint8)
  text = "Processing..."
  font = cv.FONT_HERSHEY_SIMPLEX
  font_scale = 1
  font_thickness = 2
  font_color = (255, 255, 255)
  text_size = cv.getTextSize(text, font, font_scale, font_thickness)[0]
  text_x = (width - text_size[0]) // 2
  text_y = (height + text_size[1]) // 2
  cv.putText(image, text, (text_x, text_y), font, font_scale, font_color, font_thickness)
  return image

# Selecting the video file and the folder to save the video
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("Video files",("*.avi","*.mp4","*.MP4"))])
folder_path = filedialog.askdirectory()

if (not file_path or not folder_path):
  exit()

# Creating the instance from the video file and managing error
cap = cv.VideoCapture(file_path)
if cap.isOpened()== False: 
  print("Error opening video stream or file")

# Readign first frame and setting initial variables
ret, frame = cap.read()
copy_frame = frame.copy()
not_to_show = False
output_video = False
cropped_video = 0

# Showing first frame and seeting the click event
cv.imshow('Frame', copy_frame)
cv.setMouseCallback('Frame', adding_points)

# While loop where user can remove the current rectangle or crop and save the video
# User can close the process without cropping the video by pressing q
key = cv.waitKey(0)
while key != ord('q'):
  # Removing the current rectangle
  if key == ord('r'):
    squares=[0]
    copy_frame = frame.copy()
    cv.imshow('Frame', copy_frame)

  # Saving the video ussing the current rectangle
  if key == ord('s') and len(squares) > 0:
    cv.destroyWindow('Frame')
    cv.imshow("Processing", createProcessingText())
    while cap.isOpened():
      ret, frame = cap.read()
      if not ret:
        not_to_show = True
        break
      copy_frame = frame.copy()
      
      for index, square_to_draw in enumerate(squares):
        if not output_video:
          t = time.localtime()
          current_time = time.strftime("%H%M%S", t)
          fourcc = cv.VideoWriter_fourcc(*'XVID')
          name = f"{folder_path}/Video_Cropped_{current_time}.avi"
          fps = cap.get(cv.CAP_PROP_FPS)
          size = (abs(square_to_draw[0][0] - square_to_draw[1][0]),  abs(square_to_draw[0][1] - square_to_draw[1][1]))
          cropped_video = cv.VideoWriter(name, fourcc, fps, size)
          output_video = True
        image_cropped = imgcrop(frame, square_to_draw)
        cropped_video.write(image_cropped)
        cv.waitKey(1)
    cv.destroyAllWindows()
    exit()
    
  if (not not_to_show):
    cv.imshow('Frame', copy_frame)
  key = cv.waitKey(0)

cap.release()

cv.destroyAllWindows()