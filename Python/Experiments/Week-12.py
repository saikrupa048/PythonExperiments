import random

score = 0

def add_score(points):
    global score
    score += points

def guessing_game():
    number = random.randint(1, 10)
    attempts = 5

    while attempts > 0:
        guess = int(input("Guess number: "))

        if guess == number:
            print("Correct!")
            add_score(10)
            return
        else:
            print("Wrong!")
            attempts -= 1

    print("Lost! Number was", number)

def hangman():
    words = ["python", "arcade", "coding"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6

    while attempts > 0:
        print("Word:", " ".join(guessed))
        letter = input("Enter letter: ")

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
        else:
            attempts -= 1

        if "_" not in guessed:
            print("You win!")
            add_score(15)
            return

    print("You lose!")

def arcade():
    while True:
        print("\n--- MINI ARCADE ---")
        print("1. Guessing Game")
        print("2. Hangman")
        print("3. Score")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            guessing_game()
        elif choice == "2":
            hangman()
        elif choice == "3":
            print("Score:", score)
        elif choice == "4":
            print("Thanks for playing!")
            break

arcade()
