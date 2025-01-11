FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    print(f"{(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR}°C")


def convert_to_fahrenheit(celsius):
    print(f"{(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32}°F")



prompt = int(input("Enter the temperature in Fahrenheit or Celsius: "))
celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()

match celsius_or_fahrenheit:
    case "C":
        convert_to_fahrenheit(prompt)
    case "F":
        convert_to_celsius(prompt)
    case _:
        print("Invalid input, Enter C or F ")

