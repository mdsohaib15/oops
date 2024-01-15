# ------Private access Modifier------
class BankAcount:
          def __init__(self,name,__balance):
                    self.name = name
                    self.__balance = __balance
          def deposite(self,amount):
                    self.__balance += amount
                    print(f"Deposite is successfull.New Balance is {self.__balance}")
          def withdraw(self,amount):
                    if amount>self.__balance:
                              print("Insufficient Balance")
                    else:
                              self.__balance -=amount
                              print(f"Withdrawl is successfull,Remaining Balance is :{self.__balance}")
          def __showBalance(self):
                    print(f"Current balance : {self.__balance}")

a = BankAcount("Claire",12000)
a.deposite(2000)
a.withdraw(1000)
#a.__showBalance() #>can't access directly
a._BankAcount__showBalance() #>can be access indirectly