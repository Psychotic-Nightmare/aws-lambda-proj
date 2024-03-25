import json

def lambda_handler(event, context):
    # If testing locally, read the test event from a JSON file
    if event.get('source') == 'local':
        with open('test_event.json', 'r') as file:
            event = json.load(file)
    
    # Your Lambda function logic goes here
    response = {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda!")
    }
    return response
