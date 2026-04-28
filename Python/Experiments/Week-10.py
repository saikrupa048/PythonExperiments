def arcade():
    while True:
        print("\n--- MINI ARCADE ---")
        print("1. Guessing Game")
        print("2. Hangman")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            guessing_game()
        elif choice == "2":
            hangman()
        elif choice == "3":
            break
        else:
            print("Invalid choice")
# empty file
