import os
import logging
import json
import boto3
from botocore.exceptions import ClientError
import requests
from json_operations import saveJsonData


   
session = boto3.Session(profile_name='dd-sol', region_name="ap-south-1")
dd_lambda_client = session.client('lambda', region_name="ap-south-1")

responses = dd_lambda_client.list_functions()

current_lamdas = []

for res in responses["Functions"]:
    dct = {}    
    dct["FunctionName"] = res["FunctionName"]
    dct["Runtime"]      = res["Runtime"]
    dct["Handler"]      = res["Handler"]
    dct["CodeSize"]     = res["CodeSize"]
    dct["Description"]  = res["Description"]
    dct["MemorySize"]   = res["MemorySize"]
    current_lamdas.append(dct)
saveJsonData("lambda_monitoring_data.json", current_lamdas)    

print(current_lamdas)