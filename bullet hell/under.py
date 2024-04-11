import pygame
from pygame import Vector2
import random
import math
import arse
import npc

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
bulletMode = "anything"
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


#Dashing
dash = False
dashing = False
dashtimer = 0
dashdelay = 0
trytodash = False

thevariablethattellsmethatitshit = False

#your ship variables-----------------------------------
youcent = npc.ship(Vector2(500,500),20)
picks: list[arse.shield] = [arse.shield(youcent.pos.copy(),10,45*r,50,(255,0,0)) for r in range(8)]
gunfire = [arse.bullet(Vector2(-500,-500)) for i in range(1000)]
dashblobs = [[Vector2(0,0),0] for j in range(15)]

#enemy ship variables
theircent = [npc.ship(Vector2(50*g,200)) for g in range(1,20)]
bullets = [arse.bullet(theircent[0].pos.copy()) for i in range(1000)]

 


while firing:
    clock.tick(60)
    thevariablethattellsmethatitshit = False
    trytodash = False
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
                elif event.key == pygame.K_DOWN:
                    keys[downK]=True
                elif event.key == pygame.K_UP:
                    keys[upK]=True
                elif event.key == pygame.K_RIGHT:
                    keys[rightK]=True
                elif event.key == pygame.K_SPACE:
                    keys[spaceK]=True
                elif event.key == pygame.K_w:
                    keys[wK]=True
                elif event.key == pygame.K_a:
                    keys[aK]=True
                elif event.key == pygame.K_s:
                    keys[sK]=True
                elif event.key == pygame.K_d:
                    keys[dK]=True
                elif event.key == pygame.K_d:
                    keys[dK]=True
                elif not dash and event.key == pygame.K_LSHIFT:
                    trytodash = True
                elif event.key == pygame.K_LCTRL:
                    thevariablethattellsmethatitshit=True
                    
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
                elif event.key == pygame.K_w:
                    keys[wK]=False
                elif event.key == pygame.K_a:
                    keys[aK]=False
                elif event.key == pygame.K_s:
                    keys[sK]=False
                elif event.key == pygame.K_d:
                    keys[dK]=False
    
    
    
    

    #Your movement------------------------------------
    
    if trytodash and (True in keys[0:4]):
        dashtimer = 20
        dash = True
        dashing = True

    if dashtimer % 5 == 0:
        dashblobs[dashtimer // 5][0] = youcent.pos.copy()
        dashblobs[dashtimer // 5][1] = 20

    if dashing:
        dashtimer -= 1
        if dashtimer <= 0 or not (True in keys[0:4]):
            dashing = False
            dashdelay = 40+dashtimer
            dashtimer = 0
    if dash and dashtimer <= 0:
        dashdelay -= 1
        if dashdelay <= 0:
            dash = False

    if youcent.alive:
        if keys[rightK] and youcent.pos.x < 974:
            youcent.pos.x += 4 + dashtimer / 2
        if keys[leftK] and youcent.pos.x > 50:
            youcent.pos.x -= 4 + dashtimer / 2
        if keys[upK] and youcent.pos.y > 50:
            youcent.pos.y -= 4 + dashtimer / 2
        if keys[downK] and youcent.pos.y < 718:
            youcent.pos.y += 4 + dashtimer / 2
    
    for shield in picks:
        if not shield.hp <= 0:
            for h in theircent:
                if not h.alive:
                    continue
                if Vector2(shield.rotPos).distance_to(h.pos) < shield.size + h.size:
                    shield.hp -= 1
                    h.hp -= 1
                    break
        if youcent.alive:
            shield.cent = youcent.pos
        else:
            shield.reach += 2


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
            deadbullet = False
            if bull.id == 10:
                    bull.xyvel.x += math.cos(zigtime)/2
            bull.move()
            for h in theircent:
                if not h.alive:
                    continue
                if bull.pos.distance_to(h.pos) < bull.size + h.size:
                    deadbullet = True
                    h.hp -= 1
                    break
            if deadbullet:
                if bull.id > 1 and bull.id < 10:
                    splitters += 1
                    splitme = True
                    for _ in range(2):
                        split.append(bull.id-1)
                        myangle.append(bull.angle)
                        mypos.append(bull.pos)
                        myvel.append(bull.vel*0.9)
                bull.id = 0
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
            if keys[spaceK] and not (shot or dashing or delaying):
                
                
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
                bull.pos = youcent.pos.copy()
    
    shotter = False

    for bull in bullets:
        if bull.id != 0:
            deadbullet = False
            bull.move()
            if not youcent.alive:
                continue
            if bull.pos.distance_to(youcent.pos) < bull.size + youcent.size:
                deadbullet = True
                youcent.hp -= 1
            else:
                for h in picks:
                    if h.hp <= 0:
                        continue
                    if bull.pos.distance_to(h.rotPos) < bull.size + h.size:
                        deadbullet = True
                        h.hp -= 1
            if deadbullet:
                if bull.id > 1 and bull.id < 10:
                    splitters += 1
                    splitme = True
                    for _ in range(2):
                        split.append(bull.id-1)
                        myangle.append(bull.angle)
                        mypos.append(bull.pos)
                        myvel.append(bull.vel*0.9)
                bull.id = 0
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
            if keys[spaceK] and not (shotter or dashing or delaying):
                
                
                bull.vel = dbspeed
                shotted += 1
                delay = delayed
                bull.id = 1
                
                bull.turn(0-angel)
                shotter = True
                bull.pos = theircent[0].pos.copy()

    youcent.dieplease()
    #The Enemy Physics-------------------------------------------
    for g in theircent:
        g.move()
        g.dieplease()
    #Render--------------------------------------------
    screen.fill((0,0,0))
    if not youcent.dead:
        for b in dashblobs:
            if b[1] <= 0:
                continue
            b[1] -= 1
            pygame.draw.circle(screen,(0,b[1]*10,b[1]*10),b[0],20)
    if dash:
        if dashing:
            youcent.color = (0,255,255)
        else:
            youcent.color = (0,0,255)
    else:
        youcent.color = (127,0,255)
    
    if not youcent.dead:
        youcent.draw(screen)
    
    for g in theircent:
        if not g.dead:
            g.draw(screen)
    
    for b in gunfire:
        if b.id == 0:
            continue
        b.draw(screen)
    for b in bullets:
        if b.id == 0:
            continue
        b.draw(screen)
    for p in picks:
        p.draw(screen)

    pygame.display.flip()
pygame.quit()