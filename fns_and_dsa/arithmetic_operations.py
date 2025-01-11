def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return ZeroDivisionError("division by zero")
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"


print("The arithmetic_operations.py script has been created successfully.")



# def perform_operation(num1,num2,operation):
#     # num1 =float(input("Numb1"))
#     # num2 =float(input("Numb2"))
#     # operation = input("Enter the operation to be performed: add/subtract/multiply/divide").lower()
#     match operation:
#         case "add":
#             result = num1+num2
#             return result
#         case "subtract":
#             result = num1-num2
#             return result
#         case "multiply":
#             result = num1*num2
#             return result
#         case "divide":
#             try:
#                 result = num1/num2
#                 return result
#             except ZeroDivisionError:
#                 return f"{num1} cannot be divided by zero"
#
#         case _:
#             print("Invalid operation")


