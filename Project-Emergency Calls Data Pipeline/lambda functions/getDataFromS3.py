import json
import boto3
def lambda_handler(event, context):
    s3 = boto3.resource('s3',aws_access_key_id ='AKIAXZLTWQIDYOIAK4WU' ,aws_secret_access_key = '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' ,region_name = 'us-east-1')
    bucket = s3.Bucket('transcribe-audiototext1')

    for obj in bucket.objects.all():
        if obj.key == event['params']['querystring']['jobname'] + '.json':
            key = obj.key
            body = obj.get()['Body'].read()
            text = json.loads(body)
            print(text)
            
    return {
        'body': text['results']['transcripts'][0]['transcript']
    }
