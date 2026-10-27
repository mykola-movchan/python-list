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
