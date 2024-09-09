# Coffee Shop

## Overview

The Coffee Shop project is a simple Python application that models a coffee shop system. It includes classes for customers, coffees, and orders, allowing for the creation and management of orders and retrieval of information about customers and coffees.

## Classes

### Customer

Represents a customer of the coffee shop.

- **Attributes:**
  - `name`: A string representing the name of the customer. Must be between 1 and 15 characters.
  - `_orders`: A list of orders placed by the customer.

- **Methods:**
  - `create_order(coffee, price)`: Creates a new order with the specified coffee and price, and adds it to the customer's order list.
  - `orders()`: Returns a list of all orders placed by the customer.
  - `coffees()`: Returns a list of unique coffees ordered by the customer.

### Coffee

Represents a type of coffee available at the shop.

- **Attributes:**
  - `name`: A string representing the name of the coffee. Must be at least 3 characters long.
  - `_orders`: A list of orders containing this coffee.

- **Methods:**
  - `orders()`: Returns a list of all orders that include this coffee.
  - `customers()`: Returns a list of unique customers who have ordered this coffee.
  - `num_orders()`: Returns the number of orders for this coffee.
  - `average_price()`: Returns the average price of this coffee across all orders.

### Order

Represents an order placed by a customer for a coffee.

- **Attributes:**
  - `customer`: The customer who placed the order.
  - `coffee`: The coffee ordered.
  - `price`: The price of the coffee in the order.

## Installation

To use this code, you'll need Python installed on your system. You also need to install `pytest` for running the tests.

```bash
pip install pytest

## License

MIT License

Copyright (c) [2024] [Benson Mwangi]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

