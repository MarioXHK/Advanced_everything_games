#Can someone please tell me how to give more resources to this app so I can throttle it and have a smooth 60 fps while my computer combusts into flames
#Some optimization help would be nice too
showfps = False
#the setting that controls if you'd like to do life or not (Experimental sorta)

oob = 0

import os
import pygame
from pygame import Vector2
#WHY DOES YOU NOT EVEN THE AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
from copy import deepcopy
import random
import time

#Save folder things

usesavefolder = True
if usesavefolder:
    print("Using the sandsaves folder as a save directory")
    try:
        os.mkdir('sandsaves')
        print("sandsave folder made automatically!")
    except:
        print("sandsave folder already in place (yippee!)")

pygame.init()
screen = pygame.display.set_mode((10,10))
pygame.display.set_caption("Sandbox game!")
breaking=True
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

#mouse variables--------------------------------
mousePos = Vector2(0,0)
fire = False
tap = True

#Element Variables

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
    16:"Cloud",
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
    55:"Molten Salt",
    56:"Smoke",
    57:"Virus",
    58:"Gold",
    59:"Covered Wire",
    60:"Strange Matter",
    61:"Shockwave",
    62:"Sapling",
    63:"Broken Brick",
    64:"Acid Cloud",
    65:"Acid",
    66:"Acid Sludge",
    67:"Explosion",
    68:"TNT",
    69:"C4",
    70:"Nuke",
    71:"Holy Water",
    72:"Dead Plant",
    73:"Coal",
    74:"Natural Gas",
    75:"Polluted Water",
    76:"Greenhouse Sun"
}

werealsodoinglife = False
eyedropper = False
dither = False
elementary = False
elements = []
mirror = False

#File Variables
illegals = ('\\','//',':','*','?','"','<','>','|')




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
            b = [0,1,3,4,6,8,9,11,15,27,28,29,30,32,34,45,46,47,56,65,71,75]
        else:
            b = [0,3,15,27,29,30,34,47,56,65,71,75]
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
def stoneCheck(grid: list[list[list[int]]],pos: list[int] | tuple[int,int], floats: bool = False, reverse: bool = False, gas: bool = False) -> tuple[bool,int]:
    #returns if something's under it (or above it if in reverse)
    l = 1
    if reverse:
        l = -1
    b = (0,0)
    if not floats:
        if gas:
            b = [0,1,3,4,6,8,9,11,15,27,28,29,30,32,34,45,46,47,56,65,71,75]
        else:
            b = [0,3,15,27,29,34,47,56,65,71,75]
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
        b = [0,3,15,27,29,34,47,56,65,71,75]
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
        b = [3,15,27,29,34,47,56,65,71,75]
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



# ======================================================================================
# ----------- The thing that makes all of this possible, it's DOSTUFF!!!! --------------
# ======================================================================================



