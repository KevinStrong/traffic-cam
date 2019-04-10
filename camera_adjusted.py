#!/usr/bin/python3
import sys
import picamera
import picamera.array
import numpy as np
from time import sleep
from datetime import datetime
from picamera import Color

file_name = sys.argv[1]
THRESHOLD = 60

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 24
    with picamera.array.PiYUVArray(camera) as stream:
        sleep(1)
        camera.capture(stream, format='yuv', use_video_port=True)
        average = np.average(stream.array[..., 0])
        if average > THRESHOLD:
            camera.exposure_compensation -= int((average - THRESHOLD) /10)
        currentTime = datetime.now()
        timestampMessage = currentTime.strftime("%Y.%m.%d-%H:%M:%S") 
        camera.annotate_background = Color('black')
        camera.annotate_text = timestampMessage 
        sleep(1)
        camera.capture(file_name)

