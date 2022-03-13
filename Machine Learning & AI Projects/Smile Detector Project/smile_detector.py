import cv2

#Face Classifier
#Assign Face detection model to face_detector
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Grab live feed from webcam
webcam = cv2.VideoCapture(0)

#Run the following in a loop
while True:  
    #Determine wheter webcome is sctive and assign each frame to frame
    read_value, frame = webcam.read() 
    #End loop is video is not accessible
    if not read_value:
        break
    #Change frame colour to black and white
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Detect faces
    faces = face_detector.detectMultiScale(frame_grayscale)
    for (x,y,w,h)in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (150,10,40), 2)   #Flip the frame horizontally
    image = cv2.flip(frame, 1)    
    #Display each frame in 'Smile Detector' window
    cv2.imshow('Smile Detector', image)
    #Hold the display for 1 millisecond
    cv2.waitKey(1)

#Clean Up
webcam.release() #Release the webcam
cv2.destroyAllWindows()#closes opened windows

#Code run without error
print("Code Completed!")