import math


def square (x):
    square = x*x
    return square


x = float(input())
result = square (x)
rounded = math.ceil(result)
print(rounded)

