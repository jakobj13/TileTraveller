"""
First check position. Identify open walls in the position and print out the options for the player.
When player moves, check position again and print options. If invalid direction is entered allow the
player to choose again. End game when victory location is reached
"""

#Repo -- https://github.com/jakobj13/TileTraveller
north = False
south = False
west = False
east = False
position = [1,1]
choice = "n"
bad_choice_counter = 0

def move(choice,position):
    if choice == 'n' or choice == 'N':
        position[1] = position[1] + 1
    elif choice == 's' or choice == 'S':
        position[1] = position[1] - 1
    elif choice == 'w' or choice =='W':
        position[0] = position[0] - 1
    elif choice == 'e' or choice == 'E':
        position[0] = position[0] + 1
    else:
        return position
    return position

def check_valid_direction(choice):
    if choice == "n" or choice == "N":
        if north:
            return True
    elif choice == "s" or choice == "S":
        if south:
            return True
    elif choice == "w" or choice == "W":
        if west:
            return True
    elif choice == "e" or choice == "E":
        if east:
            return True
    else:
        return False     

def get_choice():
    choice = input('Direction: ')
    return choice

while position != [3,1]:
    if position == [1,1] and bad_choice_counter == 0:
        north = True
        south = False
        east = False
        west = False
        print("You can travel: (N)orth.")
    if position == [1,2] and bad_choice_counter == 0:
        south = True
        east = True
        north = True
        west = False
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    if position == [1,3] and bad_choice_counter == 0:
        north = False
        west = False
        south = True
        east = True
        print("You can travel: (E)ast or (S)outh.")
    if position == [2,1] and bad_choice_counter == 0:
        north = True
        west = False
        east = False
        south = False
        print("You can travel: (N)orth.")
    if position == [2,2] and bad_choice_counter == 0:
        north = False
        east = False
        south = True
        west = True
        print("You can travel: (S)outh or (W)est.")
    if position == [2,3] and bad_choice_counter == 0:
        north = False
        south = False
        east = True
        west = True
        print("You can travel: (E)ast or (W)est.")
    if position == [3,1] and bad_choice_counter == 0:
        north = True
        south = False
        west = False
        east = False
    if position == [3,2] and bad_choice_counter == 0:
        north = True
        east = False
        west = False
        south = True
        print("You can travel: (N)orth or (S)outh.")
    if position == [3,3] and bad_choice_counter == 0:
        north = False
        east = False
        west = True
        south = True
        print("You can travel: (S)outh or (W)est.")
    choice = get_choice()
    if choice == 'q':
        break
    elif check_valid_direction(choice):
        bad_choice_counter = 0
        position = move(choice, position)
    else: 
        print('Not a valid direction!')
        bad_choice_counter += 1
if position == [3,1]:
    print("Victory!")

