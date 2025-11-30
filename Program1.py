Problem 1


def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operation")


a = float(input("Enter a: "))
b = float(input("Enter b: "))
op = input("Enter operation (+, -, *, /): ")

print("Result:", calculate(a, b, op))
