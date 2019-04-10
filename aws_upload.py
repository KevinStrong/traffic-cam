#!/usr/bin/python3
import boto3
import sys

bucket = 'narcindin.com'
local_file_name = sys.argv[1]

if len(sys.argv) > 2:
    aws_file_name = sys.argv[2] + "/" + local_file_name
else:
    aws_file_name = local_file_name

metadata = {"Content-Type" : "image/jpeg"}


s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket)
data = open(local_file_name, 'rb');
bucket.put_object(Key=aws_file_name, Body=data, ContentType='image/jpeg')

