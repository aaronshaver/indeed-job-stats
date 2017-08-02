import uuid
import datetime
import json
import boto3
from bs4 import BeautifulSoup
import requests


def get_query_count(url):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    div = soup.find('div', {'id': 'searchCount'})
    return div.text.split()[-1]


def lambda_handler(event, context):
    client = boto3.client('dynamodb')

    query = '%22software+engineer%22'
    url = 'https://www.indeed.com/jobs?q=%s&l=Portland%2C+OR', query

    stat_id = str(uuid.uuid4())
    timestamp = str(datetime.datetime.utcnow())
    count = get_query_count(url)

    client.put_item(TableName='JobTitleCounts', Item={
        'StatId':{'S':stat_id},
        'StatTimestamp':{'S':timestamp},
        'Title':{'S':query},
        'Count':{'N':count}
    })

    return 'Done'
