# Q1(b)
class A:
          def __init__(self,n='Adam'):
	          self.name = n
class B(A):
          def __init__(self,roll):
                    self.rollno=roll

object = B(23)
print(object.name)