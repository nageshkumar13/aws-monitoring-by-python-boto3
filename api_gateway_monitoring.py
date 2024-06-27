import boto3
from json_operations import saveJsonData

session = boto3.Session(profile_name='dd-sol', region_name="ap-south-1")
api_client = session.client('apigateway')

responses = api_client.get_rest_apis()

current_apis = []

for res in responses['items']:
    apis = {}
    new_date = res["createdDate"].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    apis["ID"] = res['id']
    apis['Api_Name'] = res['name']
    apis['description'] = res['description']
    apis['Created_date_time'] = new_date
    apis['endpointConfiguration'] = res['endpointConfiguration']['types']
    current_apis.append(apis)

print(current_apis)
saveJsonData("apis_monitoring.json", current_apis)