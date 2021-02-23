import cv2
# print(cv2.__version__)

capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('../fastface_1/haarcascade_frontalface_default.xml')
while True:
    ret, img = capture.read()

    faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('From my camera', img)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()