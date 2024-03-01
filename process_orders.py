import json

def read_orders(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)
