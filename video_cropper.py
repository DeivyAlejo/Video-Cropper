import cv2 as cv

squares = []
square = []

def adding_points(event, x, y, flags, params):
  global squares, square
  if event == cv.EVENT_LBUTTONDOWN:
    square.append([x,y])
    if len(square)%2 == 0:
      squares.append([square[-1], square[-2]])
      print(squares)

    

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
    if not ret:
      break

    # Display the resulting frame
  for square_to_draw in squares:
    cv.rectangle(frame, square_to_draw[0], square_to_draw[1], (0,0,255))
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