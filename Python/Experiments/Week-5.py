events = {}
types = set()
logs = []

eid = input("Enter ID: ")
name = input("Enter Name: ")
etype = input("Enter Type: ")

events[eid] = {"name": name, "type": etype}
types.add(etype)
logs.append((name, "Added"))

print(events)
print(types)
print(logs)