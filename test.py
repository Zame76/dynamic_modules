# This will be a module run by timer
def calculate(a, b):
    return a * b

def execute():
    x = 5
    y = 7
    op = calculate(x, y)
    print(f"test.py calculates value of {x} * {y} which is {op}")
