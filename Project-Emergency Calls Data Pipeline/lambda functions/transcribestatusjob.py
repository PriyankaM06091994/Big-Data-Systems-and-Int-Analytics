import json
import boto3
def lambda_handler(event, context):
    client = boto3.client('transcribe',aws_access_key_id ='AKIAXZLTWQIDYOIAK4WU' ,aws_secret_access_key = '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' ,region_name = 'us-east-1')
    responsecheck = client.get_transcription_job(
                TranscriptionJobName=event['params']['querystring']['jobname']
            )
    print(responsecheck)
    return {
        'body': responsecheck['TranscriptionJob']['TranscriptionJobStatus']
    }