events = []

while True:
    print("\n1.Add 2.View 3.Exit")
    ch = input()

    if ch == "1":
        title = input("Title: ")
        events.append(title)

    elif ch == "2":
        print(events)

    elif ch == "3":
        break