import random

def guessing_game():
    number = random.randint(1, 10)
    attempts = 5

    while attempts > 0:
        guess = int(input("Guess number (1-10): "))

        if guess == number:
            print("Correct!")
            return
        elif guess < number:
            print("Too low")
        else:
            print("Too high")

        attempts -= 1

    print("You lost! Number was", number)
