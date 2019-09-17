"""
First check position. Identify open walls in the position and print out the options for the player.
When player moves, check position again and print options. If invalid direction is entered allow the
player to choose again. End game when victory location is reached
"""
position = (1,1)
north = False
south = False
west = False
east = False

def move(choice,position):

    return None

def get_choice():
    choice = input('Direction: ')
    return choice

def print_directions(position):

    return
choice = 'h'
if position == (1,1):
    north = True
if position == (1,2):
    south = True
    east = True
    north = True
if position == (1,3):
    south = True
    east = True
if position == (2,1):
    north = True
if position == (2,2):
    south = True
    west = True
if position == (2,3):
    east = True
    west = True
if position == (3,1):
    north = True
if position == (3,2):
    north = True
    south = True
if position == (3,3):
    west = True
    south = True

while position != (3,1) and choice != "q":
    choice = get_choice()
    move(choice, position)

