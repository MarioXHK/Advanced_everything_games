import pygame
from pygame import Vector2
import random
import math
import tools



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

#pickaxe variables-----------------------------------
picks = [tools.pickaxe(mousePos,0,45*r) for r in range(8)]


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
    
    

    #Sword movement------------------------------------
    for pickaxe in picks:
        pickaxe.cent = mousePos
        pickaxe.move()
    
    #Physics-------------------------------------------
    
    fire = False
    #Render--------------------------------------------
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(127,0,255),mousePos,20)
    for p in picks:
        p.draw(screen)

    pygame.display.flip()
pygame.quit()