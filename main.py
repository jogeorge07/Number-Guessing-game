import random

print("Welcome to Number Guessing Game")

while True:
    user_input = input("Enter the maximum range for the number (greater than 0): ")
    if user_input.isdigit():
        user_max = int(user_input)
        if user_max > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    else:
        print("Please enter a valid number.")

random_num = random.randint(1, user_max)
guess_count = 0

while True:
    guess_count += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a valid number.")
        continue

    if user_guess == random_num:
        print("Congratulations! You guessed the number in", guess_count, "attempts.")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            random_num = random.randint(1, user_max)
            guess_count = 0
            continue
        else:
            print("Thank you for playing. Goodbye!")
            break
    elif user_guess > random_num:
        print("Too high.")
    else:
        print("Too low.")
