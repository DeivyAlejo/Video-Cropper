import cv2 as cv

square = []
squares = []
copy_frame = cv.Mat

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

cap = cv.VideoCapture('Media1.MP4')

cv.namedWindow('Frame')
cv.setMouseCallback('Frame', adding_points)

# Check if camera opened successfully
if cap.isOpened()== False: 
  print("Error opening video stream or file")

ret, frame = cap.read()
print(frame.shape)
copy_frame = frame.copy()
not_to_show = False

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
    # Capture frame-by-frame
      ret, frame = cap.read()
      if not ret:
        not_to_show = True
        break
      copy_frame = frame.copy()
      
      for index, square_to_draw in enumerate(squares):
        # cv.rectangle(frame, square_to_draw[0], square_to_draw[1], (0,0,255))
        # image_cropped = frame[197:829, 7:777]
        image_cropped = imgcrop(frame, square_to_draw)
        image_name = f"Image Cropped {index}"
        cv.imshow(image_name, image_cropped)
        cv.waitKey(1)
        # print(square_to_draw)
    
  if (not not_to_show):
    cv.imshow('Frame', copy_frame)
  key = cv.waitKey(0)

cap.release()

cv.destroyAllWindows()