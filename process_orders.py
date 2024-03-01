import json

def read_orders(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def create_customers_json(orders):
    customers = {order['customer']['phone']: order['customer']['name'] for order in orders}
    with open('customers.json', 'w') as file:
        json.dump(customers, file)