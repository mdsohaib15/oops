target_numbers = "123456"
current_index = 0
while current_index<len(target_numbers):
    current_number =target_numbers[current_index]
    user_guess = input(f"Guess the position{current_index+1}: ")
    if user_guess == current_number:
        print("Correct! Moving on to the next number.")
        current_index += 1
    else:
        print(f"Wrong number. The Correct Number was {current_number}.\n Game Over")
        break
    if current_index == len(target_numbers):
        print("Congratulation!! you guess all the number correctly")