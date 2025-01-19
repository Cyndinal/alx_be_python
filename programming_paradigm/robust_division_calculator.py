# Division by Zero: Use a try-except block to catch ZeroDivisionError.
# Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch
# ValueError for non-numeric inputs.
# Return appropriate messages for errors or the result for successful division.



# def safe_divide(numerator, denominator):
#     numerator = float(numerator)
#     denominator = float(denominator)
#     try:
#         result =numerator / denominator
#         return f"{result} Success!"
#     except ZeroDivisionError:
#         return "Error: Cannot divide by zero"
#     except ValueError:
#         return "Error: Non-numeric input provided. Please enter valid numbers."
#

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division
        result = numerator / denominator
        return f"The result is {result:.2f}"

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    except ValueError:
        return "Error: Non-numeric input provided. Please enter valid numbers."