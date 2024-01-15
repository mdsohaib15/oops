# ------Public Access Modifier---------
class Employee:
          def __init__(self,name,age):
                    self.name = name
                    self.age = age
          def display(self):
                    print("Employee Name: ",self.name)
                    print("Employee Age: ",self.age)
e1 = Employee("Joe",29)
e1.display()