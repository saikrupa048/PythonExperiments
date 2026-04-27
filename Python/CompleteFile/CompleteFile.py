import json
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# MODELS
# =========================

class Event:
    def __init__(self, eid, title, date, start, end, dept, etype):
        self.eid = eid
        self.title = title
        self.date = date
        self.start = start
        self.end = end
        self.dept = dept
        self.etype = etype

    def to_dict(self):
        return self.__dict__


class Room:
    def __init__(self, rid, capacity, features):
        self.rid = rid
        self.capacity = capacity
        self.features = features

    def to_dict(self):
        return self.__dict__


class Booking:
    def __init__(self, event, room):
        self.event = event
        self.room = room

# =========================
# DATA STORAGE
# =========================

events = {}
rooms = {}
bookings = []

# =========================
# FILE HANDLING
# =========================

def save_data():
    with open("events.json", "w") as f:
        json.dump({k: v.to_dict() for k, v in events.items()}, f)

def load_data():
    global events
    try:
        with open("events.json", "r") as f:
            data = json.load(f)
            for k, v in data.items():
                events[k] = Event(**v)
    except:
        pass

# =========================
# CORE FUNCTIONS
# =========================

def add_room():
    rid = input("Room ID: ")
    cap = int(input("Capacity: "))
    features = set(input("Features (comma separated): ").split(","))

    rooms[rid] = Room(rid, cap, features)
    print("✅ Room added")

def add_event():
    eid = input("Event ID: ")
    title = input("Title: ")
    date = input("Date (YYYY-MM-DD): ")
    start = input("Start Time (HH:MM): ")
    end = input("End Time (HH:MM): ")
    dept = input("Department: ")
    etype = input("Type: ")

    events[eid] = Event(eid, title, date, start, end, dept, etype)
    print("✅ Event added")

def check_conflict(room_id, date, start, end):
    for b in bookings:
        if b.room.rid == room_id and b.event.date == date:
            if (start < b.event.end and end > b.event.start):
                return True
    return False

def book_room():
    eid = input("Enter Event ID: ")
    rid = input("Enter Room ID: ")

    if eid not in events or rid not in rooms:
        print("❌ Invalid ID")
        return

    event = events[eid]

    if check_conflict(rid, event.date, event.start, event.end):
        print("❌ Conflict detected!")
        return

    bookings.append(Booking(event, rooms[rid]))
    print("✅ Room booked successfully")

def view_bookings():
    for b in bookings:
        print(f"{b.event.title} -> {b.room.rid} ({b.event.start}-{b.event.end})")

# =========================
# ANALYTICS
# =========================

def analytics():
    if not bookings:
        print("No data")
        return

    data = []
    for b in bookings:
        data.append({
            "Room": b.room.rid,
            "Type": b.event.etype
        })

    df = pd.DataFrame(data)

    print("\n📊 Event Data:")
    print(df)

    df["Room"].value_counts().plot(kind="bar")
    plt.title("Room Usage")
    plt.show()

# =========================
# MENU
# =========================

def menu():
    load_data()

    while True:
        print("\n==== SESS MENU ====")
        print("1. Add Room")
        print("2. Add Event")
        print("3. Book Room")
        print("4. View Bookings")
        print("5. Analytics")
        print("6. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add_room()
        elif ch == "2":
            add_event()
        elif ch == "3":
            book_room()
        elif ch == "4":
            view_bookings()
        elif ch == "5":
            analytics()
        elif ch == "6":
            save_data()
            break
        else:
            print("Invalid choice!")

# =========================
# RUN PROGRAM
# =========================

menu()