#!/bin/sh

cd /home/pi/cam

python3 camera_timestamp.py
python3 aws_upload.py
