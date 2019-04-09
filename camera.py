#!/usr/bin/python3
import picamera 
from time import sleep
from subprocess import call
from datetime import datetime

fileName ="/home/pi/cam/picture.jpg"

sleep(15)

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.capture(fileName)
