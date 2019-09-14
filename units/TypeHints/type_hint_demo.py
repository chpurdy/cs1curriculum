"""
A demo program showing how type hints work
"""

def sum_two(a: int, b: int) -> int:
    return a + b

print(sum_two("hello", "goodbye"))
