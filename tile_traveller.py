"""
First check position. Identify open walls in the position and print out the options for the player.
When player moves, check position again and print options. If invalid direction is entered allow the
player to choose again. End game when victory location is reached
"""
north = False
south = False
west = False
east = False
position = [1,1]
choice = "n"

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
    if choice == "n" or choice == "N" or choice == "s" or choice == "S" or choice == "w" or choice == "W" or choice == "e" or choice == "E" :
        return True 
    else:
        return False     

def get_choice():
    choice = input('Direction: ')
    return choice

def print_directions(position):

    return None

if position == [1,1]:
    north = True
if position == [1,2]:
    south = True
    east = True
    north = True
if position == [1,3]:
    south = True
    east = True
if position == [2,1]:
    north = True
if position == [2,2]:
    south = True
    west = True
if position == [2,3]:
    east = True
    west = True
if position == [3,1]:
    north = True
if position == [3,2]:
    north = True
    south = True
if position == [3,3]:
    west = True
    south = True

while position != [3,1]:
    choice = get_choice()
    if choice == 'q':
        break
    elif check_valid_direction(choice):
        position = move(choice, position)
    else: 
        print('Not a valid direction!')
    #print(position)

