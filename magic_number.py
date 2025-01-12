import os, platform

min_number = 1
max_number = 10
max_tries = 3

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

magic_number = str(5)

# ask player for their number
player_number = input("What is my number? ")

# TODO do a check if their number == magic_number
while magic_number != player_number:
    max_tries -= 1
    print(f"Wrong guess. Try again. You have {max_tries} tries left.")
    player_number = input("What is my number? ")


# TODO endgame condition
print("You guessed my number! Congrats!!!!")