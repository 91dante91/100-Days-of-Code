from replit import clear
from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        result = operations.get(operation_symbol)(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if answer == "y":
            num1 = result
        else:
            should_continue = False
            clear()
            calculator()


calculator()
