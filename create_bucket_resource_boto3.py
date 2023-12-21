import boto3


# create s3 bucket with RESOURCE

s3 = boto3.resource('s3')
bucket = s3.Bucket('name')
response = bucket.create( Bucket='sugam-buc-2')

# list all buckets  
for bucket in s3.buckets.all():
    print(bucket.name)