from buttons import button
from fash import fish
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

pond = button(Color(0,255,255),Rect(0,350,250,250))


fishes = [fish(Color(0,0,255),Rect(200,200,200,200))]

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
    
    #clock.tick(120)#This is too slow u_u

    dragme.tick(fire,mousePos)

    dragme.drag(mousePos)

    if pond.tick(tap,mousePos):
        sizes = [random.randint(100,300),random.randint(100,200)]
        fishes.append(fish(Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)),Rect(mousePos[0]-sizes[0]/2,mousePos[1]-sizes[1]/2,sizes[0],sizes[1])))

    screen.fill((0,0,0))
    dragme.render(screen)
    pond.render(screen)
    for f in fishes:
        f.tick(fire,mousePos)
        f.swim()
        f.drag(mousePos)
        f.render(screen)

    pygame.display.flip()
    tap = False

pygame.quit()