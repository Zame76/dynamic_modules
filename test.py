# exec(8,7)

# This will be a module run by timer
def calculate(a, b):
    return a * b

def exec(x = 0, y = 0):
    op = calculate(x, y)
    print(f"test.py calculates value of {x} * {y} which is {op}")
