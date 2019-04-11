#!/bin/sh

script_folder='/home/pi/cam'
cd $script_folder

folder="daily"

image="houston_traffic.jpg"
timestamp=$(date +%H:%M)
timestamp_image="houston_traffic-$timestamp.jpg"

#Upload as most recent image
python3 $script_folder/camera_adjusted.py $image
python3 $script_folder/aws_upload.py $image

#Upload as timestamped image
mv $image $timestamp_image
python3 $script_folder/aws_upload.py $timestamp_image $folder
mv $timestamp_image $folder
