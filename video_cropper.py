import cv2 as cv

def square(event, x, y, flags, params):
    # global frame
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(frame,(x,y),2,(0,0,255),-1)
        cv.imshow('Frame', frame)
        print(x,y)

cap = cv.VideoCapture('Media1.mp4')

paused = False

cv.namedWindow('Frame')
cv.setMouseCallback('Frame', square)
 
# Check if camera opened successfully
if cap.isOpened()== False: 
  print("Error opening video stream or file")
 
# Read until video is completed
while cap.isOpened():
  # Capture frame-by-frame
    if not paused:
        ret, frame = cap.read()
        if not ret:
            break

    # Display the resulting frame
    cv.imshow('Frame', frame)
    
    
    # Press Q on keyboard to  exit
    key = cv.waitKey(25)
    if key == ord('q'):
        exit(0)
    if key == ord('p'):
        paused = not paused
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv.destroyAllWindows()