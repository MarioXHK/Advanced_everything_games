#Can someone please tell me how to give more resources to this app so I can throttle it and have a smooth 60 fps while my computer combusts into flames

showfps = False

import pygame
from pygame import Vector2
from copy import deepcopy
import random

screenx = 800
screeny = 600

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

landx = 80
landy = 60
land = [[[0,0] for _ in range(landx)] for i in range(landy)]
landyx = (screenx/landx)
landyy = (screeny/landy)

element = 1
werealsodoinglife = False
brushsize = 0

def coinflip() -> bool:
    return bool(random.getrandbits(1))

def neighborCount(grid: list[list[list[int]]],pointx: int, pointy: int, checker: list[int] | tuple[int]) -> int:
    count = 0
    for l in range(-1,2):
        for m in range(-1,2):
            if (l,m) == (0,0):
                continue
            ex = pointx+m
            why = pointy+l
            if ex == len(grid[0]):
                continue
            elif ex == -1:
                continue
            if why == len(grid):
                continue
            elif why == -1:
                continue
                
            if grid[why][ex][0] in checker:
                count += 1
                
    return count

#Checks if a neightbor is in the checker list
def neighborCheck(grid: list[list[list[int]]],pointx: int, pointy: int, checker: list[int] | tuple[int]) -> bool:
    for l in range(-1,2):
        for m in range(-1,2):
            cant = False
            if (l,m) == (0,0):
                continue
            ex = pointx+m
            why = pointy+l
            if ex == len(grid[0]):
                cant = True
            elif ex == -1:
                cant = True
            if why == len(grid):
                cant = True
            elif why == -1:
                cant = True
                
            if cant:
                continue
            else:
                if grid[why][ex][0] in checker:
                    return True
    return False

#gets the neighbor's ID
def myNeighbor(grid: list[list[list[int]]],pointx: int, pointy: int, shouldnt: list[int] | tuple[int]) -> int:
    for l in range(-1,2):
        for m in range(-1,2):
            cant = False
            if (l,m) == (0,0):
                continue
            ex = pointx+m
            why = pointy+l
            if ex == len(grid[0]):
                cant = True
            elif ex == -1:
                cant = True
            if why == len(grid):
                cant = True
            elif why == -1:
                cant = True
                
            if cant:
                continue
            else:
                if grid[why][ex][0] != 0 and not grid[why][ex][0] in shouldnt:
                    return grid[why][ex][0]
    return 0

#Checks the "Temprature" of it's neighbors
def neighborTempCheck(grid: list[list[list[int]]],pointx: int, pointy: int, checker: list[int] | tuple[int], maths: str = ">", temp: int = 0) -> tuple[bool,int]:
    answer = 0
    answered = False
    for l in range(-1,2):
        for m in range(-1,2):
            cant = False
            if (l,m) == (0,0):
                continue
            ex = pointx+m
            why = pointy+l
            if ex == len(grid[0]):
                cant = True
            elif ex == -1:
                cant = True
            if why == len(grid):
                cant = True
            elif why == -1:
                cant = True
                
            if cant:
                continue
            else:
                if grid[why][ex][0] in checker:
                    #Did this to make it more readable. Ironic considering the rest of my code
                    if maths == "==" and grid[why][ex][1] == temp:
                        return (True,grid[why][ex][1])
                    elif maths == "<" and grid[why][ex][1] < temp and grid[why][ex][1] < answer:
                        answered = True
                        answer = grid[why][ex][1]
                    elif maths == ">" and grid[why][ex][1] > temp and grid[why][ex][1] > answer:
                        answered = True
                        answer = grid[why][ex][1]
                    elif maths == "<=" and grid[why][ex][1] <= temp and grid[why][ex][1] <= answer:
                        answered = True
                        answer = grid[why][ex][1]
                    elif maths == ">=" and grid[why][ex][1] >= temp and grid[why][ex][1] >= answer:
                        answered = True
                        answer = grid[why][ex][1]
    if answered:
        return (True,answer)
    
    return (False,0)

