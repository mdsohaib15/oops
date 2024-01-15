# -------POLYMORPHISM------
'''Poly ---> manuy
morphism ---> forms'''
x=3
print(x)
x="DUET"
print(len(x))
# -----User Defined Polymorpishm--------
def add(a,b,c=1):
          return a+b+c
print(add(2,3,4)) #>output:9
print(add(2,3)) #>output:6


#-----class-object polymorphism----
class Pakistan:
          def capital(self):
                    print("Islamabad")
          def famous_food(self):
                    print("Biryani")
          def sports(self):
                    print("Cricket")
class India:
          def capital(self):
                    print("Dehli")
          def famous_food(self):
                    print("Pani puri")
          def sports(self):
                    print("cricket")
p = Pakistan()
p.famous_food()
p.capital()
p.sports()

i = India()
i.capital()
i.famous_food()
i.sports()