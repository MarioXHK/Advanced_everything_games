import pygame
from pygame import Vector2
from copy import deepcopy
import random

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Sandbox game!")
breaking=True
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

#mouse variables--------------------------------
mousePos = Vector2(0,0)
fire = False
tap = True

landx = 100
landy = 100
land = [[[0,0] for _ in range(landx)] for i in range(landy)]
landyx = (1000/landx)
landyy = (1000/landy)

element = 1

def coinflip() -> bool:
    return bool(random.getrandbits(1))


def neighborCheck(grid: list[list[bool]],pointx: int, pointy: int, checker) -> bool:
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
                if grid[why][ex][0] == checker:
                    return True
    return False

# Sand Physics ---------------------------------------------------
def sandCheck(grid: list[list[bool]],pointx: int, pointy: int, floats: bool = False) -> tuple[int]:
    #Returns a list, the 1st element determines where the sand should fall. If 0, then nowhere, 1 is left, 2 is falling middle, 3 is right
    #The second element is the element should be subsituted for air (only if it sinks)
    b = (0,3)
    if pointy == len(grid) - 1:
        return (0,0)
    under = True
    sinks = not floats
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
            
        if grid[pointy+1][ex][0] == 0 or (grid[pointy+1][ex][0] in b and sinks):
            under = False
    if under:
        return (0,0)
    else:
        if floats:
            if grid[pointy+1][pointx][0] == 0:
                return (2,0)
            elif (grid[pointy+1][pointx-1][0] == 0) and (grid[pointy+1][pointx+1][0] == 0) and canLeft and canRight:
                doing = coinflip()
                if doing:
                    return (1,0)
                else:
                    return (3,0)
            elif (grid[pointy+1][pointx-1][0] == 0) and canLeft:
                return (1,0)
            elif (grid[pointy+1][pointx+1][0] == 0) and canRight:
                return (3,0)
        else:
            if grid[pointy+1][pointx][0] in b:
                return (2,grid[pointy+1][pointx][0])
            elif (grid[pointy+1][pointx-1][0] in b) and (grid[pointy+1][pointx+1][0] in b) and canLeft and canRight:
                doing = coinflip()
                if doing:
                    return (1,grid[pointy+1][pointx-1][0])
                else:
                    return (3,grid[pointy+1][pointx+1][0])
            elif (grid[pointy+1][pointx-1][0] in b) and canLeft:
                return [1,grid[pointy+1][pointx-1][0]]
            elif (grid[pointy+1][pointx+1][0] in b) and canRight:
                return (3,grid[pointy+1][pointx+1][0])
    return [0,0] #To assure something gets returned if everything else is wrong

# Stone Physics ---------------------------------------------------
def stoneCheck(grid: list[list[bool]],pointx: int, pointy: int, floats: bool = False) -> tuple[bool,int]:
    #returns if something's under it
    b = (0,3)
    if pointy == len(grid) - 1:
        return [True,0]
    elif grid[pointy+1][pointx][0] != 0 and floats:
        return [True,0]
    elif grid[pointy+1][pointx][0] == 0 and floats:
        return [False,0]
    elif grid[pointy+1][pointx][0] in b and not floats:
        return [False,grid[pointy+1][pointx][0]]
    else:
        return [True,0]

def lrWanderCheck(grid: list[list[bool]],pointx: int,pointy: int, floaty: bool = False) -> tuple[bool]:
    canRight = True
    canLeft = True
    if pointx + 1 == len(grid[0]):
        canRight = False
    elif grid[pointy][pointx+1][0] != 0:
        canRight = False
    elif floaty and grid[pointy+1][pointx+1][0] != 0:
            canRight = False
    
    if pointx - 1 == -1:
        canLeft = False
    elif grid[pointy][pointx-1][0] != 0:
        canLeft = False
    elif floaty and grid[pointy+1][pointx-1][0] != 0:
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

def doStuff(plain):
    grid = deepcopy(plain)
    for a in range(len(plain)):
        for b in range(len(plain[0])):
            
            #Air
            if plain[a][b][0] == 0:
                continue
            
            #Sand
            elif plain[a][b][0] == 1:
                e = 1
                if random.randint(1,50) == 1:
                    if neighborCheck(grid,b,a,3):
                        e = 10
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    if e == 1:
                        continue
                    else:
                        grid[a][b] = [e,0]
                else:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b+(c[0]-2)] = [e,0]
            #Stone
            elif plain[a][b][0] == 2:
                e = 2
                if random.randint(1,1000) == 1:
                    if neighborCheck(grid,b,a,3):
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
                c = sandCheck(grid,b,a,True)
                if c[0] == 0:
                    d = lrWanderCheck(grid,b,a)
                    if not d[0]:
                        continue
                    else:
                        grid[a][b] = [0,0]
                        if d[1]:
                            grid[a][b+1] = [3,0]
                        else:
                            grid[a][b-1] = [3,0]

                else:
                    grid[a][b] = [0,0]
                    grid[a+1][b+(c[0]-2)] = [3,0]
            #Sugar
            elif plain[a][b][0] == 4:
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    continue
                else:
                    grid[a][b] = [c[1],0]
                    if c[0] == 2:
                        d = lrWanderCheck(grid,b,a, True)
                        if not d[0]:
                            grid[a+1][b] = [4,0]
                        else:
                            if d[1]:
                                grid[a+1][b+1] = [4,0]
                            else:
                                grid[a+1][b-1] = [4,0]
                    else:
                        grid[a+1][b+(c[0]-2)] = [4,0]
            #Wall
            elif plain[a][b][0] == 5:
                continue          
            #Dirt
            elif plain[a][b][0] == 6:
                e = 6
                if random.randint(1,100) == 1:
                    if neighborCheck(grid,b,a,3):
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
                c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [7,0]
            #Plant
            elif plain[a][b][0] == 8:
                c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [8,0]
            #Lava
            elif plain[a][b][0] == 9:
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    if random.randint(1,20) != 20:
                        continue
                    d = lrWanderCheck(grid,b,a)
                    if not d[0]:
                        continue
                    else:
                        grid[a][b] = [c[1],0]
                        if d[1]:
                            grid[a][b+1] = [9,0]
                        else:
                            grid[a][b-1] = [9,0]

                else:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b+(c[0]-2)] = [9,0]
            #Wet Sand
            elif plain[a][b][0] == 10:
                c = stoneCheck(grid,b,a)
                if not c[0]:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b] = [10,0]
            #Gravel
            elif plain[a][b][0] == 11:
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    continue
                else:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b+(c[0]-2)] = [11,0]
    return grid


live = False
alive = False
ice = False

print("Press the keys for the element!\n1: Sand  2: Stone  3: Water  4: Sugar  5: Wall\n6: Dirt  7: Mud  8: Plant  9: Lava")

fliposwitch = True
#this makes sure that the sand keeps going in a straight line

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
    
    clock.tick(60)

    if live:
        land = doStuff(land)


    if fliposwitch and alive:
        fliposwitch = False
    else:
        fliposwitch = True

    if (not tap) and fliposwitch:
        x = int(mousePos.x/landyx)
        y = int(mousePos.y/landyy)
        try:
            if ice:
                land[y][x] = [0,0]
            else:
                land[y][x] = [element,0]
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
    if not alive:
        live = False
    pygame.display.flip()