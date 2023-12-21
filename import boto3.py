import boto3
import json
import os
# Create an S3 client
s3 = boto3.client('s3')
#get all buckets
response = s3.list_buckets()
# response = json.loads(response)
# Print out bucket names
# print(type(response.get('Buckets')))
bucket_name = None
for key, val in response.items():
    if key == 'Buckets':
        for val2 in val:
            print(val2['Name'])
            if val2['Name'].startswith('de-you-raw-'):
                bucket_name = val2['Name']


# print all files name from folder
# for item in os.listdir('C:/Users/abhij/OneDrive/Documents/DE_project/youtube_project'):
#     if item.endswith(".json"):
#         # upload file to s3 bucket
#         s3.upload_file('C:/Users/abhij/OneDrive/Documents/DE_project/youtube_project/'+item, bucket_name, item)

# print all files name from bucket
response = s3.list_objects(Bucket=bucket_name)
print(response)
