# Interactive Calculator and Unit Converter

# Conversion factors
KM_TO_MILES = 0.621371
KG_TO_POUNDS = 2.20462


# Safe number reader
def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


# Arithmetic functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Error! Cannot divide by zero.")
        return None
    return a / b


# Unit conversion functions
def km_to_miles(km):
    return km * KM_TO_MILES


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def kg_to_pounds(kg):
    return kg * KG_TO_POUNDS


# Unit converter menu
def unit_converter():
    while True:
        print("\n===== UNIT CONVERTER =====")
        print("1. Kilometres to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Kilograms to Pounds")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            value = read_number("Enter kilometres: ")
            print("Miles:", round(km_to_miles(value), 2))

        elif choice == "2":
            value = read_number("Enter Celsius: ")
            print("Fahrenheit:",
                  round(celsius_to_fahrenheit(value), 2))

        elif choice == "3":
            value = read_number("Enter kilograms: ")
            print("Pounds:", round(kg_to_pounds(value), 2))

        elif choice == "4":
            break

        else:
            print("Invalid choice! Try again.")


# Main calculator program
def main():
    while True:
        print("\n===== INTERACTIVE CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Unit Converter")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "6":
            print("Thank you for using the calculator!")
            break

        elif choice == "5":
            unit_converter()

        elif choice in ["1", "2", "3", "4"]:
            num1 = read_number("Enter first number: ")
            num2 = read_number("Enter second number: ")

            if choice == "1":
                result = add(num1, num2)

            elif choice == "2":
                result = subtract(num1, num2)

            elif choice == "3":
                result = multiply(num1, num2)

            else:
                result = divide(num1, num2)

            if result is not None:
                print("Result:", result)

        else:
            print("Invalid choice! Please select 1 to 6.")


# Start the program
if __name__ == "__main__":
    main()