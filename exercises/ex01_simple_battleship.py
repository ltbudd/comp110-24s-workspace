"""EX01 - Simple Battleship - A cute step towards Battleship."""

__author__ = "730648114"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

result = ""

# User Input - Pick boat location
p1_loc = input("Pick a secret boat location between 1 and 4: ")
if p1_loc.isnumeric() == False:
    print("Error! " + p1_loc + " is invalid. Please enter a valid number.")
    exit()
elif int(p1_loc) < 1:
    print("Error! " + str(p1_loc) + " too low!")
    exit()
elif int(p1_loc) > 4:
    print("Error! " + str(p1_loc) + " too high!")
    exit()

# User Input - Guess boat location
p2_loc = input("Guess a number between 1 and 4: ")
if p2_loc.isnumeric() == False:
    print("Error! " + p1_loc + " is invalid. Please enter a valid number.")
    exit()
elif int(p2_loc) < 1:
    print("Error! " + str(p1_loc) + " too low!")
    exit()
elif int(p2_loc) > 4:
    print("Error! " + str(p1_loc) + " too high!")
    exit()

# If Else statement for results
if int(p2_loc) == int(p1_loc):
    result = RED_BOX
    if int(p2_loc) == 1:
        print(result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    elif int(p2_loc) == 2:
        print(BLUE_BOX + result + BLUE_BOX + BLUE_BOX)
    elif int(p2_loc) == 3:
        print(BLUE_BOX + BLUE_BOX + result + BLUE_BOX)
    else:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + result)
    print("Correct! You hit the ship.")
else:
    result = WHITE_BOX
    if int(p2_loc) == 1:
        print(result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    elif int(p2_loc) == 2:
        print(BLUE_BOX + result + BLUE_BOX + BLUE_BOX)
    elif int(p2_loc) == 3:
        print(BLUE_BOX + BLUE_BOX + result + BLUE_BOX)
    else:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + result)
    print("Incorrect! You missed the ship.")