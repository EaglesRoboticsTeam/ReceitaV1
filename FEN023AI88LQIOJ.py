import cv2 as cv
import numpy as np

kernel = np.ones((5,5),np.uint8)

# Take input from webcam
cap = cv.VideoCapture(-1)

# Reduce the size of video to 320x240 so rpi can process faster
cap.set(3,320)
cap.set(4,240)

def nothing(x):
    pass
# Creating a windows for later use
cv.namedWindow('HueComp')
cv.namedWindow('SatComp')
cv.namedWindow('ValComp')
cv.namedWindow('closing')
cv.namedWindow('tracking')


# Creating track bar for min and max for hue, saturation and value
# You can adjust the defaults as you like
cv.createTrackbar('hmin', 'HueComp',12,179,nothing)
cv.createTrackbar('hmax', 'HueComp',37,179,nothing)

cv.createTrackbar('smin', 'SatComp',96,255,nothing)
cv.createTrackbar('smax', 'SatComp',255,255,nothing)

cv.createTrackbar('vmin', 'ValComp',186,255,nothing)
cv.createTrackbar('vmax', 'ValComp',255,255,nothing)

# My experimental values
# hmn = 12
# hmx = 37
# smn = 145
# smx = 255
# vmn = 186
# vmx = 255


while(1):

    buzz = 0
    _, frame = cap.read()

    #converting to HSV
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    hue,sat,val = cv.split(hsv)

    # get info from track bar and appy to result
    hmn = cv.getTrackbarPos('hmin','HueComp')
    hmx = cv.getTrackbarPos('hmax','HueComp')
    

    smn = cv.getTrackbarPos('smin','SatComp')
    smx = cv.getTrackbarPos('smax','SatComp')


    vmn = cv.getTrackbarPos('vmin','ValComp')
    vmx = cv.getTrackbarPos('vmax','ValComp')

    # Apply thresholding
    hthresh = cv.inRange(np.array(hue),np.array(hmn),np.array(hmx))
    sthresh = cv.inRange(np.array(sat),np.array(smn),np.array(smx))
    vthresh = cv.inRange(np.array(val),np.array(vmn),np.array(vmx))

    # AND h s and v
    tracking = cv.bitwise_and(hthresh,cv.bitwise_and(sthresh,vthresh))

    # Some morpholigical filtering
    dilation = cv.dilate(tracking,kernel,iterations = 1)
    closing = cv.morphologyEx(dilation, cv.MORPH_CLOSE, kernel)
    closing = cv.GaussianBlur(closing,(5,5),0)

    # Detect circles using HoughCircles
    circles = cv.HoughCircles(closing,cv.HOUGH_GRADIENT,2,120,param1=120,param2=50,minRadius=10,maxRadius=0)
    # circles = np.uint16(np.around(circles))

    #Draw Circles
    if circles is not None:
            for i in circles[0,:]:
                # If the ball is far, draw it in green
                if int(round(i[2])) < 30:
                    cv.circle(frame,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(0,255,0),5)
                    cv.circle(frame,(int(round(i[0])),int(round(i[1]))),2,(0,255,0),10)
				# else draw it in red
                elif int(round(i[2])) > 35:
                    cv.circle(frame,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(0,0,255),5)
                    cv.circle(frame,(int(round(i[0])),int(round(i[1]))),2,(0,0,255),10)
                    buzz = 1

	#you can use the 'buzz' variable as a trigger to switch some GPIO lines on Rpi :)
    # print buzz                    
    # if buzz:
        # put your GPIO line here

    
    #Show the result in frames
    cv.imshow('HueComp',hthresh)
    cv.imshow('SatComp',sthresh)
    cv.imshow('ValComp',vthresh)
    cv.imshow('closing',closing)
    cv.imshow('tracking',frame)

    k = cv.waitKey(60) & 0xFF
    if k == 27:
        break

cap.release()

cv.destroyAllWindows()