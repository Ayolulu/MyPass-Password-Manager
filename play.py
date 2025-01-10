import json
with open("data.json", "r") as data_file:
    data = json.load(data_file)
    for site, details in data.items():
        print(details["email"])