# Sand Physics ---------------------------------------------------
def sandCheck(grid: list[list[list[int]]],pointx: int, pointy: int, floats: bool = False, reverse: bool = False, gas: bool = False) -> tuple[int]:
    #Returns a list, the 1st element determines where the sand should fall. If 0, then nowhere, 1 is left, 2 is falling middle, 3 is right
    #The second element is the element should be subsituted for air (only if it sinks)
    b = (0,0)
    l = 1
    if reverse:
        l = -1
    if (pointy == len(grid) - 1 and not reverse) or (pointy == 0 and reverse):
        return (0,0)
    under = True
    if not floats:
        if gas:
            b = [0,1,3,4,6,8,9,11,15,27,28,32,34]
        else:
            b = [0,3,15,27,29,34]
        if grid[pointy][pointx][0] in b:
            b.remove(grid[pointy][pointx][0])
        b = tuple(b)
    canLeft = True
    canRight = True
    for m in range(-1,2):
        
        ex = pointx+m
        if ex == len(grid[0]):
            canRight = False
            continue
            
        elif ex == -1:
            canLeft = False
            continue
            
        if grid[pointy+l][ex][0] in b:
            under = False
    if under:
        return (0,0)
    else:
        if grid[pointy+l][pointx][0] in b:
            return (2,grid[pointy+l][pointx][0])
        elif canLeft and canRight and (grid[pointy+l][pointx-1][0] in b) and (grid[pointy+l][pointx+1][0] in b):
            doing = coinflip()
            if doing:
                return (1,grid[pointy+l][pointx-1][0])
            else:
                return (3,grid[pointy+l][pointx+1][0])
        elif canLeft and (grid[pointy+l][pointx-1][0] in b):
            return [1,grid[pointy+l][pointx-1][0]]
        elif canRight and (grid[pointy+l][pointx+1][0] in b):
            return (3,grid[pointy+l][pointx+1][0])
    return [0,0] #To assure something gets returned if everything else is wrong

# Stone Physics ---------------------------------------------------
def stoneCheck(grid: list[list[list[int]]],pointx: int, pointy: int, floats: bool = False, reverse: bool = False, gas: bool = False) -> tuple[bool,int]:
    #returns if something's under it (or above it if in reverse)
    l = 1
    if reverse:
        l = -1
    b = (0,0)
    if not floats:
        if gas:
            b = [0,1,3,4,6,8,9,11,15,27,28,32,34]
        else:
            b = [0,3,15,27,29,34]
        if grid[pointy][pointx][0] in b:
            b.remove(grid[pointy][pointx][0])
        b = tuple(b)
    if (pointy == len(grid) - 1 and not reverse) or (pointy == 0 and reverse):
        return [True,0]
    elif grid[pointy+l][pointx][0] in b:
        return [False,grid[pointy+l][pointx][0]]
    else:
        return [True,0]

#Me when there's plenty of stuff below me but I wanna wander left or right
def lrWanderCheck(grid: list[list[list[int]]],pointx: int,pointy: int, floaty: bool = False, waterlike: bool = False, reverse: bool = False) -> tuple[bool,bool,int]:
    b = (0,0)
    if waterlike:
        b = [0,3,15,27,29]
        if grid[pointy][pointx][0] in b:
            b.remove(grid[pointy][pointx][0])
        b = tuple(b)
    l = 1
    if reverse:
        l = -1
    if floaty and (pointy - 1 == -1 or pointy + 1 == len(grid)):
        floaty = False
    
    canRight = True
    canLeft = True
    if pointx + 1 == len(grid[0]):
        canRight = False
    elif not grid[pointy][pointx+1][0] in b:
        canRight = False
    elif floaty and not grid[pointy+l][pointx+1][0] in b:
            canRight = False
    
    if pointx - 1 == -1:
        canLeft = False
    elif not grid[pointy][pointx-1][0] in b:
        canLeft = False
    elif floaty and not grid[pointy+l][pointx-1][0] in b:
            canLeft = False

    if not(canRight or canLeft):
        return (False,False,0)
    if coinflip():
        if canLeft and canRight:
            x = coinflip()
            l = -1
            if x:
                l = 1
            return (True,x,grid[pointy][pointx-l][0])
        elif not canRight:
            return (True,False,grid[pointy][pointx-1][0])
        else:
            return (True,True,grid[pointy][pointx+1][0])
    return (False,False,0)

