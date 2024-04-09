import pygame
from pygame import Vector2
import random
import math
import arse



#Required pygame things------------------------
pygame.init()
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Minecraft but not really, it's just some flash game I found that's fun in principle")
crafting=True
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

#mouse variables--------------------------------
mousePos = Vector2(0,0)
fire = False
tap = True
coins: int = 0

#keyboard variables--------------------------------
contType = "arrow"
keys = [False,False,False,False,False]
upK = 0
downK = 1
leftK = 2
rightK = 3
spaceK = 4
rotation = 0
#pickaxe variables-----------------------------------
youcent = Vector2(500,500)
picks: list[arse.orbiter] = [arse.orbiter(youcent,45*r) for r in range(8)]
gunfire = [arse.bullet(Vector2(-500,-500)) for i in range(100)]


while crafting:
    clock.tick(60)
    #Input--------------------------------------------
    for event in pygame.event.get(): #Event Queue (or whatever it's called)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            crafting = False
        if event.type == pygame.MOUSEBUTTONDOWN and tap:
            fire = True
            tap = False
        if event.type == pygame.MOUSEBUTTONUP:
            tap = True
        if event.type == pygame.MOUSEMOTION:
            mousePos = Vector2(event.pos)
        if contType == "arrow":
            if event.type == pygame.KEYDOWN: #keyboard input
                if event.key == pygame.K_LEFT:
                    keys[leftK]=True
                elif event.key == pygame.K_DOWN:
                    keys[downK]=True
                elif event.key == pygame.K_UP:
                    keys[upK]=True
                elif event.key == pygame.K_RIGHT:
                    keys[rightK]=True
                elif event.key == pygame.K_SPACE:
                    keys[spaceK]=True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys[leftK]=False
                elif event.key == pygame.K_UP:
                    keys[upK]=False
                elif event.key == pygame.K_RIGHT:
                    keys[rightK]=False
                elif event.key == pygame.K_DOWN:
                    keys[downK]=False
                elif event.key == pygame.K_SPACE:
                    keys[spaceK]=False
    
    
    
    

    #Sword movement------------------------------------
    
    if keys[rightK]:
        youcent.x += 4
    if keys[leftK]:
        youcent.x -= 4
    if keys[upK]:
        youcent.y -= 4
    if keys[downK]:
        youcent.y += 4
    
    for shield in picks:
        shield.cent = youcent


        shield.move()
    
    for bull in gunfire:
        #bull's short for bullets. I'm doing horrid shorteninghs
        if keys[spaceK] and bull.id == 0:
            bull.id = 1
            bull.pos = youcent.copy()
            break
        else:
            bull.move()


    #Physics-------------------------------------------
    
    fire = False
    #Render--------------------------------------------
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(127,0,255),youcent,20)
    for b in gunfire:
        if b.id == 0:
            continue
        b.draw(screen)
    for p in picks:
        p.draw(screen)

    pygame.display.flip()
pygame.quit()