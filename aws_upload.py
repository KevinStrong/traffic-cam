#!/usr/bin/python3
import boto3

file_name = 'houston_traffic.jpg'
bucket = 'narcindin.com'

metadata = {"Content-Type" : "image/jpeg"}


s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket)
data = open(file_name, 'rb');
bucket.put_object(Key=file_name, Body=data, ContentType='image/jpeg')
#s3.Object(bucket, file_name).put(Key=file_name, Body=file_name, Metadata=metadata)

