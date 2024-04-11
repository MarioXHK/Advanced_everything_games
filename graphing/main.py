from buttons import button
from buttons import graphNode
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.color import Color
import pygame
import random
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800)) #create game screen
pygame.display.set_caption("Baby gaem") #window title
graphingCalculator = True

fire = False
tap = False
mousePos = Vector2(0,0)
tapped = False
taken = None
connect = False
connecting = False
connectTo = 0
didConnect = False

dragme:list[graphNode] = []

while graphingCalculator:
    #The little input you have
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            graphingCalculator = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not tapped:
                    tap = True
                    tapped = True
                fire = True
            elif event.button == 3:
                if not didConnect:
                    didConnect = True
                    connect = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                fire = False
                tapped = False
                taken = None
            elif event.button == 3:
                didConnect = False
        if event.type == pygame.MOUSEMOTION:
            mousePos = Vector2(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dragme.append(graphNode(Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)),Vector2(random.randint(0,800),random.randint(0,800)),25,Color(255,255,255),str(len(dragme))))
            elif event.key == pygame.K_LCTRL:
                for i in range(10):
                    dragme.append(graphNode(Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)),Vector2(random.randint(0,800),random.randint(0,800)),25,Color(255,255,255),str(len(dragme))))
    
    clock.tick(60)
    for n in dragme:
        if taken == None and n.tick(fire,mousePos):
            #Dragging nodes around via left click
            taken = n.color
        elif n.basicTick(connect,mousePos):
            #Connecting nodes to eachother via right click
            if not connecting:
                print("Connecting started!")
                connecting = True
                connectTo = dragme.index(n)
            else:
                connecting = False
                dragme[connectTo].connections.append(dragme.index(n))
                print("Connected", connectTo, "to", dragme.index(n))
        if n.color == taken:
            n.drag(mousePos)

    screen.fill((0,0,0))
    for n in dragme:
        if len(n.connections) > 0:
            for c in n.connections:
                if c == dragme.index(n):
                    pygame.draw.circle(screen,n.color,n.pos,n.rad*1.5,8)
                elif dragme.index(n) in dragme[c].connections:
                    pygame.draw.line(screen,(255,255,255),n.pos,dragme[c].pos,5)
                else:
                    pygame.draw.line(screen,n.color,n.pos,dragme[c].pos,5)
        n.render(screen)

    pygame.display.flip()
    tap = False
    connect = False
pygame.quit()