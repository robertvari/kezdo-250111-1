import os, platform

min_number = 1
max_number = 10
max_tries = 3
magic_number = 5

# Clear terminal for the game
if platform.system() == "Windows":
    os.system("cls")
elif platform.system() == "Darwin":
    os.system("clear")
elif platform.system() == "Linux":
    os.system("clear")

# print an introduction of the game
print("-"*50, "MAGIC NUMBER", "-"*50)
print(f"I have a number between {min_number} and {max_number}. Can you guess it?")
print(f"You can try {max_tries} times.")

# TODO ask player for their number
# TODO do a check if their number == magic_number
# TODO endgame condition