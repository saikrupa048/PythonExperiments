import json

data = {"event": "Workshop"}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    print(json.load(f))