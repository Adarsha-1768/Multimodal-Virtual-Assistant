import cv2
import sys
import os



# Initialize video capture (0 for the default camera, change if using a different camera)
video_capture = cv2.VideoCapture(0)

if len(sys.argv) < 2:
    print("Usage: python face_recognition.py <cascPath>")
    sys.exit(1)
cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if faceCascade.empty():
    print("Error: Failed to load the cascade classifier XML file")
    sys.exit(1)


cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:
        print("Error reading frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
video_capture.release()
cv2.destroyAllWindows()
