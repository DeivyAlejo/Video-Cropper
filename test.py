import cv2 as cv
import  tkinter as tk
from tkinter import filedialog

# Gloal variables
square = []
squares = []
copy_frame = cv.Mat

# Functions
def adding_points(event, x, y, flags, params):
  global squares, square
  if event == cv.EVENT_MBUTTONDOWN:
    square.append([x,y])
    if len(square)%2 == 0:
      squares.append([square[-2], square[-1]])
      showRectangles()
      # print(squares)

def imgcrop(frame, rectangle_points):
  point1 = rectangle_points[0]
  point2 = rectangle_points[1]
  return frame[point1[1]:point2[1], point1[0]:point2[0]]

def showRectangles():
  global copy_frame
  for index, square_to_draw in enumerate(squares):
      cv.rectangle(copy_frame, square_to_draw[0], square_to_draw[1], (0,255,0),2)
  cv.imshow('Frame', copy_frame)


# Main
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)



cap = cv.VideoCapture(file_path)

fourcc = cv.VideoWriter_fourcc(*'XVID')

cv.namedWindow('Frame')
cv.setMouseCallback('Frame', adding_points)

# Check if camera opened successfully
if cap.isOpened()== False: 
  print("Error opening video stream or file")

ret, frame = cap.read()
copy_frame = frame.copy()
not_to_show = False
output_video = False
cropped_video = 0

cv.imshow('Frame', copy_frame)

key = cv.waitKey(0)
while key != ord('q'):
  if key == ord('r'):
    squares=[]
    copy_frame = frame.copy()
    cv.imshow('Frame', copy_frame)
  if key == ord('s') and len(squares) > 0:
    cv.destroyWindow('Frame')
    while cap.isOpened():
      ret, frame = cap.read()
      if not ret:
        not_to_show = True
        break
      copy_frame = frame.copy()
      
      for index, square_to_draw in enumerate(squares):
        if not output_video:
          name = f"Video_Cropped_{index}.avi"
          fps = cap.get(cv.CAP_PROP_FPS)
          print(fps)
          size = (abs(square_to_draw[0][0] - square_to_draw[1][0]),  abs(square_to_draw[0][1] - square_to_draw[1][1]))
          cropped_video = cv.VideoWriter(name, fourcc, 30, size)
          output_video = True
          print(size)
        image_cropped = imgcrop(frame, square_to_draw)
        cropped_video.write(image_cropped)
        image_name = f"Image Cropped {index}"
        cv.imshow(image_name, image_cropped)
        cv.waitKey(1)
    
  if (not not_to_show):
    cv.imshow('Frame', copy_frame)
  key = cv.waitKey(0)

cap.release()

cv.destroyAllWindows()