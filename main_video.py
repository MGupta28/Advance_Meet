import cv2
from simple_facerec import SimpleFacerec
from line import Line_detection
# import serial
# from serial import Serial
import time

from pyfirmata import Arduino ,SERVO ,util

# Encode faces from a folder
sfr = SimpleFacerec()
ld = Line_detection()
sfr.load_encoding_images("training images/")


file_name = "Test Lecture"

# Load Camera
cap = cv2.VideoCapture(2)
# cap.set(cv2.CAP_PROP_FPS, 60)

if (cap.isOpened() == False): 
    print("Error reading from camera source")

# out = cv2.VideoWriter('RecordedVideo' + file_name + '.avi', -1, 20.0, (640,480))

# start a serial port from arduino
# arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)

port ="/dev/ttyUSB0"
pin=9
board =Arduino(port)
board.digital[pin].mode=SERVO
board.digital[pin].write(90)

angle=90
while (cap.isOpened()):
    # read from camera
    ret, frame = cap.read()

    if ret==True:
        # frame = cv2.flip(frame,0)

        # write the flipped frame
        # out.write(frame)

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            # board.digital[pin].write(sub)

            sub = -(((int(frame.shape[1]/2)) - int((x1 + x2)/2))/5)
            #angle=int(90-sub)
            if sub > 7:
                if angle > 5:
                    angle = angle - 3
            if sub < -7:
                if angle < 175:
                    angle = angle + 3
                    
            # board.digital[pin].write(160)
            print(angle)
            board.digital[pin].write(angle)
            # arduino.write(bytes(sub, 'utf-8'))
            time.sleep(0.05)

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            cv2.circle(frame, (int((x1 + x2) / 2), int((y1 + y2) / 2)), 5, (255, 255, 255), -1)
            ld.draw_grid(frame,(2,2))
            cv2.line(frame,(int((x1 + x2) / 2), 0),(int((x1 + x2) / 2), 480), color=(0, 255, 0), thickness=3)


        cv2.imshow("Frame", frame)
        cv2.moveWindow("Frame",1200,250)


        key = cv2.waitKey(1)
        if cv2.waitKey(10) & 0xff == ord('q'):   # 1 is the time in ms
            break

cap.release()
cv2.destroyAllWindows()