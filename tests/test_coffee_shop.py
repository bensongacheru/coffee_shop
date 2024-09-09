# tests/test_coffee_shop.py

import pytest
from src.coffee_shop import Customer, Coffee, Order

def test_customer_initialization():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_coffee_initialization():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_order_creation():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 4.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5

def test_customer_orders():
    customer = Customer("Charlie")
    coffee1 = Coffee("Mocha")
    coffee2 = Coffee("Cappuccino")
    customer.create_order(coffee1, 5.0)
    customer.create_order(coffee2, 6.0)
    assert len(customer.orders()) == 2
    assert len(customer.coffees()) == 2

def test_coffee_num_orders():
    coffee = Coffee("Americano")
    customer = Customer("Dana")
    customer.create_order(coffee, 3.0)
    customer.create_order(coffee, 3.5)
    assert coffee.num_orders() == 2

def test_coffee_average_price():
    coffee = Coffee("Caffè Latte")
    customer = Customer("Eve")
    customer.create_order(coffee, 4.0)
    customer.create_order(coffee, 6.0)
    assert coffee.average_price() == 5.0
