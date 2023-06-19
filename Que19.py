'''
Write a Python program to create a calculator class. Include methods for
basic arithmetic operations.
'''
class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Error: Division by zero is not allowed.")


# Create an instance of the Calculator class
calculator = Calculator()

# Perform arithmetic operations until the user chooses to exit
while True:
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == '5':
        break

    try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = calculator.add(num1, num2)
            operation = "Addition"
        elif choice == '2':
            result = calculator.subtract(num1, num2)
            operation = "Subtraction"
        elif choice == '3':
            result = calculator.multiply(num1, num2)
            operation = "Multiplication"
        elif choice == '4':
            result = calculator.divide(num1, num2)
            operation = "Division"
        
        print(f"{operation} Result: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.\n")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.\n")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

print("Calculator program exited.")
