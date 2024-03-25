import json
from lambda_function import lambda_handler

# Read test event from JSON file
with open('test_event.json', 'r') as file:
    test_event = json.load(file)

# Invoke Lambda function
result = lambda_handler(test_event, None)

# Print result
print(result)
