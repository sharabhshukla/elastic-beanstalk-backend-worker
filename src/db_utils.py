import awswrangler as wr
import boto3
import pandas as pd
from typing import List

dynamodb = boto3.resource('dynamodb')
session = boto3.Session(region_name='us-east-1')

# Create an entry in dynamodb using boto3
def create_entry(table_name: str, item: dict):
    wr.dynamodb.put_items(
        table_name=table_name,
        items=[item],
        boto3_session=session
    )
    return "Success!!"


# Update an entry in dynamodb using boto3
def update_job_status(username, job_id, new_status):
    table = dynamodb.Table('job-status')

    response = table.update_item(
        Key={
            'username': username,
            'jobid': job_id
        },
        UpdateExpression='SET job_status = :status',
        ExpressionAttributeValues={
            ':status': new_status
        },
        ReturnValues='UPDATED_NEW'
    )

    return response['Attributes']
