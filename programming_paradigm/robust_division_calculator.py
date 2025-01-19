# Division by Zero: Use a try-except block to catch ZeroDivisionError.
# Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch
# ValueError for non-numeric inputs.
# Return appropriate messages for errors or the result for successful division.



def safe_divide(numerator, denominator):
    try:
        result =numerator / denominator
        return f"{result} Success!"
    except ZeroDivisionError:
        return 0
    except ValueError:
        return "Input must be a number."
