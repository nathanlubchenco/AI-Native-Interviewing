"""
batcher.py: Utility to split a list of items into batches.
"""
def batch(items, size):
    """
    Divide the list 'items' into chunks of length 'size'.
    Returns a list of batches (sublists).
    """
    batches = []
    for i in range(0, len(items), size):
        batches.append(items[i:i+size])
    return batches