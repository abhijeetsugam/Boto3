import boto3
import os
import json

#create s3 bucket  using CLIENT

s3 = boto3.client('s3')
response = s3.create_bucket(Bucket='sugam-buc-1')
# print(response)

# list all buckets

response = s3.list_buckets()
# print(response)

#listing only the name of buckets
for key, val in response.items():
    if key == 'Buckets':
        for val2 in val:
            print(val2['Name'])
            if val2['Name'].startswith('sugam-buc-1'):
                bucket_name = val2['Name']

# print all files name from folder
for item in os.listdir('C:/Users/abhij/OneDrive/Documents/DE_project/youtube_project'):
    if item.endswith(".json"):
        # upload json file to s3 bucket
        s3.upload_file('C:/Users/abhij/OneDrive/Documents/DE_project/youtube_project/'+item, bucket_name, "json/"+item)
        # upload csv file to s3 bucket
    elif item.endswith(".csv"):
        s3.upload_file('C:/Users/abhij/OneDrive/Documents/DE_project/youtube_project/'+item, bucket_name, "csv/"+item)

response = s3.list_objects(Bucket=bucket_name)
print(response)