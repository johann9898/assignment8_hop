"""
we make a grid where we know where player is
when we make a functions that goes around in the grid (3x3)
if we go to the grid that we cannot go, we get error messege
otherwise we move.
"""
startgrid_x = 1
startgrid_y = 1

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

print("You can travel: (N)orth.")
direction = input("Direction: ")


