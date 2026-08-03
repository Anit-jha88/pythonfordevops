import boto3

s3 = boto3.client('s3')

# for bucket in s3.buckets.all():
#         print(bucket.name)


file_name = "D:/pythonfordevops/day1/api.py"
bucket ="pythons3devops";
object_name="api.py";
response = s3.upload_file(file_name, bucket, object_name)

