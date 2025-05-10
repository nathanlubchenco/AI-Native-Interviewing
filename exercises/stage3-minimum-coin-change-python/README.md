 # Stage 3: Minimum Coin Change (Python)

 ## Description
 Implement a function `min_coins(coins: List[int], amount: int) -> int` that returns the minimum number of coins required to make up the given `amount`. If it is not possible to make the amount with the provided coins, return `-1`.

 **Constraints**
 - `0 <= amount <= 10_000`
 - `1 <= len(coins) <= 100`
 - `coins[i]` are positive integers

 **Objective**
 - Write a dynamic programming solution that runs in O(amount * len(coins)) time.

 ## Setup
 1. Open `solution.py` and implement `min_coins`.
 2. Run the tests with:
    ```bash
    pip install pytest
    pytest test_solution.py
    ```

 ## Examples
 ```python
 >>> min_coins([1, 2, 5], 11)
 3
 >>> min_coins([2], 3)
 -1
 >>> min_coins([1], 0)
 0
 ```