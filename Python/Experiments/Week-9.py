import random

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
            return

    print("You lose! Word:", word)
