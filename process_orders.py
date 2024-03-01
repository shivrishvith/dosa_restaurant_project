import json
import sys

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
        json.dump(customers, file, indent=4)

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
        json.dump(items, file, indent=4)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 process_orders.py <filename>")
        sys.exit(1)  # Exit the script if no filename is provided
    file_name = sys.argv[1]
    orders_data = read_orders(file_name)
    create_customers_json(orders_data)
    create_items_json(orders_data)
