import boto3

s3 = boto3.resource('s3') #connection to aws s3 

def show_all_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def upload_to_bucket(s3,file_name,bucket_name,source_path):
    data = open(source_path,'rb')
    s3.Bucket(bucket_name).put_object(key=file_name,Body=source_path)
    print("Backup stored to S3")

source_path = "/home/subhradeep/backups/backup_2025-06-05.tar.gz"
bucket_name = "trainwithshubham"
file_name = "backup_2025-06-05.tar.gz"

upload_to_bucket(s3,file_name,bucket_name,source_path)