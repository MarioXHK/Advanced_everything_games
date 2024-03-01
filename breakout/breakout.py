import pygame
import bricked
from bricked import brick

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Breakout. I seriously haven't done this before")
breaking=True
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

mario: list[brick] = []

for i in range(10):
    for j in range(15):
        mario.append(brick((100*i,50*j,100,50)))

mousePos = 0
# We only need the Mouse's X for this game!

while breaking:
    for event in pygame.event.get(): #Event Queue (or whatever it's called)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            breaking = False
    
    clock.tick(60)

    screen.fill((0,0,0))
    for p in mario:
        p.draw(screen)

    pygame.display.flip()