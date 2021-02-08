import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('test.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# for (x,y,w,h) in faces:
    # cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
# cv2.imshow('img', img)
# cv2.waitKey()


# =========== FOR VIDEO =========== #
VIDEO = cv2.VideoCapture('test4.mp4')
if VIDEO.isOpened() == False:
    print("Error opening video stream or file")

while VIDEO.isOpened():
    # capture frame by frame
    ret, frame = VIDEO.read()   
    
    if ret:
    # display the resulting frame
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grayFrame, 1.1, 4)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, 'face', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))
        cv2.imshow('video gray', frame)
        
        # press 'Q' to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        print("Done!")
        break
        
VIDEO.release()
cv2.destroyAllWindows()