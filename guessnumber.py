import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    print("secret number",secret_number)
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break

        if attempts == 5:
            print("Sorry, you've used all your attempts.")
            print(f"The correct number was {secret_number}. Better luck next time!")
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        guess_number()
    else:
        print("Thank you for playing the Number Guessing Game!")

guess_number()
