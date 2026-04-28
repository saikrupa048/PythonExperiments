import random

words = ["python", "game", "arcade"]
word = random.choice(words)

guessed = ["_"] * len(word)

print(" ".join(guessed))
