import boto3
import json
import time
s3 = boto3.resource('s3')

def lambda_handler (event, context):
  bucket=s3.Bucket('mcm-s3-jumpstart-dev')
  dest_bucket=s3.Bucket('mcm-s3-jumpstart-dev')
  print(dest_bucket)
  print(bucket)
  x=0
  for obj in bucket.objects.filter(Prefix='jumpstart-to-nahan-sftp-transfer-dev'):
      dest_key=obj.key.split('dev/')[1]
      if not dest_key=="":
        ts=time.time()
        dest_key=dest_key.replace('XYZ','XYZ'+str(ts))
        dest_key='jumpstart-to-nahan-sftp-transfer-dev/'+dest_key
        s3.Object(dest_bucket.name,dest_key).copy_from(CopySource= { 'Bucket': obj.bucket_name , 'Key' : obj.key})
        x=x+1
        if x>538:
          break
  print("Value of x:"+str(x))
