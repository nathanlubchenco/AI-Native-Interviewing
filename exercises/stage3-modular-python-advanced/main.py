++ exercises/stage3-modular-python-advanced/main.py
from threading import Thread
from ecommerce.products import Product
from ecommerce.inventory import Inventory
from ecommerce.orders import Order

def create_order(order_id, inventory, items):
    order = Order(order_id, inventory)
    for product, quantity in items:
        try:
            order.add_item(product, quantity)
        except ValueError as e:
            print(f"Order {order_id}: {e}")
    try:
        total = order.get_total()
        print(f"Order {order_id} total: {total}")
    except Exception as e:
        print(f"Order {order_id}: failed to calculate total: {e}")

def main():
    inventory = Inventory()
    # Setup products
    apple = Product(1, "Apple", 0.5)
    banana = Product(2, "Banana", 0.3)
    cherry = Product(3, "Cherry", 1.0)

    # Add initial stock
    inventory.add_stock(apple, 10)
    inventory.add_stock(banana, 5)
    inventory.add_stock(cherry, 20)

    # Define orders to run concurrently
    orders = [
        (100, [(apple, 3), (banana, 2)]),
        (101, [(banana, 4), (cherry, 5)]),
        (102, [(apple, 8), (cherry, 10)]),
        (103, [(cherry, 15)]),
    ]

    threads = []
    for order_id, items in orders:
        t = Thread(target=create_order, args=(order_id, inventory, items))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()