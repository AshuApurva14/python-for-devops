## Automation Level 1

### Lab 1 :- Writing & Running Unit Tests with unittest
---

Create a file  `calculator.py` 

```python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

```

Use below shortcut:

- Save the file. You can use: python3 -c "..." or a heredoc, or simply run: cat > /lab/calculator.py << 'EOF' ... EOF

- Test using - python3 -c "import sys; sys.path.insert(0, '/lab'); from calculator import add, subtract, multiply, divide; print('OK')"