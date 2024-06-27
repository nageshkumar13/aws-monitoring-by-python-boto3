import os
import logging
import json
import boto3
from botocore.exceptions import ClientError
from boto3.s3.transfer import TransferConfig
import requests
from json_operations import saveJsonData


# defining function listing bucket
def list_buckets( region="ap-south-1"):    
    session = boto3.Session(profile_name='dd-sol')
    dd_s3_client = session.client('s3')
    try:            
        response = dd_s3_client.list_buckets()
        print('Existing buckets:')
        current_buckets = []
        
        for bucket in response['Buckets']:
            bckt = {}            
            #print(f'  {bucket}')            
            new_date = bucket["CreationDate"].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            bckt["Name"] = bucket['Name']
            bckt["CreationDate"] = f"{new_date}"
            current_buckets.append(bckt)
        print(current_buckets)
        saveJsonData("s3_data.json", current_buckets)
    except ClientError as e:
        logging.error(e)
        return False
    return True


bucket_name = ""
# specifying region where we want to create the bucket
region_name = "ap-south-1"

# Listing all the buckets in the region
list_buckets(region_name)

