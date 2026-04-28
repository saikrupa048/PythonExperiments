import random
import time

# ---------------- GLOBAL VARIABLES ----------------
score = 0
games_played = 0
games_won = 0


# ---------------- UTILITY FUNCTIONS ----------------
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()


def line():
    print("-" * 40)


# ---------------- GUESSING GAME ----------------
def guessing_game():
    global score, games_played, games_won

    line()
    slow_print("🎯 GUESSING GAME")

    print("Select Difficulty:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    choice = input("Enter choice: ")

    if choice == "1":
        low, high, attempts = 1, 10, 5
    elif choice == "2":
        low, high, attempts = 1, 50, 7
    else:
        low, high, attempts = 1, 100, 10

    number = random.randint(low, high)
    games_played += 1

    while attempts > 0:
        try:
            guess = int(input(f"Guess number ({low}-{high}): "))
        except:
            print("Invalid input! Enter a number.")
            continue

        if guess == number:
            slow_print("🎉 Correct! You win!")
            score += 10 * attempts
            games_won += 1
            return
        elif guess < number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

        attempts -= 1
        print("Attempts left:", attempts)

    slow_print(f"💀 You lost! Number was {number}")


# ---------------- HANGMAN GAME ----------------
def hangman():
    global score, games_played, games_won

    categories = {
        "Animals": ["tiger", "lion", "elephant", "zebra"],
        "Fruits": ["apple", "banana", "mango", "orange"],
        "Tech": ["python", "computer", "keyboard", "internet"]
    }

    line()
    slow_print("🪢 HANGMAN GAME")

    print("Categories:", ", ".join(categories.keys()))
    cat = input("Choose category: ").capitalize()

    if cat not in categories:
        cat = random.choice(list(categories.keys()))
        print("Random category selected:", cat)

    word = random.choice(categories[cat])
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    games_played += 1

    while attempts > 0:
        line()
        print("Word:", " ".join(guessed))
        print("Guessed letters:", guessed_letters)
        print("Attempts left:", attempts)

        letter = input("Enter letter: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Enter a single valid letter!")
            continue

        if letter in guessed_letters:
            print("Already guessed!")
            continue

        guessed_letters.append(letter)

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
            print("✅ Correct guess!")
        else:
            attempts -= 1
            print("❌ Wrong guess!")

        if "_" not in guessed:
            slow_print(f"🎉 You guessed the word: {word}")
            score += 15 + attempts * 2
            games_won += 1
            return

    slow_print(f"💀 You lost! Word was: {word}")


# ---------------- STATS ----------------
def show_stats():
    line()
    print("📊 GAME STATISTICS")
    print("Games Played:", games_played)
    print("Games Won:", games_won)
    print("Total Score:", score)

    if games_played > 0:
        win_rate = (games_won / games_played) * 100
        print(f"Win Rate: {win_rate:.2f}%")
    else:
        print("Win Rate: 0%")


# ---------------- MAIN ARCADE ----------------
def arcade():
    while True:
        line()
        print("🎮 MINI ARCADE")
        print("1. Guessing Game")
        print("2. Hangman")
        print("3. View Stats")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            guessing_game()
        elif choice == "2":
            hangman()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            slow_print("👋 Thanks for playing!")
            break
        else:
            print("Invalid choice! Try again.")


# ---------------- RUN PROGRAM ----------------
if __name__ == "__main__":
    arcade()
