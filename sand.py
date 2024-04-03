#Can someone please tell me how to give more resources to this app so I can throttle it and have a smooth 60 fps while my computer combusts into flames
#Some optimization help would be nice too
showfps = False

#the setting that controls if you'd like to do life or not (Experimental sorta)
werealsodoinglife = False

import pygame
from pygame import Vector2
#WHY DOES YOU NOT EVEN THE AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
from copy import deepcopy
import random

#How large the screen is
screenx = 400
screeny = 400

pygame.init()
screen = pygame.display.set_mode((screenx,screeny))
pygame.display.set_caption("Sandbox game!")
breaking=True
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

#mouse variables--------------------------------
mousePos = Vector2(0,0)
fire = False
tap = True

#How many pixels are there in the sandbox (x*y of course)
landx = 40
landy = 40
land = [[[0,0] for _ in range(landx)] for i in range(landy)]
landyx = (screenx/landx)
landyy = (screeny/landy)

element = 1
brushsize = 0

elementNames = {
    0:"Air",
    1:"Sand",
    2:"Stone",
    3:"Water",
    4:"Sugar",
    5:"Wall",
    6:"Dirt",
    7:"Mud",
    8:"Plant",
    9:"Lava",
    10:"Wet Sand",
    11:"Gravel",
    12:"Obsidian",
    13:"Steam",
    14:"Glass",
    15:"Sugar Water",
    16:"Clouds",
    17:"Brick",
    18:"Algae",
    19:"Glass Shards",
    20:"The Sun",
    21:"The Moon",
    22:"Snow",
    23:"Ice",
    24:"Sugar Crystals",
    25:"Packed Ice",
    26:"Life Particle",
    27:"Sludge",
    28:"Flower Seed",
    29:"Oil",
    30:"Fire",
    31:"Wood",
    32:"Ash",
    33:"Cloner",
    34:"Clay",
    35:"Void",
    36:"Petal",
    37:"Cancer Particle",
    38:"Iron",
    39:"Iron Sand",
    40:"Iron Brick",
    41:"Smart Remover",
    42:"Smart Converter",
    43:"Electricity",
    44:"Rustish Iron",
    45:"Rust",
    46:"Salt",
    47:"Salt Water",
    48:"Salt Crystal",
    49:"Leaf",
    50:"Jammer",
    51:"Antisand",
    52:"Antistone",
    53:"Antiwater",
    54:"Identity Crisis",
    55:"Molten Salt"
}

#File Variables
illegals = ('\\','/',':','*','?','"','<','>','|')




#Function definitions

def coinflip() -> bool:
    return bool(random.getrandbits(1))

def neighborCount(grid: list[list[list[int]]], checker: list[int] | tuple[int]) -> int:
    count = 0
    for l in range(len(grid)):
        for m in range(len(grid[0])):
            if grid[l][m][0] in checker:
                count += 1
                
    return count

#Checks if a neighbor is in the checker list
def neighborCheck(grid: list[list[list[int]]], checker: list[int] | tuple[int]) -> bool:
    for l in range(len(grid)):
        for m in range(len(grid[0])):
            if grid[l][m][0] in checker:
                return True
    return False

#gets the neighbor's ID
def myNeighbor(grid: list[list[list[int]]], shouldnt: list[int] | tuple[int]) -> int:
    for l in range(len(grid)):
        for m in range(len(grid[0])):
            if grid[l][m][0] != 0 and grid[l][m][0] != "self" and not grid[l][m][0] in shouldnt:
                return grid[l][m][0]
    return 0

#Checks the "Temprature" of it's neighbors
def neighborTempCheck(grid: list[list[list[int]]], checker: list[int] | tuple[int], maths: str = ">", temp: int = 0) -> tuple[bool,int]:
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
def sandCheck(grid: list[list[list[int]]],pos: list[int] | tuple[int], floats: bool = False, reverse: bool = False, gas: bool = False) -> tuple[int]:
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
            b = [0,1,3,4,6,8,9,11,15,27,28,32,34,45,46,47]
        else:
            b = [0,3,15,27,29,34,47]
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

# Stone Physics ---------------------------------------------------
def stoneCheck(grid: list[list[list[int]]],pos: list[int] | tuple[int], floats: bool = False, reverse: bool = False, gas: bool = False) -> tuple[bool,int]:
    #returns if something's under it (or above it if in reverse)
    l = 1
    if reverse:
        l = -1
    b = (0,0)
    if not floats:
        if gas:
            b = [0,1,3,4,6,8,9,11,15,27,28,32,34,45,46,47]
        else:
            b = [0,3,15,27,29,34,47]
        if grid[pos[0]][pos[1]][1] in b:
            b.remove(grid[pos[0]][pos[1]][1])
        b = tuple(b)
    if len(grid) == 2 and ((pos[0] == 1 and not reverse) or (pos[0] == 0 and reverse)):
        return (True,0)
    elif grid[pos[0]+l][pos[1]][0] in b:
        return [False,grid[pos[0]+l][pos[1]][0]]
    else:
        return [True,0]

#Me when there's plenty of stuff below me but I wanna wander left or right
def lrWanderCheck(grid: list[list[list[int]]],pos: list[int] | tuple[int], floaty: bool = False, waterlike: bool = False, reverse: bool = False) -> tuple[bool,bool,int]:
    b = (0,0)
    if waterlike:
        b = [0,3,15,27,29,34,47]
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
def udWanderCheck(grid: list[list[list[int]]],pos: list[int] | tuple[int], waterlike: bool = False) -> tuple[bool,bool,int]:
    b = (0,0)
    if waterlike:
        b = [3,15,27,29,34,47]
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

    unsupportable = (0,1,3,4,6,8,9,10,11,13,15,16,18,19,22,23,27,28,29,30,32,35,36,39,43,45,46,47,51,53,55)
    if idcIfUnsupportable:
        unsupportable = [0]
    if plain[posx-1][0] in unsupportable or plain[posx+1][0] in unsupportable:
        return False
    return True

#checks if there's a single pixel of a specific element anywhere (more optimized I guess but more specific)
def checkEverywhere(grid: list[list[list[int]]], thing) -> bool:
    for i in range(len(grid)):
        if thing in grid[i]:
            return True
    return False

def randomelement(randTemp:bool = True) -> list[int]:
    e = random.randint(0,55)
    t = 0
    if randTemp:
        if e == 30:
            t = random.randint(0,5)
        else:
            t = random.randint(0,10)
    return [e,t]


#same as checksEverywhere but only checks the ID of an element (less optimized I guess but less specific)
def checkAbsolutelyEverywhere(grid: list[list[list[int]]], thing) -> bool:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j][0] == thing:
                return True
    return False



# ======================================================================================
# ----------- The thing that makes all of this possible, it's DOSTUFF!!!! --------------
# ======================================================================================



