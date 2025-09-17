import random

print("Welcome to 'Guess the Number'!")

while True:
    secret_number = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10.")

    while True:
        guess = input("Please enter your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            print(f"The secret number was: {secret_number}")
            break  # Exit inner loop when guessed correctly

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower().strip() != "yes":
        print("Goodbye!")
        break  # Exit outer loop if the player doesn't want to play again