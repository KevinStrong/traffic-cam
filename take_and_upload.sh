#!/bin/sh

cd /home/pi/cam

file_name="houston_traffic.jpg"

python3 camera_adjusted.py $file_name
python3 aws_upload.py $file_name
