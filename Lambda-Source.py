# This code will invoke another lambda 

import boto3, json
def lambda_handler(event, context):
	#change region_name as per the destination lambda function region
    invokeLam = boto3.client("lambda", region_name="ap-south-1")
    payload = {"message": "Hiii, Lambda has been invoked."}

    #For InvocationType = "RequestResponse"
    resp = invokeLam.invoke(FunctionName = "Lambda-Destination", InvocationType = "RequestResponse", Payload = json.dumps(payload))
    print(resp["Payload"].read())

    #For InvocationType = "Event"
    resp = invokeLam.invoke(FunctionName = "Lambda-Destination", InvocationType = "Event", Payload = json.dumps(payload))
    return 'Thanks'
