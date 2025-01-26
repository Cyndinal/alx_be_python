
class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(cls.calculation_type)
        return a * b

# Example usage
if __name__ == "__main__":
    # Using the static method
    sum_result = Calculator.add(5, 3)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(5, 3)
    print(f"The product is: {product_result}")
