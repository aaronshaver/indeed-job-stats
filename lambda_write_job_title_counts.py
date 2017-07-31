import datetime
import json
import boto3

print('Loading function')

def lambda_handler(event, context):
    client = boto3.client('dynamodb')

    timestamp = str(datetime.datetime.utcnow())
    client.put_item(TableName='job_title_counts', Item={
        'StatId':{'N':'456'},'StatTimestamp':{'S':timestamp}
    })
    return 'Done'
