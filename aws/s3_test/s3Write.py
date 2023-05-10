import boto3, os

s3 = boto3.resource('s3')

bucket_name = os.getenv("BUCKET")
file_name = 'testfile.txt'

file_contents = 'The s3 is connected'
with open(file_name, 'w') as f:
    f.write(file_contents)

s3.meta.client.upload_file(file_name, bucket_name, file_name)
