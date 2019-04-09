#!/usr/bin/python3
import picamera
import picamera.array
import numpy as np
from time import sleep
#from subprocess import call
#from datetime import datetime

fileName ="/home/pi/cam/houston_traffic.jpg"
THRESHOLD = 60

with picamera.PiCamera() as camera:
    sleep(0.1) #let camera start up
    camera.resolution = (1280, 720)
    camera.framerate = 24
    with picamera.array.PiYUVArray(camera) as stream:
        camera.capture(stream, format='yuv', use_video_port=True)
        average = np.average(stream.array[..., 0])
        if average > THRESHOLD:
            camera.exposure_compensation -= int((average - THRESHOLD) /10)

#currentTime = datetime.now()
#timestampMessage = currentTime.strftime("%Y.%m.%d-%H:%M:%S") 
#timestampCommand = "/usr/bin/convert " + fileName + " -pointsize 32 \
 #       -fill red -annotate +975+700 '" + timestampMessage + "' " + fileName
#call([timestampCommand], shell=True)
