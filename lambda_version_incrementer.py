import json
import os

def lambda_handler(event, context):
    access_key_present = False

    try:
        if event["queryStringParameters"]["accesskey"]:
            access_key_present = True
            access_key_value = event["queryStringParameters"]["accesskey"]
            main_access_key = os.environ.get('access_key')
            if main_access_key != access_key_value:
                return{
                    'statusCode': 401,
                    'body': json.dumps("Access Denied")
                }
    except:
        pass


    if access_key_present:
        try:
            if event["queryStringParameters"]["versiondetails"]:
                version_details = event["queryStringParameters"]["versiondetails"]
        except:
            error = {
                "error":"True",
                "error_details":"request parameter absent",
                "parameter": "versiondetails"
            }
            return {
                'statusCode': 400,
                'body': json.dumps(error)
            }
        
        version_dictonary = {}
        semantic_system = ["major", "minor", "patch"]
        semantic_version = version_details.split("|")[0].split(".")
        version_boolean = version_details.split("|")[1].split(".")
        
        for value in range(3):
            version_dictonary[semantic_system[value]] = version_boolean[value]
        
        # Log History for every invocation
        print("Received version: " + str(version_details.split("|")[0]))
        print(version_dictonary)
        
        if version_dictonary["major"].lower() == "true":
            semantic_version[0] = int(semantic_version[0]) + 1
            semantic_version[1] = 0
            semantic_version[2] = 0
        
        if version_dictonary["minor"].lower() == "true":
            semantic_version[1] = int(semantic_version[1]) + 1
            semantic_version[2] = 0
        
        if version_dictonary["patch"].lower() == "true":
            semantic_version[2] = int(semantic_version[2]) + 1
            
        returned_version = str(semantic_version[0])+"."+str(semantic_version[1])+"."+str(semantic_version[2])
        print("Returned version: " + returned_version)
        
        return {
            'statusCode': 200,
            'body': json.dumps(returned_version)
        }
        
    else:
        return{
            'statusCode': 400,
            'body': json.dumps("Bad Request!!")
        }