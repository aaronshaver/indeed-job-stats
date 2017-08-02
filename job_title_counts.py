import uuid
import datetime
import json
import boto3
from bs4 import BeautifulSoup
import requests

print('Loading function')



def lambda_handler(event, context):
    client = boto3.client('dynamodb')

    url = 'https://www.indeed.com/jobs?q=%22software+engineer%22&l=Portland%2C+OR'
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)

    for link in soup.find_all('a'):
        print(link.get('href'))

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
