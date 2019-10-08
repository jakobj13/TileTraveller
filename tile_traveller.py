NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true is player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions_and_coins(directions_str, col, row, coins):
    ''' Prints the directions, and checks the col, row for lever. If lever, add to coins and return coins. '''
    lever = False
    lever = check_lever(col,row)
    inp = ""
    if lever:
        inp = input("Pull a lever (y/n): ")
        if inp == 'y' or inp == 'Y':
            coins += 1
            print("You received 1 coin, your total is now ", coins, ".", sep ='')
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
    return coins
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def check_lever(col, row):
    ''' Returns true if lever is on the col, and row'''
    lever = False
    if col == 1 and row == 2: # (1,2)
        lever = True
    elif col == 2 and row == 2: # (2,2)
        lever = True
    elif col == 2 and row == 3: # (2,3)
        lever = True
    elif col == 3 and row == 2: # (3,2)
        lever = True
    return lever


def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row

# The main program starts here
victory = False
lever = False
row = 1
col = 1
coins = 0

valid_directions = NORTH
print_directions_and_coins(valid_directions, col, row, coins)

while not victory:
    victory, col, row = play_one_move(col, row, valid_directions)
    if victory:
        print("Victory! Total coins ", coins, ".", sep = '')
        play_again = input("Play again (y/n): ")
        if play_again == 'y' or play_again == 'Y':
            victory = False
            lever = False
            row = 1
            col = 1
            coins = 0

            valid_directions = NORTH
            print_directions_and_coins(valid_directions, col, row, coins)

    else:
        valid_directions = find_directions(col, row)
        coins = print_directions_and_coins(valid_directions, col, row, coins)