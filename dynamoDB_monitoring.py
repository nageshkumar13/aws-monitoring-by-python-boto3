import boto3
from json_operations import saveJsonData

session = boto3.Session(profile_name='dd-sol', region_name="ap-south-1")
db_client = session.client('dynamodb')

response = db_client.list_tables()

responses = response['TableNames']

current_db = []

for res in responses:
    dct = {}
    print(res)
    describe = db_client.describe_table(TableName=res)
    print(describe['Table']['TableStatus'])
    print(describe['Table']['CreationDateTime'])
    status = describe['Table']['TableStatus']
    new_date = describe['Table']['CreationDateTime'].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    dct['dB_Name'] = res
    dct['created_time'] = new_date
    dct['Status'] = status
    current_db.append(dct)

print(current_db)
saveJsonData('db_monitoring.json', current_db)
