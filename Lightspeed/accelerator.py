print("Hello, World!")
import pygame
import random
from pygame import Vector2
from particles import particle
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Particle Simulation or whatever")

print("Giving the mouse some cheese")
fire = False
tap = False
mousePos = (0,0)
tapped = False

particling = []
for i in range(1):
    particling.append(particle())

particling[0].vel = 100

#particling = [particle(Vector2(500,500),20,Vector2(-0.1,0),5,False)]

aCERN = True

while aCERN:
    #The input you have
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            aCERN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not tapped:
                tap = True
                tapped = True
            fire = True
        if event.type == pygame.MOUSEBUTTONUP:
            fire = False
            tapped = False
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos

    for i in particling:
        i.tick(particling)

    screen.fill((0,0,0))

    for i in particling:
        i.see(screen)

    pygame.display.flip()
    tap = False