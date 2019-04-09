#!/usr/bin/python3
import sys
import picamera 
from time import sleep
from subprocess import call
from datetime import datetime

file_name = sys.argv[1]
#fileName ="/home/pi/cam/picture.jpg"


with picamera.PiCamera() as camera:
    sleep(1)
    camera.resolution = (1280, 720)
    camera.capture(file_name)
