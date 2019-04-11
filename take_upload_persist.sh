#!/bin/sh

script_folder='/home/pi/cam'
cd $script_folder

image="houston_traffic.jpg"
timestamp=$(date +%H:%M)
timestamp_image="houston_traffic-$timestamp.jpg"

python3 $script_folder/camera_adjusted.py $image
python3 $script_folder/aws_upload.py $image
mv $image $timestamp_image
python3 $script_folder/aws_upload.py $timestamp_image $folder
