"""
we make a grid where we know where player is
when we make a functions that goes around in the grid (3x3)
if we go to the grid that we cannot go, we get error messege
otherwise we move.
"""
grid_x = 1
grid_y = 1
n_valid = False
s_valid = False
e_valid = False
w_valid = False

def grid_generator(x,y):    
    gridx = x
    gridy = y
    if gridx > 3:
        gridx -=1
    if gridx < 1:
        gridx += 1
    if gridx <= 3 or gridx >= 1:
        if gridy > 3:
            gridy -=1
        elif gridy < 1:
            gridy += 1
    return gridx, gridy

"""def move_player(direction,grid_x,grid_y):
    if direction.lower() == 'n':
        grid_y += 1
        grid_generator(grid_x,grid_y)
    elif direction.lower() == 's':
        grid_y -= 1
        grid_generator(grid_x, grid_y)
    elif direction.lower() == 'w':
        grid_x -= 1
        grid_generator(grid_x,grid_y)
    elif direction.lower() == 'e':
        grid_x += 1
        grid_generator(grid_x+1,grid_y)"""

"""def move_player(direction,x,y):
    if direction.lower() == 'n':
        return x, y+1
    elif direction.lower() == 's':
        return x, y-1
    elif direction.lower() == 'w':
        return x-1, y
    elif direction.lower() == 'e':
        return x+1,y"""

def move_player(direction,x,y,n_valid,s_valid,e_valid,w_valid):
    if direction.lower() == 'n' and n_valid == True:
        return x, y+1
    elif direction.lower() == 's' and s_valid == True:
        return x, y-1
    elif direction.lower() == 'w' and w_valid == True:
        return x-1, y
    elif direction.lower() == 'e' and e_valid == True:
        return x+1,y
    else:
        print("Not a valid direction!")
        return x,y
    
    

def check_location(x,y,n_valid,s_valid,e_valid,w_valid):
    if (x == 1 or x == 2) and y == 1:
        print('You can travel: (N)orth.') 
        return n_valid = True
    elif x == 1 and y == 2:
        print('You can travel: (N)orth or (E)ast or (S)outh.')
    elif x == 3 and y == 2:
        print('You can travel: (N)orth or (S)outh.')
    elif (x == 2 and y == 2) or (x == 3 and y == 3):
        print('You can travel: (S)outh or (W)est.')
    elif x == 1 and y == 3:
        print('You can travel: (E)ast or (S)outh.')
    elif x == 2 and y == 3:
        print('You can travel: (E)ast or (W)est.')
    elif x == 3 and y == 1:
        print("Victory")
    else:
        print('Not a valid direction!')




loop = True

while loop == True:
    check_location(grid_x,grid_y)
    if grid_x == 3 and grid_y == 1:
        loop = False
    else:
        direction = input("Direction: ")
        grid_x,grid_y = move_player(direction,grid_x,grid_y)
        grid_generator(grid_x,grid_y)





