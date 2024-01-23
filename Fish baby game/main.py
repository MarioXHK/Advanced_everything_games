from buttons import button
from fash import fish
import pygame
import random
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800)) #create game screen
pygame.display.set_caption("Baby gaem") #window title
fishy = True

fire = False
tap = False
mousePos = (0,0)

dragme = button((255,0,0),[300,300,400,300])

fishme = fish((0,0,255),[200,200,200,200])
fishme.aftint()

fishes = [fish((random.randint(0,255),random.randint(0,255),random.randint(0,255)),[200,200,150,150]) for a in range(100)]
for i in fishes:
    i.aftint()
while fishy:
    #The little input you have
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            fishy = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            fire = True
        if event.type == pygame.MOUSEBUTTONUP:
            fire = False
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
    
    #clock.tick(120)#This is too slow u_u

    dragme.tick(fire,mousePos)
    fishme.tick(fire,mousePos)

    fishme.swim()

    dragme.drag(mousePos)
    fishme.drag(mousePos)

    screen.fill((0,0,0))
    dragme.render(screen)
    fishme.render(screen)

    for f in fishes:
        f.tick(fire,mousePos)
        f.swim()
        f.drag(mousePos)
        f.render(screen)

    pygame.display.flip()

pygame.quit()