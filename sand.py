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

landx = 50
landy = 50
land = [[[0,0] for _ in range(landx)] for i in range(landy)]
landyx = (1000/landx)
landyy = (1000/landy)

element = 1
werealsodoinglife = False
brushsize = 0

def coinflip() -> bool:
    return bool(random.getrandbits(1))

def neighborCount(grid: list[list[bool]],pointx: int, pointy: int, checker: list[int] | tuple[int]) -> int:
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

def neighborCheck(grid: list[list[bool]],pointx: int, pointy: int, checker: list[int] | tuple[int]) -> bool:
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

# Sand Physics ---------------------------------------------------
def sandCheck(grid: list[list[bool]],pointx: int, pointy: int, floats: bool = False, reverse: bool = False, gas: bool = False) -> tuple[int]:
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
            b = [0,1,3,4,6,8,9,11,15]
        else:
            b = [0,3,15]
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
def stoneCheck(grid: list[list[bool]],pointx: int, pointy: int, floats: bool = False, reverse: bool = False, gas: bool = False) -> tuple[bool,int]:
    #returns if something's under it (or above it if in reverse)
    l = 1
    if reverse:
        l = -1
    b = (0,0)
    if not floats:
        if gas:
            b = [0,1,3,4,6,8,9,11,15]
        else:
            b = [0,3,15]
        if grid[pointy][pointx][0] in b:
            b.remove(grid[pointy][pointx][0])
        b = tuple(b)
    if (pointy == len(grid) - 1 and not reverse) or (pointy == 0 and reverse):
        return [True,0]
    elif grid[pointy+l][pointx][0] in b:
        return [False,grid[pointy+l][pointx][0]]
    else:
        return [True,0]

def lrWanderCheck(grid: list[list[bool]],pointx: int,pointy: int, floaty: bool = False, waterlike: bool = False, reverse: bool = False) -> tuple[bool,bool,int]:
    b = (0,0)
    if waterlike:
        b = [0,3,15]
        if grid[pointy][pointx][0] in b:
            b.remove(grid[pointy][pointx][0])
        b = tuple(b)
    l = 1
    if reverse:
        l = -1
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

def udWanderCheck(grid: list[list[bool]],pointx: int,pointy: int, waterlike: bool = False) -> tuple[bool,bool,int]:
    b = (0,0)
    if waterlike:
        b = [3,15]
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

# The thing that makes all of this possible, it's DOSTUFF!!!!

def doStuff(plain):
    t = 0
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
                if random.randint(1,50) == 1:
                    if neighborCheck(grid,b,a,(3,15)):
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
                if random.randint(1,1000) == 1:
                    if neighborCheck(grid,b,a,[3]):
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
                if neighborCheck(plain,b,a,[9]):
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
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    if random.randint(1,100) == 1:
                        if neighborCheck(grid,b,a,[3]):
                            e = 15
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
                if neighborCheck(plain,b,a,(3,15)):
                    e = 12
                c = sandCheck(grid,b,a)
                if c[0] == 0:
                    if random.randint(1,20) != 20:
                        if e == 9:
                            continue
                        else:
                            grid[a][b] = [e,0]
                    d = lrWanderCheck(grid,b,a)
                    if not d[0]:
                        if e == 9:
                            continue
                        else:
                            grid[a][b] = [e,0]
                    else:
                        grid[a][b] = [c[1],0]
                        if d[1]:
                            grid[a][b+1] = [e,0]
                        else:
                            grid[a][b-1] = [e,0]

                else:
                    grid[a][b] = [c[1],0]
                    grid[a+1][b+(c[0]-2)] = [e,0]
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
                if random.randint(1,10) == 1 and t > 0:
                    t -= 1
                if t <= 0 and random.randint(1,100):
                    e = 16
                c = sandCheck(grid,b,a,False,True,True)
                d = lrWanderCheck(grid,b,a)
                if c[0] == 0:
                    if not d[0]:
                        if e == 13:
                            continue
                        else:
                           grid[a][b] = [e,t] 
                    else:
                        grid[a][b] = [d[2],0]

                        if d[1]:
                            grid[a][b+1] = [e,t]
                        else:
                            grid[a][b-1] = [e,t]
                else:
                    grid[a][b] = [c[1],t]
                    if c[0] == 2:
                        if not d[0]:
                            grid[a-1][b] = [e,t]
                        else:
                            if d[1]:
                                grid[a-1][b+1] = [e,t]
                            else:
                                grid[a-1][b-1] = [e,t]
                    else:
                        grid[a-1][b+(c[0]-2)] = [e,t]
                    
                    
                    
            #Sugar Water
            elif plain[a][b][0] == 15:
                if neighborCheck(plain,b,a,[9]):
                    e = 4
                c = sandCheck(grid,b,a,True)
                if c[0] == 0:
                    d = lrWanderCheck(grid,b,a,False,True)
                    if not d[0]:
                        d = udWanderCheck(grid,b,a,True)
                        if not d[0]:
                            continue
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
                if random.randint(1,500) == 1:
                    e = 3
                if random.randint(1,20) == 1:
                    if random.randint(1,4) != 1:
                        d = lrWanderCheck(grid,b,a, True)
                        if not d[0]:
                            if e == 16:
                                continue
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
                                continue
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
            
            
            #Life
            elif plain[a][b][0] == 28:
                if werealsodoinglife:
                    l = neighborCount(plain,b,a,28)
                    if l < 2 or l > 3:
                        grid[a][b] = [0,0]
                else:
                    grid[a][b] = [random.randint(0,9),0]
    return grid


live = False
alive = False
ice = False

print("Press the keys for the element!\n1: Sand  2: Stone  3: Water  4: Sugar  5: Wall\n6: Dirt  7: Mud  8: Plant  9: Lava  0: Eraser")
print("Q: Wet sand  W: Gravel  E: Obsidian  R: Steam\nT: Glass  Y: Sugar Water  U: Cloud")
print("L: Life particle (think the game of life) (WIP)")


fliposwitch = True
#this makes sure that the sand keeps going in a straight line while placing it when it's active

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
            elif event.key == pygame.K_UP:
                brushsize += 1
                print("brush size is now", (brushsize*2-1))
            elif event.key == pygame.K_DOWN:
                if 1 < brushsize:
                    brushsize -= 1
                    print("brush size is now", (brushsize*2-1))
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
            
            elif event.key == pygame.K_l:
                element = 28
    
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
        for l in range(0-brushsize,1+brushsize):
            for m in range(0-brushsize,1+brushsize):
                try:
                    if ice:
                        land[y+l][x+m] = [0,0]
                    else:
                        land[y+l][x+m] = [element,0]
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
                pygame.draw.rect(screen,(230,90,60),(j*landyx,i*landyy,landyx,landyy))
            
            elif land[i][j][0] == 28:
                pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy))
    if not alive:
        live = False
    pygame.display.flip()