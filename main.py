# counter = 1 # iніціалізація лічильника
# while counter <= 5: # 2. Умова, яка перевіряється перед кожною ітерацією
#     print(counter)
#     counter += 1
#
# print("Loop finished.")
#
# message = ""
# while message.lower() != "exit":
#     message = input("Enter a message (or type 'exit' to quit): ")
#     if message.lower() != "exit":
#         print(f"You entered: {message}")
#
# print("Goodbye!")

# n = int(input("Enter a positive integer N: "))
#
# total_sum = 0
# current_number = 1
#
# while current_number <= n:
#     total_sum += current_number
#     current_number += 1
#
# print(f"The sum of numbers from 1 to {n} is {total_sum}.")

# for char in "Python":
#     print(char)
#
# print('----------')
#
# for i in range(5):
#     print(i)
#
# print('----------')
#
# for i in range(1, 100):
#     print(i)
#
# for i in range(1, 11):
#     result = 7 * i
#     print(f"7 * {i} = {result}")
#
# for i in range(1, 100):
#     if i % 5 == 0:
#         print(f"Found a number divisible by 5: {i}")
#         break # Виходимо з циклу
#
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue # Якщо число парне, пропускаємо print
#     print(i)

import random

game_on = True
while game_on:
    guess_number = random.randint(1, 10)
    print("New game begins...")

    for attempt in range(3):
        my_guess = input("Guess a number between 1 and 10 (or 'exit'): ").strip()

        if my_guess.lower() == "exit":
            print("Exiting...")
            game_on = False
            break

        if not my_guess.isdigit():
            print("Please enter a whole number.")
            continue

        if int(my_guess) == guess_number:
            print("Correct! You win!")
            game_on = False
            break

        remaining = 2 - attempt
        if remaining > 0:
            print(f"Incorrect guess. {remaining} tries left.")
    else:
        # Runs only if the for loop finished without break
        print(f"Out of tries! The number was {guess_number}.")