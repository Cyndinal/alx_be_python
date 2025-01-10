from numpy.f2py.auxfuncs import throw_error


def perform_operation(num1,num2,operation):
    # num1 =float(input("Numb1"))
    # num2 =float(input("Numb2"))
    # operation = input("Enter the operation to be performed: add/subtract/multiply/divide").lower()
    match operation:
        case "add":
            result = num1+num2
            return result
        case "subtract":
            result = num1-num2
            return result
        case "multiply":
            result = num1*num2
            return result
        case "divide":
            try:
                result = num1/num2
                return result
            except ZeroDivisionError:
                if num2 == 0:
                    throw_error(f"{num2} cannot be zero, Review!")
        case _:
            print("Invalid operation")


