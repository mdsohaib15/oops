# Q3(a)Solve Y*x using oop. In this program method "calculate " does the calculation and method "display" displays the result . values of X and Y are assigned to the object of class.solve the problem using oop concepts  

class EquationSolver:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.result = None

    def calculate(self):
        self.result = self.y * self.x

    def display(self):
        if self.result is not None:
            print(f"The result of {self.y} * {self.x} is: {self.result}")
        else:
            print("Result has not been calculated. Call the 'calculate' method first.")

# Create an object of the EquationSolver class
equation_solver = EquationSolver(x=5, y=8)

# Call the calculate method to perform the calculation
equation_solver.calculate()

# Call the display method to show the result
equation_solver.display()
