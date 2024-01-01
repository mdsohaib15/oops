
def calculator():
    print("calculator")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator(+,-,*,/): ")
    if operator == "+":
     print(num1 + num2)
    elif operator == "-":
      print(num1 - num2)
    elif operator == "*":
     print(num1 * num2)
    elif operator == "/":
      print(num1 / num2)
    else:
     print("Error!")
def guessnumber():
    target_numbers = "123456"
    current_index = 0
    while current_index < len(target_numbers):
        current_number = target_numbers[current_index]
        user_guess = input(f"Guess the position{current_index + 1}: ")
        if user_guess == current_number:
            print("Correct! Moving on to the next number.")
            current_index += 1
        else:
            print(f"Wrong number. The Correct Number was {current_number}.\n Game Over")
            break
        if current_index == len(target_numbers):
            print("Congratulation!! you guess all the number correctly")

def password():
    password = 1234
    user_input = int(input("Enter Password: "))
    while password != user_input:
        print("Incorrect password!")
        user_input = int(input("Please Enter Password Again: "))
    print("Right Password")



# while True:
#     print("1. open calcultor ")
#     print("2. guess number ")
#     print("3. password ")
#     print("4. quit ")
#     choice = input("Enter number 1-4: ")
#     if choice == "1":
#         calculator()
#     elif choice == "2":
#         guessnumber()
#     elif choice == "3":
#         password()
#     elif choice == "4":
#         print("Quit")
#         break
#     else:
#         print("Invalid choice\nPlease try again")


