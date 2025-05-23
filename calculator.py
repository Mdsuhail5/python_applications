from art import calc


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(calc)

    num1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        for op in operations:
            print(op)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        function = operations[operation_symbol]
        answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
