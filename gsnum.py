import random
def number_guessing_game():
    print("🎲 Welcome to number guessing game!")
    print("Im thinking of a number between 1-100 and you will have to try and guess it.")
    secret_number = random.randint(1,100)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please enter a number between 1-100.")
            elif guess < secret_number:
                print("higher")
            elif guess > secret_number:
                print("lower")
            else:
                print(f"Correct! You guessed the number with {attempts} attempts")
                break
        except ValueError:
            print("Please enter a valid number.")
number_guessing_game()