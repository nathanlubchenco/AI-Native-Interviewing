++ exercises/stage3-modular-python-advanced/ecommerce/orders.py
from ecommerce.products import Product
from ecommerce.inventory import Inventory

class Order:
    def __init__(self, order_id: int, inventory: Inventory):
        self.order_id = order_id
        self.inventory = inventory
        self.items = []  # list of tuples (Product, quantity)

    def add_item(self, product: Product, quantity: int):
        """
        Reserve stock for the given product and add to the order.
        """
        raise NotImplementedError

    def get_total(self) -> float:
        """
        Calculate total price of the order, applying a 10% discount
        if the pre-discount total exceeds 20.0.
        """
        raise NotImplementedError