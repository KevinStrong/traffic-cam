#!/usr/bin/python3
import picamera 
from time import sleep
from subprocess import call
from datetime import datetime

fileName ="/home/pi/cam/houston_traffic.jpg"

with picamera.PiCamera() as camera:
    sleep(0.1) #let camera start up
    camera.resolution = (1280, 720)
    camera.capture(fileName)

currentTime = datetime.now()
timestampMessage = currentTime.strftime("%Y.%m.%d-%H:%M:%S") 
timestampCommand = "/usr/bin/convert " + fileName + " -pointsize 32 \
        -fill red -annotate +975+700 '" + timestampMessage + "' " + fileName
call([timestampCommand], shell=True)
