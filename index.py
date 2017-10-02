import json

print('Loading function')

def handler(event, context):
  #print("Received event: " + json.dumps(event, indent=2))
  print("add print test")
  return "test" # Echo back the first key value

