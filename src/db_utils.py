import boto3


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
session = boto3.Session(region_name='us-east-1')


# Create an entry in dynamodb using boto3
def create_entry(table_name: str, item: dict):
    # Get a reference to the DynamoDB table
    table = dynamodb.Table(table_name)

    # Write the item to the table
    table.put_item(Item=item)

    print(f"Successfully wrote item to table {table_name}")
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
