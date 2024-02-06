cookies = 0

import pygame
import random
import clickers

from pygame import Vector2

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Cookie Clicker 2: Cookie Haven")


music = pygame.mixer.music.load("click.mp3")
pygame.mixer.music.play(-1)

cursoring = True

big_cookie = clickers.cookie("cc",Vector2(400,400),150)

held = False
tap = False
mousePos = (0,0)
tapped = False

print("Starting game")
while cursoring:
    #The input you have
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            cursoring = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not tapped:
                tap = True
                tapped = True
            held = True
        if event.type == pygame.MOUSEBUTTONUP:
            held = False
            tapped = False
        if event.type == pygame.MOUSEMOTION:
            mousePos = Vector2(event.pos)
    clock.tick(60)

    if big_cookie.tick(tap,mousePos):
        cookies += 1
        print("Clicked!")
    
    
    screen.fill((238,204,119))
    
    big_cookie.render(screen)

    pygame.display.flip()
    tap = False
pygame.quit()