import os, platform, random

min_number = 1
max_number = 10

while True:  # start game loop
    # Clear terminal for the game
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Linux":
        os.system("clear")

    max_tries = 3

    # print an introduction of the game
    print("-"*50, "MAGIC NUMBER", "-"*50)
    print(f"I have a number between {min_number} and {max_number}. Can you guess it?")
    print(f"You can try {max_tries} times.")

    magic_number = str( random.randint(min_number, max_number) )
    # print(f"HINT: {magic_number}")

    # ask player for their number
    player_number = input("What is my number? ")

    # do a check if their number == magic_number
    while magic_number != player_number:
        max_tries -= 1
        if max_tries == 0:
            break

        print(f"Wrong guess. Try again. You have {max_tries} tries left.")
        player_number = input("What is my number? ")


    # endgame condition
    if magic_number == player_number:
        print("You guessed my number! Congrats!!!!")
    else:
        print(f"No, {player_number} is not my number.")
    
    new_game = input("Do you want to play again? (y/n)")
    if new_game != "y":
        print("Thank you for playing my game.")
        break