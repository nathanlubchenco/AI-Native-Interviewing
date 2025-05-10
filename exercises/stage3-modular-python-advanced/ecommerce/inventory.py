++ exercises/stage3-modular-python-advanced/ecommerce/inventory.py
from ecommerce.products import Product
import threading

class Inventory:
    def __init__(self):
        self.stock = {}  # product_id -> quantity
        self._lock = threading.Lock()

    def add_stock(self, product: Product, quantity: int):
        """
        Add quantity of product to stock in a thread-safe manner.
        """
        raise NotImplementedError

    def reserve(self, product: Product, quantity: int):
        """
        Reserve quantity of product if available, else raise ValueError.
        Must be thread-safe.
        """
        raise NotImplementedError