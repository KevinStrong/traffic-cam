#!/usr/bin/python3
import sys
import picamera
from picamera import Color
from time import sleep
from subprocess import call
from datetime import datetime


file_name = sys.argv[1]
#fileName ="/home/pi/cam/picture.jpg"

currentTime = datetime.now()
timestampMessage = currentTime.strftime("%Y.%m.%d-%H:%M:%S") 

with picamera.PiCamera() as camera:
    sleep(1)
    camera.resolution = (1280, 720)
    camera.annotate_background = Color('black')
    camera.annotate_text = timestampMessage 
    camera.capture(file_name)
