import sys

def add(first, second):
    print(first + second)
def substract(first, second):
    print(first - second)
def multiply(first, second):
        print(first * second)
def divide(first, second):
    print(first / second)


def type_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                exit()

first = type_int("Enter a number(or a letter to exit): ")
operation = input("Enter an operator: ")
second = type_int("Enter second number: ")

if operation == "+":
        result = first + second
        print("Result:", result)
elif operation == "-":
        result = first - second
        print("Result:", result)
elif operation == "*":
        result = first * second
        print("Result:", result)
elif operation == "/":
        result = first / second
        print("Result:", result)
else:
        print("Invalid sign")
