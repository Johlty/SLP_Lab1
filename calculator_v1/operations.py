import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

def square_root(num1):
    if num1 < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(num1)

def modulo(num1, num2):
    return num1 % num2
