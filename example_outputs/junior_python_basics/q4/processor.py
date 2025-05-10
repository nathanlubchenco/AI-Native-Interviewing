"""
processor.py: Processes items in batches.
"""
from batcher import batch

def process(item):
    """
    Placeholder processing function for a single item.
    """
    print(f"Processing {item}")

def process_all(items, size):
    """
    Process all items in batches of the given size.
    Bug: currently iterates over full list instead of each batch.
    """
    for b in batch(items, size):
        for item in items:
            process(item)