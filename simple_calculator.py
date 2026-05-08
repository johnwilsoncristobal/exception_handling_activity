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