import random
#Function definitions

def coinflip() -> bool:
    return bool(random.getrandbits(1))

def neighborCount(grid: list[list[list[int]]], checker: list[int] | tuple[int, ...]) -> int:
    count = 0
    for l in range(len(grid)):
        for m in range(len(grid[0])):
            if grid[l][m][0] in checker:
                count += 1
                
    return count

#Checks if a neighbor is in the checker list
def neighborCheck(grid: list[list[list[int]]], checker: list[int] | tuple[int, ...]) -> bool:
    for l in range(len(grid)):
        for m in range(len(grid[0])):
            if grid[l][m][0] in checker:
                return True
    return False

#gets the neighbor's ID
def myNeighbor(grid: list[list[list[int]]], shouldnt: list[int] | tuple[int, ...]) -> int:
    for l in range(len(grid)):
        for m in range(len(grid[0])):
            if grid[l][m][0] != 0 and grid[l][m][0] != "self" and not grid[l][m][0] in shouldnt:
                return grid[l][m][0]
    return 0

#Checks the "Temprature" of it's neighbors
def neighborTempCheck(grid: list[list[list[int]]], checker: list[int] | tuple[int, ...], maths: str = ">", temp: int = 0) -> tuple[bool,int]:
    answer = 0
    answered = False
    for l in range(len(grid)):
        for m in range(len(grid[0])):
            if grid[l][m][0] in checker:
                #Did this to make it more readable. Ironic considering the rest of my code
                if maths == "==" and grid[l][m][1] == temp:
                    return (True,grid[l][m][1])
                elif maths == "<" and grid[l][m][1] < temp and grid[l][m][1] < answer:
                    answered = True
                    answer = grid[l][m][1]
                elif maths == ">" and grid[l][m][1] > temp and grid[l][m][1] > answer:
                    answered = True
                    answer = grid[l][m][1]
                elif maths == "<=" and grid[l][m][1] <= temp and grid[l][m][1] <= answer:
                    answered = True
                    answer = grid[l][m][1]
                elif maths == ">=" and grid[l][m][1] >= temp and grid[l][m][1] >= answer:
                    answered = True
                    answer = grid[l][m][1]
    if answered:
        return (True,answer)
    
    return (False,0)

# Sand Physics ---------------------------------------------------
def sandCheck(grid: list[list[list[int]]],pos: list[int] | tuple[int,int], floats: bool = False, reverse: bool = False, gas: bool = False) -> tuple[int,int]:
    #Returns a list, the 1st element determines where the sand should fall. If 0, then nowhere, 1 is left, 2 is falling middle, 3 is right
    #The second element is the element should be subsituted for air (only if it sinks)
    b = (0,0)
    l = 1
    if reverse:
        l = -1
    if len(grid) == 2 and ((pos[0] == 1 and not reverse) or (pos[0] == 0 and reverse)):
        return (0,0)
    under = True
    if not floats:
        if gas:
            b = [0,1,3,4,6,8,9,11,15,27,28,29,30,32,34,45,46,47,56,65,71,75,77,79,80,81,82,83,84]
        else:
            b = [0,3,15,27,29,30,34,47,56,65,71,75,79,81]
        if grid[pos[0]][pos[1]][1] in b:
            b.remove(grid[pos[0]][pos[1]][1])
        b = tuple(b)
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
        if grid[pos[0]+l][m][0] in b:
            under = False
            break
    
    
    if under:
        return (0,0)
    else:
        if grid[pos[0]+l][pos[1]][0] in b:
            return (2,grid[pos[0]+l][pos[1]][0])
        elif canLeft and canRight and (grid[pos[0]+l][pos[1]-1][0] in b) and (grid[pos[0]+l][pos[1]+1][0] in b):
            doing = coinflip()
            if doing:
                return (1,grid[pos[0]+l][pos[1]-1][0])
            else:
                return (3,grid[pos[0]+l][pos[1]+1][0])
        elif canLeft and (grid[pos[0]+l][pos[1]-1][0] in b):
            return (1,grid[pos[0]+l][pos[1]-1][0])
        elif canRight and (grid[pos[0]+l][pos[1]+1][0] in b):
            return (3,grid[pos[0]+l][pos[1]+1][0])
    return (0,0) #To assure something gets returned if everything else is wrong


# Oversimplified sand physics ---------------------------------------------------
def sandCheckLess(grid: list[list[int]],pos: list[int] | tuple[int,int]) -> tuple[int,int]:
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


