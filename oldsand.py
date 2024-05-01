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


def neighborCount(grid: list[list[bool]],pointx: int, pointy: int) -> int:
    count = 0
    # grid = deepcopy(plain) #I'M NOT DOING THIS STUPID LINKED LIST AGAIN, PYTHON!
    for l in range(-1,2):
        for m in range(-1,2):
            if (l,m) == (0,0):
                continue
            ex = pointx+m
            why = pointy+l
            if ex == len(grid[0]):
                ex = 0
            elif ex == -1:
                ex = len(grid[0]) - 1
            if why == len(grid):
                why = 0
            elif why == -1:
                why = len(grid) - 1

            if grid[why][ex]:
                count += 1

    return count

def sandCheck(grid: list[list[bool]],pointx: int, pointy: int) -> int:
    if pointy == len(grid) - 1:
        return 0
    under = True
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

        if grid[pointy+1][ex][0] == 0:
            under = False
    if under:
        return 0
    else:
        if grid[pointy+1][pointx][0] == 0:
            return 2
        elif (grid[pointy+1][pointx-1][0] == 0) and (grid[pointy+1][pointx+1][0] == 0) and canLeft and canRight:
            doing = coinflip()
            if doing:
                return 1
            else:
                return 3
        elif (grid[pointy+1][pointx-1][0] == 0) and canLeft:
            return 1
        elif (grid[pointy+1][pointx+1][0] == 0) and canRight:
            return 3
    return 0 #To assure something gets returned if everything else is wrong

def stoneCheck(grid: list[list[bool]],pointx: int, pointy: int) -> bool:
    #returns if something's under it
    if pointy == len(grid) - 1:
        return True
    elif grid[pointy+1][pointx][0] != 0:
        return True
    return False

def fluidCheck(grid: list[list[bool]],pointx: int,pointy: int) -> tuple[bool]:
    canRight = True
    canLeft = True
    if pointx + 1 == len(grid[0]):
        canRight = False
    elif grid[pointy][pointx+1][0] != 1:
        canRight = False
    if pointx - 1 == -1:
        canLeft = False
    elif grid[pointy][pointx-1][0] != 1:
        canLeft = False
    if not(canRight or canLeft):
        return [False,False]
    if coinflip():
        if not canRight:
            return [True,False]
        elif not canLeft:
            return [True,True]
        else:
            return [True,coinflip()]
    return [False,False]

def doStuff(plain):
    grid = deepcopy(plain)
    for a in range(len(plain)):
        for b in range(len(plain[0])):
            if plain[a][b][0] == 0:
                continue
            elif plain[a][b][0] == 1:
                c = sandCheck(plain,b,a)
                if c == 0:
                    continue
                else:
                    grid[a][b] = [0,0]
                    grid[a+1][b+(c-2)] = [1,0]
            elif plain[a][b][0] == 2:
                if not stoneCheck(plain,b,a):
                    grid[a][b] = [0,0]
                    grid[a+1][b] = [2,0]
            elif plain[a][b][0] == 3:
                c = sandCheck(plain,b,a)
                grid[a][b] = [0,0]
                f = 0
                if c != 0:
                    f = 1
                d = fluidCheck(plain,b,a)
                e = 0
                if d[0]:
                    if d[1]:
                        e = 1
                    else:
                        e = -1
                grid[a+f][b+(c-2)+e] = [3,0]
    return grid


live = False
alive = False
ice = False

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
            if event.key == pygame.K_0:
                element = 0
            if event.key == pygame.K_1:
                element = 1
            if event.key == pygame.K_2:
                element = 2
            if event.key == pygame.K_3:
                element = 3

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
    if not alive:
        live = False
    pygame.display.flip()