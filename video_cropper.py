import cv2 as cv

squares = []
square = []

def adding_points(event, x, y, flags, params):
  global squares, square
  if event == cv.EVENT_LBUTTONDOWN:
    square.append([x,y])
    if len(square)%2 == 0:
      squares.append([square[-2], square[-1]])
      # print(squares)

def imgcrop(frame, rectangle_points):
  point1 = rectangle_points[0]
  point2 = rectangle_points[1]
  return frame[point1[1]:point2[1], point1[0]:point2[0]]
    

cap = cv.VideoCapture('Media1.mp4')

paused = False
refresh = True

cv.namedWindow('Frame')
cv.setMouseCallback('Frame', adding_points)
 
# Check if camera opened successfully
if cap.isOpened()== False: 
  print("Error opening video stream or file")
 
# Read until video is completed
while cap.isOpened():
  # Capture frame-by-frame
  if not paused:
    refresh = True
    ret, frame = cap.read()
    copy_frame = frame.copy()
    if not ret:
      break

    # Display the resulting frame
  for index, square_to_draw in enumerate(squares):
    # cv.rectangle(frame, square_to_draw[0], square_to_draw[1], (0,0,255))
    # image_cropped = frame[197:829, 7:777]
    image_cropped = imgcrop(frame, square_to_draw)
    image_name = f"Image Cropped {index}"
    cv.imshow(image_name, image_cropped)
    # print(square_to_draw)
  cv.imshow('Frame', frame)
    
    
    # Press Q on keyboard to  exit
  key = cv.waitKey(1)
  if key == ord('q'):
    exit(0)
  if key == ord('p'):
    paused = not paused
  
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv.destroyAllWindows()