 # Stage 5: Mathematical Expression Evaluator (Python)

 ## Description
 Implement a function `evaluate(expression: str) -> int` that evaluates a mathematical expression string and returns its integer result.
 The expression may contain:
 - Non-negative integers
 - `+`, `-`, `*`, `/` operators (integer division truncating towards zero)
 - Parentheses `(` and `)`
 - Whitespace

 **Operator Precedence**
 1. Parentheses
 2. Multiplication and division (left-associative)
 3. Addition and subtraction (left-associative)

 ## Setup
 1. Open `solution.py` and implement `evaluate`.
 2. Run the tests with:
    ```bash
    pip install pytest
    pytest test_solution.py
    ```

 ## Examples
 ```python
 >>> evaluate("3+2*2")
 7
 >>> evaluate(" 3/2 ")
 1
 >>> evaluate("(1+(4+5+2)-3)+(6+8)")
 23
 ```