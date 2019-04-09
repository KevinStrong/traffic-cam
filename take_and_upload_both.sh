#!/bin/sh

cd /home/pi/cam

standard="houston_traffic_tall.jpg"
adjusted="houston_traffic_short.jpg"

python3 camera.py $standard
python3 aws_upload.py $standard

python3 camera_adjusted.py $adjusted
python3 aws_upload.py $adjusted
