import json, os

# check if user_data.json exists
if os.path.exists("user_data.json"):
    # open user_data.json and create the user_data dictionary
    with open("user_data.json") as f:
        user_data = json.load(f)
    
    # Update address for Kriszta
    user_data["kriszta@gmail.com"]["address"] = "Budapest"

    print(user_data)

# this runs if above is false
else:
    print("user_data.json doesn't exist :(((")