# my_api.py
# This file is the "API" — a set of functions your student can call from their own program.


def greet(name):
    """Returns a greeting string for the given name."""
    return f"Hello, {name}! Welcome to the API."


def shout(text):
    """Returns the text in ALL CAPS with an exclamation mark."""
    return text.upper() + "!"


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b
