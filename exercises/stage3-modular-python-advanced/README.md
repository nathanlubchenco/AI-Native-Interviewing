++ exercises/stage3-modular-python-advanced/README.md
# Stage 3: Modular Python Advanced Exercise

In this exercise, you will work with a simple e-commerce system structured as a Python package. The goal is to implement missing functionality across multiple modules, manage inventory, process orders, and handle concurrency.

Directory structure:
```
exercises/stage3-modular-python-advanced/
├── ecommerce/
│   ├── __init__.py
│   ├── products.py
│   ├── inventory.py
│   └── orders.py
└── main.py
```

Requirements:
1. Implement `Inventory.add_stock(product, quantity)` to add stock for a product.
2. Implement `Inventory.reserve(product, quantity)` to reserve stock or raise `ValueError` if insufficient.
3. Ensure `Inventory` is thread-safe by using a lock (import `threading`).
4. In `Order` class:
   - Implement `add_item(product, quantity)` to reserve stock and track items in the order.
   - Implement `get_total()` to calculate total price.
   - Apply a 10% discount if the total before discount exceeds 20.0.
5. In `main.py`, demonstrate:
   - Adding stock and creating products.
   - Creating multiple orders in concurrent threads against the same `Inventory`.
   - Handling out-of-stock errors gracefully.
   - Printing order totals and any errors.

You may add helper methods or classes as needed. You are encouraged to write tests to validate thread safety and correctness.