#Me when I'd like to go up or down spontaniously
def udWanderCheck(grid: list[list[list[int]]],pointx: int,pointy: int, waterlike: bool = False) -> tuple[bool,bool,int]:
    b = (0,0)
    if waterlike:
        b = [3,15,27,29]
        if grid[pointy][pointx][0] in b:
            b.remove(grid[pointy][pointx][0])
        b = tuple(b)
    canUp = True
    canDown = True
    if pointy + 1 == len(grid):
        canUp = False
    elif not grid[pointy+1][pointx][0] in b:
        canUp = False
    
    if pointy - 1 == -1:
        canDown = False
    elif not grid[pointy-1][pointx][0] in b:
        canDown = False

    if not(canUp or canDown):
        return (False,False,0)
    if coinflip():
        if canDown and canUp:
            x = coinflip()
            l = 1
            if x:
                l = -1
            return (True,x,grid[pointy+l][pointx][0])
        elif not canUp:
            return (True,False,grid[pointy-1][pointx][0])
        else:
            return (True,True,grid[pointy+1][pointx][0])
    return (False,False,0)

#check if there's something that can support it on both left and right sides
def lrCheck(plain: list[list[int]],pointx: int, idcIfUnsupportable: bool = False) -> bool:
    if pointx + 1 == len(plain) or pointx - 1 == -1:
        return False
    unsupportable = (0,1,3,4,6,8,9,10,11,13,15,16,18,19,22,23,27,28,29,30,32,35,36)
    if idcIfUnsupportable:
        unsupportable = [0]
    if plain[pointx-1][0] in unsupportable or plain[pointx+1][0] in unsupportable:
        return False
    return True

#checks if there's a single pixel of a specific element anywhere (more optimized I guess but more specific)
def checkEverywhere(grid: list[list[list[int]]], thing) -> bool:
    for i in range(len(grid)):
        if thing in grid[i]:
            return True
    return False

#same as checksEverywhere but only checks the ID of an element (less optimized I guess but less specific)
def checkAbsolutelyEverywhere(grid: list[list[list[int]]], thing) -> bool:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j][0] == thing:
                return True
    return False

# The thing that makes all of this possible, it's DOSTUFF!!!!

