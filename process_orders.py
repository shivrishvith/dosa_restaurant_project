import json

def read_orders(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def create_customers_json(orders):
    customers = {}
    for order in orders:
        phone = order['phone']
        name = order['name']
        customers[phone] = name
    with open('customers.json', 'w') as file:
        json.dump(customers, file)

def create_items_json(orders):
    items = {}
    for order in orders:
        for item in order['items']:
            name = item['name']
            price = item['price']
            if name not in items:
                items[name] = {'price': price, 'orders': 1}
            else:
                items[name]['orders'] += 1
    with open('items.json', 'w') as file:
        json.dump(items, file)

if __name__ == '__main__':
    orders_data = read_orders('example_orders.json')  # Ensure this path is correct
    create_customers_json(orders_data)
    create_items_json(orders_data)
