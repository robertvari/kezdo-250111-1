import json, os

# Create an empty dictionary for storing user data
user_database = {}


# check if user_data.json exists
if os.path.exists("user_data.json"):
    # if it does, open it and update user_database with the content of the file
    with open("user_data.json") as f:
        user_database = json.load(f)

# Ask user for data
email = input("What is your email? ")
name = input("What is your name? ")
address = input("Where do you live? ")

# Add user data to dictionary
user_database[email] = {"name": name, "address": address}


# write out dictionary as a json file
with open("user_data.json", "w") as f:
    json.dump(user_database, f)


print(user_database)