def doStuff(plain,switch):
    e = 0
    t = 0
    sun = checkEverywhere(plain,[20,0])
    moon = checkEverywhere(plain,[21,0])
    grid = deepcopy(plain)
    for a in range(len(plain)):
        for b in range(len(plain[0])):
            
            if plain[a][b] != grid[a][b]:
                continue
            
            e = plain[a][b][0]
            t = plain[a][b][1]
            
            #Air
            if plain[a][b][0] == 0:
                if not werealsodoinglife:
                    continue
                #I need to optimize this more it's laggy as hell currently :(
                l = neighborCount(plain,b,a,28)
                if l == 3:
                    grid[a][b] = [28,0]
            
            #Sand
            elif plain[a][b][0] == 1:
                if neighborCheck(plain,b,a,[9]):
                    e = 14
                    t = 2
                else:
                    n = neighborTempCheck(plain,b,a,[14])
                    if n[0]:
                        e = 14
                        t = n[1]-1
                    elif random.randint(1,50) == 1:
                        if neighborCheck(grid,b,a,(3,15)):
                            e = 10
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    if e == 1:
                        continue
                    else:
                        grid[a][b] = [e,t]
                else:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b+(c[0]-2)] = [e,t]
            #Stone
            elif plain[a][b][0] == 2:
                if random.randint(1,1000) == 1:
                    if neighborCheck(grid,b,a,[3,15]):
                        e = 11
                c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [e,0]
                else:
                    if e == 2:
                        continue
                    else:
                        grid[a][b] = [e,0]
            #Water
            elif plain[a][b][0] == 3:
                if coinflip():
                    if neighborCheck(plain,b,a,[30]):
                        e = 13
                        t = 10
                    elif neighborCount(plain,b,a,[22,23,27]) > 3:
                        e = 27
                if neighborCheck(plain,b,a,[9]):
                    e = 13
                    t = 15
                elif random.randint(1,10000) == 1:
                    if neighborCheck(grid,b,a,[18]):
                        e = 18
                elif random.randint(1,20000) == 1:
                    if sun:
                        e = 13
                        t = 10
                c = sandCheck(grid,b,a,True)
                if c[0] == 0:
                    d = lrWanderCheck(grid,b,a)
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
            elif plain[a][b][0] == 4:
                if neighborCheck(plain,b,a,(9,20,21)):
                    e = 24
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    if random.randint(1,100) == 1:
                        if neighborCheck(grid,b,a,[3]):
                            e = 15
                    elif random.randint(1,5000) == 1:
                        if neighborCheck(grid,b,a,[18]):
                            e = 18
                    if e == 4:
                        continue
                    else:
                       grid[a][b] = [e,0] 
                else:
                    if random.randint(1,10) == 1:
                        if neighborCheck(grid,b,a,[3]):
                            e = 15
                    grid[a][b] = [c[1],0]
                    if c[0] == 2:
                        d = lrWanderCheck(grid,b,a, True)
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
            elif plain[a][b][0] == 5:
                continue          
            #Dirt
            elif plain[a][b][0] == 6:
                if random.randint(1,900) == 1:
                    if neighborCheck(grid,b,a,[8]) and sun:
                        e = 8
                if random.randint(1,100) == 1:
                    if neighborCheck(grid,b,a,[3]):
                        e = 7
                c = sandCheck(grid,b,a,True)
                if c[0] == 0:
                    if e == 6:
                        continue
                    else:
                        grid[a][b] = [e,0]
                else:
                    grid[a][b] = [0,0]
                    grid[a+1][b+(c[0]-2)] = [e,0]
            #Mud
            elif plain[a][b][0] == 7:
                if random.randint(1,400) == 1:
                    if neighborCheck(grid,b,a,[8]) and sun:
                        e = 8
                if neighborCheck(plain,b,a,[9,30]):
                    e = 6
                if random.randint(1,5000) == 1:
                    if neighborCheck(grid,b,a,[18]):
                        e = 18
                    elif neighborCheck(grid,b,a,[8]):
                        e = 8
                c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [e,0]
                else:
                    if e == 7:
                        continue
                    else:
                        grid[a][b] = [e,0]
            #Plant
            elif plain[a][b][0] == 8:
                c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [8,0]
            #Lava
            elif plain[a][b][0] == 9:
                if neighborCheck(plain,b,a,(3,7,10,13,15,18,22,23,25,27)):
                    t -= 2
                    if neighborCheck(plain,b,a,(3,15,22,23,25,27)):
                        t -= 4
                
                if neighborCheck(plain,b,a,[20]):
                    t = 10
                elif neighborCheck(plain,b,a,[21]):
                    t = -10
                
                if random.randint(1,10) == 1:
                    if moon:
                        t -= 1
                if t <= -10:
                    
                    e = 12
                
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    if random.randint(1,25) != 1:
                        if e == 9:
                            grid[a][b] = [e,t]
                            continue
                        else:
                            grid[a][b] = [e,0]
                            continue
                    d = lrWanderCheck(grid,b,a)
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
            elif plain[a][b][0] == 10:
                if neighborCheck(plain,b,a,[9,30]):
                    e = 14
                    t = 1
                else:
                    n = neighborTempCheck(plain,b,a,[14])
                    if n[0]:
                        e = 14
                        t = n[1]-1
                c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [e,t]
                else:
                    if e == 10:
                        grid[a][b] = [e,t]
                    else:
                        grid[a][b] = [e,0]
            
            #Gravel
            elif plain[a][b][0] == 11:
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    continue
                else:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b+(c[0]-2)] = [11,0]
            #Obsidian
            elif plain[a][b][0] == 12:
                c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [12,0]
                else:
                    continue
            #Steam
            elif plain[a][b][0] == 13:
                if random.randint(1,20) == 1 and t > 0:
                    t -= 1
                if t <= 0 and random.randint(1,34) == 1:
                    e = 16
                c = sandCheck(grid,b,a,False,True,True)
                if c[0] == 0:
                    d = lrWanderCheck(grid,b,a,False,False,True)
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
                        d = lrWanderCheck(grid,b,a,True,False,True)
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
            elif plain[a][b][0] == 14:
                if coinflip() and t > 0:
                    t -= 1
                o = lrCheck(plain[a],b)
                if o:
                    continue
                c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [14,t]
                else:
                    continue
                    
            #Sugar Water
            elif plain[a][b][0] == 15:
                if coinflip() and neighborCheck(plain,b,a,[30]):
                    e = 4
                elif neighborCheck(plain,b,a,[9]):
                    e = 4
                elif random.randint(1,2500) == 1:
                    if neighborCheck(grid,b,a,[18]):
                        e = 18
                    elif neighborCheck(grid,b,a,[24]):
                        e = 4
                c = sandCheck(grid,b,a,True)
                if c[0] == 0:
                    d = lrWanderCheck(grid,b,a,False,True)
                    if not d[0]:
                        d = udWanderCheck(grid,b,a,True)
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
            elif plain[a][b][0] == 16:
                if random.randint(1,800) == 1:
                    if moon:
                        e = 22 
                    else:
                        e = 3
                if random.randint(1,20) == 1:
                    if random.randint(1,4) != 1:
                        d = lrWanderCheck(grid,b,a, True)
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
                        d = udWanderCheck(grid,b,a)
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
            elif plain[a][b][0] == 17:
                o = lrCheck(plain[a],b)
                if o:
                    continue
                c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [e,0]
                else:
                    continue
            
            #Algae
            elif plain[a][b][0] == 18:
                o = lrCheck(plain[a],b,True)
                if o:
                    continue
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    if e == 1:
                        grid[a][b] = [e,t]
                    else:
                        grid[a][b] = [e,0]
                else:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b+(c[0]-2)] = [e,0]
            
            #Glass shards or dust or whatever you wanna see it as
            elif plain[a][b][0] == 19:
                if neighborCheck(plain,b,a,[9]):
                    e = 14
                    t = 3
                elif coinflip() and neighborCheck(plain,b,a,[30]):
                    e = 14
                    t = 0
                else:
                    n = neighborTempCheck(plain,b,a,[14])
                    if n[0]:
                        e = 14
                        t = n[1]-1
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    if e == 19:
                        grid[a][b] = [e,t]
                    else:
                        grid[a][b] = [e,0]
                else:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b+(c[0]-2)] = [e,t]
            #Sun
            elif plain[a][b][0] == 20:
                continue
            #Moon
            elif plain[a][b][0] == 21:
                continue
            
            #Snow
            elif plain[a][b][0] == 22:
                if random.randint(1,100) == 1:
                    if sun:
                        e = 3
                if random.randint(1,10) == 1:
                    if (not moon) and neighborCheck(plain,b,a,(3,15)):
                        e = 3
                if neighborCheck(plain,b,a,(9,13,20)):
                    e = 3
                if random.randint(1,5000) == 1:
                    e = 3
                if random.randint(1,10000) == 1:
                    e = 23
                if switch:
                    c = sandCheck(grid,b,a,True)
                    if c[0] == 0:
                        if e == 22:
                            grid[a][b] = [e,t]
                        else:
                            grid[a][b] = [e,0] 
                    else:
                        grid[a][b] = [c[1],0]
                        if c[0] == 2:
                            d = lrWanderCheck(grid,b,a, True)
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
            elif plain[a][b][0] == 23:
                if random.randint(1,200) == 1:
                    if sun:
                        e = 3
                if coinflip():
                    if neighborCheck(plain,b,a,(13,20)):
                        e = 3
                if neighborCheck(plain,b,a,[9,30]):
                    e = 3
                if random.randint(1,1000) == 1:
                    if neighborCheck(grid,b,a,(3,15)):
                        e = 3
                c = stoneCheck(grid,b,a,True)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [e,0]
                else:
                    if e == 2:
                        grid[a][b] = [e,t]
                    else:
                        grid[a][b] = [e,0]
            
            #Sugar Crystal
            elif plain[a][b][0] == 24:
                if random.randint(1,7000) == 1:
                    if neighborCheck(grid,b,a,[18]):
                        e = 18
                elif random.randint(1,5000) == 1:
                    if neighborCheck(grid,b,a,[3,15]):
                        e = 4
                o = lrCheck(plain[a],b)
                if o:
                    if e == 24:
                        grid[a][b] = [e,t]
                    else:
                        grid[a][b] = [e,0]
                c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [e,0]
                else:
                    if e == 24:
                        grid[a][b] = [e,t]
                    else:
                        grid[a][b] = [e,0]
            
            #Packed Ice
            elif plain[a][b][0] == 25:
                if random.randint(1,5) == 1:
                    if neighborCheck(plain,b,a,[9]):
                        e = 23
                o = lrCheck(plain[a],b)
                if o:
                    continue
                c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [e,0]
                else:
                    if e == 25:
                        grid[a][b] = [e,t]
                    else:
                        grid[a][b] = [e,0]
            
            #Life
            elif plain[a][b][0] == 26:
                if werealsodoinglife:
                    l = neighborCount(plain,b,a,26)
                    if l < 2 or l > 3:
                        grid[a][b] = [0,0]
                else:
                    grid[a][b] = [random.randint(0,9),0]
            
            
            #Sludge
            elif plain[a][b][0] == 27:
                if random.randint(1,50) == 1:
                    if sun:
                        e = 3
                if random.randint(1,500) == 1 and not moon:
                        e = 3
                if coinflip():
                    if (not moon) and neighborCheck(plain,b,a,(3,15)):
                        e = 3
                if coinflip() and e != 27:
                    if neighborCount(plain,b,a,[22,23,27]) > 3:
                        e = 27
                if random.randint(1,20) == 1:
                    if neighborCount(plain,b,a,[22,23,27]) > 4:
                        e = 23
                if neighborCheck(plain,b,a,(9,13,20)):
                    e = 13
                c = sandCheck(grid,b,a)
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
            elif plain[a][b][0] == 28:
                if random.randint(1,15) == 1:
                    if neighborCheck(plain,b,a,[9,30]):
                        if coinflip():
                            e = 30
                            t = 5
                        else:
                            e = 32
                #Seed
                if plain[a][b][1] == 0:
                    c = sandCheck(grid,b,a)
                    if c[0] == 0:
                        if random.randint(1,100) == 1 and neighborCheck(plain,b,a,(7,8,10,18,27,32)):
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
            elif plain[a][b][0] == 29:
                if random.randint(1,15) == 1:
                    if neighborCheck(plain,b,a,[9,30]):
                        e = 30
                        t = 5
                c = sandCheck(grid,b,a,True)
                if c[0] == 0:
                    d = lrWanderCheck(grid,b,a,False,True)
                    if not d[0]:
                        d = udWanderCheck(grid,b,a,True)
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
            elif plain[a][b][0] == 30:
                flame = False
                if (random.randint(1,4) == 1 or moon) and t > 0:
                    if not sun:
                        t -= 1
                    else:
                        if coinflip():
                            t -= 1
                if neighborCheck(plain,b,a,(4,8,15,18,20,24,28,29,31)):
                    t = 5
                    flame = True
                elif neighborCheck(plain,b,a,[33]):
                    t = 2
                elif coinflip():
                    o = neighborTempCheck(plain,b,a,[30],">",t)
                    if o[0]:
                        t = o[1] - 1
                if t <= 0:
                    e = 0
                if flame and random.randint(1,5) != 1:
                    c = [0]
                else:
                    c = sandCheck(grid,b,a,False,True,True)
                if c[0] == 0:
                    if flame and random.randint(1,8) != 1:
                        d = [False]
                    else:
                        d = lrWanderCheck(grid,b,a,False,False,True)
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
                        d = lrWanderCheck(grid,b,a,True,False,True)
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
            elif plain[a][b][0] == 31:
                if coinflip():
                    if neighborCount(plain,b,a,(9,30)) > random.randint(1,5):
                        e = 32
                elif random.randint(1,20) == 1:
                    if neighborCheck(plain,b,a,[30]):
                        e = 30
                        t = 5
                elif random.randint(1,40) == 1:
                    if neighborCheck(plain,b,a,[9]):
                        e = 30
                        t = 5
                
                if e != 31:
                    grid[a][b] = [e,t]
            
            #Ash
            elif plain[a][b][0] == 32:
                if random.randint(1,1000) == 1:
                    if neighborCount(plain,b,a,[2,11,29,32]) > 3:
                        t += random.randint(1,2)
                elif random.randint(1,100) == 1:
                    if neighborCheck(plain,b,a,[3,15]):
                        e = 34
                if t >= 100:
                    e = 29
                    t = 0
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    grid[a][b] = [e,t] 
                else:
                    grid[a][b] = [c[1],0]
                    if c[0] == 2:
                        d = lrWanderCheck(grid,b,a, True)
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
            elif plain[a][b][0] == 33:
                if plain[a][b][1] == 0:
                    grid[a][b][1] = myNeighbor(grid,b,a,[33])
                else:
                    if a + 1 != len(plain) and grid[a+1][b][0] == 0:
                        grid[a+1][b] = [plain[a][b][1],0]
                    if a - 1 != -1 and grid[a-1][b][0] == 0:
                        grid[a-1][b] = [plain[a][b][1],0]
                    if b + 1 != len(plain[0]) and grid[a][b+1][0] == 0:
                        grid[a][b+1] = [plain[a][b][1],0]
                    if b - 1 != -1 and grid[a][b-1][0] == 0:
                        grid[a][b-1] = [plain[a][b][1],0]
            
            #Clay
            elif plain[a][b][0] == 34:
                if neighborCheck(plain,b,a,[9,30]):
                    e = 17
                
                if random.randint(1,10) == 1:
                    if moon:
                        t -= 1
                if t <= -10:
                    
                    e = 12
                
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    if random.randint(1,40) != 1:
                        if e == 17:
                            grid[a][b] = [e,t]
                            continue
                        else:
                            grid[a][b] = [e,0]
                            continue
                    d = lrWanderCheck(grid,b,a)
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
            elif plain[a][b][0] == 35:
                if a + 1 != len(plain) and grid[a+1][b][0] != 35:
                    grid[a+1][b] = [0,0]
                if a - 1 != -1 and grid[a-1][b][0] != 35:
                    grid[a-1][b] = [0,0]
                if b + 1 != len(plain[0]) and grid[a][b+1][0] != 35:
                    grid[a][b+1] = [0,0]
                if b - 1 != -1 and grid[a][b-1][0] != 35:
                    grid[a][b-1] = [0,0]
            
            #Petal (Hidden)
            elif plain[a][b][0] == 36:
                if random.randint(1,15) == 1:
                    if neighborCheck(plain,b,a,[9,30]):
                        if coinflip():
                            e = 30
                            t = 5
                        else:
                            e = 32
                if neighborCheck(plain,b,a,[8,28,36]):
                    c = [True]
                else:
                    c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [e,t]
                else:
                    grid[a][b] = [e,t]
                    
    return grid