def doStuff(plain: list[list[list[int]]],switch: bool,lifeIG: bool = False) -> list[list[list[int]]]:
    e = 0
    t = 0
    #I'll take my small victories in optimization where I can
    
    #The tuple that holds the elements that are required to have a mini plane map
    requireminip = [1,2,3,4,6,7,8,9,10,11,14,15,16,17,18,19,20,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,54,55,56,58,59,60,62,65,66,68,69,70,71,72,73,74,75]
    if lifeIG:
        requireminip.append(0)
        requireminip.append(26)
    requireminip = tuple(requireminip)
    
    #The tuple that holds the elements that are required to have a mini grid map
    requireminig = (1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,22,23,24,25,27,28,29,30,32,34,36,39,40,41,42,43,44,45,46,47,48,49,51,52,53,54,55,56,57,58,60,62,63,64,65,66,68,70,71,72,73,74,75)
    
    
    waters = (3,15,47,71,75)
        
    goodfossilizers = (2,9,12,18,29,32,38,40,51,53,55,58,72,73)
    
    conductors = (38,39,40,44,47,55,58,59,69)

    acidimmune = (0,2,3,5,9,12,16,17,20,21,30,35,38,43,47,50,51,53,55,56,61,64,65,66,71)

    blastproof = (5,12,61,67)
    
    
    #Self explanitory
    supersun: bool = checkEverywhere(plain,[76,0])
    sun: bool = (checkEverywhere(plain,[20,0]) or supersun)
    moon: bool = checkEverywhere(plain,[21,0])
    jam: bool = checkAbsolutelyEverywhere(plain,50)
    grid = deepcopy(plain)
    for a in range(len(plain)):
        for b in range(len(plain[0])):
            if switch:
                bb = len(plain[0])-b-1
            else:
                bb = b
            
            if plain[a][bb] != grid[a][bb]:
                continue
            
            e = plain[a][bb][0]
            t = plain[a][bb][1]
            
            au = False
            ad = False
            al = False
            ar = False
            
            if a + 1 < len(plain):
                ad = True
            if a - 1 > -1:
                au = True
            if bb + 1 < len(plain[0]):
                ar = True
            if bb - 1 > -1:
                al = True
            
            miniplain = []
            minigrid = []
            localPos = (1,1)
            
            if plain[a][bb][0] in requireminip:
                for i in range(0-int(au),1+int(ad)):
                    p = []
                    for j in range(0-int(al),1+int(ar)):
                        if (i,j) == (0,0):
                            p.append(("self",e))
                            localPos = (1-int(not au),1-int(not al))
                            continue
                        p.append(tuple(plain[a+i][bb+j]))
                    miniplain.append(tuple(p))
            
            if plain[a][bb][0] in requireminig:
                for i in range(0-int(au),1+int(ad)):
                    g = []
                    for j in range(0-int(al),1+int(ar)):
                        if (i,j) == (0,0):
                            g.append(("self",e))
                            localPos = (1-int(not au),1-int(not al))
                            continue
                        g.append(tuple(grid[a+i][bb+j]))
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
                        grid[a][bb] = [37,0]
                        continue
                    else:
                        l = neighborCount(miniplain,[26])
                        if l == 3:
                            grid[a][bb] = [26,0]
                            continue
                
                #Sand
                
                elif e == 1:
                    if neighborCheck(miniplain,(9,30,55,67)):
                        e = 14
                        t = 2
                    elif random.randint(1,50) == 1:
                        if neighborCheck(miniplain,(3,15,71)):
                            e = 10
                    elif random.randint(1,42) == 1:
                        if neighborCheck(miniplain,[53]):
                            e = 51
                    else:
                        n = neighborTempCheck(miniplain,[14])
                        if n[0]:
                            e = 14
                            t = n[1]-1
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if e == 1:
                            continue
                        else:
                            grid[a][bb] = [e,t]
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Stone
                
                elif e == 2:
                    if random.randint(1,1000) == 1:
                        if neighborCheck(miniplain,waters):
                            e = 11
                    elif coinflip():
                        if neighborCheck(miniplain,(61,65,66)):
                            e = 11
                    elif neighborCheck(miniplain,[67]):
                        e = 11
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Water
                
                elif e == 3:
                    if coinflip():
                        if neighborCheck(miniplain,(30,67)):
                            e = 13
                            t = 10
                        elif neighborCount(miniplain,(22,23,27)) > 3:
                            e = 27
                        elif neighborCount(miniplain,[71]) > 3:
                            e = 71
                            t = 0
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
                    elif (random.randint(1,101) == 1 and neighborCheck(miniplain,(29,45,50))) or (random.randint(1,12) == 1 and neighborCheck(miniplain,(56,64,65,66))):
                        e = 75
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            if e == 3:
                                continue
                            else:
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [0,0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Sugar
                
                elif e == 4:
                    if neighborCheck(miniplain,(9,20,21)):
                        e = 24
                    elif random.randint(1,5) == 1:
                        if neighborCheck(miniplain,(30,67)):
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
                            grid[a][bb] = [e,t] 
                    else:
                        if random.randint(1,10) == 1:
                            if neighborCheck(miniplain,[3]):
                                e = 15
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a+1][bb] = [e,0]
                            else:
                                if d[1]:
                                    grid[a+1][bb+1] = [e,0]
                                else:
                                    grid[a+1][bb-1] = [e,0]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,0]
                
                #Wall
                
                elif e == 5:
                    continue          
                
                #Dirt
                
                elif e == 6:
                    if random.randint(1,900) == 1:
                        if sun and neighborCheck(miniplain,[8]) and neighborCount(miniplain,[8]) < 2:
                            e = 8
                    if random.randint(1,100) == 1:
                        if neighborCheck(miniplain,(3,15,71)):
                            e = 7
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        if e == 6:
                            continue
                        else:
                            grid[a][bb] = [e,0]
                    else:
                        grid[a][bb] = [0,0]
                        grid[a+1][bb+(c[0]-2)] = [e,0]
                
                #Mud
                
                elif e == 7:
                    if random.randint(1,400) == 1:
                        if sun and neighborCheck(miniplain,[8]) and neighborCount(miniplain,[8]) < 4:
                            e = 8
                    if neighborCheck(miniplain,(9,30,55,67)):
                        e = 6
                    elif random.randint(1,100) == 1:
                        if neighborCheck(miniplain,(46,47,48)):
                            e = 6
                    elif random.randint(1,40) == 1:
                        if sun and neighborCount(miniplain,(3,10,7,15,27)) < 3:
                            e = 6
                    if random.randint(1,5000) == 1:
                        if neighborCheck(miniplain,[18]):
                            e = 18
                        elif neighborCheck(miniplain,[8]):
                            e = 8
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        if e == 7:
                            continue
                        else:
                            grid[a][bb] = [e,0]
                
                #Plant
                
                elif e == 8:
                    
                    if (random.randint(1,30) == 1 and neighborCheck(miniplain,(23,46,47,48,61))) or (supersun and random.randint(1,10000) == 1) or neighborCheck(miniplain,(30,55,67)):
                        e = 72
                        t = 0
                    elif coinflip() and neighborCheck(miniplain,[53]):
                        e = 57
                        t = 0
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Lava
                
                elif e == 9:
                    if neighborCheck(miniplain,(3,7,10,13,15,18,22,23,25,27,47,71)):
                        t -= 2
                        if neighborCheck(miniplain,(3,15,22,23,25,27,47,71)):
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
                            grid[a][bb] = [e,t]
                            continue
                        d = lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            grid[a][bb] = [e,t]
                            continue
                        else:
                            grid[a][bb] = [c[1],0]
                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Wet Sand
                
                elif e == 10:
                    if neighborCheck(miniplain,(9,30,55,67)):
                        e = 14
                        t = 1
                    elif random.randint(1,100) == 1:
                        if neighborCheck(miniplain,(46,47,48)):
                            e = 1
                    elif random.randint(1,40) == 1:
                        if sun and neighborCount(miniplain,(3,10,7,15,27)) < 3:
                            e = 1
                    else:
                        n = neighborTempCheck(miniplain,[14])
                        if n[0]:
                            e = 14
                            t = n[1]-1
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        if e == 10:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                
                #Gravel
                
                elif e == 11:
                    if random.randint(1,42) == 1:
                        if neighborCheck(miniplain,[53]):
                            e = 52
                        elif neighborCheck(miniplain,[71]):
                            e = 2
                    elif random.randint(1,3333) == 1:
                        if neighborCheck(miniplain,(3,15,47)):
                            e = 1
                            #It gets converted into sand after awhile! (You need a lot of erosion to do this)
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        continue
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [11,0]
                
                #Obsidian
                
                elif e == 12:
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [12,0]
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
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [e,0]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]
                    else:
                        grid[a][bb] = [c[1],t]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos,True,False,True)
                            if not d[0]:
                                grid[a-1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a-1][bb+1] = [e,t]
                                else:
                                    grid[a-1][bb-1] = [e,t]
                        else:
                            grid[a-1][bb+(c[0]-2)] = [e,t]
                        
                #Glass
                
                elif e == 14:
                    if coinflip() and t > 0:
                        t -= 1
                    elif neighborCheck(miniplain,(61,67)):
                        e = 19
                        t = random.randint(1,6294)
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        continue
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                        
                #Sugar Water
                
                elif e == 15:
                    if sun and random.randint(1,25000) == 1:
                        e = 13
                        t = 8
                    elif neighborCheck(miniplain,(9,55)) or (coinflip() and neighborCheck(miniplain,(30,67))):
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
                                    grid[a][bb] = [e,t]
                                else:
                                    grid[a][bb] = [e,0]
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,0]
                                else:
                                    grid[a-1][bb] = [e,0]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,0]
                            else:
                                grid[a][bb-1] = [e,0]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,0]
                
                #Clouds
                
                elif e == 16:
                    if random.randint(1,800) == 1:
                        if moon:
                            e = 22 
                        else:
                            e = 3
                    elif neighborCount(miniplain,(56,74)) > 6:
                        e = 64
                        t = 15
                    if random.randint(1,20) == 1:
                        if random.randint(1,4) != 1:
                            d = lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]
                                
                                if d[1]:
                                    grid[a][bb+1] = [e,t]
                                else:
                                    grid[a][bb-1] = [e,t]
                        else:
                            d = udWanderCheck(minigrid,localPos)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    grid[a-1][bb] = [e,t]
                    else:
                        continue
                
                #Brick
                
                elif e == 17:
                    if coinflip():
                        if neighborCheck(miniplain,[61]):
                            e = 63
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        grid[a][bb] = [e,t]
                        continue
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Algae
                
                elif e == 18:
                    if (random.randint(1,30) == 1 and neighborCheck(miniplain,(23,46,47,48,61))) or (supersun and random.randint(1,10000) == 1) or neighborCheck(miniplain,(30,55,67)):
                        e = 72
                        t = 0
                    elif neighborCheck(miniplain,(46,47,48)):
                        e = 0
                    o = lrCheck(miniplain[localPos[0]],localPos[1],True)
                    if o:
                        continue
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t]
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,0]
                
                #Glass shards or dust or whatever you wanna see it as
                
                elif e == 19:
                    if neighborCheck(miniplain,(9,55)):
                        e = 14
                        t = 3
                    elif coinflip() and neighborCheck(miniplain,(30,71)):
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
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                #Sun
                
                elif e == 20:
                    if supersun or (random.randint(1,100) == 1 and neighborCount(miniplain,[56]) >= 7): #Me when the runaway greenhouse effect
                        grid[a][bb] = [76,0]
                    else:
                        continue
                #Moon
                
                elif e == 21:
                    if random.randint(1,100) == 1 and supersun:
                        grid[a][bb] = [2,0]
                    else:
                        continue
                
                #Snow
                
                elif e == 22:
                    if random.randint(1,100) == 1:
                        if sun:
                            e = 3
                    if random.randint(1,10) == 1:
                        if (not moon) and neighborCheck(miniplain,(3,15)):
                            e = 3
                    if neighborCheck(miniplain,(9,13,20,30,46,47,48,55,67)):
                        e = 3
                    if random.randint(1,5000) == 1:
                        e = 3
                    if random.randint(1,10000) == 1:
                        e = 23
                    if switch:
                        c = sandCheck(minigrid,localPos,True)
                        if c[0] == 0:
                            if e == 22:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [e,0] 
                        else:
                            grid[a][bb] = [c[1],0]
                            if c[0] == 2:
                                d = lrWanderCheck(minigrid,localPos, True)
                                if not d[0]:
                                    grid[a+1][bb] = [e,0]
                                else:
                                    if d[1]:
                                        grid[a+1][bb+1] = [e,0]
                                    else:
                                        grid[a+1][bb-1] = [e,0]
                            else:
                                grid[a+1][bb+(c[0]-2)] = [e,0]
                    else:
                        if e == 22:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                
                #Ice
                
                elif e == 23:
                    if random.randint(1,200) == 1:
                        if sun:
                            e = 3
                    if coinflip():
                        if neighborCheck(miniplain,(13,20)):
                            e = 3
                    if neighborCheck(miniplain,(9,30,46,47,48,55,67)):
                        e = 3
                    if random.randint(1,1000) == 1:
                        if neighborCheck(miniplain,(3,15)):
                            e = 3
                    c = stoneCheck(minigrid,localPos,True)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        if e == 2:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                
                #Sugar Crystal
                
                elif e == 24:
                    if random.randint(1,7000) == 1:
                        if neighborCheck(miniplain,[18]):
                            e = 18
                    elif random.randint(1,5000) == 1:
                        if neighborCheck(miniplain,[3,15]):
                            e = 4
                    elif random.randint(1,50) == 1:
                        if neighborCheck(miniplain,(30,67)):
                            e = 30
                            t = 5
                    elif random.randint(1,8) > 3:
                        if neighborCheck(miniplain,[61]):
                            e = 4
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        if e == 24:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        if e == 24:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                
                #Packed Ice
                
                elif e == 25:
                    if random.randint(1,5) == 1:
                        if neighborCheck(miniplain,(9,48,55,71)) or supersun:
                            e = 23
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        continue
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        if e == 25:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                
                #Life WORKING?!!~?!?!?!@43TUHREGAGR\\\
                
                elif e == 26:
                    if lifeIG:
                        #Now life has a few more rules that tell it that it's neighbors don't have to be it's own kind of life, but can be of different kinds of life or things that allow for life! (This should have very interesting effects)
                        l = neighborCount(miniplain,(4,8,15,21,24,26,28,31,37,71))
                        if jam or supersun:
                            if l < random.randint(0,10) or l > random.randint(0,10):
                                grid[a][bb] = [0,0]
                            else:
                                grid[a][bb] = [26,0]
                        else:
                            if l < 2 or l > 3:
                                grid[a][bb] = [0,0]
                            else:
                                grid[a][bb] = [26,0]
                        continue
                    else:
                        grid[a][bb] = randomElement()
                        continue
                
                #Sludge
                
                elif e == 27:
                    if (sun and random.randint(1,50) == 1) or ((not moon) and random.randint(1,500) == 1) or neighborCheck(miniplain,(3,15,46,47,48)):
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
                    if neighborCheck(miniplain,(9,13,20,30,55,67)):
                        e = 13
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if e == 27:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            grid[a+1][bb] = [e,0]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,0]

                #Flower things
                
                elif e == 28:
                    if jam:
                        t = 1
                        continue
                    if random.randint(1,4) == 1:
                        if neighborCheck(miniplain,(9,30,55,67)):
                            if coinflip():
                                e = 30
                                t = 5
                            else:
                                e = 32
                    #Seed
                    if plain[a][bb][1] == 0:
                        c = sandCheck(minigrid,localPos)
                        if c[0] == 0:
                            if random.randint(1,100) == 1 and neighborCheck(miniplain,(7,8,10,18,27,32,71)) and not neighborCheck(miniplain,(46,47,48)):
                                grid[a][bb] = [e,random.randint(2,8)]
                            else:
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                    #Stem
                    elif plain[a][bb][1] > 1 and a - 1 != 0:
                        t -= 1
                        grid[a-1][bb] = [e,t]
                        t = -1
                        grid[a][bb] = [e,t]
                    #Bloom
                    elif plain[a][bb][1] != -1:
                        grid[a][bb] = [36,random.randint(0,11)]
                        c = random.randint(0,11)
                        if a + 1 != len(plain):
                            grid[a+1][bb] = [36,c]
                        if a - 1 != -1 and grid[a-1][bb][0] == 0:
                            grid[a-1][bb] = [36,c]
                        if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                            grid[a][bb+1] = [36,c]
                        if bb - 1 != -1 and grid[a][bb-1][0] == 0:
                            grid[a][bb-1] = [36,c]
                           
                #Oil (Pls don't take americuh)
                
                elif e == 29:
                    if random.randint(1,15) == 1:
                        if neighborCheck(miniplain,(9,30,55,67)):
                            e = 30
                            t = 5
                    elif coinflip() and neighborCheck(miniplain,[71]):
                        e = 7
                        t = 0
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos,False,True)
                        if not d[0]:
                            d = udWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                if e == 29:
                                    grid[a][bb] = [e,t]
                                else:
                                    grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],t]

                                if d[1]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    grid[a-1][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,0]
                
                #Fire
                
                elif e == 30:
                    flame = False
                    superflame = False
                    if (random.randint(1,4) == 1 or moon or jam or neighborCount(miniplain,[56]) > 3) and t > 0:
                        if not sun:
                            t -= 1
                        else:
                            if coinflip():
                                t -= 1
                    if neighborCheck(miniplain,(4,8,15,18,20,24,28,29,31,36,49,53,57,72,73,74,76)):
                        if moon:
                            if (coinflip() or sun) and t < 2:
                                t = 2
                        else:
                            t = 5
                        flame = True
                        if neighborCheck(miniplain,(29,53,73,74,76)):
                            superflame = True
                    elif neighborCheck(miniplain,(33,59)) and t < 2:
                        t = 2
                    elif random.randint(1,10) == 1:
                        o = neighborTempCheck(miniplain,[30],">",t)
                        if o[0]:
                            t = o[1] - 1
                    if neighborCheck(miniplain,(3,15,47,71)):
                        e = 56
                        t *= 2
                    elif t <= 0:
                        e = 56
                        t = 10
                    if flame and (random.randint(1,15) != 1 or superflame):
                        c = [0]
                        if superflame and random.randint(1,5) == 2:
                            if coinflip() and a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                                grid[a+1][bb] = [56,10]
                            if coinflip() and a - 1 != -1 and grid[a-1][bb][0] == 0:
                                grid[a-1][bb] = [56,10]
                            if coinflip() and bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                                grid[a][bb+1] = [56,10]
                            if coinflip() and bb - 1 != -1 and grid[a][bb-1][0] == 0:
                                grid[a][bb-1] = [56,10]
                    else:
                        c = sandCheck(minigrid,localPos,False,True,True)
                    if c[0] == 0:
                        if flame and random.randint(1,8) != 1:
                            d = [False]
                        else:
                            d = lrWanderCheck(minigrid,localPos,False,False,True)
                        if not d[0]:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]
                    else:
                        grid[a][bb] = [c[1],t]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos,True,False,True)
                            if not d[0]:
                                grid[a-1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a-1][bb+1] = [e,t]
                                else:
                                    grid[a-1][bb-1] = [e,t]
                        else:
                            grid[a-1][bb+(c[0]-2)] = [e,t]
                
                #Wood
                
                elif e == 31:
                    if coinflip():
                        if neighborCount(miniplain,(9,30,55,67)) > random.randint(1,5):
                            e = 32
                    elif random.randint(1,20) == 1:
                        if neighborCheck(miniplain,(30,67)):
                            e = 30
                            t = 5
                    elif random.randint(1,40) == 1:
                        if neighborCheck(miniplain,(9,55)):
                            e = 30
                            t = 5
                    
                    if e != 31:
                        grid[a][bb] = [e,t]
                
                #Ash
                
                elif e == 32:
                    if random.randint(1,1000) == 1:
                        if neighborCount(miniplain,goodfossilizers) > 3:
                            t += random.randint(1,2)
                    elif random.randint(1,100) == 1:
                        if neighborCheck(miniplain,[3,15]):
                            e = 34
                        elif neighborCheck(miniplain,[71]):
                            e = 8
                            t = 0
                    if t >= 100:
                        e = 29
                        t = 0
                    elif jam:
                        t = 0
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t] 
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a+1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a+1][bb+1] = [e,t]
                                else:
                                    grid[a+1][bb-1] = [e,t]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Cloner (Yes, I went there)
                
                elif e == 33:
                    if jam:
                        t = 0
                    elif plain[a][bb][1] == 0:
                        t = myNeighbor(miniplain,[33])
                    else:
                        if a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                            grid[a+1][bb] = [plain[a][bb][1],0]
                        if a - 1 != -1 and grid[a-1][bb][0] == 0:
                            grid[a-1][bb] = [plain[a][bb][1],0]
                        if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                            grid[a][bb+1] = [plain[a][bb][1],0]
                        if bb - 1 != -1 and grid[a][bb-1][0] == 0:
                            grid[a][bb-1] = [plain[a][bb][1],0]
                    grid[a][bb] = [e,t]
                
                #Clay
                
                elif e == 34:
                    if neighborCheck(miniplain,(9,30,55)):
                        e = 17
                    elif neighborCheck(miniplain,[67]):
                        e = 63
                    
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        if random.randint(1,40) != 1:
                            if random.randint(1,10) == 1:
                                d = udWanderCheck(minigrid,localPos,True)
                            else:
                                d = [False]
                            if not d[0]:
                                if e == 17:
                                    grid[a][bb] = [e,t]
                                    continue
                                else:
                                    grid[a][bb] = [e,0]
                                    continue
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,0]
                                else:
                                    grid[a-1][bb] = [e,0]
                                continue
                            
                        d = lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            if e == 17:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [e,0]
                        else:
                            grid[a][bb] = [c[1],0]
                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #VOID
                
                elif e == 35:
                    if jam or neighborCheck(miniplain,[71]):
                        continue
                    if a + 1 != len(plain) and grid[a+1][bb][0] != 35:
                        grid[a+1][bb] = [0,0]
                    if a - 1 != -1 and grid[a-1][bb][0] != 35:
                        grid[a-1][bb] = [0,0]
                    if bb + 1 != len(plain[0]) and grid[a][bb+1][0] != 35:
                        grid[a][bb+1] = [0,0]
                    if bb - 1 != -1 and grid[a][bb-1][0] != 35:
                        grid[a][bb-1] = [0,0]
                
                #Petal
                
                elif e == 36:
                    if random.randint(1,15) == 1:
                        if neighborCheck(miniplain,(9,30,55,67)):
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
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Cancer (Doesn't know how to die)
                
                elif e == 37:
                    if lifeIG:
                        if neighborCheck(miniplain,[71]):
                            grid[a][bb] = [0,0]
                        elif jam:
                            #This makes it obey Life's rules
                            l = neighborCount(miniplain,(4,8,15,21,24,26,28,31,37))
                            if l < 2 or l > 3:
                                grid[a][bb] = [0,0]
                            else:
                                grid[a][bb] = [37,0]
                        continue
                    else:
                        grid[a][bb] = randomElement()
                
                #Iron
                
                elif e == 38:
                    if random.randint(1,1000) == 1:
                        if neighborCheck(miniplain,(3,15,47)):
                            e = 44
                    if t == 1 or jam:
                        t = 2
                    elif (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    grid[a][bb] = [e,t] 
                
                #Iron Sand
                
                elif e == 39:
                    if random.randint(1,1000) == 1:
                        if neighborCheck(miniplain,[3,15,47]):
                            e = 45
                    elif neighborCheck(miniplain,(9,55)):
                        e = 38
                    
                    if t == 1 or jam:
                        t = 2
                    elif (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t]
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
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
                        grid[a][bb] = [e,t]
                        continue
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Smart Remover (Based on the bacteria mod from minecraft)
                
                elif e == 41:
                    if jam:
                        t = 0
                        if random.randint(1,4) == 1:
                            e = 0
                    elif t == 0:
                        if a + 1 != len(plain) and grid[a+1][bb][0] != 0 and plain[a+1][bb][1] != 41 and (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]):
                            t = grid[a+1][bb][0]
                    elif t != 41:
                        if a + 1 != len(plain) and grid[a+1][bb][0] == t:
                            grid[a+1][bb] = [e,t]
                        if a - 1 != -1 and grid[a-1][bb][0] == t:
                            grid[a-1][bb] = [e,t]
                        if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == t:
                            grid[a][bb+1] = [e,t]
                        if bb - 1 != -1 and grid[a][bb-1][0] == t:
                            grid[a][bb-1] = [e,t]
                        if not neighborCheck(miniplain,[t]) or neighborCount(miniplain,[41]) == 0:
                            e = 0
                            t = 0
                    c = stoneCheck(minigrid,localPos,True)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Smart Converter (Probably my most complicated element yet since it's temprature is off the charts!)
                
                elif e == 42:
                    if jam:
                        t = 0
                        if random.randint(1,4) == 1:
                            e = 0
                    elif t == 0:
                        if a + 1 != len(plain) and grid[a+1][bb][0] != 0 and grid[a+1][bb][1] != 42 and a - 1 != -1 and grid[a-1][bb][0] != 0 and grid[a-1][bb][1] != 42 and (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]):
                            #This is complex, lemme explain
                            
                            t = grid[a-1][bb][0]*1000
                            #This gets the value of the pixel above it and multiplies it by 1000, so when we do our lil // later, we can get this element back
                            
                            t += grid[a+1][bb][0]
                            #This gets the value of the pixel below it and adds it to the temp, so when we can do our lil % later and get this element back too!
                    else:
                        rt = t//1000 #The element that's gonna REPLACE the converted element
                        ct = t%1000 #The element that's gonna get CONVERTED into the replaced element
                        if rt != 42 and ct != 42:
                            if a + 1 != len(plain) and grid[a+1][bb][0] == ct:
                                grid[a+1][bb] = [e,t]
                            if a - 1 != -1 and grid[a-1][bb][0] == ct:
                                grid[a-1][bb] = [e,t]
                            if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == ct:
                                grid[a][bb+1] = [e,t]
                            if bb - 1 != -1 and grid[a][bb-1][0] == ct:
                                grid[a][bb-1] = [e,t]
                            if not neighborCheck(miniplain,[ct]) or neighborCount(miniplain,[42]) == 0:
                                e = rt
                                t = 0
                    c = stoneCheck(minigrid,localPos,True)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                
                #Electricity
                
                elif e == 43:
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0 or jam:
                        grid[a][bb] = [0,0]
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                grid[a+1][bb] = [e,0]
                            else:
                                if d[1]:
                                    grid[a+1][bb+1] = [e,0]
                                else:
                                    grid[a+1][bb-1] = [e,0]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,0]
                
                #Rusted Iron
                
                elif e == 44:
                    if coinflip() and neighborCheck(miniplain,[71]):
                            e = 38
                    elif random.randint(1,1000) == 1:
                        if neighborCheck(miniplain,(3,15,47)):
                            e = 45
                    if t == 1 or jam:
                        t = 2
                    elif neighborTempCheck(miniplain,conductors,"==",1)[0] and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        grid[a][bb] = [e,t]
                        continue
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Rust
                
                elif e == 45:
                    if coinflip() and neighborCheck(miniplain,[71]):
                            e = 40
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if e == 1:
                            continue
                        else:
                            grid[a][bb] = [e,t]
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Salt
                
                elif e == 46:
                    if neighborCheck(miniplain,(9,55)):
                        e = 55
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if random.randint(1,100) == 1:
                            if neighborCheck(miniplain,[3]):
                                e = 47
                        grid[a][bb] = [e,t]
                    else:
                        if random.randint(1,10) == 1:
                            if neighborCheck(miniplain,[3]):
                                e = 47
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Salt Water
                
                elif e == 47:
                    if t == 1 or jam:
                        t = 2
                    elif (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    if sun and random.randint(1,10000) == 1:
                        e = 13
                        t = 12
                    elif neighborCheck(miniplain,(9,55)) or (coinflip() and neighborCheck(miniplain,(30,67))):
                        if coinflip():
                            e = 46
                        else:
                            e = 13
                    elif random.randint(1,100) == 1 and neighborCheck(miniplain,(4,15)):
                        e = 71
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos,False,True)
                        if not d[0]:
                            d = udWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    grid[a-1][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Salt Crystal
                
                elif e == 48:
                    if neighborCheck(miniplain,(9,55)):
                        e = 55
                    elif random.randint(1,5000) == 1:
                        if neighborCheck(miniplain,[3,47]):
                            e = 46
                    elif random.randint(1,3):
                        if neighborCheck(miniplain,[61]):
                            e = 46
                    
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        grid[a][bb] = [e,t]
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        if e == 24:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                
                #leaf
                
                elif e == 49:
                    if t > 9 or random.randint(1,10-t) == 1:
                        if (random.randint(1,10) == 1 and neighborCheck(miniplain,(23,46,47,48,61))) or (supersun and random.randint(1,10000) == 1) or neighborCheck(miniplain,(30,55,67)):
                            e = 72
                            t = 0
                    if neighborCheck(miniplain,[71]):
                        t = 0
                        if random.randint(1,14) == 1:
                            e = 36
                            t = random.randint(0,11)
                    
                    if coinflip() or (neighborCheck(miniplain,(8,31)) and not (((random.randint(1,400) == 1 and moon)) or neighborCheck(miniplain,[61]) or t == 1)):
                        grid[a][bb] = [e,t]
                        continue
                    if t == 0:
                        t = 1
                    elif random.randint(1,200) == 1 and t < 8:
                        t += 1
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t] 
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a+1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a+1][bb+1] = [e,t]
                                else:
                                    grid[a+1][bb-1] = [e,t]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                
                
                #Antisand
                
                elif e == 51:
                    c = sandCheck(minigrid,localPos,False,True)
                    if c[0] == 0:
                        grid[a][bb] = [e,t]
                        continue
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a-1][bb+(c[0]-2)] = [e,t]
                
                #Antistone
                
                elif e == 52:
                    c = stoneCheck(minigrid,localPos,False,True)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a-1][bb] = [e,0]
                    else:
                        grid[a][bb] = [e,0]
                
                #Antiwater
                
                elif e == 53:
                    c = sandCheck(minigrid,localPos,True,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos,False,True,True)
                        if not d[0]:
                            if e == 3:
                                continue
                            else:
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [0,0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a-1][bb+(c[0]-2)] = [e,t]
                
                #IDENTITY NOT FOUND =( https://www.youtube.com/watch?v=4bLf2wDJA5s
                elif e == 54:
                    
                    idk = random.randint(1,6)
                    t = idk
                    if jam or neighborCheck(miniplain,[71]):
                        e = idk
                    
                    #Sandbit
                    
                    if idk == 1:
                        if neighborCheck(miniplain,(9,30,55,67)):
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
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                    
                    #Stonebit
                    
                    elif idk == 2:
                        if random.randint(1,1000) == 1:
                            if neighborCheck(miniplain,[3,15,47]):
                                e = 11
                        c = stoneCheck(minigrid,localPos)
                        if not c[0]:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,t]
                    
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
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [0,0]

                                if d[1]:
                                    grid[a][bb+1] = [e,t]
                                else:
                                    grid[a][bb-1] = [e,t]

                        else:
                            grid[a][bb] = [0,0]

                            grid[a+1][bb+(c[0]-2)] = [e,t]
                    
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
                            grid[a][bb] = [e,t] 
                            continue
                        else:
                            if random.randint(1,10) == 1:
                                if neighborCheck(miniplain,[3]):
                                    e = 15
                            grid[a][bb] = [c[1],0]
                            if c[0] == 2:
                                d = lrWanderCheck(minigrid,localPos, True)
                                if not d[0]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    if d[1]:
                                        grid[a+1][bb+1] = [e,t]
                                    else:
                                        grid[a+1][bb-1] = [e,t]
                            else:
                                grid[a+1][bb+(c[0]-2)] = [e,t]
                    
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
                            grid[a][bb] = [e,t]
                            continue
                        else:
                            grid[a][bb] = [0,0]
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Jammer
                
                elif e == 50:
                    o = 0
                    t += 1
                    if supersun:
                        t += 2
                        o = -10
                    n = neighborCheck(miniplain,[71])
                    if t <= 50 and not n:
                        grid[a][bb] = [e,t]
                    else:
                        if random.randint(1,20-o) == 1 or n:
                            grid[a][bb] = [61,3]
                        else:
                            grid[a][bb] = [0,0]

                #Molten Salt (Yes, it's a thing)
                
                elif e == 55:
                    if t == 1 or jam:
                        t = 2
                    elif (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    if random.randint(1,25) == 1 or ((not sun) and neighborCheck(miniplain,[8])):
                        e = 46
                    #Too salty to just go away without holyness...
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if random.randint(1,25) != 1:
                            if e == 9:
                                grid[a][bb] = [e,t]
                                continue
                            else:
                                grid[a][bb] = [e,t]
                                continue
                        d = lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            if e == 9:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [c[1],0]
                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Smoke
                
                elif e == 56:
                    if (random.randint(1,10) == 1 and not (moon or sun)) or (random.randint(1,6) == 1 and moon and not sun) or (random.randint(1,12) == 1 and sun and not supersun) or (random.randint(1,20) == 1 and supersun):
                        t -= 1
                    if t <= 0 or neighborCheck(miniplain,[71]):
                        e = 0
                    else:
                        o = neighborTempCheck(miniplain,[56], ">", 5)
                        oo = neighborTempCheck(miniplain,[56], ">", 10)
                        if (not (moon or oo[0])) and ((not sun and random.randint(1,70000) == 1) or (sun and random.randint(1,7000) == 1)) and neighborCount(miniplain,[56]) >= 8 and o[0]:
                            e = 64
                            t = 15
                    c = sandCheck(minigrid,localPos,False,True,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos,False,False,True)
                        if not d[0]:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos,True,False,True)
                            if not d[0]:
                                grid[a-1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a-1][bb+1] = [e,t]
                                else:
                                    grid[a-1][bb-1] = [e,t]
                        else:
                            grid[a-1][bb+(c[0]-2)] = [e,t]
                
                
                #Virus
                
                elif e == 57:
                    n = neighborCheck(miniplain,[71])
                    if not (jam or n):
                        if a + 1 != len(plain) and not grid[a+1][bb][0] in (0,71):
                            grid[a+1][bb] = [e,grid[a+1][bb]]
                        if a - 1 != -1 and not grid[a-1][bb][0] in (0,71):
                            grid[a-1][bb] = [e,grid[a-1][bb]]
                        if bb + 1 != len(plain[0]) and not grid[a][bb+1][0] in (0,71):
                            grid[a][bb+1] = [e,grid[a][bb+1]]
                        if bb - 1 != -1 and not grid[a][bb-1][0] in (0,71):
                            grid[a][bb-1] = [e,grid[a][bb-1]]
                    if n:
                        e = t
                        t = 0
                    c = stoneCheck(minigrid,localPos,True)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Gold
                
                elif e == 58:
                    if t == 1 or jam:
                        t = 2
                    elif (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    o = lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        grid[a][bb] = [e,t]
                        continue
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Wire
                
                elif e == 59:
                    if coinflip():
                        if neighborCheck(miniplain,(9,30,55,67)):
                            e = 38
                    if t == 1 or jam:
                        t = 2
                    elif neighborTempCheck(miniplain,conductors,"==",1)[0] and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    grid[a][bb] = [e,t]
                
                #Strange Matter (Fun fact: You can't obtain this without disabling life and getting it by random chance since there's no natural process that creates it!)
                
                elif e == 60:
                    n = neighborCheck(miniplain,[71])
                    if not (moon or n):
                        if a + 1 != len(plain) and not grid[a+1][bb][0] in (0,71):
                            grid[a+1][bb] = [e,t]
                        if a - 1 != -1 and not grid[a-1][bb][0] in (0,71):
                            grid[a-1][bb] = [e,t]
                        if bb + 1 != len(plain[0]) and not grid[a][bb+1][0] in (0,71):
                            grid[a][bb+1] = [e,t]
                        if bb - 1 != -1 and not grid[a][bb-1][0] in (0,71):
                            grid[a][bb-1] = [e,t]
                    elif n:
                        e = 0
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if random.randint(1,25) != 1:
                            grid[a][bb] = [e,t]
                            continue
                        d = lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            grid[a][bb] = [e,t]
                            continue
                        else:
                            grid[a][bb] = [c[1],0]
                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Shockwave
                
                elif e == 61:
                    if t <= 0:
                        e = 0
                    else:
                        if t > 2:
                            if a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                                grid[a+1][bb] = [e,t]
                            if a - 1 != -1 and grid[a-1][bb][0] == 0:
                                grid[a-1][bb] = [e,t]
                            if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                                grid[a][bb+1] = [e,t]
                            if bb - 1 != -1 and grid[a][bb-1][0] == 0:
                                grid[a][bb-1] = [e,t]
                    t -= 1
                    grid[a][bb] = [e,t]
                    
                #Sapling into tree!
                
                elif e == 62:
                    if jam:
                        t = 1
                        continue
                    if random.randint(1,4) == 1:
                        if neighborCheck(miniplain,(9,30,55,67)):
                            if coinflip():
                                e = 30
                                t = 5
                            else:
                                e = 32
                    #Sapling
                    if t == 0:
                        c = stoneCheck(minigrid,localPos)
                        if not c[0]:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb] = [e,t]
                        else:
                            if random.randint(1,100) == 1 and neighborCheck(miniplain,(7,8,10,18,27,32,71)) and not neighborCheck(miniplain,(46,47,48)):
                                grid[a][bb] = [e,3]
                            else:
                                grid[a][bb] = [e,t]
                    #Stem
                    elif t == 3:
                        if random.randint(1,6) == 1 or a - 1 == 0:
                            t = 1
                            grid[a][bb] = [e,t]
                            continue
                        grid[a-1][bb] = [e,t]
                        grid[a][bb] = [31,0]
                        if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                            if random.randint(1,3) == 1:
                                grid[a][bb+1] = [e,2]
                            else:
                                grid[a][bb+1] = [49,0]
                        if bb - 1 != -1 and grid[a][bb-1][0] == 0:
                            if random.randint(1,3) == 1:
                                grid[a][bb-1] = [e,2]
                            else:
                                grid[a][bb-1] = [49,0]
                    #Branch
                    
                    elif t == 2:
                        if random.randint(1,4) == 1 or bb - 1 == 0 or bb + 1 == len(plain[0])-1:
                            t = 1
                            grid[a][bb] = [e,t]
                            continue
                        if grid[a][bb+1][0] != 31:
                            grid[a][bb+1] = [e,t]
                        else:
                            grid[a][bb-1] = [e,t]
                        grid[a][bb] = [31,0]
                            
                        if a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                            grid[a+1][bb] = [49,0]
                        if a - 1 != -1 and grid[a-1][bb][0] == 0:
                            grid[a-1][bb] = [49,0]
                    
                    #Finished
                    elif t == 1:
                        grid[a][bb] = [31,random.randint(0,11)]
                        if a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                            grid[a+1][bb] = [49,0]
                        if a - 1 != -1 and grid[a-1][bb][0] == 0:
                            grid[a-1][bb] = [49,0]
                        if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                            grid[a][bb+1] = [49,0]
                        if bb - 1 != -1 and grid[a][bb-1][0] == 0:
                            grid[a][bb-1] = [49,0]
                
                #Broken Brick
                
                elif e == 63:
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Acid Clouds
                
                elif e == 64:
                    if random.randint(1,800) == 1:
                        e = 65
                        t = 20
                    elif coinflip() and t <= 0:
                        e = 0
                    elif neighborCheck(miniplain,[71]):
                        e = 16
                    
                    if not jam:
                        if a + 1 != len(plain) and not grid[a+1][bb][0] in acidimmune:
                            t -= 1
                            grid[a+1][bb] = [66,0]
                        if a - 1 != -1 and not grid[a-1][bb][0] in acidimmune:
                            t -= 1
                            grid[a-1][bb] = [66,0]
                        if bb + 1 != len(plain[0]) and not grid[a][bb+1][0] in acidimmune:
                            t -= 1
                            grid[a][bb+1] = [66,0]
                        if bb - 1 != -1 and not grid[a][bb-1][0] in acidimmune:
                            t -= 1
                            grid[a][bb-1] = [66,0]
                    
                    if random.randint(1,20) == 1:
                        if random.randint(1,4) != 1:
                            d = lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]
                                
                                if d[1]:
                                    grid[a][bb+1] = [e,t]
                                else:
                                    grid[a][bb-1] = [e,t]
                        else:
                            d = udWanderCheck(minigrid,localPos)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    grid[a-1][bb] = [e,t]
                    
                
                #Acid (Acid rain ig lol)

                elif e == 65:
                    if neighborCheck(miniplain,(21,53)):
                        e = 3
                    elif coinflip() and t <= 0:
                        e = 0
                    elif random.randint(1,13) == 1 and neighborCheck(miniplain,waters):
                        e = 75
                    elif neighborCheck(miniplain,[71]):
                        e = 66
                    
                    if not jam:
                        if a + 1 != len(plain) and not grid[a+1][bb][0] in acidimmune:
                            t -= 1
                            grid[a+1][bb] = [66,0]
                        if a - 1 != -1 and not grid[a-1][bb][0] in acidimmune:
                            t -= 1
                            grid[a-1][bb] = [66,0]
                        if bb + 1 != len(plain[0]) and not grid[a][bb+1][0] in acidimmune:
                            t -= 1
                            grid[a][bb+1] = [66,0]
                        if bb - 1 != -1 and not grid[a][bb-1][0] in acidimmune:
                            t -= 1
                            grid[a][bb-1] = [66,0]
                    
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [0,0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]

                #Acid Sludge
                
                elif e == 66:
                    if (not moon) and random.randint(1,13) == 1:
                            e = 0
                            t = 0
                    elif neighborCheck(miniplain,[71]):
                        e = 74
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t]
                    else:
                        grid[a][bb] = [c[1],t]
                        if c[0] == 2:
                            grid[a+1][bb] = [e,t]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,t]

                #Explosion
                
                elif e == 67:
                    t -= 1
                    if t <= 0:
                        e = 30
                        t = 4
                    else:
                        if a + 1 != len(plain) and not grid[a+1][bb][0] in blastproof:
                            grid[a+1][bb] = [e,t]
                        if a - 1 != -1 and not grid[a-1][bb][0] in blastproof:
                            grid[a-1][bb] = [e,t]
                        if bb + 1 != len(plain[0]) and not grid[a][bb+1][0] in blastproof:
                            grid[a][bb+1] = [e,t]
                        if bb - 1 != -1 and not grid[a][bb-1][0] in blastproof:
                            grid[a][bb-1] = [e,t]
                    grid[a][bb] = [e,t]

                #TNT
                
                elif e == 68:
                    if neighborCheck(miniplain,[71]):
                        e = 31
                    elif neighborCheck(miniplain,(9,30,67)):
                            e = 67
                            t = 8
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        grid[a][bb] = [e,t]
                
                
                #C4
                
                elif e == 69: #Not a word
                    if neighborCheck(miniplain,[71]):
                        e = 31
                    elif neighborCheck(miniplain,(9,67)):
                            e = 67
                            t = 4
                    
                    if t == 1 or jam:
                        t = 2
                    elif (neighborCheck(miniplain,[43]) or neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    if t == 2 and not jam:
                        e = 67
                        t = 10
                    grid[a][bb] = [e,t] 
                
                #Nuke (Mandatory when there are explosions in the game)
                
                elif e == 70:
                    if jam:
                        t = -1
                    if t == 0 and neighborCheck(miniplain,(43,67)):
                            e = 67
                            t = random.randint(40,60)
                    if neighborCheck(miniplain,[71]):
                        e = 31
                    
                    c = stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        grid[a][bb] = [e,t]
                
                #Holy Water
                
                elif e == 71:
                    if neighborCheck(miniplain,[55]):
                        if coinflip():
                            e = 53
                        else:
                            e = 13
                    elif random.randint(1,9) == 1:
                        if neighborCheck(miniplain,[31]):
                            e = 49
                    if coinflip():
                        if  bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 71:
                            t = grid[a][bb+1][1]
                        if bb - 1 != -1 and grid[a][bb-1][0] == 71:
                            t = grid[a][bb-1][1]
                    else:
                        if t == 0 and random.randint(1,555) == 1:
                            if coinflip():
                                t = 1
                            else:
                                t = 2
                        elif t != 0 and coinflip():
                            t = 0
                    
                    
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos,False,True)
                        if not d[0]:
                            d = udWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                if e == 15:
                                    grid[a][bb] = [e,t]
                                else:
                                    grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    grid[a-1][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Dead Plants
                
                elif e == 72:
                    if coinflip():
                        if neighborCheck(miniplain,(9,30,55,67)):
                            if coinflip():
                                e = 30
                                t = 5
                            else:
                                e = 32
                    elif random.randint(1,500) == 1:
                        if neighborCount(miniplain,goodfossilizers) > 3:
                            t += random.randint(1,2)
                    elif neighborCheck(miniplain,[71]):
                        e = 8
                        t = 0
                    if t >= 100:
                        e = 73
                        t = 0
                    elif jam:
                        t = 0
                    c = sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t] 
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a+1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a+1][bb+1] = [e,t]
                                else:
                                    grid[a+1][bb-1] = [e,t]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Coal (Oh boy time to ruin the environment)
                
                elif e == 73:
                    if random.randint(1,120) == 1:
                        if neighborCheck(miniplain,(9,30,55,67)):
                            e = 30
                            t = 5
                    elif neighborCheck(miniplain,[71]):
                        e = 8
                        t = 0
                    if coinflip():
                        c = stoneCheck(minigrid,localPos)
                        if not c[0]:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,t]
                    else:
                        c = sandCheck(minigrid,localPos)
                        if c[0] == 0:
                            if e == 1:
                                continue
                            else:
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Natural Gas (If it's so natural then why is it hecking with the environment?)
                
                elif e == 74:
                    if random.randint(1,10) == 1:
                        if neighborCheck(miniplain,(9,30,55,67)):
                            e = 30
                            t = 5
                    elif neighborCheck(miniplain,[71]):
                        e = 16
                        t = 0
                    c = sandCheck(minigrid,localPos,False,True,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos,False,False,True)
                        if not d[0]:
                            if e == 13:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [e,0]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]
                    else:
                        grid[a][bb] = [c[1],t]
                        if c[0] == 2:
                            d = lrWanderCheck(minigrid,localPos,True,False,True)
                            if not d[0]:
                                grid[a-1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a-1][bb+1] = [e,t]
                                else:
                                    grid[a-1][bb-1] = [e,t]
                        else:
                            grid[a-1][bb+(c[0]-2)] = [e,t]
                
                #Polluted Water
                
                elif e == 75:
                    if sun and random.randint(1,30000) == 1:
                        e = 65
                        t = 10
                    c = sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = lrWanderCheck(minigrid,localPos,False,True)
                        if not d[0]:
                            d = udWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    grid[a-1][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Greenhouse sun
                
                elif e == 76:
                    if jam and random.randint(1,1000) == 1:
                        grid[a][bb] = [20,0]
                    else:
                        continue
                
                
            except IndexError:
                print("Error in doing element", grid[a][bb], "index out of range (Did you remember to put the element ID in the corisponding mini-allowed tuple?)")
    return grid


# ===============================================================================================
# ===================================== THE SETUP LOOP ==========================================
# ===============================================================================================



yeses = ("y","yes","yeah","do it","sure","alright","ok","ig","i guess","yay","pull the lever, cronk!","alrighty then","whatever","heck yes","hell yes","probably","ye","yea","yeah!","oh yes","i don't see why not","i dont see why not","the opposite of no","yep","yes sir","yessir","please do","do","1","i'd love to","i'd love to try it out","let's see what you've got","let's-a go!","lets a go","let's a go","lets a go!","mushroom kingdom here we come","may","smash","yeah, sure","yesure","let's kick bubblegum","activate","throttle","upgrade","proceed","bb","shure","surry boi","surry","yes please","yes maam","yes hoobaab")
noes = ("n","no","nah","nay","nein","it's opposite day","don't you dare","poop","do not","do not the cat","perish","hell no","heck no","probably not","jumpscare","no!","no!!","no!!!","mmm...","how could you screw it up this badly?","the opposite of yes","nope","not even close","please don't","don't","0","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","unrun","kill","oh no","ho ho ho ho no","steamed hams","nada","nay","pass","t_t","i'm sick rn","not today","chewing bubblegum","deactivate","turn back","i said turn back","snowgrave","die","di","noooooooooo","b","lmao nah","nada","zilch","q","no please","no thank you","no thanks")

screenx: int = 500
screeny: int = 500

landx: int = 50
landy: int = 50

setup = True


unanswered = True
print("Would you like to setup your own sandbox space?")
while unanswered:
    unanswered = False
    answer = input().lower()
    if answer in noes:
        print("Alright, default sandbox it is.")
        setup = False
    elif answer in yeses:
        print("Alright, let's get to setting your sandbox up!")
        setup = True
    else:
        print("Answer unrecognized, try again")
        unanswered = True

if setup:
    print("Setup your sandbox! (You can skip this and be default by putting in junk values)")

while breaking and setup:
    d = 0
    for event in pygame.event.get(): #Event Queue (or whatever it's called)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            breaking = False
    
    #Screen variables
    
    try:
        screenx = int(input("What should the window's size be in pixels horizontally?\n"))
        screeny = int(input("What should the window's size be in pixels vertically?\n"))
    except:
        print("That's not a number! Setting window size to default!")
        screenx = 500
        screeny = 500

    try:
        landx = int(input("How long should the sandbox be in units?\n"))
        landy = int(input("How tall should the sandbox be in units?\n"))
    except:
        print("That's not a number! Setting sandbox size to default!")
        landx = screenx//10
        landy = screeny//10


    landyx = (screenx/landx)
    landyy = (screeny/landy)

    screen.fill((0,0,0))

    screen = pygame.display.set_mode((screenx,screeny))

    for i in range(landy):
        for j in range(landx):
            pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy),1)

    pygame.display.flip()
    print("You should now see a preview of the sandbox that you're about to unfold.\nIs this ok?")
    unanswered = True
    while unanswered:
        unanswered = False
        answer = input().lower()
        if answer in noes:
            print("Alright, let's try again.")
        elif answer in yeses:
            print("Alright, creating the sandbox now!")
            setup = False
        else:
            print("Answer unrecognized, try again")
            unanswered = True




