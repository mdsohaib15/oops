# import calendar
# for i in range(2023,2025):
#           for j in range(1,13):
#                     print(calendar.month(i,j))

class Person:
    def __init__(self, name, age, _id):
        self.name = name
        self.age = age
        self._id = _id

    def display(self):
        print("Name is:", self.name)
        print("Age is:", self.age)
        print("Id of person is:", self._id)

class Student(Person):
    def __init__(self, name, age, _id, marks):
        super().__init__(name, age, _id)
        self.marks = marks

    def display(self):
        super().display()
        print("Marks:", self.marks)

person = Person("Chris", 23, 102)
person.display()

student = Student("Ashley", 20, 111, 99)
student.display()

