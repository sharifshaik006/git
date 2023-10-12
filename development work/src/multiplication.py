# addition.py
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

# subtraction.py
def subtract(a, b):
    return a - b

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(1, -1) == 2

# multiplication.py
def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(1, -1) == -1
