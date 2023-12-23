import cv2 as cv

square = []
squares = []

def adding_points(event, x, y, flags, params):
  global squares, square
  if event == cv.EVENT_MBUTTONDOWN:
    square.append([x,y])
    if len(square)%2 == 0:
      squares.append([square[-2], square[-1]])
      print(squares)


cap = cv.VideoCapture('Media1.MP4')

cv.namedWindow('Frame')
cv.setMouseCallback('Frame', adding_points)

# Check if camera opened successfully
if cap.isOpened()== False: 
  print("Error opening video stream or file")

ret, frame = cap.read()
print(frame.shape)
copy_frame = frame.copy()

cv.imshow('Frame', frame)

key = cv.waitKey(0)
if key == ord('c'):
  for index, square_to_draw in enumerate(squares):
    cv.rectangle(frame, square_to_draw[0], square_to_draw[1], (0,255,0),2)
    # image_cropped = frame[197:829, 7:777]
    # image_cropped = imgcrop(frame, square_to_draw)
    # image_name = f"Image Cropped {index}"
    
cv.imshow('Frame', frame)

cv.waitKey(0)

cap.release()

cv.destroyAllWindows()