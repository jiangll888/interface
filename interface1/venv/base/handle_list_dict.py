import json

def handle(data):
    data = json.loads(data)
    for key,value in data.items():
        if  isinstance(value,dict) or isinstance(value,list):
            print(key,value)
            data[key] = json.dumps(value)

    return json.dumps(data)