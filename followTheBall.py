# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

import numpy as np 

#library to rotate, scale, etc images
import imutils
import RPi.GPIO as gpio ## Import GPIO library
import os
import sys    
import termios
import fcntl
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
#widthScreen = 610
#heightScreen = 344
#widthScreen = 305
#heightScreen = 150
widthScreen = 405
heightScreen = 210
line1V = widthScreen / 3
line2V = (widthScreen / 3) * 2
line1H = heightScreen / 3
line2H = (heightScreen / 3) * 2
velocityWheels = 0.03
camera.resolution = (widthScreen, heightScreen)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(widthScreen, heightScreen))
 
# allow the camera to warmup
time.sleep(0.1)



def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def fordward(tf):
    init()
    gpio.output(17,True)
    gpio.output(22,False)
    gpio.output(23,True)
    gpio.output(24,False)
    time.sleep(tf)
    gpio.cleanup()

def back(tf):
    init()
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,False)
    gpio.output(24,True)
    time.sleep(tf)
    gpio.cleanup()

def turnLeft(tf):
    init()
    gpio.output(17,True)
    gpio.output(22,False)
    gpio.output(23,False)
    gpio.output(24,True)
    time.sleep(tf)
    gpio.cleanup()
def turnRight(tf):
    init()
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,True)
    gpio.output(24,False)
    time.sleep(tf)
    gpio.cleanup()




 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text

	image = frame.array
	#Rotate image 180 grades
        frameRotated = imutils.rotate(image, 180)

        output = frameRotated.copy()
        gray = cv2.cvtColor(frameRotated, cv2.COLOR_BGR2GRAY)

        # detect circles in the image
        circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100)
        #circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT,1.2,100,param1=50,param2=30,minRadius=30,maxRadius=200)
 
        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
 
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                print x, y, r
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle

                #comentado para que no gaste tiempo en tratar las imagenes para pintarles los circulos
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		#cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)		
            # show the output image
            # cv2.imshow("detecting circle", np.hstack([image, output]))
            font = cv2.FONT_HERSHEY_DUPLEX
            bottomLeftCornerOfText = (10,10)
            fontScale = 0.3
            fontColor = (0,255,0)
            lineType = 2
            centerX = x + r/2
            centerY = y + r/2
            #cv2.putText(output,"(" + str(x) + "," + str(y) + ")(r:" + str(r) + ")", bottomLeftCornerOfText, font, fontScale, fontColor,lineType)
            print "center: " + str(centerX) + "," + str(centerY)
            if centerX < line1V:
                print "move left"
                turnRight(velocityWheels)
            elif (centerX > line1V ) and (centerX < line2V):
                print "stay center"
                if r < 50:
                    fordward(velocityWheels)
                elif r > 50:
                    back(velocityWheels)
            elif (centerX > line2V) and (centerX < widthScreen):
                print "move rigth"
                turnLeft(velocityWheels)
                
            cv2.imshow("detecting circle", output)
        else:
            cv2.imshow("detecting circle", frameRotated)

        key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
