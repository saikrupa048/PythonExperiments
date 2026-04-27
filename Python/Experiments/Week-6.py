class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def display(self):
        print(self.name, self.date)

e = Event("Workshop", "2025-01-01")
e.display()