# Stone Physics ---------------------------------------------------
def stoneCheck(grid: list[list[list[int]]],pos: list[int] | tuple[int,int], floats: bool = False, reverse: bool = False, gas: bool = False) -> tuple[bool,int]:
    #returns if something's under it (or above it if in reverse)
    l = 1
    if reverse:
        l = -1
    b = (0,0)
    if not floats:
        if gas:
            b = [0,1,3,4,6,8,9,11,15,27,28,29,30,32,34,45,46,47,56,65,71,75,77,79,80,81]
        else:
            b = [0,3,15,27,29,34,47,56,65,71,75,79,81]
        if grid[pos[0]][pos[1]][1] in b:
            b.remove(grid[pos[0]][pos[1]][1])
        b = tuple(b)
    if len(grid) == 2 and ((pos[0] == 1 and not reverse) or (pos[0] == 0 and reverse)):
        return (True,0)
    elif grid[pos[0]+l][pos[1]][0] in b:
        return (False,grid[pos[0]+l][pos[1]][0])
    else:
        return (True,0)

#Me when there's plenty of stuff below me but I wanna wander left or right
def lrWanderCheck(grid: list[list[list[int]]],pos: list[int] | tuple[int,int], floaty: bool = False, waterlike: bool = False, reverse: bool = False) -> tuple[bool,bool,int]:
    b = (0,0)
    if waterlike:
        b = [0,3,15,27,29,34,47,56,65,71,75,79,81]
        if grid[pos[0]][pos[1]][1] in b:
            b.remove(grid[pos[0]][pos[1]][1])
        b = tuple(b)
    l = 1
    if reverse:
        l = -1
    if floaty and len(grid) == 2 and ((pos[0] == 1 and not reverse) or (pos[0] == 0 and reverse)):
        floaty = False
    
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
        if not grid[pos[0]][pos[1]+1][0] in b:
            canRight = False
        elif floaty and not grid[pos[0]+l][pos[1]+1][0] in b:
                canRight = False
    
    if canLeft:
        if not grid[pos[0]][pos[1]-1][0] in b:
            canLeft = False
        elif floaty and not grid[pos[0]+l][pos[1]-1][0] in b:
                canLeft = False

    if not(canRight or canLeft):
        return (False,False,0)
    if coinflip():
        if canLeft and canRight:
            x = coinflip()
            l = -1
            if x:
                l = 1
            return (True,x,grid[pos[0]][pos[1]-l][0])
        elif not canRight:
            return (True,False,grid[pos[0]][pos[1]-1][0])
        else:
            return (True,True,grid[pos[0]][pos[1]+1][0])
    return (False,False,0)

#Me when I'd like to go up or down spontaniously
def udWanderCheck(grid: list[list[list[int]]],pos: list[int] | tuple[int,int], waterlike: bool = False) -> tuple[bool,bool,int]:
    b = (0,0)
    if waterlike:
        b = [3,15,27,29,34,47,56,65,71,75,79,81]
        if grid[pos[0]][pos[1]][1] in b:
            b.remove(grid[pos[0]][pos[1]][1])
        b = tuple(b)
    canUp = True
    canDown = True
    
    
    if len(grid) == 1:
        canUp = False
        canDown = False
    elif len(grid) == 2:
        if pos[0] == 0:
            canUp = False
        else:
            canDown = False
    
    
    if canUp:
        if not grid[pos[0]-1][pos[1]][0] in b:
            canUp = False
    
    if canDown:
        if not grid[pos[0]+1][pos[1]][0] in b:
            canDown = False

    if not(canUp or canDown):
        return (False,False,0)
    if coinflip():
        if canDown and canUp:
            x = coinflip()
            l = 1
            if x:
                l = -1
            return (True,x,grid[pos[0]+l][pos[1]][0])
        elif canUp:
            return (True,False,grid[pos[0]-1][pos[1]][0])
        else:
            return (True,True,grid[pos[0]+1][pos[1]][0])
    return (False,False,0)

#check if there's something that can support it on both left and right sides
def lrCheck(plain: list[list[int]],posx: int, idcIfUnsupportable: bool = False) -> bool:
    
    if len(plain) == 1 or len(plain) == 2:
        return False
    if idcIfUnsupportable:
        unsupportable = [0]
    else:
        unsupportable = (0,1,3,4,6,8,9,10,11,13,15,16,18,19,22,23,27,28,29,30,32,35,36,39,43,45,46,47,51,53,55,56,60,61,62,63,64,65,66,67,71)
    
    if plain[posx-1][0] in unsupportable or plain[posx+1][0] in unsupportable:
        return False
    return True

#checks if there's a single pixel of a specific element anywhere (more optimized I guess but more specific)
def checkEverywhere(grid: list[list[list[int]]], thing) -> bool:
    for i in range(len(grid)):
        if thing in grid[i]:
            return True
    return False

def randomElement(randTemp:bool = True) -> list[int]:
    e = random.randint(0,76)
    t = 0
    if randTemp:
        if e in (30,49):
            t = random.randint(0,5)
        else:
            t = random.randint(0,20)
    return [e,t]


#same as checksEverywhere but only checks the ID of an element (less optimized I guess but less specific)
def checkAbsolutelyEverywhere(grid: list[list[list[int]]], thing) -> bool:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j][0] == thing:
                return True
    return False

print("Newton says an object in motion stays in motion.\nI say....Gravity is a lie, and so is the sky.")