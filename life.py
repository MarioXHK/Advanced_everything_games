import pygame
from pygame import Vector2
from copy import deepcopy

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Life rn")
breaking=True
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

#mouse variables--------------------------------
mousePos = Vector2(0,0)
fire = False
tap = True

land = [[False for _ in range(100)] for i in range(100)]


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

def doLife(plain):
    grid = deepcopy(plain)
    for a in range(len(plain)):
        for b in range(len(plain[0])):
            c = neighborCount(plain,b,a)
            if c < 2 or c > 3:
                grid[a][b] = False
            if c == 3:
                grid[a][b] = True
    return grid


live = False
alive = False
ice = False

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
                land = [[False for _ in range(100)] for i in range(100)]
            if event.key == pygame.K_RALT:
                land = [[True for _ in range(100)] for i in range(100)]
    
    clock.tick(60)

    if live:
        land = doLife(land)

    if not tap:
        x = int(mousePos.x/10)
        y = int(mousePos.y/10)
        if ice:
            land[y][x] = False
        else:
            land[y][x] = True
        #land[x][y] = True

    fire = False
    screen.fill((120,120,120))
    for i in range(100):
        for j in range(100):
            e = neighborCount(land,j,i)
            d += e
            pygame.draw.rect(screen,(30*e,0,0),(j*10,i*10,10,10))
            if land[i][j]:
                pygame.draw.rect(screen,(255,255,255),(j*10,i*10,10,10),3)
            else:
                pygame.draw.rect(screen,(0,0,0),(j*10,i*10,10,10),3)
    print(d)
    if not alive:
        live = False
    pygame.display.flip()