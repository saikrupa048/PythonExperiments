events = []

def add_event():
    events.append(input("Enter Event: "))

def view_events():
    for e in events:
        print(e)

while True:
    print("1.Add 2.View 3.Exit")
    ch = input()

    if ch == "1":
        add_event()
    elif ch == "2":
        view_events()
    else:
        break