# Produce Python code that demonstrate the concept of multiple
# Inheritance also brief about its classification with appropriate
# block diagram?
# 
# Multiple Inheritance

# Base class 1:
class Animal:
    def speak(self):
        print("Animal Speaks")


# Base class 2:
class Mammal:
    def eat(self):
        print("Mamal eats")


# Derived class inheriting from both Animal and Mammal
class Dog(Animal, Mammal):
    def bark(self):
        print("Dog Barks")


# Create an instance of Dog and demonstrate multiple inheritance
my_dog = Dog()
my_dog.speak()
my_dog.eat()
my_dog.bark()

# Develop code for the concept of Exceptional Handling in Python
# object-oriented environment.

class Calculator:
    def divide(self, numerator, denominator):
        try:
            result = numerator / denominator
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except TypeError:
            print("Error: Please provide valid numeric values for division.")
        else:
            print(f"Result of division: {result}")
        finally:
            print("Division operation completed.")


# Create an instance of the Calculator class
calculator = Calculator()

# Example 1: Division with valid inputs
calculator.divide(10, 2)

# Example 2: Division by zero
calculator.divide(8, 0)

# Example 3: Division with invalid input type
calculator.divide("abc", 2)