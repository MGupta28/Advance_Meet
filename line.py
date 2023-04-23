import face_recognition
import cv2
import os
import glob
import numpy as np


class Line_detection():

    # def __init__(self):
        
    # def __init__(self):
    #     rospy.init_node('ERROR', anonymous=False) #initialize user default node and annoymous help in maintaining uniquness of node
    #     self.bridge = cv_bridge.CvBridge()
    #     self.pub = rospy.Publisher('geometry_msgs',Float32, queue_size=10)
    #     self.sub = rospy.Subscriber('geometry_msgs',Float32, queue_size=10)
    #     rate = rospy.Rate(10)
    def draw_grid(self, frame, grid_shape, color=(0, 255, 0), thickness=2):
        h, w, _ =  frame.shape
        rows, cols = grid_shape
        dy, dx = h / rows, w / cols




        # draw vertical lines
        for x in np.linspace(start=dx, stop=w-dx, num=cols-1):
            x = int(round(x))
            cv2.line(frame, (x, 0), (x, h), color=color, thickness=thickness)




        # draw horizontal lines
        # for y in np.linspace(start=dy, stop=h-dy, num=rows-1):
        #     y = int(round(y))
        #     cv2.line(frame, (0, y), (w, y), color=color, thickness=thickness)
