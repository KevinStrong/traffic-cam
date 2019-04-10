#!/bin/sh

script_folder='/home/pi/cam'
cd $script_folder

#export PATH=$(pwd):$PATH
#echo $PATH

folder="daily"
cd $folder
pwd
timestamp=$(date +%H:%M)

standard="houston_traffic_tall-$timestamp.jpg"
adjusted="houston_traffic_short-$timestamp.jpg"

python3 $script_folder/camera.py $standard
python3 $script_folder/aws_upload.py $standard $folder

python3 $script_folder/camera_adjusted.py $adjusted
python3 $script_folder/aws_upload.py $adjusted $folder
