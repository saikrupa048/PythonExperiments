events = []

while True:
    print("1.Add 2.Search 3.Exit")
    ch = input()

    if ch == "1":
        events.append(input("Enter title: "))

    elif ch == "2":
        key = input("Search: ").lower()
        for e in events:
            if key in e.lower():
                print(e)

    else:
        break