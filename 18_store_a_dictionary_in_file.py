import json

phonebook = {
    "06 20 123 4561": {"name":"Csaba", "address": "Budapest"},
    "06 20 987 6543": {"name":"Kriszta", "address": "Debrecen"},
    "06 30 658 3218": {"name":"Tamás", "address": "Pécs"},
    "06 20 123 4567": {"name": "Csilla", "address":"Miskolc"}
}

with open("phonebook.json", "w") as f:
    json.dump(phonebook, f)