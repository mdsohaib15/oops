password = 1234
user_input = int(input("Enter Password: "))
while password != user_input:
    print("Incorrect password!")
    user_input = int(input("Enter Password: "))
print("Right Password\nContinue")
