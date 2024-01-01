target_numbers = "123456"

for current_index in range(len(target_numbers)):
    current_number = target_numbers[current_index]
    user_guess = input(f"Guess the position {current_index + 1}: ")

    if user_guess == current_number:
        print("Correct! Moving on to the next number.")
    else:
        print(f"Wrong number. The Correct Number was {current_number}.\nGame Over")
        break
else:
    print("Congratulations!! You guessed all the numbers correctly.")

# user_input = int(input("Enter a number: "))
# if numbers[0] == user_input:
#     print("Yes this number is in list")
# elif numbers[1] == user_input:
#     print("Yes this number is in list")
# elif numbers[2] == user_input:
#     print("Yes this number is in list")
# elif numbers[3] == user_input:
#     print("Yes this number is in list")
# elif numbers[4] == user_input:
#     print("Yes this number is in list")
# else:
#     print("wrong guess")


# numbers2 = [11,22,33,44,55]
# user_input = int(input("Enter a number: "))
# if numbers2[0] == user_input:
#
#     print("Yes this number is in list")
#     if numbers2[0] == user_input:
#         print("ef")
# elif numbers2[1] == user_input:
#     print("Yes this number is in list")
# elif numbers2[2] == user_input:
#     print("Yes this number is in list")
# elif numbers2[3] == user_input:
#     print("Yes this number is in list")
# elif numbers2[4] == user_input:
#     print("Yes this number is in list")
# else:
#     print("wrong guess")