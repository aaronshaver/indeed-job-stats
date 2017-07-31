import uuid
import datetime
import json
import boto3

print('Loading function')

def lambda_handler(event, context):
    client = boto3.client('dynamodb')

    stat_id = str(uuid.uuid4())
    timestamp = str(datetime.datetime.utcnow())
    title = 'dummy title'
    count = '3'

    client.put_item(TableName='JobTitleCounts', Item={
        'StatId':{'S':stat_id},
        'StatTimestamp':{'S':timestamp},
        'Title':{'S':title},
        'Count':{'N':count}
    })
    return 'Done'
