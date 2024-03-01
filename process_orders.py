import json

def read_orders(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def create_customers_json(orders):
    customers = {order['customer']['phone']: order['customer']['name'] for order in orders}
    with open('customers.json', 'w') as file:
        json.dump(customers, file)

def create_items_json(orders):
    items = {}
    for order in orders:
        for item in order['items']:
            if item['name'] not in items:
                items[item['name']] = {'price': item['price'], 'orders': 1}
            else:
                items[item['name']]['orders'] += 1
    with open('items.json', 'w') as file:
        json.dump(items, file)

if __name__ == '__main__':
    orders_data = read_orders('example_orders.json')
    create_customers_json(orders_data)
    create_items_json(orders_data)