live = False
alive = False
ice = False
fps = 60

def remindMe() -> None:
    print("Press the keys for the element!\n1: Sand  2: Stone  3: Water  4: Sugar  5: Wall\n6: Dirt  7: Mud  8: Plant  9: Lava  0: Eraser")
    print("Q: Wet sand  W: Gravel  E: Obsidian  R: Steam\nT: Glass  Y: Sugar Water  U: Cloud  I: Brick O: Clay\nP: Void  A: Algae  S: Glass shards  D: Sun  F: Moon")
    print("G: Snow  H: Ice  J: Sugar Crystal  K: Packed Ice\nL: Life particle (think the game of life) (WIP, for now it just despenses random carp)")
    print("Z: Sludge  X: Flower Seed  C: Oil  V: Fire\nB: Wood  N: Ash  M: Cloner")
    print("To show this again, hit backspace")

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
            elif event.key == pygame.K_0:
                element = 0
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
                element = 10
            elif event.key == pygame.K_w:
                element = 11
            elif event.key == pygame.K_e:
                element = 12
            elif event.key == pygame.K_r:
                element = 13
            elif event.key == pygame.K_t:
                element = 14
            elif event.key == pygame.K_y:
                element = 15
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
                element = 25
            elif event.key == pygame.K_l:
                element = 26
            elif event.key == pygame.K_z:
                element = 27
            elif event.key == pygame.K_x:
                element = 28
            elif event.key == pygame.K_c:
                element = 29
            elif event.key == pygame.K_v:
                element = 30
            elif event.key == pygame.K_b:
                element = 31
            elif event.key == pygame.K_n:
                element = 32
            #Oops I just realized that I forgot to include o and p
            elif event.key == pygame.K_m:
                element = 33
            elif event.key == pygame.K_o:
                element = 34
            elif event.key == pygame.K_p:
                element = 35
    
    clock.tick(60)
    if showfps and fps != int(clock.get_fps()):
        fps = int(clock.get_fps())
        print("fps:", fps)
    
    if live:
        land = doStuff(land,fliposwitch)


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
            if land[i][j][0] == 1:
                pygame.draw.rect(screen,(255,255,0),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 2:
                pygame.draw.rect(screen,(150,150,150),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 3:
                pygame.draw.rect(screen,(0,0,255),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 4:
                pygame.draw.rect(screen,(250,250,250),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 5:
                pygame.draw.rect(screen,(100,100,100),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 6:
                pygame.draw.rect(screen,(200,100,50),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 7:
                pygame.draw.rect(screen,(150,50,10),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 8:
                pygame.draw.rect(screen,(0,255,0),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 9:
                pygame.draw.rect(screen,(255,0,0),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 10:
                pygame.draw.rect(screen,(200,200,50),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 11:
                pygame.draw.rect(screen,(200,200,200),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 12:
                pygame.draw.rect(screen,(30,20,40),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 13:
                pygame.draw.rect(screen,(128,200,255),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 14:
                pygame.draw.rect(screen,(0,255,255),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 15:
                pygame.draw.rect(screen,(0,128,255),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 16:
                pygame.draw.rect(screen,(230,230,230),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 17:
                pygame.draw.rect(screen,(150,90,60),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 18:
                pygame.draw.rect(screen,(0,128,0),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 19:
                random.seed(land[i][j][1])
                pygame.draw.rect(screen,(random.randint(0,50),50+random.randint(0,200),100+random.randint(0,150)),(j*landyx,i*landyy,landyx,landyy))
                random.seed()
            elif land[i][j][0] == 20:
                pygame.draw.rect(screen,(255,255,128),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 21:
                pygame.draw.rect(screen,(10,60,180),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 22:
                pygame.draw.rect(screen,(240,250,255),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 23:
                pygame.draw.rect(screen,(200,255,255),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 24:
                pygame.draw.rect(screen,(240,220,255),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 25:
                pygame.draw.rect(screen,(100,200,230),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 26:
                pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 27:
                pygame.draw.rect(screen,(170,210,250),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 28:
                if land[i][j][1] == 0:
                    pygame.draw.rect(screen,(40,20,10),(j*landyx,i*landyy,landyx,landyy))
                else:
                    pygame.draw.rect(screen,(0,255,0),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 29:
                pygame.draw.rect(screen,(24,24,24),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 30:
                pygame.draw.rect(screen,(random.randint(150,200+land[i][j][1]*10),random.randint(50,100+land[i][j][1]*random.randint(20,30)),0),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 31:
                pygame.draw.rect(screen,(140,70,30),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 32:
                cool = 100-land[i][j][1]//2
                pygame.draw.rect(screen,(cool,cool,cool),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 33:
                cool = 0
                if land[i][j][1] != 0:
                    cool = 100+random.randint(-20,20)
                pygame.draw.rect(screen,(100+cool,cool//2,255),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 34:
                pygame.draw.rect(screen,(160,170,180),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 35:
                pygame.draw.rect(screen,(10,10,10),(j*landyx,i*landyy,landyx,landyy))
            elif land[i][j][0] == 36:
                colour = (255,255,255)
                if land[i][j][1] == 1:
                    colour = (255,0,0)
                elif land[i][j][1] == 2:
                    colour = (255,128,0)
                elif land[i][j][1] == 3:
                    colour = (255,255,0)
                elif land[i][j][1] == 4:
                    colour = (128,255,0)
                elif land[i][j][1] == 5:
                    colour = (0,255,0)
                elif land[i][j][1] == 6:
                    colour = (0,255,128)
                elif land[i][j][1] == 7:
                    colour = (255,255,255)
                elif land[i][j][1] == 8:
                    colour = (0,128,255)
                elif land[i][j][1] == 9:
                    colour = (0,0,255)
                elif land[i][j][1] == 8:
                    colour = (128,0,255)
                elif land[i][j][1] == 9:
                    colour = (255,0,255)
                elif land[i][j][1] == 10:
                    colour = (128,0,255)
                elif land[i][j][1] == 11:
                    colour = (128,128,128)
                pygame.draw.rect(screen,colour,(j*landyx,i*landyy,landyx,landyy))
    if not alive:
        live = False
    pygame.display.flip()
pygame.quit()
print("Process exit with code: \"Pee pee poo poo caca do do fart we wa woooooo\"")