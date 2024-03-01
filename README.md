# Dosa Restaurant Order Processor

This Python application processes customer orders for a Dosa restaurant, reading from a JSON file to generate two key outputs: a customer directory (`customers.json`) and an itemized summary (`items.json`). The customer directory associates phone numbers with names, while the itemized summary details menu items, their prices, and order frequency.

## Setup

Ensure Python 3 is installed on your machine. Clone this repository to your local environment to get started.

### Requirements

- Python 3.x

### Running the Application

To process the orders, navigate to the project directory in your terminal and execute:

```bash
python3 process_orders.py example_orders.json       #This command initiates the script with example_orders.json as the input file. Adjust the filename as needed based on the actual input file you wish to process.


##Project Structure

process_orders.py: The script that reads and processes order data.
example_orders.json: A sample file containing order data.
customers.json: Output file mapping customer phone numbers to names.
items.json: Output file detailing menu items, prices, and order counts.


#Contributions

Contributions are welcome. Please fork the repository and submit pull requests for review. For significant changes, open an issue first to discuss what you'd like to change.

#More info
Replace `python3 process_orders.py example_orders.json` with the correct command if your setup requires something different. This README provides a clear, concise guide to understanding, setting up, and running your project, suitable for inclusion in your GitHub repository.
