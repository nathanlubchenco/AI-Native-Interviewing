import pytest
from solution import evaluate

@pytest.mark.parametrize("expr, expected", [
    ("3+2*2", 7),
    (" 3/2 ", 1),
    ("(1+(4+5+2)-3)+(6+8)", 23),
    ("2*(5+5*2)/3+(6/2+8)", 21),
    ("(2+6* 3+5- (3*14/7+2)*5)+3", -12),
])
def test_evaluate(expr, expected):
    assert evaluate(expr) == expected