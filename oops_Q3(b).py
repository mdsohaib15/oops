# Q3(b)
class Base(object):
          def __init__(self, name):
                    self.name = name 
          def getName(self):
                    return self.name

class Child(Base):
          def __init__(self, name, age):
                    Base.__init__(self,name)
                    def getAge(self):
                              return self.age

class GrandChild(Child):
          def __init__(self,name,age,address):
                    Child.__init__(self,name,age)
                    self.address=address
          def getAddress(self):
                    return self.address
g = GrandChild("Object1",23,"Warwick")
print(g.getName(),g.getAge(),g.getAddress())