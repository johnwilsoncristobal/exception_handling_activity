# Base class
class Operation:
    def calculate(self, first_number, second_number):
        raise NotImplementedError

# Subclasses for each operation
class Addition(Operation):
    def calculate(self, first_number, second_number):
        return first_number + second_number

class Subtraction(Operation):
    def calculate(self, first_number, second_number):
        return first_number - second_number
        
class Multiplication(Operation):
    def calculate(self, first_number, second_number):
        return first_number * second_number
        
class Division(Operation):
    def calculate(self, first_number, second_number):
        if second_number = 0:
            raise ZeroDivisionError
        return first_number / second_number

# Main program loop
def run_calculator():
    while True:
        print("\nChoose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        try:
            choice = int(input("Enter choice (1-4): "))
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))

            operations = {
                1: Addition(),
                2: Subtraction(),
                3: Multiplication(),
                4: Division()
            }