def doStuff(plain: list[list[list[int]]],switch: bool,lifeIG: bool = False):
    e = 0
    t = 0
    #I'll take my small victories in optimization where I can
    
    #The tuple that holds the elements that are required to have a mini plane map
    requireminip = [1,2,3,4,6,7,8,9,10,14,15,17,18,19,22,23,24,25,27,28,29,30,31,32,33,34,36,38,39,40,41,42,44,45,46,47,48,49,54,55]
    if lifeIG:
        requireminip.append(0)
        requireminip.append(26)
    requireminip = tuple(requireminip)
    
    #The tuple that holds the elements that are required to have a mini grid map
    requireminig = (1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,22,23,24,25,27,28,29,30,32,34,36,39,40,41,42,43,44,45,46,47,48,49,51,52,53,54,55)
    
    conductors = (38,39,40,44,47,55)
    #Self explanitory
    
    sun = checkEverywhere(plain,[20,0])
    moon = checkEverywhere(plain,[21,0])
    jam = checkAbsolutelyEverywhere(plain,50)
    grid = deepcopy(plain)
    for a in range(len(plain)):
        for b in range(len(plain[0])):
            
            
            if plain[a][b] != grid[a][b]:
                continue
            
            e = plain[a][b][0]
            t = plain[a][b][1]
            
            au = False
            ad = False
            al = False
            ar = False
            
            if a + 1 < len(plain):
                ad = True
            if a - 1 > -1:
                au = True
            if b + 1 < len(plain[0]):
                ar = True
            if b - 1 > -1:
                al = True
            
            miniplain = []
            minigrid = []
            localPos = (1,1)
            
            if plain[a][b][0] in requireminip:
                for i in range(0-int(au),1+int(ad)):
                    p = []
                    for j in range(0-int(al),1+int(ar)):
                        if (i,j) == (0,0):
                            p.append(("self",e))
                            localPos = (1-int(not au),1-int(not al))
                            continue
                        p.append(tuple(plain[a+i][b+j]))
                    miniplain.append(tuple(p))
            
            if plain[a][b][0] in requireminig:
                for i in range(0-int(au),1+int(ad)):
                    g = []
                    for j in range(0-int(al),1+int(ar)):
                        if (i,j) == (0,0):
                            g.append(("self",e))
                            localPos = (1-int(not au),1-int(not al))
                            continue
                        g.append(tuple(grid[a+i][b+j]))
                    minigrid.append(tuple(g))
            
            miniplain = tuple(miniplain)
            minigrid = tuple(minigrid)
            
            #Possibly my biggest try statement
            
            try:
                
                #Air
                
                if e == 0:
                    if not lifeIG:
                        continue
                    #I need to optimize this more it's laggy as hell currently :(
                    l = neighborCount(miniplain,[37])
                    if l == 3:
                        grid[a][b] = [37,0]
                        continue
                    else:
                        l = neighborCount(miniplain,[26])
                        if l == 3:
                            grid[a][b] = [26,0]
                            continue
                
                #Sand
                
                elif e == 1:
                    if neighborCheck(miniplain,(9,30,55)):
                        e = 14
                        t = 2
                    else:
                        n = neighborTempCheck(miniplain,[14])
                        if n[0]:
                            e = 14
                            t = n[1]-1
                        elif random.randint(1,50) == 1:
                            if neighborCheck(miniplain,(3,15)):
                                e = 10
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if e == 1:
                            continue
                        else:
                            grid[a][b] = [e,t]
                    else:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b+(c[0]-2)] = [e,t]
                
                #Stone
                
                elif e == 2:
                    if random.randint(1,1000) == 1:
                        if neighborCheck(miniplain,[3,15,47]):
                            e = 11
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,0]
                    else:
                        if e == 2:
                            continue
                        else:
                            grid[a][b] = [e,0]
                
                #Water
                
                elif e == 3:
                    if coinflip():
                        if neighborCheck(miniplain,[30]):
                            e = 13
                            t = 10
                        elif neighborCount(miniplain,[22,23,27]) > 3:
                            e = 27
                    if neighborCheck(miniplain,(9,55)):
                        e = 13
                        t = 15
                    elif random.randint(1,10000) == 1:
                        if neighborCheck(miniplain,[18]):
                            e = 18
                    elif random.randint(1,20000) == 1:
                        if sun:
                            e = 13
                            t = 10
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            if e == 3:
                                continue
                            else:
                                grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [0,0]

                            if d[1]:
                                grid[a][b+1] = [e,t]
                            else:
                                grid[a][b-1] = [e,t]

                    else:
                        grid[a][b] = [0,0]

                        grid[a+1][b+(c[0]-2)] = [e,t]
                
                #Sugar
                
                elif e == 4:
                    if neighborCheck(miniplain,(9,20,21)):
                        e = 24
                    elif random.randint(1,5) == 1:
                        if neighborCheck(miniplain,[30]):
                            e = 30
                            t = 5
                    
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if random.randint(1,100) == 1:
                            if neighborCheck(miniplain,[3]):
                                e = 15
                        elif random.randint(1,5000) == 1:
                            if neighborCheck(miniplain,[18]):
                                e = 18
                        if e == 4:
                            continue
                        else:
                            grid[a][b] = [e,t] 
                    else:
                        if random.randint(1,10) == 1:
                            if neighborCheck(miniplain,[3]):
                                e = 15
                        grid[a][b] = [c[1],0]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a+1][b] = [e,0]
                            else:
                                if d[1]:
                                    grid[a+1][b+1] = [e,0]
                                else:
                                    grid[a+1][b-1] = [e,0]
                        else:
                            grid[a+1][b+(c[0]-2)] = [e,0]
                
                #Wall
                
                elif e == 5:
                    continue          
                
                #Dirt
                
                elif e == 6:
                    if random.randint(1,900) == 1:
                        if neighborCheck(miniplain,[8]) and sun:
                            e = 8
                    if random.randint(1,100) == 1:
                        if neighborCheck(miniplain,[3]):
                            e = 7
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        if e == 6:
                            continue
                        else:
                            grid[a][b] = [e,0]
                    else:
                        grid[a][b] = [0,0]
                        grid[a+1][b+(c[0]-2)] = [e,0]
                
                #Mud
                
                elif e == 7:
                    if random.randint(1,400) == 1:
                        if neighborCheck(miniplain,[8]) and sun:
                            e = 8
                    if neighborCheck(miniplain,(9,30,55)):
                        e = 6
                    elif random.randint(1,100) == 1:
                        if neighborCheck(miniplain,(46,47,48)):
                            e = 6
                    if random.randint(1,5000) == 1:
                        if neighborCheck(miniplain,[18]):
                            e = 18
                        elif neighborCheck(miniplain,[8]):
                            e = 8
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,0]
                    else:
                        if e == 7:
                            continue
                        else:
                            grid[a][b] = [e,0]
                
                #Plant
                
                elif e == 8:
                    if coinflip():
                        if neighborCheck(miniplain,[30]):
                            e = 31
                            t = 0
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,t]
                    else:
                        grid[a][b] = [e,t]
                
                #Lava
                
                elif e == 9:
                    if neighborCheck(miniplain,(3,7,10,13,15,18,22,23,25,27)):
                        t -= 2
                        if neighborCheck(miniplain,(3,15,22,23,25,27)):
                            t -= 4
                    
                    if neighborCheck(miniplain,[20]):
                        t = 10
                    elif neighborCheck(miniplain,[21]):
                        t = -10
                    
                    if random.randint(1,10) == 1:
                        if moon:
                            t -= 1
                    if t <= -10:
                        
                        e = 12
                    
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if random.randint(1,25) != 1:
                            if e == 9:
                                grid[a][b] = [e,t]
                                continue
                            else:
                                grid[a][b] = [e,0]
                                continue
                        d = lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            if e == 9:
                                grid[a][b] = [e,t]
                            else:
                                grid[a][b] = [e,0]
                        else:
                            grid[a][b] = [c[1],0]
                            if d[1]:
                                grid[a][b+1] = [e,t]
                            else:
                                grid[a][b-1] = [e,t]

                    else:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b+(c[0]-2)] = [e,t]
                
                #Wet Sand
                
                elif e == 10:
                    if neighborCheck(miniplain,(9,30,55)):
                        e = 14
                        t = 1
                    elif random.randint(1,100) == 1:
                        if neighborCheck(miniplain,(46,47,48)):
                            e = 1
                    else:
                        n = neighborTempCheck(miniplain,[14])
                        if n[0]:
                            e = 14
                            t = n[1]-1
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,t]
                    else:
                        if e == 10:
                            grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [e,0]
                
                #Gravel
                
                elif e == 11:
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        continue
                    else:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b+(c[0]-2)] = [11,0]
                
                #Obsidian
                
                elif e == 12:
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [12,0]
                    else:
                        continue
                
                #Steam
                
                elif e == 13:
                    if random.randint(1,20) == 1 and t > 0:
                        t -= 1
                    if t <= 0 and random.randint(1,34) == 1:
                        e = 16
                    c = sandCheck(minigrid,localPos,False,True,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos,False,False,True)
                        if not d[0]:
                            if e == 13:
                                grid[a][b] = [e,t]
                            else:
                                grid[a][b] = [e,0]
                        else:
                            grid[a][b] = [d[2],0]

                            if d[1]:
                                grid[a][b+1] = [e,t]
                            else:
                                grid[a][b-1] = [e,t]
                    else:
                        grid[a][b] = [c[1],t]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos,True,False,True)
                            if not d[0]:
                                grid[a-1][b] = [e,t]
                            else:
                                if d[1]:
                                    grid[a-1][b+1] = [e,t]
                                else:
                                    grid[a-1][b-1] = [e,t]
                        else:
                            grid[a-1][b+(c[0]-2)] = [e,t]
                        
                #Glass
                
                elif e == 14:
                    if coinflip() and t > 0:
                        t -= 1
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        continue
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [14,t]
                    else:
                        continue
                        
                #Sugar Water
                
                elif e == 15:
                    if neighborCheck(miniplain,(9,55)) or (coinflip() and neighborCheck(miniplain,[30])):
                        if coinflip():
                            e = 4
                        else:
                            e = 13
                    elif random.randint(1,2500) == 1:
                        if neighborCheck(miniplain,[18]):
                            e = 18
                        elif neighborCheck(miniplain,[24]):
                            e = 4
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos,False,True)
                        if not d[0]:
                            d = udWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                if e == 15:
                                    grid[a][b] = [e,t]
                                else:
                                    grid[a][b] = [e,0]
                            else:
                                grid[a][b] = [d[2],0]

                                if d[1]:
                                    grid[a+1][b] = [e,0]
                                else:
                                    grid[a-1][b] = [e,0]
                        else:
                            grid[a][b] = [d[2],0]

                            if d[1]:
                                grid[a][b+1] = [e,0]
                            else:
                                grid[a][b-1] = [e,0]

                    else:
                        grid[a][b] = [0,0]

                        grid[a+1][b+(c[0]-2)] = [e,0]
                
                #Clouds
                
                elif e == 16:
                    if random.randint(1,800) == 1:
                        if moon:
                            e = 22 
                        else:
                            e = 3
                    if random.randint(1,20) == 1:
                        if random.randint(1,4) != 1:
                            d = lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                if e == 16:
                                    grid[a][b] = [e,t]
                                else:
                                    grid[a][b] = [e,0]
                            else:
                                grid[a][b] = [d[2],0]
                                
                                if d[1]:
                                    grid[a][b+1] = [e,0]
                                else:
                                    grid[a][b-1] = [e,0]
                        else:
                            d = udWanderCheck(minigrid,localPos)
                            if not d[0]:
                                if e == 16:
                                    grid[a][b] = [e,t]
                                else:
                                    grid[a][b] = [e,0]
                            else:
                                grid[a][b] = [d[2],0]

                                if d[1]:
                                    grid[a+1][b] = [e,0]
                                else:
                                    grid[a-1][b] = [e,0]
                    else:
                        continue
                
                #Brick
                
                elif e == 17:
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        continue
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,0]
                    else:
                        continue
                
                #Algae
                
                elif e == 18:
                    if random.randint(1,6) == 1:
                        if neighborCheck(miniplain,(9,30,55)):
                            if coinflip():
                                e = 30
                                t = 5
                            else:
                                e = 32
                    o = lrCheck(miniplain[localPos[0]],localPos[1],True)
                    if o:
                        continue
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][b] = [e,t]
                    else:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b+(c[0]-2)] = [e,0]
                
                #Glass shards or dust or whatever you wanna see it as
                
                elif e == 19:
                    if neighborCheck(miniplain,(9,55)):
                        e = 14
                        t = 3
                    elif coinflip() and neighborCheck(miniplain,[30]):
                        e = 14
                        t = 0
                    else:
                        n = neighborTempCheck(miniplain,[14])
                        if n[0]:
                            e = 14
                            t = n[1]-1
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if e == 19:
                            grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [e,0]
                    else:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b+(c[0]-2)] = [e,t]
                #Sun
                
                elif e == 20:
                    continue
                #Moon
                
                elif e == 21:
                    continue
                
                #Snow
                
                elif e == 22:
                    if random.randint(1,100) == 1:
                        if sun:
                            e = 3
                    if random.randint(1,10) == 1:
                        if (not moon) and neighborCheck(miniplain,(3,15)):
                            e = 3
                    if neighborCheck(miniplain,(9,13,20,30,55)):
                        e = 3
                    if random.randint(1,5000) == 1:
                        e = 3
                    if random.randint(1,10000) == 1:
                        e = 23
                    if switch:
                        c = sandCheck(minigrid,localPos,True)
                        if c[0] == 0:
                            if e == 22:
                                grid[a][b] = [e,t]
                            else:
                                grid[a][b] = [e,0] 
                        else:
                            grid[a][b] = [c[1],0]
                            if c[0] == 2:
                                d = lrWanderCheck(minigrid,localPos, True)
                                if not d[0]:
                                    grid[a+1][b] = [e,0]
                                else:
                                    if d[1]:
                                        grid[a+1][b+1] = [e,0]
                                    else:
                                        grid[a+1][b-1] = [e,0]
                            else:
                                grid[a+1][b+(c[0]-2)] = [e,0]
                    else:
                        if e == 22:
                            grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [e,0]
                
                #Ice
                
                elif e == 23:
                    if random.randint(1,200) == 1:
                        if sun:
                            e = 3
                    if coinflip():
                        if neighborCheck(miniplain,(13,20)):
                            e = 3
                    if neighborCheck(miniplain,(9,30,55)):
                        e = 3
                    if random.randint(1,1000) == 1:
                        if neighborCheck(miniplain,(3,15)):
                            e = 3
                    c = stoneCheck(minigrid,localPos,True)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,0]
                    else:
                        if e == 2:
                            grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [e,0]
                
                #Sugar Crystal
                
                elif e == 24:
                    if random.randint(1,7000) == 1:
                        if neighborCheck(miniplain,[18]):
                            e = 18
                    elif random.randint(1,5000) == 1:
                        if neighborCheck(miniplain,[3,15]):
                            e = 4
                    elif random.randint(1,50) == 1:
                        if neighborCheck(miniplain,[30]):
                            e = 30
                            t = 5
                    
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        if e == 24:
                            grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [e,0]
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,0]
                    else:
                        if e == 24:
                            grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [e,0]
                
                #Packed Ice
                
                elif e == 25:
                    if random.randint(1,5) == 1:
                        if neighborCheck(miniplain,(9,55)):
                            e = 23
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        continue
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,0]
                    else:
                        if e == 25:
                            grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [e,0]
                
                #Life WORKING?!!~?!?!?!@43TUHREGAGR\\\
                
                elif e == 26:
                    if lifeIG:
                        #Now life has a few more rules that tell it that it's neighbors don't have to be it's own kind of life, but can be of different kinds of life or things that allow for life! (This should have very interesting effects)
                        l = neighborCount(miniplain,(4,8,15,21,24,26,28,31,37))
                        if jam:
                            if l < random.randint(0,10) or l > random.randint(0,10):
                                grid[a][b] = [0,0]
                            else:
                                grid[a][b] = [26,0]
                        else:
                            if l < 2 or l > 3:
                                grid[a][b] = [0,0]
                            else:
                                grid[a][b] = [26,0]
                        continue
                    else:
                        grid[a][b] = randomelement()
                        continue
                
                #Sludge
                
                elif e == 27:
                    if random.randint(1,50) == 1:
                        if sun:
                            e = 3
                    if random.randint(1,500) == 1 and not moon:
                            e = 3
                    if coinflip():
                        if (not moon) and neighborCheck(miniplain,(3,15)):
                            e = 3
                    if coinflip() and e != 27:
                        if neighborCount(miniplain,[22,23,27]) > 3:
                            e = 27
                    if random.randint(1,20) == 1:
                        if neighborCount(miniplain,[22,23,27]) > 4:
                            e = 23
                    if neighborCheck(miniplain,(9,13,20,30,55)):
                        e = 13
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if e == 27:
                            grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [e,0]
                    else:
                        grid[a][b] = [c[1],0]
                        if c[0] == 2:
                            grid[a+1][b] = [e,0]
                        else:
                            grid[a+1][b+(c[0]-2)] = [e,0]

                #Flower things
                
                elif e == 28:
                    if jam:
                        t = 1
                        continue
                    if random.randint(1,4) == 1:
                        if neighborCheck(miniplain,(9,30,55)):
                            if coinflip():
                                e = 30
                                t = 5
                            else:
                                e = 32
                    #Seed
                    if plain[a][b][1] == 0:
                        c = sandCheck(minigrid,localPos)
                        if c[0] == 0:
                            if random.randint(1,100) == 1 and neighborCheck(miniplain,(7,8,10,18,27,32)):
                                grid[a][b] = [e,random.randint(2,8)]
                            else:
                                grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [c[1],0]
                            grid[a+1][b+(c[0]-2)] = [e,t]
                    #Stem
                    elif plain[a][b][1] > 1 and a - 1 != 0:
                        t -= 1
                        grid[a-1][b] = [e,t]
                        t = -1
                        grid[a][b] = [e,t]
                    #Bloom
                    elif plain[a][b][1] != -1:
                        grid[a][b] = [36,random.randint(0,11)]
                        c = random.randint(0,11)
                        if a + 1 != len(plain):
                            grid[a+1][b] = [36,c]
                        if a - 1 != -1 and grid[a-1][b][0] == 0:
                            grid[a-1][b] = [36,c]
                        if b + 1 != len(plain[0]) and grid[a][b+1][0] == 0:
                            grid[a][b+1] = [36,c]
                        if b - 1 != -1 and grid[a][b-1][0] == 0:
                            grid[a][b-1] = [36,c]
                           
                #Oil (Pls don't take americuh)
                
                elif e == 29:
                    if random.randint(1,15) == 1:
                        if neighborCheck(miniplain,(9,30,55)):
                            e = 30
                            t = 5
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos,False,True)
                        if not d[0]:
                            d = udWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                if e == 29:
                                    grid[a][b] = [e,t]
                                else:
                                    grid[a][b] = [e,t]
                            else:
                                grid[a][b] = [d[2],t]

                                if d[1]:
                                    grid[a+1][b] = [e,t]
                                else:
                                    grid[a-1][b] = [e,t]
                        else:
                            grid[a][b] = [d[2],0]

                            if d[1]:
                                grid[a][b+1] = [e,t]
                            else:
                                grid[a][b-1] = [e,t]

                    else:
                        grid[a][b] = [0,0]

                        grid[a+1][b+(c[0]-2)] = [e,0]
                
                #Fire
                
                elif e == 30:
                    flame = False
                    if (random.randint(1,4) == 1 or moon or jam) and t > 0:
                        if not sun:
                            t -= 1
                        else:
                            if coinflip():
                                t -= 1
                    if neighborCheck(miniplain,(4,8,15,18,20,24,28,29,31)):
                        if moon:
                            if (coinflip() or sun) and t < 2:
                                t = 2
                        else:
                            t = 5
                        flame = True
                    elif neighborCheck(miniplain,[33]):
                        t = 2
                    elif random.randint(1,10) == 1:
                        o = neighborTempCheck(miniplain,[30],">",t)
                        if o[0]:
                            t = o[1] - 1
                    if t <= 0:
                        e = 0
                    if flame and random.randint(1,5) != 1:
                        c = [0]
                    else:
                        c = sandCheck(minigrid,localPos,False,True,True)
                    if c[0] == 0:
                        if flame and random.randint(1,8) != 1:
                            d = [False]
                        else:
                            d = lrWanderCheck(minigrid,localPos,False,False,True)
                        if not d[0]:
                            if e == 30:
                                grid[a][b] = [e,t]
                            else:
                                grid[a][b] = [e,0]
                        else:
                            grid[a][b] = [d[2],0]

                            if d[1]:
                                grid[a][b+1] = [e,t]
                            else:
                                grid[a][b-1] = [e,t]
                    else:
                        grid[a][b] = [c[1],t]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos,True,False,True)
                            if not d[0]:
                                grid[a-1][b] = [e,t]
                            else:
                                if d[1]:
                                    grid[a-1][b+1] = [e,t]
                                else:
                                    grid[a-1][b-1] = [e,t]
                        else:
                            grid[a-1][b+(c[0]-2)] = [e,t]
                
                #Wood
                
                elif e == 31:
                    if coinflip():
                        if neighborCount(miniplain,(9,30,55)) > random.randint(1,5):
                            e = 32
                    elif random.randint(1,20) == 1:
                        if neighborCheck(miniplain,[30]):
                            e = 30
                            t = 5
                    elif random.randint(1,40) == 1:
                        if neighborCheck(miniplain,(9,55)):
                            e = 30
                            t = 5
                    
                    if e != 31:
                        grid[a][b] = [e,t]
                
                #Ash
                
                elif e == 32:
                    if random.randint(1,1000) == 1:
                        if neighborCount(miniplain,[2,11,29,32]) > 3:
                            t += random.randint(1,2)
                    elif random.randint(1,100) == 1:
                        if neighborCheck(miniplain,[3,15]):
                            e = 34
                    if t >= 100:
                        e = 29
                        t = 0
                    elif jam:
                        t = 0
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][b] = [e,t] 
                    else:
                        grid[a][b] = [c[1],0]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a+1][b] = [e,t]
                            else:
                                if d[1]:
                                    grid[a+1][b+1] = [e,t]
                                else:
                                    grid[a+1][b-1] = [e,t]
                        else:
                            grid[a+1][b+(c[0]-2)] = [e,t]
                
                #Cloner (Yes, I went there)
                
                elif e == 33:
                    if jam:
                        t = 0
                    elif plain[a][b][1] == 0:
                        t = myNeighbor(miniplain,[33])
                    else:
                        if a + 1 != len(plain) and grid[a+1][b][0] == 0:
                            grid[a+1][b] = [plain[a][b][1],0]
                        if a - 1 != -1 and grid[a-1][b][0] == 0:
                            grid[a-1][b] = [plain[a][b][1],0]
                        if b + 1 != len(plain[0]) and grid[a][b+1][0] == 0:
                            grid[a][b+1] = [plain[a][b][1],0]
                        if b - 1 != -1 and grid[a][b-1][0] == 0:
                            grid[a][b-1] = [plain[a][b][1],0]
                    grid[a][b] = [e,t]
                
                #Clay
                
                elif e == 34:
                    if neighborCheck(miniplain,(9,30,55)):
                        e = 17
                    
                    if random.randint(1,10) == 1:
                        if moon:
                            t -= 1
                    if t <= -10:
                        
                        e = 12
                    
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        if random.randint(1,40) != 1:
                            if random.randint(1,10) == 1:
                                d = udWanderCheck(minigrid,localPos,True)
                            else:
                                d = [False]
                            if not d[0]:
                                if e == 17:
                                    grid[a][b] = [e,t]
                                    continue
                                else:
                                    grid[a][b] = [e,0]
                                    continue
                            else:
                                grid[a][b] = [d[2],0]

                                if d[1]:
                                    grid[a+1][b] = [e,0]
                                else:
                                    grid[a-1][b] = [e,0]
                                continue
                            
                        d = lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            if e == 17:
                                grid[a][b] = [e,t]
                            else:
                                grid[a][b] = [e,0]
                        else:
                            grid[a][b] = [c[1],0]
                            if d[1]:
                                grid[a][b+1] = [e,t]
                            else:
                                grid[a][b-1] = [e,t]

                    else:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b+(c[0]-2)] = [e,t]
                
                #VOID
                
                elif e == 35:
                    if jam:
                        continue
                    if a + 1 != len(plain) and grid[a+1][b][0] != 35:
                        grid[a+1][b] = [0,0]
                    if a - 1 != -1 and grid[a-1][b][0] != 35:
                        grid[a-1][b] = [0,0]
                    if b + 1 != len(plain[0]) and grid[a][b+1][0] != 35:
                        grid[a][b+1] = [0,0]
                    if b - 1 != -1 and grid[a][b-1][0] != 35:
                        grid[a][b-1] = [0,0]
                
                #Petal (Hidden)
                
                elif e == 36:
                    if random.randint(1,15) == 1:
                        if neighborCheck(miniplain,(9,30,55)):
                            if coinflip():
                                e = 30
                                t = 5
                            else:
                                e = 32
                    if neighborCheck(miniplain,[8,28,36]):
                        c = [True]
                    else:
                        c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,t]
                    else:
                        grid[a][b] = [e,t]
                
                #Cancer (Doesn't know how to die) (Hidden)
                
                elif e == 37:
                    if lifeIG:
                        if jam:
                            #This makes it obey Life's rules
                            if l < 2 or l > 3:
                                grid[a][b] = [0,0]
                            else:
                                grid[a][b] = [37,0]
                        continue
                    else:
                        grid[a][b] = randomelement()
                
                #Iron
                
                elif e == 38:
                    if random.randint(1,1000) == 1:
                        if neighborCheck(miniplain,[3,15,47]):
                            e = 44
                    if t == 1 or jam:
                        t = 2
                    elif (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    grid[a][b] = [e,t] 
                
                #Iron Sand
                
                elif e == 39:
                    if random.randint(1,1000) == 1:
                        if neighborCheck(miniplain,[3,15,47]):
                            e = 45
                    if t == 1 or jam:
                        t = 2
                    elif (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][b] = [e,t]
                    else:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b+(c[0]-2)] = [e,t]
                
                #Iron Brick
                
                elif e == 40:
                    if random.randint(1,1000) == 1:
                        if neighborCheck(miniplain,[3,15,47]):
                            e = 44
                    if t == 1 or jam:
                        t = 2
                    elif (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        grid[a][b] = [e,t]
                        continue
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,t]
                    else:
                        grid[a][b] = [e,t]
                
                #Smart Remover (Based on the bacteria mod from minecraft)
                
                elif e == 41:
                    if jam:
                        t = 0
                        if random.randint(1,4) == 1:
                            e = 0
                    elif t == 0:
                        if a + 1 != len(plain) and grid[a+1][b][0] != 0 and plain[a+1][b][1] != 41:
                            t = grid[a+1][b][0]
                    elif t != 41:
                        if a + 1 != len(plain) and grid[a+1][b][0] == t:
                            grid[a+1][b] = [e,t]
                        if a - 1 != -1 and grid[a-1][b][0] == t:
                            grid[a-1][b] = [e,t]
                        if b + 1 != len(plain[0]) and grid[a][b+1][0] == t:
                            grid[a][b+1] = [e,t]
                        if b - 1 != -1 and grid[a][b-1][0] == t:
                            grid[a][b-1] = [e,t]
                        if not neighborCheck(miniplain,[t]) or neighborCount(miniplain,[41]) == 0:
                            e = 0
                            t = 0
                    c = stoneCheck(minigrid,localPos,True)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,t]
                    else:
                        grid[a][b] = [e,t]
                
                #Smart Converter (Probably my most complicated element yet since it's temprature is off the charts!)
                
                elif e == 42:
                    if jam:
                        t = 0
                        if random.randint(1,4) == 1:
                            e = 0
                    elif t == 0:
                        if a + 1 != len(plain) and grid[a+1][b][0] != 0 and grid[a+1][b][1] != 42 and a - 1 != -1 and grid[a-1][b][0] != 0 and grid[a-1][b][1] != 42:
                            #This is complex, lemme explain
                            
                            t = grid[a-1][b][0]*1000
                            #This gets the value of the pixel above it and multiplies it by 1000, so when we do our lil // later, we can get this element back
                            
                            t += grid[a+1][b][0]
                            #This gets the value of the pixel below it and adds it to the temp, so when we can do our lil % later and get this element back too!
                    else:
                        rt = t//1000 #The element that's gonna REPLACE the converted element
                        ct = t%1000 #The element that's gonna get CONVERTED into the replaced element
                        if rt != 42 and ct != 42:
                            if a + 1 != len(plain) and grid[a+1][b][0] == ct:
                                grid[a+1][b] = [e,t]
                            if a - 1 != -1 and grid[a-1][b][0] == ct:
                                grid[a-1][b] = [e,t]
                            if b + 1 != len(plain[0]) and grid[a][b+1][0] == ct:
                                grid[a][b+1] = [e,t]
                            if b - 1 != -1 and grid[a][b-1][0] == ct:
                                grid[a][b-1] = [e,t]
                            if not neighborCheck(miniplain,[ct]) or neighborCount(miniplain,[42]) == 0:
                                e = rt
                                t = 0
                    c = stoneCheck(minigrid,localPos,True)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,t]
                    else:
                        grid[a][b] = [e,t]
                
                
                #Electricity
                
                elif e == 43:
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0 or jam:
                        grid[a][b] = [0,0]
                    else:
                        grid[a][b] = [c[1],0]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                grid[a+1][b] = [e,0]
                            else:
                                if d[1]:
                                    grid[a+1][b+1] = [e,0]
                                else:
                                    grid[a+1][b-1] = [e,0]
                        else:
                            grid[a+1][b+(c[0]-2)] = [e,0]
                
                #Rusted Iron
                
                elif e == 44:
                    if random.randint(1,1000) == 1:
                        if neighborCheck(miniplain,[3,15,47]):
                            e = 45
                    if t == 1 or jam:
                        t = 2
                    elif neighborTempCheck(miniplain,conductors,"==",1)[0] and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        grid[a][b] = [e,t]
                        continue
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,t]
                    else:
                        grid[a][b] = [e,t]
                
                #Rust
                
                elif e == 45:
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if e == 1:
                            continue
                        else:
                            grid[a][b] = [e,t]
                    else:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b+(c[0]-2)] = [e,t]
                
                #Salt
                
                elif e == 46:
                    if neighborCheck(miniplain,(9,55)):
                        e = 55
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if random.randint(1,100) == 1:
                            if neighborCheck(miniplain,[3]):
                                e = 47
                        grid[a][b] = [e,t]
                    else:
                        if random.randint(1,10) == 1:
                            if neighborCheck(miniplain,[3]):
                                e = 47
                        grid[a][b] = [c[1],0]
                        grid[a+1][b+(c[0]-2)] = [e,t]
                
                #Salt Water
                
                elif e == 47:
                    if t == 1 or jam:
                        t = 2
                    elif (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    
                    if neighborCheck(miniplain,(9,55)) or (coinflip() and neighborCheck(miniplain,[30])):
                        if coinflip():
                            e = 46
                        else:
                            e = 13
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos,False,True)
                        if not d[0]:
                            d = udWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                grid[a][b] = [e,t]
                            else:
                                grid[a][b] = [d[2],0]

                                if d[1]:
                                    grid[a+1][b] = [e,t]
                                else:
                                    grid[a-1][b] = [e,t]
                        else:
                            grid[a][b] = [d[2],0]

                            if d[1]:
                                grid[a][b+1] = [e,t]
                            else:
                                grid[a][b-1] = [e,t]

                    else:
                        grid[a][b] = [0,0]

                        grid[a+1][b+(c[0]-2)] = [e,t]
                
                #Salt Crystal
                
                elif e == 48:
                    if neighborCheck(miniplain,(9,55)):
                        e = 55
                    elif random.randint(1,5000) == 1:
                        if neighborCheck(miniplain,[3,47]):
                            e = 46
                    
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        grid[a][b] = [e,t]
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b] = [e,0]
                    else:
                        if e == 24:
                            grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [e,0]
                
                #leaf
                
                elif e == 49:
                    
                    if neighborCheck(miniplain,(9,30,55)):
                        if coinflip():
                            e = 30
                            t = 5
                        else:
                            e = 32
                    
                    if coinflip() or (neighborCheck(miniplain,[8,31]) and not (random.randint(1,400) == 1 and moon)):
                        grid[a][b] = [e,t]
                        continue
                    
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][b] = [e,t] 
                    else:
                        grid[a][b] = [c[1],0]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a+1][b] = [e,0]
                            else:
                                if d[1]:
                                    grid[a+1][b+1] = [e,0]
                                else:
                                    grid[a+1][b-1] = [e,0]
                        else:
                            grid[a+1][b+(c[0]-2)] = [e,0]
                
                
                #Antisand
                
                elif e == 51:
                    c = sandCheck(minigrid,localPos,False,True)
                    if c[0] == 0:
                        grid[a][b] = [e,t]
                        continue
                    else:
                        grid[a][b] = [c[1],0]
                        grid[a-1][b+(c[0]-2)] = [e,t]
                
                #Antistone
                
                elif e == 52:
                    c = stoneCheck(minigrid,localPos,False,True)
                    if not c[0]:
                        grid[a][b] = [c[1],0]
                        grid[a-1][b] = [e,0]
                    else:
                        grid[a][b] = [e,0]
                
                #Antiwater
                
                elif e == 53:
                    c = sandCheck(minigrid,localPos,True,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos,False,True,True)
                        if not d[0]:
                            if e == 3:
                                continue
                            else:
                                grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [0,0]

                            if d[1]:
                                grid[a][b+1] = [e,t]
                            else:
                                grid[a][b-1] = [e,t]

                    else:
                        grid[a][b] = [0,0]

                        grid[a-1][b+(c[0]-2)] = [e,t]
                
                #IDENTITY NOT FOUND =( https://www.youtube.com/watch?v=4bLf2wDJA5s
                elif e == 54:
                    
                    idk = random.randint(1,6)
                    t = idk
                    if jam:
                        e = idk
                    
                    #Sandbit
                    
                    if idk == 1:
                        if neighborCheck(miniplain,(9,30,55)):
                            e = 14
                            t = 2
                        else:
                            n = neighborTempCheck(miniplain,[14])
                            if n[0]:
                                e = 14
                                t = n[1]-1
                            elif random.randint(1,50) == 1:
                                if neighborCheck(miniplain,(3,15)):
                                    e = 10
                        c = sandCheck(minigrid,localPos)
                        if c[0] == 0:
                            if e == 1:
                                continue
                            else:
                                grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [c[1],0]
                            grid[a+1][b+(c[0]-2)] = [e,t]
                    
                    #Stonebit
                    
                    elif idk == 2:
                        if random.randint(1,1000) == 1:
                            if neighborCheck(miniplain,[3,15,47]):
                                e = 11
                        c = stoneCheck(minigrid,localPos)
                        if not c[0]:
                            grid[a][b] = [c[1],0]
                            grid[a+1][b] = [e,t]
                        else:
                            grid[a][b] = [e,t]
                    
                    #Waterbit
                    
                    elif idk == 3:
                        if coinflip():
                            if neighborCheck(miniplain,[30]):
                                e = 13
                                t = 10
                            elif neighborCount(miniplain,[22,23,27]) > 3:
                                e = 27
                        if neighborCheck(miniplain,(9,55)):
                            e = 13
                            t = 15
                        elif random.randint(1,10000) == 1:
                            if neighborCheck(miniplain,[18]):
                                e = 18
                        elif random.randint(1,20000) == 1:
                            if sun:
                                e = 13
                                t = 10
                        c = sandCheck(minigrid,localPos,True)
                        if c[0] == 0:
                            d = lrWanderCheck(minigrid,localPos)
                            if not d[0]:
                                grid[a][b] = [e,t]
                            else:
                                grid[a][b] = [0,0]

                                if d[1]:
                                    grid[a][b+1] = [e,t]
                                else:
                                    grid[a][b-1] = [e,t]

                        else:
                            grid[a][b] = [0,0]

                            grid[a+1][b+(c[0]-2)] = [e,t]
                    
                    #Sugarbit
                    
                    elif idk == 4:
                        if neighborCheck(miniplain,(9,20,21)):
                            e = 24
                        elif random.randint(1,5) == 1:
                            if neighborCheck(miniplain,[30]):
                                e = 30
                                t = 5
                        
                        c = sandCheck(minigrid,localPos)
                        if c[0] == 0:
                            if random.randint(1,100) == 1:
                                if neighborCheck(miniplain,[3]):
                                    e = 15
                            elif random.randint(1,5000) == 1:
                                if neighborCheck(miniplain,[18]):
                                    e = 18
                            grid[a][b] = [e,t] 
                            continue
                        else:
                            if random.randint(1,10) == 1:
                                if neighborCheck(miniplain,[3]):
                                    e = 15
                            grid[a][b] = [c[1],0]
                            if c[0] == 2:
                                d = lrWanderCheck(minigrid,localPos, True)
                                if not d[0]:
                                    grid[a+1][b] = [e,t]
                                else:
                                    if d[1]:
                                        grid[a+1][b+1] = [e,t]
                                    else:
                                        grid[a+1][b-1] = [e,t]
                            else:
                                grid[a+1][b+(c[0]-2)] = [e,t]
                    
                    #Wallbit
                    
                    elif idk == 5:
                        continue          
                    
                    #Dirtbit
                    
                    elif idk == 6:
                        if random.randint(1,900) == 1:
                            if neighborCheck(miniplain,[8]) and sun:
                                e = 8
                        if random.randint(1,100) == 1:
                            if neighborCheck(miniplain,[3]):
                                e = 7
                        c = sandCheck(minigrid,localPos,True)
                        if c[0] == 0:
                            grid[a][b] = [e,t]
                            continue
                        else:
                            grid[a][b] = [0,0]
                            grid[a+1][b+(c[0]-2)] = [e,t]
                
                #Jammer
                
                elif e == 50:
                    t += 1
                    if t <= 50:
                        grid[a][b] = [e,t]
                    else:
                        grid[a][b] = [0,0]

                #Molten Salt (Yes, it's a thing)
                
                elif e == 55:
                    if t == 1 or jam:
                        t = 2
                    elif (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    
                    if random.randint(1,25) == 1:
                        e = 46
                    #Too salty to just go away...
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if random.randint(1,25) != 1:
                            if e == 9:
                                grid[a][b] = [e,t]
                                continue
                            else:
                                grid[a][b] = [e,t]
                                continue
                        d = lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            if e == 9:
                                grid[a][b] = [e,t]
                            else:
                                grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [c[1],0]
                            if d[1]:
                                grid[a][b+1] = [e,t]
                            else:
                                grid[a][b-1] = [e,t]

                    else:
                        grid[a][b] = [c[1],0]
                        grid[a+1][b+(c[0]-2)] = [e,t]
                
            except IndexError:
                print("Error in doing element", grid[a][b], "index out of range (Did you remember to put the element ID in the corisponding mini-allowed tuple?)")
    return grid


live = False
alive = False
ice = False
fps = 60

def remindMe() -> None:
    print("Press the keys for the element!  1: Sand  2: Stone  3: Water  4: Sugar  5: Wall  6: Dirt  7: Mud  8: Plant  9: Lava ")
    print("Q: Iron  W: Gravel  E: Obsidian  R: Steam  T: Glass  Y: Salt  U: Cloud  I: Brick O: Clay  P: Void  A: Algae")
    print("G: Snow  H: Ice  J: Sugar Crystal  K: Leaf  L: Life particle (think the game of life, If turned off it will just be random)")
    print("Z: Electricity  X: Flower Seed  C: Oil  V: Fire  B: Wood  N: Jammer (Screws stuff up)  M: Cloner  S: Glass shards  D: Sun  F: Moon")
    print("To start the sandbox, press Ctrl. To go a single step in the sandbox, press Space.\nTo clear the sandbox, press the left Alt key. To clear the sandbox and have there be an ocean, hit the right Alt key.\nIf you want it to be lava, hit the Del key. Sugar water ocean? Right Ctrl.\nTo activate the game of life and all it's whimsy, press the CAPS LOCK key. To get an element that's not on this list, press the Right Shift key then enter the element's ID (number) in the console.\nTo change the brush size, hit up to grow it, hit down to shrink it.")
    print("To save your sandbox, press either enter key. To load a sandbox, press the 0 key. To show this again, hit backspace")

remindMe()

fliposwitch = True
#this makes sure that the sand keeps going in a straight line while placing it when it's active, and also some other stuff

while breaking:
    d = 0
    for event in pygame.event.get(): #Event Queue (or whatever it's called)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            breaking = False
        if event.type == pygame.MOUSEBUTTONDOWN and tap:
            fire = True
            tap = False
            if event.button == 3:
                ice = True
        if event.type == pygame.MOUSEBUTTONUP:
            tap = True
            ice = False
        if event.type == pygame.MOUSEMOTION:
            mousePos = Vector2(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                live = True
                #Go a single step forward
            if event.key == pygame.K_LCTRL:
                live = True
                if alive:
                    alive = False
                else:
                    alive = True
                #Go a step forward every tick until pressed again
            if event.key == pygame.K_LALT:
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
            elif event.key == pygame.K_RALT:
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[3,0] for _ in range(landx)]
            elif event.key == pygame.K_RCTRL:
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[15,0] for _ in range(landx)]
            elif event.key == pygame.K_DELETE:
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[9,0] for _ in range(landx)]
            elif event.key == pygame.K_SLASH:
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[29,0] for _ in range(landx)]
            elif event.key == pygame.K_UP:
                brushsize += 1
                print("brush size is now", (brushsize*2+1))
            elif event.key == pygame.K_DOWN:
                if 0 < brushsize:
                    brushsize -= 1
                    print("brush size is now", (brushsize*2+1))
            elif event.key == pygame.K_BACKSPACE:
                remindMe()
            elif event.key == pygame.K_TAB:
                if showfps:
                    showfps = False
                else:
                    showfps = True
            elif event.key == pygame.K_CAPSLOCK:
                if werealsodoinglife:
                    werealsodoinglife = False
                    print("Destroying life")
                else:
                    werealsodoinglife = True
                    print("Doing life")
            elif event.key == pygame.K_1:
                element = 1
            elif event.key == pygame.K_2:
                element = 2
            elif event.key == pygame.K_3:
                element = 3
            elif event.key == pygame.K_4:
                element = 4
            elif event.key == pygame.K_5:
                element = 5
            elif event.key == pygame.K_6:
                element = 6
            elif event.key == pygame.K_7:
                element = 7
            elif event.key == pygame.K_8:
                element = 8
            elif event.key == pygame.K_9:
                element = 9
            elif event.key == pygame.K_q:
                element = 38
            elif event.key == pygame.K_w:
                element = 11
            elif event.key == pygame.K_e:
                element = 12
            elif event.key == pygame.K_r:
                element = 13
            elif event.key == pygame.K_t:
                element = 14
            elif event.key == pygame.K_y:
                element = 46
            elif event.key == pygame.K_u:
                element = 16
            elif event.key == pygame.K_i:
                element = 17
            elif event.key == pygame.K_a:
                element = 18
            elif event.key == pygame.K_s:
                element = 19
            elif event.key == pygame.K_d:
                element = 20
            elif event.key == pygame.K_f:
                element = 21
            elif event.key == pygame.K_g:
                element = 22
            elif event.key == pygame.K_h:
                element = 23
            elif event.key == pygame.K_j:
                element = 24
            elif event.key == pygame.K_k:
                element = 49
            elif event.key == pygame.K_l:
                element = 26
            elif event.key == pygame.K_z:
                element = 43
            elif event.key == pygame.K_x:
                element = 28
            elif event.key == pygame.K_c:
                element = 29
            elif event.key == pygame.K_v:
                element = 30
            elif event.key == pygame.K_b:
                element = 31
            elif event.key == pygame.K_n:
                element = 50
            #Oops I just realized that I forgot to include o and p
            elif event.key == pygame.K_m:
                element = 33
            elif event.key == pygame.K_o:
                element = 34
            elif event.key == pygame.K_p:
                element = 35
            #For elements that aren't here
            elif event.key == pygame.K_RSHIFT:
                try:
                    element = int(input("Enter the element ID\n"))
                    print("Set element to", elementNames[element])
                except:
                    print("THAT'S NOT A VALID NUMBER FOR AN ELEMENT!!!")
            #The ultimate thing: SAVING!
            elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                alive = False
                print("What would you like to name your file? (If it's a save that already exists, it will override the save)")
                filename = input()
                legal = True
                for char in filename:
                    if char in illegals:
                        print("File cannot contain an illegal character!", illegals)
                        legal = False
                        break
                if legal:
                    print("Saving", filename+ ".txt to your saves folder... (You better not close your program!)")
                    try:
                        thefile = open('sandsaves/'+filename+'.txt', 'w')
                        data = []
                        data.append(str(landx))
                        data.append(str(landy))
                        data.append(str(screenx))
                        data.append(str(screeny))
                        for ay in range(len(land)):
                            for bx in range(len(land[0])):
                                data.append(str(land[ay][bx][0]))
                                data.append(str(land[ay][bx][1]))
                        writing = ' '.join(data)
                        thefile.write(writing)
                        thefile.close()
                        print("Save successful!")
                    except FileNotFoundError as e:
                        print(f'An error occured: {e}')
                        print("Maybe you don't have a sandsaves folder for the saves to go to. (You'll have to make it manually)")
                    except:
                        print(f'An error occured, but we don\'t know how!')
                        print("Please contact the creator of this sandbox to see what the issue could be")
            #What's the use of saving if you can't LOAD?
            elif event.key == pygame.K_0:
                alive = False
                print("What file would you like to load?")
                filename = input()
                legal = True
                for char in filename:
                    if char in illegals:
                        print("File cannot contain an illegal character!", illegals)
                        legal = False
                        break
                if legal:
                    backupx = landx
                    backupy = landy
                    bacnupsx = screenx
                    backupsy = screeny
                    backupland = deepcopy(land)
                    backupscreen = screen
                    fail = True
                    print("Loading", filename+ ".txt from your saves folder...")
                    try:
                        thefile = open('sandsaves/'+filename+'.txt', 'r')
                        reading = thefile.read().split()
                        thefile.close()
                        print(filename, "read with", len(reading), "numbers!")
                        for inny in range(len(reading)):
                            reading[inny] = int(reading[inny])
                        landx = reading[0]
                        landy = reading[1]
                        screenx = reading[2]
                        screeny = reading[3]
                        print("Grid size:", landx, "by", landy, "pixels on a", screenx, "by", screeny, "gaming window.")
                        land = []
                        for ay in range(landy):
                            land.append([])
                            for bx in range(landx):
                                pxl = (bx+(landx*ay)) * 2 + 4
                                land[ay].append([reading[pxl],reading[pxl+1]])
                        
                        screen = pygame.display.set_mode((screenx,screeny))
                        #The loading should go smoothly from here so we don't have to worry about these variables being screwed
                        landyx = (screenx/landx)
                        landyy = (screeny/landy)
                        fail = False
                        if (not werealsodoinglife) and (checkEverywhere(land,[26,0]) or checkEverywhere(land,[37,0])):
                            print("Warning! This save contains life particles and life isn't enabled. You should probably enable it for the intended experience!")
                        print("Load successful!")
                    except FileNotFoundError as e:
                        print(f'An error occured: {e}')
                        print("Try again with a file that exists. (Maybe you don't have any :/))")
                    except TypeError as e:
                        print(f'An error occured: {e}')
                        print("Your file might have more than just numbers in it.")
                    except IndexError as e:
                        print(f'An error occured: {e}')
                        print("It's possible your grid isn't matching up with the data in a way!")
                    except:
                        print(f'An error occured, but we don\'t know how!')
                        print("Please contact the creator of this sandbox to see what the issue could be")
                    if fail:
                        landx = backupx
                        landy = backupy
                        screenx = bacnupsx
                        screeny = backupsy
                        land = deepcopy(backupland)
                        screen = backupscreen
    
    clock.tick(60)
    if showfps and fps != int(clock.get_fps()):
        fps = int(clock.get_fps())
        print("fps:", fps)
    
    if live:
        land = doStuff(land,fliposwitch,werealsodoinglife)


    if fliposwitch and alive:
        fliposwitch = False
    else:
        fliposwitch = True

    if (not tap) and fliposwitch:
        x = int(mousePos.x/landyx)
        y = int(mousePos.y/landyy)
        for l in range(0-brushsize,1+brushsize):
            for m in range(0-brushsize,1+brushsize):
                t = 0
                try:
                    if element == 13 or element == 30:
                        t = 5
                    elif element == 19:
                        t = random.randint(0,255)
                    elif element == 54:
                        t = random.randint(1,6)
                    if ice:
                        land[y+l][x+m] = [0,t]
                    else:
                        land[y+l][x+m] = [element,t]
                except IndexError:
                    print("OUT OF BOUNDS, FOOL!!!")

    fire = False
    screen.fill((0,0,0))
    for i in range(len(land)):
        for j in range(len(land[0])):
            el = land[i][j][0]
            et = land[i][j][1]
            if el == 1:
                pygame.draw.rect(screen,(255,255,0),(j*landyx,i*landyy,landyx,landyy))
            elif el == 2:
                pygame.draw.rect(screen,(150,150,150),(j*landyx,i*landyy,landyx,landyy))
            elif el == 3:
                pygame.draw.rect(screen,(0,0,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 4:
                pygame.draw.rect(screen,(250,250,250),(j*landyx,i*landyy,landyx,landyy))
            elif el == 5:
                pygame.draw.rect(screen,(100,100,100),(j*landyx,i*landyy,landyx,landyy))
            elif el == 6:
                pygame.draw.rect(screen,(200,100,50),(j*landyx,i*landyy,landyx,landyy))
            elif el == 7:
                pygame.draw.rect(screen,(150,50,10),(j*landyx,i*landyy,landyx,landyy))
            elif el == 8:
                pygame.draw.rect(screen,(0,255,0),(j*landyx,i*landyy,landyx,landyy))
            elif el == 9:
                cool = 200+et*10+random.randint(0,50)
                if cool > 255:
                    cool = 255
                elif cool < 0:
                    cool = 0
                pygame.draw.rect(screen,(cool,random.randint(0,50),0),(j*landyx,i*landyy,landyx,landyy))
            elif el == 10:
                pygame.draw.rect(screen,(200,200,50),(j*landyx,i*landyy,landyx,landyy))
            elif el == 11:
                pygame.draw.rect(screen,(200,200,200),(j*landyx,i*landyy,landyx,landyy))
            elif el == 12:
                pygame.draw.rect(screen,(30,20,40),(j*landyx,i*landyy,landyx,landyy))
            elif el == 13:
                pygame.draw.rect(screen,(128,200,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 14:
                pygame.draw.rect(screen,(0,255,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 15:
                pygame.draw.rect(screen,(0,128,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 16:
                pygame.draw.rect(screen,(230,230,230),(j*landyx,i*landyy,landyx,landyy))
            elif el == 17:
                pygame.draw.rect(screen,(150,90,60),(j*landyx,i*landyy,landyx,landyy))
            elif el == 18:
                pygame.draw.rect(screen,(0,128,0),(j*landyx,i*landyy,landyx,landyy))
            elif el == 19:
                random.seed(et)
                pygame.draw.rect(screen,(random.randint(0,50),50+random.randint(0,200),100+random.randint(0,150)),(j*landyx,i*landyy,landyx,landyy))
                random.seed()
            elif el == 20:
                pygame.draw.rect(screen,(255,255,128),(j*landyx,i*landyy,landyx,landyy))
            elif el == 21:
                pygame.draw.rect(screen,(10,60,180),(j*landyx,i*landyy,landyx,landyy))
            elif el == 22:
                pygame.draw.rect(screen,(240,250,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 23:
                pygame.draw.rect(screen,(200,255,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 24:
                pygame.draw.rect(screen,(240,220,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 25:
                pygame.draw.rect(screen,(100,200,230),(j*landyx,i*landyy,landyx,landyy))
            elif el == 26:
                pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 27:
                pygame.draw.rect(screen,(170,210,250),(j*landyx,i*landyy,landyx,landyy))
            elif el == 28:
                if et == 0:
                    pygame.draw.rect(screen,(40,20,10),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(0,255,0),(j*landyx,i*landyy,landyx,landyy))
            elif el == 29:
                pygame.draw.rect(screen,(24,24,24),(j*landyx,i*landyy,landyx,landyy))
            elif el == 30:
                pygame.draw.rect(screen,(random.randint(150,200+et*10),random.randint(50,100+et*random.randint(20,30)),0),(j*landyx,i*landyy,landyx,landyy))
            elif el == 31:
                pygame.draw.rect(screen,(140,70,30),(j*landyx,i*landyy,landyx,landyy))
            elif el == 32:
                cool = 100-et//2
                pygame.draw.rect(screen,(cool,cool,cool),(j*landyx,i*landyy,landyx,landyy))
            elif el == 33:
                cool = 0
                if et != 0:
                    cool = 100+random.randint(-20,20)
                pygame.draw.rect(screen,(100+cool,cool//2,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 34:
                pygame.draw.rect(screen,(160,170,180),(j*landyx,i*landyy,landyx,landyy))
            elif el == 35:
                pygame.draw.rect(screen,(10,10,10),(j*landyx,i*landyy,landyx,landyy))
            elif el == 36:
                colour = (255,255,255)
                if et == 1:
                    colour = (255,0,0)
                elif et == 2:
                    colour = (255,128,0)
                elif et == 3:
                    colour = (255,255,0)
                elif et == 4:
                    colour = (128,255,0)
                elif et == 5:
                    colour = (0,255,0)
                elif et == 6:
                    colour = (0,255,128)
                elif et == 7:
                    colour = (255,255,255)
                elif et == 8:
                    colour = (0,128,255)
                elif et == 9:
                    colour = (0,0,255)
                elif et == 8:
                    colour = (128,0,255)
                elif et == 9:
                    colour = (255,0,255)
                elif et == 10:
                    colour = (128,0,255)
                elif et == 11:
                    colour = (128,128,128)
                pygame.draw.rect(screen,colour,(j*landyx,i*landyy,landyx,landyy))
            elif el == 37:
                pygame.draw.rect(screen,(random.randint(0,250),random.randint(0,100),random.randint(150,250)),(j*landyx,i*landyy,landyx,landyy))
            elif el == 38:
                if et == 1:
                    pygame.draw.rect(screen,(255,255,20),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(180,180,170),(j*landyx,i*landyy,landyx,landyy))
            elif el == 39:
                if et == 1:
                    pygame.draw.rect(screen,(255,255,20),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(200,200,190),(j*landyx,i*landyy,landyx,landyy))
            elif el == 40:
                if et == 1:
                    pygame.draw.rect(screen,(255,255,20),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(200,200,150),(j*landyx,i*landyy,landyx,landyy))
            elif el == 41:
                cool = 0
                if et != 0:
                    cool = random.randint(-20,20)
                pygame.draw.rect(screen,(100,20+cool//2,240),(j*landyx,i*landyy,landyx,landyy))
            elif el == 42:
                cool = 0
                if et != 0:
                    cool = random.randint(-50,50)
                pygame.draw.rect(screen,(200+cool,50+cool,50+cool),(j*landyx,i*landyy,landyx,landyy))
            
            elif el == 43:
                if coinflip():
                    pygame.draw.rect(screen,(255,255,0),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(255,255,128),(j*landyx,i*landyy,landyx,landyy))
            elif el == 44:
                pygame.draw.rect(screen,(180,130,100),(j*landyx,i*landyy,landyx,landyy))
            elif el == 45:
                pygame.draw.rect(screen,(60,30,15),(j*landyx,i*landyy,landyx,landyy))
            elif el == 46:
                pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 47:
                pygame.draw.rect(screen,(128,128,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 48:
                pygame.draw.rect(screen,(200,230,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 49:
                pygame.draw.rect(screen,(0,150,0),(j*landyx,i*landyy,landyx,landyy))
            elif el == 50:
                if fliposwitch:
                    pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(255,0,0),(j*landyx,i*landyy,landyx,landyy))
            elif el == 51:
                pygame.draw.rect(screen,(0,0,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 52:
                pygame.draw.rect(screen,(105,105,105),(j*landyx,i*landyy,landyx,landyy))
            elif el == 53:
                pygame.draw.rect(screen,(255,255,0),(j*landyx,i*landyy,landyx,landyy))
            elif el == 54:
                if et == 1:
                    pygame.draw.rect(screen,(255,255,0),(j*landyx,i*landyy,landyx,landyy))
                elif et == 2:
                    pygame.draw.rect(screen,(150,150,150),(j*landyx,i*landyy,landyx,landyy))
                elif et == 3:
                    pygame.draw.rect(screen,(0,0,255),(j*landyx,i*landyy,landyx,landyy))
                elif et == 4:
                    pygame.draw.rect(screen,(250,250,250),(j*landyx,i*landyy,landyx,landyy))
                elif et == 5:
                    pygame.draw.rect(screen,(100,100,100),(j*landyx,i*landyy,landyx,landyy))
                elif et == 6:
                    pygame.draw.rect(screen,(200,100,50),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(255,0,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 55:
                pygame.draw.rect(screen,(255,200+random.randint(0,55),200+random.randint(0,55)),(j*landyx,i*landyy,landyx,landyy))
            elif el != 0:
                pygame.draw.rect(screen,(255,0,255),(j*landyx,i*landyy,landyx,landyy))
    if not alive:
        live = False
    pygame.display.flip()
pygame.quit()
print("Process exit with code: \"Pee pee poo poo caca do do fart we wa woooooo\"")