#Sandbox initialization!

land = [[[0,0] for _ in range(landx)] for i in range(landy)]
landyx = (screenx/landx)
landyy = (screeny/landy)

screen = pygame.display.set_mode((screenx,screeny))


live = False
alive = False
ice = False
fps = 60

print("Welcome to the sandbox!")
def remindMe() -> None:
    print("ELEMENTS: Press the keys for the element!  1: Sand  2: Stone  3: Water  4: Sugar  5: Wall  6: Dirt  7: Mud  8: Plant  9: Lava ")
    print("ELEMENTS: Q: Iron  W: Gravel  E: Obsidian  R: Steam  T: Glass  Y: Salt  U: Cloud  I: Brick O: Clay  P: Void  A: Algae")
    print("ELEMENTS: G: Snow  H: Ice  J: TNT  K: Sapling  L: Life particle (think the game of life, If turned off it will just be random)")
    print("ELEMENTS: Z: Electricity  X: Flower Seed  C: Oil  V: Fire N: Jammer (Screws stuff up)  M: Cloner  B: Smart Remover  S: Smart Converter  D: Sun  F: Moon")
    print("If you would like more information about how the smart remover/converter works, please visit https://www.youtube.com/watch?v=w_oNW7uHfcw")
    #I'm sure dr. mo wouldn't mind......
    print("ELEMENT CONTROLS: Left click to place down the element, Right click to use the eraser. You will have to discover the rest of the elements on your own through trial and error :)\nTo do multiple elements with a brush, press the comma for it to be random of some elements. To dither the brush, press the slash key.")
    print("ELEMENT CONTROLS: To get an element that's not on this list, press the Right Shift key then enter the element's ID (number) in the console.\nAlternatively, you can eyedrop (copy) an element from the sandbox by pressing period and then clicking the element")
    print("BRUSH CONTROLS: To enter/exit mirror mode, hit the backslash key. To undo an action, press the left square bracket, to redo said action, press the right square bracket ([ and ] respectively)")
    print("IMPORTANT: To start/pause the sandbox, press Left Ctrl. To go a single step in the sandbox, press Space.\nTo clear the sandbox, press the left Alt key. To clear the sandbox and have there be an ocean, hit the right Alt key.\nThere are several other kinds of oceans that can be created on the right hand side of the keyboard by pressing it's buttons.\nTo activate/deactivate the game of life and all it's whimsy, press the CAPS LOCK key. To change the brush size, hit up to grow it, hit down to shrink it.")
    print("SAVE/LOAD CONROLS: To save your sandbox, press either enter key. To load a sandbox, press the 0 key. To show this again, hit the backspace key")


