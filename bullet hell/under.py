import pygame
from pygame import Vector2
import random
import math
import arse

firing = True

#Required pygame things------------------------
pygame.init()
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Bullets and junk")
crafting=True
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

#Bullet Variables-----------------

delay = 0
delayed = 5
angel = -90
rotation = 0
bulletMode = "squiggle"
umbratime = 0
dbspeed = 5
bspeed = dbspeed
zigtime = 0

#mouse variables--------------------------------
mousePos = Vector2(0,0)
fire = False
tap = True
coins: int = 0

#keyboard variables--------------------------------
contType = "arrow"
keys = [False,False,False,False,False,False,False,False,False]
upK = 0
downK = 1
leftK = 2
rightK = 3
spaceK = 4
wK = 5
aK = 6
sK = 7
dK = 8

thevariablethattellsmethatitshit = False

#pickaxe variables-----------------------------------
youcent = Vector2(500,500)
picks: list[arse.orbiter] = [arse.orbiter(youcent,45*r) for r in range(8)]
gunfire = [arse.bullet(Vector2(-500,-500)) for i in range(1000)]


while firing:
    clock.tick(60)
    thevariablethattellsmethatitshit = False
    #Input--------------------------------------------
    for event in pygame.event.get(): #Event Queue (or whatever it's called)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            firing = False
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
                if event.key == pygame.K_DOWN:
                    keys[downK]=True
                if event.key == pygame.K_UP:
                    keys[upK]=True
                if event.key == pygame.K_RIGHT:
                    keys[rightK]=True
                if event.key == pygame.K_SPACE:
                    keys[spaceK]=True
                if event.key == pygame.K_w:
                    keys[wK]=True
                if event.key == pygame.K_a:
                    keys[aK]=True
                if event.key == pygame.K_s:
                    keys[sK]=True
                if event.key == pygame.K_d:
                    keys[dK]=True
                if event.key == pygame.K_LCTRL:
                    thevariablethattellsmethatitshit=True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys[leftK]=False
                if event.key == pygame.K_UP:
                    keys[upK]=False
                if event.key == pygame.K_RIGHT:
                    keys[rightK]=False
                if event.key == pygame.K_DOWN:
                    keys[downK]=False
                if event.key == pygame.K_SPACE:
                    keys[spaceK]=False
                if event.key == pygame.K_w:
                    keys[wK]=False
                if event.key == pygame.K_a:
                    keys[aK]=False
                if event.key == pygame.K_s:
                    keys[sK]=False
                if event.key == pygame.K_d:
                    keys[dK]=False
    
    
    
    

    #Sword movement------------------------------------
    
    if keys[rightK] and youcent.x < 974:
        youcent.x += 4
    if keys[leftK] and youcent.x > 50:
        youcent.x -= 4
    if keys[upK] and youcent.y > 50:
        youcent.y -= 4
    if keys[downK] and youcent.y < 718:
        youcent.y += 4
    
    for shield in picks:
        shield.cent = youcent


        shield.move()
    shot = False
    

    #Bullets in this bullet hell---------------------------------

    if keys[wK]:
        if keys[aK]:
            angel = 225
        elif keys[dK]:
            angel = 315
        else:
            angel = 270
    elif keys[aK]:
        if keys[sK]:
            angel = 135
        else:
            angel = 180
    elif keys[sK]:
        if keys[dK]:
            angel = 45
        else:
            angel = 90
    elif keys[dK]:
        angel = 0


    if delay > 0:
        delay -= 1
    delaying:bool = (delay > 0)
    shotted = 0
    umbratime += 1
    splitme = False
    myangle = []
    mypos = []
    splited = 0
    split = []
    myvel = []
    splitters = 0
    zigtime += 0.1
    if umbratime < 360:
        umbratime -= 360
    if zigtime < 360:
        umbratime -= 360
    for bull in gunfire:
        #bull's short for bullets. I'm doing horrid shorteninghs
        if bull.id != 0:
            bull.move()
            if thevariablethattellsmethatitshit and bull.id > 1 and bull.id < 10:
                splitters += 1
                splitme = True
                for _ in range(2):
                    split.append(bull.id-1)
                    myangle.append(bull.angle)
                    mypos.append(bull.pos)
                    myvel.append(bull.vel*0.9)
                bull.id = 0
            elif bull.id == 10:
                bull.xyvel.x += math.cos(zigtime)/2
        elif splitme:
            splited += 1
            bull.vel = myvel.pop()
            if splited % 2 == 1:
                bull.turn(myangle.pop()-5)
            else:
                bull.turn(myangle.pop()+5)
            bull.id = split.pop()
            bull.pos = mypos.pop().copy()
            
            if splited >= splitters*2:
                splitme = False
        else:
            if keys[spaceK] and not (shot or delaying):
                
                
                bull.vel = dbspeed
                shotted += 1
                delay = delayed
                bull.id = 1
                if bulletMode == "multishot":
                    if shotted == 1:
                        bull.turn(angel)
                    if shotted == 2:
                        bull.turn(angel+10)
                    if shotted >= 3:
                        bull.turn(angel-10)
                        shot = True
                elif bulletMode == "umbrella":
                    bull.turn(shotted*22.5+umbratime)
                    if shotted >= 16:
                        shot = True
                elif bulletMode == "shotgun":
                    bull.vel = dbspeed + random.random()*2
                    bull.turn(angel+random.randint(-15,15))
                    if shotted >= random.randint(5,8):
                        shot = True
                elif bulletMode == "splitshot":
                    bull.id = 2
                    bull.turn(angel)
                    shot = True
                elif bulletMode == "squiggle":
                    bull.xyvel = Vector2(0,(0-dbspeed))
                    bull.id = 10
                    shot = True
                else:
                    bull.turn(angel)
                    shot = True
                bull.pos = youcent.copy()
        


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