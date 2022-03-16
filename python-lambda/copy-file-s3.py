import boto3
import json
s3 = boto3.resource('s3')

def lambda_handler (event, context):
  bucket=s3.Bucket('test-s3-dev')
  dest_bucket=s3.Bucket('test-s3-dev')
  print(dest_bucket)
  print(bucket)
  x=10003
  for obj in bucket.objects.filter(Prefix='file-transfer-key’):
      dest_key=obj.key.split('dev/')[1]
      if not dest_key=="":
        dest_key=dest_key.replace('XYZ','XYZ'+str(x))
        dest_key='file-transfer-key/'+dest_key
        s3.Object(dest_bucket.name,dest_key).copy_from(CopySource= { 'Bucket': obj.bucket_name , 'Key' : obj.key})
        x+=1
        if x>250001:
          break
  print("Value of x:"+str(x))
