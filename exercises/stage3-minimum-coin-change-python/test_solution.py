import pytest
from solution import min_coins

def test_examples():
    assert min_coins([1, 2, 5], 11) == 3
    assert min_coins([2], 3) == -1
    assert min_coins([1], 0) == 0
    assert min_coins([2, 5, 10, 1], 27) == 4

def test_edge_cases():
    assert min_coins([], 0) == 0
    assert min_coins([], 1) == -1
    assert min_coins([1], 1) == 1

def test_large():
    coins = list(range(1, 101))
    amount = 10000
    # Best is using 100 coins of denomination 100 => 100
    assert min_coins(coins, amount) == 100