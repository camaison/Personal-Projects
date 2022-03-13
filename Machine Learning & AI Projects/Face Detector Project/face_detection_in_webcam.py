import random 
import cv2

#Function to Keep track of all the faces present
def tracker(face_coordinates): 
    track = 0
    #Looping through all the faces present in the image or frame
    for set in face_coordinates: 
        [x,y,w,h] = face_coordinates[track] #Assigning the face coordinates to x,y,w,h to be used in the function below
        cv2.rectangle(frame, (x,y), (x+w, y+h), (25, 100, 150), 3 ) #Calling the x,y,w,h, coordinates in the rectangle function and definig the RGB colour using the values 25 for blue, 100 for green and 150 for red, and assigning the value, 3 to the box thickness
        track+=1 


trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #Assigining the trained face data to a variable

#Assigning the live feed from the primary webcam to the variable cam. The value, 0, can be replaced with the file name of a video, ecample 'funny_clip.mp4' or a different integer that represents a camera aside the primary web cam(0)
cam = cv2.VideoCapture(0) 

#Runs in a loop in order to grab and output video frames in real time
while True:
    frame_read, frame = cam.read() #Assigns a boolean to the frame_read variable and the image of every single frame to the frame variable

    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converts the coloured image to a gray scale to be easily decipherable by the program

    face_coordinates = trained_face_data.detectMultiScale(grayscale) # Asssigning the nested list of cordinates of the faces detected to the variable face_coordinates

    tracker(face_coordinates) # Calling the tracker function on face coordinates

    cv2.imshow('Face Detector', frame)  #Displays the live feed in a program called face detector with rectangles on the detected faces
    key = cv2.waitKey(1) #The frames are looped through every 1 millisecond to keep the video feed in real time

    #The program ends if the letter 'q' Capital and small q are represented by 81 and 113 on the ASCII table
    if key == 81 or key==113: 
        break
print("Code Completed!")

