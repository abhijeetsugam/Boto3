import boto3

s3 = boto3.client('s3')

# delete all files from s3 bucket
bucket_name = 'sugam-buc-1'
response = s3.list_objects(Bucket=bucket_name)



for key in response['Contents']:
    if key['Key'].startswith('json') or key['Key'].startswith('csv'):
        continue
    s3.delete_object(Bucket=bucket_name, Key=key['Key'])


# delete bucket
s3.delete_bucket(Bucket=bucket_name)



