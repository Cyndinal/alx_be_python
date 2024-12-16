from pygments.lexer import default

first = int(input("Enter the first number:"))
second = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        print(f"The result is {first + second}")
    case "-":
        print(f"The result is {first - second}")
    case "*":
        print(f"The result is {first * second}")
    case "/":
        try:
            print(f"The result is {first / second}")
        except ZeroDivisionError:
            print("Cannot divide by zero")







