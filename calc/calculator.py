from add import add
from subtract import subtract
from multiply import multiply
from division import divide

OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a, b, operator):
    if operator not in OPERATIONS:
        raise ValueError(f"Unknown operator: {operator}")
    return OPERATIONS[operator](a, b)


def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        b = float(input("Enter second number: "))
        result = calculate(a, b, operator)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
