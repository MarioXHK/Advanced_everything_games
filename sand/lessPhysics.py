from physics import coinflip
# Oversimplified sand physics ---------------------------------------------------
def sandCheckLess(grid: list[list[int]],pos: list[int] | tuple[int,int]) -> int:
    #Returns an int. If 0, then nowhere, 1 is left, 2 is falling middle, 3 is right
    l = 1
    if len(grid) == 2 and pos[0] == 1:
        return 0
    under = True
    canLeft = True
    canRight = True
    if len(grid[0]) == 1:
        canRight = False
        canLeft = False
    elif len(grid[0]) == 2:
        if pos[1] == 0:
            canLeft = False
        else:
            canRight = False
    
    for m in range(len(grid[0])):
        if grid[pos[0]+l][m] == 0:
            under = False
            break
    
    
    if under:
        return 0
    else:
        if grid[pos[0]+l][pos[1]] == 0:
            return 2
        elif canLeft and canRight and (grid[pos[0]+l][pos[1]-1] == 0) and (grid[pos[0]+l][pos[1]+1] == 0):
            doing = coinflip()
            if doing:
                return 1
            else:
                return 3
        elif canLeft and (grid[pos[0]+l][pos[1]-1] == 0):
            return 1
        elif canRight and (grid[pos[0]+l][pos[1]+1] == 0):
            return 3
    return 0 #To assure something gets returned if everything else is wrong

# Oversimplified Stone Physics -------------------------------------------------------------------
def stoneCheckLess(grid: list[list[int]],pos: list[int]) -> bool:
    #returns if something's under it (or above it if in reverse)
    if (len(grid) == 2 and pos[0] == 1) or grid[pos[0]+1][pos[1]] != 0:
        return True
    else:
        return False

#Me when there's plenty of stuff below me but I wanna wander left or right
def lrWanderCheckLess(grid: list[list[int]],pos: list[int] | tuple[int,int]) -> tuple[bool,bool]:
    
    canRight = True
    canLeft = True
    
    if len(grid[0]) == 1:
        canRight = False
        canLeft = False
    elif len(grid[0]) == 2:
        if pos[1] == 0:
            canLeft = False
        else:
            canRight = False
    
    if canRight:
        if not grid[pos[0]][pos[1]+1] == 0:
            canRight = False
    
    if canLeft:
        if not grid[pos[0]][pos[1]-1] == 0:
            canLeft = False

    if not(canRight or canLeft):
        return (False,False)
    if coinflip():
        if canLeft and canRight:
            x = coinflip()
            return (True,x)
        elif not canRight:
            return (True,False)
        else:
            return (True,True)
    return (False,False)