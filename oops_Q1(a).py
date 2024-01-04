# Q1(a)apply inheritance concepets, write a class polygon with a method that takes number of sides as input and another method that displays it.create a subclass triangle , which calls input and display methods from the parent class and contains a method to calculate the area of triangle.create object for triangle and call methods to take input, calculate area of a triangle and display the result and show the output. 
class Polygon:
    def __init__(self):
        self.abc = {} 
    def Input(self):
        self.numOfSides = int(input('Enter Number of Sides '))
        for i in range(1,self.numOfSides+1):
           self.abc[i] = float(input(f'Enter Length{i}: '))
    def Display(self):
        print(f'{self.numOfSides} Sides of Shape:\n ')
        for iter in range(1,self.numOfSides+1):
            print(f'{iter} Value: {self.abc[iter]}\n')
class Triangle(Polygon):
    def __init__(self):
        super()._init_()
        super().Input()
        super().Display()
    def AreaofTriangle(self):
        if self.numOfSides == 2:
            self.areaofTriangle = 0.5*self.abc[1] * self.abc[2] 
            print(f'Area of Triangle: {self.areaofTriangle}')
p = Triangle()
p.AreaofTriangle()