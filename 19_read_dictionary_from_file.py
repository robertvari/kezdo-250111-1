import json

with open("phonebook.json") as f:
    phonebook = json.load(f)

print(phonebook["06 20 123 4561"])