# ===============================================================================================
# ====================================== THE GAME LOOP ==========================================
# ===============================================================================================

sandstack = []
restack = []

remindMe()

fliposwitch = True
#this makes sure that the sand keeps going in a straight line while placing it when it's active, and also some other stuff

while breaking:
    d = 0
    for event in pygame.event.get(): #Event Queue (or whatever it's called)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            if input("Are you sure you want to quit?\n").lower() in yeses:
                breaking = False
        if event.type == pygame.MOUSEBUTTONDOWN and tap:
            sandstack.append(deepcopy(land))
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
            
            #Command Keys
            
            if event.key == pygame.K_SPACE:
                if not alive:
                    sandstack.append(deepcopy(land))
                    restack = []
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
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
            elif event.key == pygame.K_RALT:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[3,0] for _ in range(landx)]
            elif event.key == pygame.K_RCTRL:
                sandstack.append(deepcopy(land))
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[15,0] for _ in range(landx)]
            elif event.key == pygame.K_END:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[9,0] for _ in range(landx)]
            elif event.key == pygame.K_DELETE:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[65,20] for _ in range(landx)]
            elif event.key == pygame.K_HOME:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[29,0] for _ in range(landx)]
            elif event.key == pygame.K_PAGEUP:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[71,0] for _ in range(landx)]
            elif event.key == pygame.K_PAGEDOWN:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[75,0] for _ in range(landx)]
            elif event.key == pygame.K_NUMLOCK:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[60,0] for _ in range(landx)]
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
            elif event.key == pygame.K_SLASH:
                if dither:
                    dither = False
                else:
                    dither = True
            elif event.key == pygame.K_BACKSLASH:
                if mirror:
                    mirror = False
                else:
                    mirror = True
            elif event.key == pygame.K_COMMA:
                if elementary:
                    elementary = False
                else:
                    elementary = True
                    elements = []
                    print("Please choose the elements you want to do. To stop choosing, say something other than an int")
                    try:
                        while True:
                            elements.append(int(input()))
                    except ValueError:
                        elements = tuple(elements)
                        print("Brush now has elements", elements)
                    if len(elements) == 0:
                        print("HEY! YOU FORGOT TO DO ELEMENTS! (Defaulting to what you did last time)")
                        elementary = False
            elif event.key == pygame.K_RIGHTBRACKET:
                if len(restack) != 0:
                    sandstack.append(deepcopy(land))
                    restack = []
                    land = restack.pop()
            elif event.key == pygame.K_LEFTBRACKET:
                if len(sandstack) != 0:
                    restack.append(deepcopy(land))
                    land = sandstack.pop()
            
            #Element Keys
            
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
                element = 42
            elif event.key == pygame.K_d:
                element = 20
            elif event.key == pygame.K_f:
                element = 21
            elif event.key == pygame.K_g:
                element = 22
            elif event.key == pygame.K_h:
                element = 23
            elif event.key == pygame.K_j:
                element = 68
            elif event.key == pygame.K_k:
                element = 62
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
                element = 41
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
                    try:
                        print("Set element to", elementNames[element])
                    except:
                        print("Set to an unknown element:", element)
                except:
                    print("THAT'S NOT A VALID NUMBER FOR AN ELEMENT!!!")
            elif event.key == pygame.K_PERIOD:
                eyedropper = True
                print("Pick an element from the sandbox to copy")
                alive = False
            
            
            #The ultimate thing: SAVING!
            elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                alive = False
                print("What would you like to name your file? (If it's a save that already exists, it will override the save)")
                filename = input()
                legal = True
                for char in illegals:
                    if char in filename:
                        print("File cannot contain an illegal character!", illegals)
                        legal = False
                        break
                if legal:
                    print("Saving", filename+ ".txt to your saves folder... (You better not close your program!)")
                    try:
                        if usesavefolder:
                            thefile = open('sandsaves/'+filename+'.txt', 'w')
                        else:
                            thefile = open(filename+'.txt', 'w')
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
                for char in illegals:
                    if char in filename:
                        print("File cannot contain an illegal character!", illegals)
                        legal = False
                        break
                if legal:
                    sandstack.append(deepcopy(land))
                    backupx = landx
                    backupy = landy
                    bacnupsx = screenx
                    backupsy = screeny
                    backupland = deepcopy(land)
                    backupscreen = screen
                    fail = True
                    print("Loading", filename+ ".txt from your saves folder...")
                    try:
                        if usesavefolder:
                            thefile = open('sandsaves/'+filename+'.txt', 'r')
                        else:
                            thefile = open(filename+'.txt', 'r')
                        reading = thefile.read().split()
                        thefile.close()
                        print(filename, "read with", len(reading), "numbers!")
                        readed = []
                        for inny in range(len(reading)):
                            readed.append(int(reading[inny]))
                        landx = readed[0]
                        landy = readed[1]
                        screenx = readed[2]
                        screeny = readed[3]
                        print("Grid size:", landx, "by", landy, "pixels on a", screenx, "by", screeny, "gaming window.")
                        land = []
                        for ay in range(landy):
                            land.append([])
                            for bx in range(landx):
                                pxl = (bx+(landx*ay)) * 2 + 4
                                land[ay].append([readed[pxl],readed[pxl+1]])
                        
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
                        sandstack.pop()
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
        mx = int((screenx-mousePos.x)/landyx)
        y = int(mousePos.y/landyy)
        for l in range(0-brushsize,1+brushsize):
            for m in range(0-brushsize,1+brushsize):
                t = 0
                try:
                    if eyedropper:
                        element = land[y+l][x+m][0]
                        print("Copied", end = " ")
                        eyedropper = False
                        try:
                            print(elementNames[element], end = " ")
                        except:
                            print("An unknown element", end = " ")
                        print("from the sandbox. (ID:", str(element)+")")
                        time.sleep(0.5)#To assure you don't accidentally screw something up (I had to import an entire library here just for this one command ;w;)
                    else:
                        if (not dither) or random.randint(1,5) == 1:
                            if ice:
                                land[y+l][x+m] = [0,0]
                            else:
                                if elementary:
                                    element = random.choice(elements)
                                if element in (13, 30, 56):
                                    t = 5
                                elif element == 19:
                                    t = random.randint(0,255)
                                elif element == 54:
                                    t = random.randint(1,6)
                                elif element == 61:
                                    t = 3
                                elif element in (64, 65):
                                    t = 20
                                elif element == 67:
                                    t = 10
                                land[y+l][x+m] = [element,t]
                                if mirror:
                                    land[y+l][mx+m] = [element,t]
                except IndexError:
                    oob += 1

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
                pygame.draw.rect(screen,(0,200,0),(j*landyx,i*landyy,landyx,landyy))
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
                cool = 200+et*10
                if cool > 255:
                    cool = 255
                cooler = random.randint(50,100+et*random.randint(20,30))
                if cooler > 255:
                    cooler = 255
                pygame.draw.rect(screen,(cool,cooler,0),(j*landyx,i*landyy,landyx,landyy))
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
                if random.randint(1,111) == 1 and et == 1:
                    pygame.draw.rect(screen,(255,255,0),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(128,128,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 48:
                pygame.draw.rect(screen,(200,230,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 49:
                if et < 0:
                    et = 0
                elif et > 10:
                    et = 10
                pygame.draw.rect(screen,(et*20,150-et*10,0),(j*landyx,i*landyy,landyx,landyy))
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
            elif el == 56:
                pygame.draw.rect(screen,(et*5,et*5,et*5),(j*landyx,i*landyy,landyx,landyy))
            elif el == 57:
                pygame.draw.rect(screen,(100,20+random.randint(-20,20)//2,240),(j*landyx,i*landyy,landyx,landyy))
            elif el == 58:
                if et == 1:
                    pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(240,230,0),(j*landyx,i*landyy,landyx,landyy))
            elif el == 59:
                pygame.draw.rect(screen,(25,25,30),(j*landyx,i*landyy,landyx,landyy))
            elif el == 60:
                pygame.draw.rect(screen,(random.randint(0,50),random.randint(25,255),random.randint(0,50)),(j*landyx,i*landyy,landyx,landyy))
            elif el == 61:
                if et == 0:
                    pygame.draw.rect(screen,(64,64,64),(j*landyx,i*landyy,landyx,landyy))
                elif et == 1:
                    pygame.draw.rect(screen,(128,128,128),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 62:
                if et == 0:
                    pygame.draw.rect(screen,(32,24,16),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(140,70,30),(j*landyx,i*landyy,landyx,landyy))
            elif el == 63:
                pygame.draw.rect(screen,(130,80,60),(j*landyx,i*landyy,landyx,landyy))
            elif el == 64:
                pygame.draw.rect(screen,(170,250,190),(j*landyx,i*landyy,landyx,landyy))
            elif el == 65:
                pygame.draw.rect(screen,(0,255,0),(j*landyx,i*landyy,landyx,landyy))
            elif el == 66:
                pygame.draw.rect(screen,(random.randint(0,20),200+random.randint(0,20),random.randint(0,20)),(j*landyx,i*landyy,landyx,landyy))
            elif el == 67:
                pygame.draw.rect(screen,(random.randint(150,255),random.randint(50,230),random.randint(0,40)),(j*landyx,i*landyy,landyx,landyy))
            elif el == 68:
                pygame.draw.rect(screen,(200,0,0),(j*landyx,i*landyy,landyx,landyy))
            elif el == 69:
                if et == 1:
                    pygame.draw.rect(screen,(255,random.randint(0,255),random.randint(0,255)),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(200,180,150),(j*landyx,i*landyy,landyx,landyy))
            elif el == 70:
                pygame.draw.rect(screen,(80,100,60),(j*landyx,i*landyy,landyx,landyy))
            elif el == 71:
                if et != 0:
                    pygame.draw.rect(screen,(200,255,230),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(200,200,255),(j*landyx,i*landyy,landyx,landyy))
            elif el == 72:
                pygame.draw.rect(screen,(120-et,60-(et//5),10-(et//10)),(j*landyx,i*landyy,landyx,landyy))
            elif el == 73:
                pygame.draw.rect(screen,(20,20,20),(j*landyx,i*landyy,landyx,landyy))
            elif el == 74:
                pygame.draw.rect(screen,(60,30,15),(j*landyx,i*landyy,landyx,landyy))
            elif el == 75:
                pygame.draw.rect(screen,(0,random.randint(100,200),random.randint(30,100)),(j*landyx,i*landyy,landyx,landyy))
            elif el == 76:
                pygame.draw.rect(screen,(255,150,120),(j*landyx,i*landyy,landyx,landyy))
            
            else:
                if el != 0:
                    pygame.draw.rect(screen,(255,0,255),(j*landyx,i*landyy,landyx,landyy))
            
    if not alive:
        live = False
    pygame.display.flip()
pygame.quit()
print("Process exit with code: \"Pee pee poo poo caca do do fart we wa woooooo\"")
print("You went out of bounds", oob, "times!")
if oob == 0:
    print("Good job!")
elif oob < 100:
    print("Almost good")
elif oob < 200:
    print("Pls do better uwu")
elif oob < 500:
    print("Trace in the screen next time!!")
elif oob < 1000:
    print("You can only draw in the screen, please don't make me remind you again!")
elif oob < 10000:
    print("Please stop going out of bounds so much, it's annoying")
elif oob < 1000000:
    print("Please remain inside these boundaries.")
else:
    print("Are you trying to enter the backrooms or something???")