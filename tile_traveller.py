"""
we make a grid where we know where player is
when we make a functions that goes around in the grid (3x3)
if we go to the grid that we cannot go, we get error messege
otherwise we move.
"""
grid_x = 1
grid_y = 1

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

def move_player(direction):
    if direction.lower() == 'n':
        grid_generator(grid_x,grid_y+1)
    elif direction.lower() == 's':
        grid_generator(grid_x, grid_y-1)
    elif direction.lower() == 'w':
        grid_generator(grid_x-1,grid_y)
    elif direction.lower() == 'e':
        grid_generator(grid_x+1,grid_y)
    
    

def check_location(x,y):
    if x == 1:
        if y == 1:
            print('You can travel: (N)orth.')
        elif y == 2:
            print('You can travel: (N)orth or (E)ast or (S)outh')
        elif y == 3:
            print('You can travel: (E)ast or (S)outh')
    
    elif x == 2:
        if y == 1:
            print('You can travel: (N)orth.')
        elif y == 2:
            print('You can travel: (S)outh or (W)est.')
        elif y == 3:
            print('You can travel: (E)ast or (W)est.')
    
    elif x == 3:
        if y == 1:
            print('Victory!')
        elif y == 2:
            print('You can travel: (N)orth or (S)outh.')
        elif y == 3:
            print('You can travel: (E)ast or (S)outh.')




grid_generator(startgrid_x, startgrid_y)


print("You can travel: (N)orth.")
direction = input("Direction: ")


