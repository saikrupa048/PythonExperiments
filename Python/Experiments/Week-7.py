class Record:
    def __init__(self, id):
        self.id = id

class Event(Record):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

    def show(self):
        print(self.id, self.name)

e = Event(1, "Seminar")
e.show()