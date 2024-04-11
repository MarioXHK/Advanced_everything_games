from buttons import button
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.color import Color
import pygame
import random
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800)) #create game screen
pygame.display.set_caption("Baby gaem") #window title
fishy = True

fire = False
tap = False
mousePos = Vector2(0,0)
tapped = False

dragme = button(Color(255,0,0),Rect(300,300,400,300))

while fishy:
    #The little input you have
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            fishy = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not tapped:
                tap = True
                tapped = True
            fire = True
        if event.type == pygame.MOUSEBUTTONUP:
            fire = False
            tapped = False
        if event.type == pygame.MOUSEMOTION:
            mousePos = Vector2(event.pos)
    
    clock.tick(60)

    dragme.tick(fire,mousePos)

    dragme.drag(mousePos)

    
    screen.fill((0,0,0))
    dragme.render(screen)

    pygame.display.flip()
    tap = False

pygame.quit()