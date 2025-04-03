uniqueElements = 103

import sys
print(sys.executable)
#Libraries used: Pygame, Pillow

aSeriousError = False
killOrder = 100
#Can someone please tell me how to give more resources to this app so I can throttle it and have a smooth 60 fps while my computer combusts into flames
#Some optimization help would be nice too
showfps = False
#the setting that controls if you'd like to do life or not (Experimental sorta)

oob = 0
import traceback
import os

import pygame
from pygame import Vector2
from pygame.rect import Rect
from pygame.color import Color
from copy import deepcopy
import random
import time
import foreverglobals
import buttons

#I caved (It was a good thing)
from physics import coinflip
from physics import checkEverywhere
import doing
from drawing import drawStuff
from inputkeys import keyboard
from drawing import drawLessStuff
from imageLoad import loadImage

pygame.font.init()
font = (
    pygame.font.Font("PressStart2P.ttf", 30),
    pygame.font.SysFont('Comic Sans MS', 30),
    pygame.font.SysFont('Comic Sans MS', 15),
    pygame.font.SysFont('Comic Sans MS', 20),
    pygame.font.Font("PressStart2P.ttf", 24),
    pygame.font.Font("PressStart2P.ttf", 18),
    pygame.font.Font("PressStart2P.ttf", 12)
    )

texts = ()

doaflip = True

rememberme = False

#Save folder things

usesavefolder = True
if usesavefolder:
    print("Using the sandsaves folder as a save directory")
    try:
        os.mkdir('sandsaves')
        print("sandsave folder made automatically.")
    except:
        print("sandsave folder already in place (yippee!)")

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Sandbox game!")
playingMySandbox=True
clock = pygame.time.Clock()

#mouse variables--------------------------------
mousePos = Vector2(0,0)
fire = False
tap = True

wheeled = False
wheel = 0

#Element Variables

preEl = 1
element = 1
brushSize = 0

testbutton = buttons.button(Color(255,255,0),Rect(200,200,100,100),None,"Test!")

werealsodoinglife = False
eyeDropper = False
dither = False
elementary = False
elements = []
mirror = False

doingafilething = False
anElement = ""

gamma = 100
smoothColors = True

elementNameText = font[0].render("Sand",1,Color(255,255,255))
elementText = [
    font[6].render("Sand",1,Color(255,255,255))
            ]

screenx: int = 500
screeny: int = 500

landx: int = 50
landy: int = 50

setup = True
filename = ""


arrowkeys = [False,False,False,False]
delayme = [6,10]
changeScreen = True
shiftKey = False
dontgointothenegatives = [False,False]
wasdkeys = [False,False,False,False]

unlockedElements = [0,1,2,3,4,5,6,7,8,9]


live = False
alive = False
ice = False
fps = 60

undoList = []
redoList = []
pickAnElement = False

tutorial = 1
tutorialprogress = 0
gameState = "title"
loadState = gameState
actualGame = gameState
games = ("title","sandbox","terrarium")
responded = False
fliposwitch = True

yesbutton = buttons.button(Color(0,255,0),Rect(0,0,100,70),None,"Yes")
nobutton = buttons.button(Color(255,0,0),Rect(0,0,100,70),None,"No")
wannaBreak = False

playButton = buttons.button(Color(255,255,255),Rect(200,350,200,50),Color(255,255,0),"Play",Color(0,0,0),0)


createButton = buttons.button(Color(255,255,0),Rect(50,250,200,50),Color(0,0,0),"Create",Color(0,0,0),0)


loadButton = buttons.button(Color(255,255,0),Rect(350,250,200,50),Color(0,0,0),"Load",Color(0,0,0),0)


sandboxButton = buttons.button(Color(255,255,0),Rect(50,450,200,50),Color(0,0,0),"Sandbox",Color(0,0,0),0)


terrariumButton = buttons.button(Color(0,0,255),Rect(350,450,200,50),Color(0,0,0),"Terrarium",Color(255,255,255),4)


continueButton = buttons.button(Color(255,255,128),Rect(200,350,200,50),Color(0,0,0),"Continue",Color(0,0,0),4)


titleState = 0
#Title state has a few values for what it is:
#0: Very start of the game, only the play button The options button can be selected in every other state
#1: Gamemode Selection, selects weather to be a sandbox, or terrarium. There's also the continue button that puts you back where you last were in that session
#2: Sandbox Gamemode
#3: Terrarium Gamemode

titleLand = deepcopy(foreverglobals.titleScreenSandbox)
appendKey = ""
sandBoxed = False

eColumns = 6

elementButtons = []
for why in range(len(foreverglobals.elements)//eColumns):
    for ex in range(eColumns):
        if why*eColumns + ex < len(foreverglobals.elements):
            buton = foreverglobals.elements[why*eColumns + ex]
            elementButtons.append(buttons.elButton(foreverglobals.elements[why*eColumns + ex].id,Color(10,10,10),buton.color,Rect(40,40,40,40),Color(50,50,50),buton.mColors))
            
        else:
            elementButtons.append(buttons.elButton(0,Color(0,0,0),Color(0,0,0),Rect(40,40,40,40),Color(40,40,40)))

buttonYOffset = 0
wheelv = 0
aboutToDie = False
# ===============================================================================================
# ====================================== THE GAME LOOP ==========================================
# ===============================================================================================

# this makes sure that the sand keeps going in a straight line while placing it when it's active, and also some other stuff
try:
    while playingMySandbox:
        yesbutton.box = Rect(screenx/2-(10+screenx/5),screeny*0.6,screenx/5,screeny/7)
        nobutton.box = Rect(screenx/2+10,screeny*0.6,screenx/5,screeny/7)
        #Title screen!

        if gameState == "title":
            buttonPressed = False
            if changeScreen:
                screen = pygame.display.set_mode((600,600))
                
                if sandBoxed:
                    createButton.text = font[4].render("New Box", 1, Color(0,0,0))
            
            for event in pygame.event.get(): #Event Queue for the main sandbox (or whatever it's called)
                if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)) and not wannaBreak:
                    if titleState == 0:
                        playingMySandbox = False
                    if titleState == 1:
                        texts = [
                            font[1].render("Are you sure you want to quit?",1,Color(255,255,255))
                        ]
                        aboutToDie = True
                        wannaBreak = True
                    else:
                        titleState = 1
                    
                if event.type == pygame.MOUSEBUTTONDOWN and tap:
                    if event.button in (1,3):
                        fire = True
                        tap = False
                        if event.button == 3:
                            ice = True
                if event.type == pygame.MOUSEBUTTONUP:
                    tap = True
                    ice = False
                if event.type == pygame.MOUSEMOTION:
                    mousePos = Vector2(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        preEl += 1
                        if preEl >= 5:
                            preEl = 1
                    elif event.key == pygame.K_LALT:
                        titleLand = deepcopy(foreverglobals.titleScreenSandbox)
                    elif event.key == pygame.K_F1:
                        print("Skipping stuff!")
                        tutorial = 0
                        gameState = "setup"
                        setup = False
                        screenx = 500
                        screeny = 500
                        landx = 50
                        landy = 50
            

            clock.tick(fps)

            if wannaBreak:
                if yesbutton.tick(fire,mousePos):
                    playingMySandbox = False
                elif nobutton.tick(fire,mousePos):
                    wannaBreak = False
                    aboutToDie = False



            #Omg another sandbox in the sandbox???
            if not wannaBreak:
                titleLand = doing.doLessStuff(titleLand)
            if not aboutToDie:
                if titleState == 1:
                    if sandboxButton.tick(fire,mousePos):
                        titleState = 2
                        for layer in range(45,50):
                            for pixl in range(30):
                                if titleLand[layer][pixl] == 4:
                                    titleLand[layer][pixl] = 1
                    elif terrariumButton.tick(fire,mousePos):
                        titleState = 3
                        for layer in range(45,50):
                            for pixl in range(30,60):
                                if titleLand[layer][pixl] == 4:
                                    titleLand[layer][pixl] = 3
                elif titleState == 2:

                    if createButton.tick(fire,mousePos):
                        gameState = "setup"
                        setup = True
                        buttonPressed = True
                    elif sandBoxed and continueButton.tick(fire,mousePos):
                        gameState = "sandbox"
                        buttonPressed = True
                        landyx = (screenx/landx)
                        landyy = (screeny/landy)
                        screen = pygame.display.set_mode((screenx,screeny))

                    elif loadButton.tick(fire,mousePos):
                        gameState = "file loading"
                        buttonPressed = True
                elif titleState == 3:

                    if createButton.tick(fire,mousePos):
                        gameState = "terrarium"
                        setup = True
                        buttonPressed = True

                    elif loadButton.tick(fire,mousePos):
                        gameState = "file loading terra"
                        buttonPressed = True
                else:
                    if playButton.tick(fire,mousePos):
                        titleState = 1
                        if not sandBoxed:
                            for layer in range(35,40):
                                for pixl in range(60):
                                    if titleLand[layer][pixl] == 4:
                                        titleLand[layer][pixl] = 1



            if fliposwitch:
                fliposwitch = False
            else:
                fliposwitch = True
            
            if (not tap) and fliposwitch:
                x = int(mousePos.x/10)
                y = int(mousePos.y/10)
                try:
                    if (titleLand[int(y)][int(x)] != 4 or preEl == 4) and not buttonPressed:
                        if ice:
                            titleLand[int(y)][int(x)] = 0
                        else:
                            titleLand[int(y)][int(x)] = preEl
                except IndexError:
                    oob += 1

            

            #Rendering these buttons and screen!
            
            if titleState == 2:
                screen.fill((0,0,0))
            elif titleState == 3:
                screen.fill((100,200,255))
            else:
                screen.fill((255,204,44))

            drawLessStuff(screen,titleLand,10,10,titleState)
            
            if titleState == 1:
                sandboxButton.render(screen)
                terrariumButton.render(screen)
            elif titleState in (2,3):
                createButton.render(screen)
                loadButton.render(screen)
            else:
                playButton.render(screen)
            if sandBoxed and titleState == 1:
                continueButton.render(screen)
            
            
            if aboutToDie:
                for l in range(len(texts)):
                    screen.blit(texts[l],Vector2(20, 10+40*l))
                yesbutton.render(screen)
                nobutton.render(screen)
            
            
            #pygame.display.flip()

        
        # ===============================================================================================
        # ===================================== THE SETUP LOOP ==========================================
        # ===============================================================================================


        elif gameState == "setup":
            fliposwitch = True
            d = 0
            
            
            
            for event in pygame.event.get(): #Event Queue for the setup,
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    gameState = "title"
                    titleState = 0
                    changeScreen = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT:
                        shiftKey = True
                    elif event.key == pygame.K_UP:
                        arrowkeys[0] = True
                    elif event.key == pygame.K_DOWN:
                        arrowkeys[1] = True
                    elif event.key == pygame.K_LEFT:
                        arrowkeys[2] = True
                    elif event.key == pygame.K_RIGHT:
                        arrowkeys[3] = True
                    elif event.key == pygame.K_w:
                        wasdkeys[0] = True
                    elif event.key == pygame.K_a:
                        wasdkeys[1] = True
                    elif event.key == pygame.K_s:
                        wasdkeys[2] = True
                    elif event.key == pygame.K_d:
                        wasdkeys[3] = True
                    elif event.key == pygame.K_RETURN:
                        setup = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LSHIFT:
                        shiftKey = False
                    elif event.key == pygame.K_UP:
                        arrowkeys[0] = False
                        delayme[0] = 0
                    elif event.key == pygame.K_DOWN:
                        arrowkeys[1] = False
                        delayme[0] = 0
                    elif event.key == pygame.K_LEFT:
                        arrowkeys[2] = False
                        delayme[0] = 0
                    elif event.key == pygame.K_RIGHT:
                        arrowkeys[3] = False
                        delayme[0] = 0
                    elif event.key == pygame.K_w:
                        wasdkeys[0] = False
                        delayme[1] = 0
                    elif event.key == pygame.K_a:
                        wasdkeys[1] = False
                        delayme[1] = 0
                    elif event.key == pygame.K_s:
                        wasdkeys[2] = False
                        delayme[1] = 0
                    elif event.key == pygame.K_d:
                        wasdkeys[3] = False
                        delayme[1] = 0
            clock.tick(fps)
            amount = 1
            if shiftKey:
                amount = 10

            if delayme[0] > 0:
                delayme[0] -= 1  
            else:
                dontgointothenegatives[0] = False
                if True in arrowkeys:
                    changeScreen = True
                    delayme[0] = 6
                    if arrowkeys[0]:
                        if landy - amount > 0:
                            landy -= amount
                        else:
                            dontgointothenegatives[0] = True
                    if arrowkeys[1]:
                        landy += amount
                    if arrowkeys[2]:
                        if landx - amount > 0:
                            landx -= amount
                        else:
                            dontgointothenegatives[0] = True
                    if arrowkeys[3]:
                        landx += amount

            if delayme[1] > 0:
                delayme[1] -= 1  
            else:
                dontgointothenegatives[1] = False
                if True in wasdkeys:
                    changeScreen = True
                    delayme[1] = 6
                    if wasdkeys[0]:
                        if screeny - amount > 0:
                            screeny -= amount
                        else:
                            dontgointothenegatives[1] = True
                    if wasdkeys[2]:
                        screeny += amount
                    if wasdkeys[1]:
                        if screenx - amount > 0:
                            screenx -= amount
                        else:
                            dontgointothenegatives[1] = True
                    if wasdkeys[3]:
                        screenx += amount


            screen.fill((0,0,0))
            if screenx > 300 and screeny > 230:
                texts = (
                    font[2].render("Setting up your sandbox (Preview mode)",1,Color(0,0,0)),
                    font[2].render("The grid you see is what your sandbox",1,Color(0,0,0)),
                    font[2].render("will look like in scale.",1,Color(0,0,0)),
                    font[2].render("Press the arrow keys to change",1,Color(0,0,0)),
                    font[2].render("the size of the sandbox space.",1,Color(0,0,0)),
                    font[2].render("Press the WASD keys to change",1,Color(0,0,0)),
                    font[2].render("the size of the sandbox's screen.",1,Color(0,0,0)),
                    font[2].render("Once you're finished, press enter.",1,Color(0,0,0)),
                    font[2].render((str("Current size: a " + str(landx) + " by " + str(landy) + " grid.")),1,Color(0,0,0)),
                    font[2].render((str("On a " + str(screenx) + " by " + str(screeny) + " screen.")),1,Color(0,0,0))
                )
            else:
                texts = (
                    font[2].render((str("Current size: a " + str(landx))),1,Color(255,0,0)),
                    font[2].render((str("by " + str(landy) + " grid.")),1,Color(255,0,0)),
                    font[2].render((str("On a " + str(screenx))),1,Color(255,0,0)),
                    font[2].render(("by " + str(screeny) + " screen."),1,Color(255,0,0))
                )

            if changeScreen and gameState == "setup":
                screen = pygame.display.set_mode((screenx,screeny))
            landyx = (screenx/landx)
            landyy = (screeny/landy)
            for i in range(landy):
                for j in range(landx):
                    if True in dontgointothenegatives:
                        pygame.draw.rect(screen,(255,0,0),(j*landyx,i*landyy,landyx,landyy),1)
                    else:
                        pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy),1)
            
            if screenx > 300 and screeny > 230:
                pygame.draw.rect(screen,(255,255,255),(0,0,300,230))
            for l in range(len(texts)):
                screen.blit(texts[l],Vector2(10, 10+20*l))
                #pygame.display.flip()
            unanswered = True

            if not setup:
                #Setting up the sandbox variables after the setup!
                gameState = "sandbox"
                shiftKey = False

                #Sandbox initialization!

                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                landyx = (screenx/landx)
                landyy = (screeny/landy)

                screen = pygame.display.set_mode((screenx,screeny))

                print("Welcome to the sandbox!")
                print(random.choice(foreverglobals.splashes))


                

        
        elif gameState == "sandbox":
            if not sandBoxed:
                sandBoxed = True
            changeScreen = True
            doingafilething = False
            d = 0
            if tutorial != 0:
                
                if tutorial == 1:
                    for event in pygame.event.get(): #Event Queue but it's heavily restricted and you can only do mouse stuff for now
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            tutorial = 0
                            print("Skipping Tutorial!")
                        if event.type == pygame.MOUSEBUTTONDOWN and tap:
                            if event.button in (1,3):
                                undoList.append(deepcopy(land))
                                fire = True
                                tap = False
                                if event.button == 3:
                                    ice = True
                        if event.type == pygame.MOUSEBUTTONUP:
                            tap = True
                            ice = False
                        if event.type == pygame.MOUSEMOTION:
                            mousePos = Vector2(event.pos)
                    
                    for event in pygame.event.get(): #Event Queue but you can only escape
                        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            tutorial = 0
                            print("Skipping Tutorial!")
                    texts = (
                        font[1].render("Welcome to the sandbox!",1,Color(255,255,255)),
                        font[1].render("Would you like a tutorial?",1,Color(255,255,255))
                    )
                elif tutorial == 2:
                    for event in pygame.event.get(): #Event Queue but it's heavily restricted and you can only do mouse stuff for now
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            tutorial = 0
                            print("Skipping Tutorial!")
                        if event.type == pygame.MOUSEBUTTONDOWN and tap:
                            undoList.append(deepcopy(land))
                            fire = True
                            tap = False
                        if event.type == pygame.MOUSEBUTTONUP:
                            tap = True
                            ice = False
                        if event.type == pygame.MOUSEMOTION:
                            mousePos = Vector2(event.pos)


                    texts = (
                        font[3].render("Time for the basics of the basics.",1,Color(255,255,255)),
                        font[3].render("Using your mouse, you can click",1,Color(255,255,255)),
                        font[3].render("down and draw on the screen of an",1,Color(255,255,255)),
                        font[3].render("element (You're currently on sand)",1,Color(255,255,255)),
                        font[3].render("Progress: " + str(tutorialprogress//3) + "%",1,Color(255,255,255))
                        
                    )
                    if tutorialprogress >= 300:
                        tutorialprogress = 0
                        tutorial = 3
                        continue
                elif tutorial == 3:
                    for event in pygame.event.get(): #Event Queue but it's heavily restricted and you can only do mouse stuff for now
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            tutorial = 0
                            print("Skipping Tutorial!")
                        if event.type == pygame.MOUSEBUTTONDOWN and tap:
                            if event.button in (1,3):
                                undoList.append(deepcopy(land))
                                fire = True
                                tap = False
                                if event.button == 3:
                                    ice = True
                        if event.type == pygame.MOUSEBUTTONUP:
                            tap = True
                            ice = False
                        if event.type == pygame.MOUSEMOTION:
                            mousePos = Vector2(event.pos)


                    texts = (
                        font[3].render("That's quite a bit of sand, maybe",1,Color(255,255,255)),
                        font[3].render("it's time to get rid of some of it?",1,Color(255,255,255)),
                        font[3].render("The right click acts as an eraser no",1,Color(255,255,255)),
                        font[3].render("matter the element",1,Color(255,255,255)),
                        font[3].render("Progress: " + str(tutorialprogress//2) + "%",1,Color(255,255,255))
                        
                    )
                    if tutorialprogress >= 200:
                        tutorialprogress = 0
                        tutorial = 4
                        continue
                elif tutorial == 4:
                    for event in pygame.event.get(): #Event Queue to do very basic sandbox stuff
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            tutorial = 0
                            print("Skipping Tutorial!")
                        if event.type == pygame.MOUSEBUTTONDOWN and tap:
                            if event.button in (1,3):
                                undoList.append(deepcopy(land))
                                fire = True
                                tap = False
                                if event.button == 3:
                                    ice = True
                        if event.type == pygame.MOUSEBUTTONUP:
                            tap = True
                            ice = False
                        if event.type == pygame.MOUSEMOTION:
                            mousePos = Vector2(event.pos)
                        if event.type == pygame.KEYDOWN:
                            
                            #Command Keys
                            
                            if event.key == pygame.K_SPACE:
                                if not alive:
                                    undoList.append(deepcopy(land))
                                    redoList = []
                                live = True
                                #Go a single step forward
                            elif event.key == pygame.K_LCTRL:
                                live = True
                                if alive:
                                    alive = False
                                else:
                                    alive = True
                                #Go a step forward every tick until pressed again
                    texts = (
                        font[3].render("Great, if you want to see the sand",1,Color(255,255,255)),
                        font[3].render("move, press the Left Ctrl Button!",1,Color(255,255,255)),
                        font[3].render("(Alternatively you can go single",1,Color(255,255,255)),
                        font[3].render("Steps forward by pressing Space.)",1,Color(255,255,255)),
                        font[3].render("Progress: " + str(tutorialprogress//6) + "%",1,Color(255,255,255))
                    )
                    if tutorialprogress >= 600:
                        tutorialprogress = 0
                        tutorial = 5
                        continue
                elif tutorial == 5 or tutorial == 6:
                    for event in pygame.event.get(): #Event Queue to do very basic sandbox stuff
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            tutorial = 0
                            print("Skipping Tutorial!")
                        if event.type == pygame.MOUSEBUTTONDOWN and tap:
                            if event.button in (1,3):
                                undoList.append(deepcopy(land))
                                fire = True
                                tap = False
                                if event.button == 3:
                                    ice = True
                        if event.type == pygame.MOUSEBUTTONUP:
                            tap = True
                            ice = False
                        if event.type == pygame.MOUSEMOTION:
                            mousePos = Vector2(event.pos)
                        if event.type == pygame.KEYDOWN:
                            
                            #Command Keys
                            
                            if event.key == pygame.K_SPACE:
                                if not alive:
                                    undoList.append(deepcopy(land))
                                    redoList = []
                                live = True
                                #Go a single step forward
                            elif event.key == pygame.K_LCTRL:
                                live = True
                                if alive:
                                    alive = False
                                else:
                                    alive = True
                                #Go a step forward every tick until pressed again
                            elif event.key == pygame.K_TAB:
                                gameState = "elementmenu"
                                buttonYOffset = 0
                                
                    if tutorial == 5:
                        texts = (
                            font[3].render("So far so good. You probably don't",1,Color(255,255,255)),
                            font[3].render("want to just play with only sand,",1,Color(255,255,255)),
                            font[3].render("that'll get old fast! How about we",1,Color(255,255,255)),
                            font[3].render("Place some stone? Press the TAB",1,Color(255,255,255)),
                            font[3].render("key to access the Elemental Menu.",1,Color(255,255,255))
                        )
                    else:
                        texts = (
                            font[3].render("Go back to the Tab menu for",1,Color(255,255,255)),
                            font[3].render("the tutorial!",1,Color(255,255,255))
                        )
                elif tutorial == 7:
                    for event in pygame.event.get(): #Event Queue, you're almost there...!
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            tutorial = 0
                            print("Skipping Tutorial!")
                        if event.type == pygame.MOUSEBUTTONDOWN and tap:
                            if event.button in (1,3):
                                undoList.append(deepcopy(land))
                                fire = True
                                tap = False
                                if event.button == 3:
                                    ice = True
                        if event.type == pygame.MOUSEBUTTONUP:
                            tap = True
                            ice = False
                        if event.type == pygame.MOUSEMOTION:
                            mousePos = Vector2(event.pos)
                        if event.type == pygame.KEYDOWN:
                            
                            #Command Keys
                            
                            if event.key == pygame.K_SPACE:
                                if not alive:
                                    undoList.append(deepcopy(land))
                                    redoList = []
                                live = True
                                #Go a single step forward
                            elif event.key == pygame.K_LCTRL:
                                live = True
                                if alive:
                                    alive = False
                                else:
                                    alive = True
                                #Go a step forward every tick until pressed again
                            elif event.key == pygame.K_TAB:
                                gameState = "elementmenu"
                                tutorialprogress += 5
                                buttonYOffset = 0
                            elif event.key == pygame.K_RIGHTBRACKET:
                                
                                if len(redoList) > 0:
                                    undoList.append(deepcopy(land))
                                    land = redoList.pop()
                                    tutorialprogress += 10
                            elif event.key == pygame.K_LEFTBRACKET:
                                if len(undoList) > 0:
                                    redoList.append(deepcopy(land))
                                    land = undoList.pop()
                                    tutorialprogress += 10
                            elif event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                                brushSize += 1
                                print("brush size is now", (brushSize*2+1))
                            elif event.key == pygame.K_UNDERSCORE or event.key == pygame.K_MINUS:
                                if 0 < brushSize:
                                    brushSize -= 1
                                    print("brush size is now", (brushSize*2+1))        
                                    
                                    
                                    
                    if tutorialprogress < 1000 or unlockedElements == [0,1,2,3,4,5,6,7,8,9]:
                        texts = (
                            font[3].render("Fun tip: you can press the square",1,Color(255,255,255)),
                            font[3].render("bracket keys ( [ and ] ) to undo",1,Color(255,255,255)),
                            font[3].render("and redo actions you've done.",1,Color(255,255,255)),
                            font[3].render("Progress: " + str(tutorialprogress//40) + "%",1,Color(255,255,255))
                        )
                    elif tutorialprogress < 2000:
                        texts = (
                            font[3].render("What odd new elements you seem to",1,Color(255,255,255)),
                            font[3].render("be discovering! Each element you",1,Color(255,255,255)),
                            font[3].render("unlock can be selected in the",1,Color(255,255,255)),
                            font[3].render("elements menu.",1,Color(255,255,255)),
                            font[3].render("Progress: " + str(tutorialprogress//40) + "%",1,Color(255,255,255))
                        )
                    elif tutorialprogress < 3000:
                        texts = (
                            font[3].render("Another fun tip: you can press the",1,Color(255,255,255)),
                            font[3].render("plus and minus keys to change your",1,Color(255,255,255)),
                            font[3].render("brush size.",1,Color(255,255,255)),
                            font[3].render("Progress: " + str(tutorialprogress//40) + "%",1,Color(255,255,255))
                        )
                    else:
                        texts = (
                            font[3].render("You're almost at the end of the tutorial",1,Color(255,255,255)),
                            font[3].render("Just a bit more...",1,Color(255,255,255)),
                            font[3].render("Progress: " + str(tutorialprogress//40) + "%",1,Color(255,255,255))
                        )
                    if tutorialprogress >= 4000:
                        tutorialprogress = 0
                        tutorial = 8
                        continue
                elif tutorial == 8:
                    for event in pygame.event.get(): #One last Event Queue
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            tutorial = 0
                            print("Skipping Tutorial!")
                        if event.type == pygame.MOUSEBUTTONDOWN and tap:
                            if event.button in (1,3):
                                undoList.append(deepcopy(land))
                                fire = True
                                tap = False
                                if event.button == 3:
                                    ice = True
                        if event.type == pygame.MOUSEBUTTONUP:
                            tap = True
                            ice = False
                        if event.type == pygame.MOUSEMOTION:
                            mousePos = Vector2(event.pos)
                        if event.type == pygame.KEYDOWN:
                            
                            #Command Keys
                            
                            if event.key == pygame.K_SPACE:
                                if not alive:
                                    undoList.append(deepcopy(land))
                                    redoList = []
                                live = True
                                #Go a single step forward
                            elif event.key == pygame.K_LCTRL:
                                live = True
                                if alive:
                                    alive = False
                                else:
                                    alive = True
                                #Go a step forward every tick until pressed again
                            elif event.key == pygame.K_TAB:
                                gameState = "elementmenu"
                                tutorialprogress += 5
                                buttonYOffset = 0
                            elif event.key == pygame.K_RIGHTBRACKET:
                                
                                if len(redoList) > 0:
                                    undoList.append(deepcopy(land))
                                    land = redoList.pop()
                                    tutorialprogress += 10
                            elif event.key == pygame.K_LEFTBRACKET:
                                if len(undoList) > 0:
                                    redoList.append(deepcopy(land))
                                    land = undoList.pop()
                                    tutorialprogress += 10
                            elif event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                                brushSize += 1
                                print("brush size is now", (brushSize*2+1))
                            elif event.key == pygame.K_UNDERSCORE or event.key == pygame.K_MINUS:
                                if 0 < brushSize:
                                    brushSize -= 1
                                    print("brush size is now", (brushSize*2+1))        
                            elif event.key == pygame.K_LSHIFT:
                                gameState = "file saving"   
                                           
                    texts = (
                            font[3].render("What a wonderful sandbox you've made!",1,Color(255,255,255)),
                            font[3].render("How about you save it by pressing the",1,Color(255,255,255)),
                            font[3].render("Left shift key, that way you can",1,Color(255,255,255)),
                            font[3].render("load it later by typing out the save's",1,Color(255,255,255)),
                            font[3].render("Name when pressing 0 after the tutorial.",1,Color(255,255,255))
                        )
                elif tutorial == 9:
                    for event in pygame.event.get(): #One last Event Queue
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            tutorial = 0
                            print("Tutorial Complete!")
                        if event.type == pygame.MOUSEBUTTONDOWN and tap:
                            if event.button in (1,3):
                                undoList.append(deepcopy(land))
                                fire = True
                                tap = False
                                if event.button == 3:
                                    ice = True
                        if event.type == pygame.MOUSEBUTTONUP:
                            tap = True
                            ice = False
                        if event.type == pygame.MOUSEMOTION:
                            mousePos = Vector2(event.pos)
                        if event.type == pygame.KEYDOWN:
                            
                            #Command Keys
                            
                            if event.key == pygame.K_SPACE:
                                if not alive:
                                    undoList.append(deepcopy(land))
                                    redoList = []
                                live = True
                                #Go a single step forward
                            elif event.key == pygame.K_LCTRL:
                                live = True
                                if alive:
                                    alive = False
                                else:
                                    alive = True
                                #Go a step forward every tick until pressed again
                            elif event.key == pygame.K_TAB:
                                gameState = "elementmenu"
                                tutorialprogress += 5
                                buttonYOffset = 0
                            elif event.key == pygame.K_RIGHTBRACKET:
                                
                                if len(redoList) > 0:
                                    undoList.append(deepcopy(land))
                                    land = redoList.pop()
                                    tutorialprogress += 10
                            elif event.key == pygame.K_LEFTBRACKET:
                                if len(undoList) > 0:
                                    redoList.append(deepcopy(land))
                                    land = undoList.pop()
                                    tutorialprogress += 10
                            elif event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                                brushSize += 1
                                print("brush size is now", (brushSize*2+1))
                            elif event.key == pygame.K_UNDERSCORE or event.key == pygame.K_MINUS:
                                if 0 < brushSize:
                                    brushSize -= 1
                                    print("brush size is now", (brushSize*2+1))        
                            elif event.key == pygame.K_LSHIFT:
                                gameState = "file saving"  
                            elif event.key == pygame.K_0:
                                gameState = "file loading" 
                                           
                    texts = (
                            font[2].render("You did it, you've completed the",1,Color(255,255,255)),
                            font[2].render("basics of Sandbox! One last thing",1,Color(255,255,255)),
                            font[2].render("Before you go: After this tutorial,",1,Color(255,255,255)),
                            font[2].render("All of the letters on the",1,Color(255,255,255)),
                            font[2].render("keyboard are bound to an",1,Color(255,255,255)),
                            font[2].render("element, meaning they will set",1,Color(255,255,255)),
                            font[2].render("the current element to the element",1,Color(255,255,255)),
                            font[2].render("the key is bound to without needing",1,Color(255,255,255)),
                            font[2].render("to unlock it or press tab!",1,Color(255,255,255)),
                            font[2].render("To finish this tutorial, press the",1,Color(255,255,255)),
                            font[2].render("escape key! If you need this tutorial",1,Color(255,255,255)),
                            font[2].render("again, press the backspace key.",1,Color(255,255,255))
                        )
            else:
                if pickAnElement:
                    appendKey = keyboard(True)
                else:
                    for event in pygame.event.get(): #Event Queue for the main sandbox (or whatever it's called)
                        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)) and not wannaBreak:
                            texts = (
                                font[1].render("Are you sure you want to quit to title?",1,Color(255,255,255)),
                                font[3].render("(Be sure to save your sandbox if you haven't!)",1,Color(255,255,255)),
                            )
                            alive = False
                            wannaBreak = True
                        if event.type == pygame.MOUSEBUTTONDOWN and tap:
                            if event.button in (1,3):
                                undoList.append(deepcopy(land))
                                fire = True
                                tap = False
                                if event.button == 3:
                                    ice = True
                        if event.type == pygame.MOUSEBUTTONUP:
                            tap = True
                            ice = False
                        if event.type == pygame.MOUSEMOTION:
                            mousePos = Vector2(event.pos)
                        if event.type == pygame.KEYDOWN:
                            
                            #Command Keys
                            
                            if event.key == pygame.K_SPACE:
                                if not alive:
                                    undoList.append(deepcopy(land))
                                    redoList = []
                                live = True
                                #Go a single step forward
                            if event.key == pygame.K_LCTRL:
                                live = True
                                if alive:
                                    alive = False
                                else:
                                    alive = True
                                #Go a step forward every tick until pressed again
                            if event.key == pygame.K_LALT:
                                undoList.append(deepcopy(land))
                                redoList = []
                                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                            elif event.key == pygame.K_RALT:
                                undoList.append(deepcopy(land))
                                redoList = []
                                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                                for u in range(10):
                                    land[u] = [[3,0] for _ in range(landx)]
                            elif event.key == pygame.K_RCTRL:
                                undoList.append(deepcopy(land))
                                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                                for u in range(10):
                                    land[u] = [[15,0] for _ in range(landx)]
                            elif event.key == pygame.K_END:
                                undoList.append(deepcopy(land))
                                redoList = []
                                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                                for u in range(10):
                                    land[u] = [[9,0] for _ in range(landx)]
                            elif event.key == pygame.K_DELETE:
                                undoList.append(deepcopy(land))
                                redoList = []
                                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                                for u in range(10):
                                    land[u] = [[65,20] for _ in range(landx)]
                            elif event.key == pygame.K_HOME:
                                undoList.append(deepcopy(land))
                                redoList = []
                                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                                for u in range(10):
                                    land[u] = [[29,0] for _ in range(landx)]
                            elif event.key == pygame.K_PAGEUP:
                                undoList.append(deepcopy(land))
                                redoList = []
                                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                                for u in range(10):
                                    land[u] = [[71,0] for _ in range(landx)]
                            elif event.key == pygame.K_PAGEDOWN:
                                undoList.append(deepcopy(land))
                                redoList = []
                                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                                for u in range(10):
                                    land[u] = [[75,0] for _ in range(landx)]
                            elif event.key == pygame.K_NUMLOCK:
                                undoList.append(deepcopy(land))
                                redoList = []
                                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                                for u in range(10):
                                    land[u] = [[60,0] for _ in range(landx)]
                            elif event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                                brushSize += 1
                                print("brush size is now", (brushSize*2+1))
                            elif event.key == pygame.K_UNDERSCORE or event.key == pygame.K_MINUS:
                                if 0 < brushSize:
                                    brushSize -= 1
                                    print("brush size is now", (brushSize*2+1))
                            elif event.key == pygame.K_BACKSPACE:
                                tutorial = 1
                            elif event.key == pygame.K_F1:
                                if showfps:
                                    showfps = False
                                else:
                                    showfps = True
                            elif event.key == pygame.K_CAPSLOCK:
                                if werealsodoinglife:
                                    werealsodoinglife = False
                                    print("Destroying life")
                                else:
                                    werealsodoinglife = True
                                    print("Doing life")
                            elif event.key == pygame.K_SLASH:
                                if dither:
                                    dither = False
                                else:
                                    dither = True
                            elif event.key == pygame.K_BACKSLASH:
                                if mirror:
                                    mirror = False
                                else:
                                    mirror = True
                            elif event.key == pygame.K_COMMA:
                                if elementary:
                                    elementary = False
                                else:
                                    elementary = True
                                    elements = []
                                    print("Please choose the elements you want to do. To stop choosing, say something other than an int")
                                    try:
                                        while True:
                                            elements.append(int(input()))
                                    except ValueError:
                                        elements = tuple(elements)
                                        print("Brush now has elements", elements)
                                    if len(elements) == 0:
                                        print("HEY! YOU FORGOT TO DO ELEMENTS! (Defaulting to what you did last time)")
                                        elementary = False
                            elif event.key == pygame.K_RIGHTBRACKET:
                                
                                if len(redoList) > 0:
                                    undoList.append(deepcopy(land))
                                    land = redoList.pop()
                            elif event.key == pygame.K_LEFTBRACKET:
                                if len(undoList) > 0:
                                    redoList.append(deepcopy(land))
                                    land = undoList.pop()
                            
                            #Element Keys
                            
                            elif event.key == pygame.K_1:
                                element = 1
                            elif event.key == pygame.K_2:
                                element = 2
                            elif event.key == pygame.K_3:
                                element = 3
                            elif event.key == pygame.K_4:
                                element = 4
                            elif event.key == pygame.K_5:
                                element = 5
                            elif event.key == pygame.K_6:
                                element = 6
                            elif event.key == pygame.K_7:
                                element = 7
                            elif event.key == pygame.K_8:
                                element = 8
                            elif event.key == pygame.K_9:
                                element = 9
                            elif event.key == pygame.K_q:
                                element = 38
                            elif event.key == pygame.K_w:
                                element = 11
                            elif event.key == pygame.K_e:
                                element = 12
                            elif event.key == pygame.K_r:
                                element = 83
                            elif event.key == pygame.K_t:
                                element = 80
                            elif event.key == pygame.K_y:
                                element = 46
                            elif event.key == pygame.K_u:
                                element = 16
                            elif event.key == pygame.K_i:
                                element = 78
                            elif event.key == pygame.K_a:
                                element = 18
                            elif event.key == pygame.K_s:
                                element = 42
                            elif event.key == pygame.K_d:
                                element = 20
                            elif event.key == pygame.K_f:
                                element = 21
                            elif event.key == pygame.K_g:
                                element = 22
                            elif event.key == pygame.K_h:
                                element = 79
                            elif event.key == pygame.K_j:
                                element = 68
                            elif event.key == pygame.K_k:
                                element = 62
                            elif event.key == pygame.K_l:
                                element = 26
                            elif event.key == pygame.K_z:
                                element = 43
                            elif event.key == pygame.K_x:
                                element = 28
                            elif event.key == pygame.K_c:
                                element = 29
                            elif event.key == pygame.K_v:
                                element = 77
                            elif event.key == pygame.K_b:
                                element = 41
                            elif event.key == pygame.K_n:
                                element = 50
                            #Oops I just realized that I forgot to include o and p
                            elif event.key == pygame.K_m:
                                element = 33
                            elif event.key == pygame.K_o:
                                element = 34
                            elif event.key == pygame.K_p:
                                element = 35
                            #For elements that aren't here
                            elif event.key == pygame.K_RSHIFT:
                                pickAnElement = True
                                anElement = ""
                                appendKey = ""
                            elif event.key == pygame.K_PERIOD:
                                eyeDropper = True
                                print("Pick an element from the sandbox to copy")
                                alive = False
                        
                        
                            #The ultimate thing: SAVING!
                            elif event.key == pygame.K_LSHIFT:
                                gameState = "file saving"
                                
                            #What's the use of saving if you can't LOAD?
                            elif event.key == pygame.K_0:
                                gameState = "file loading"
                                
                            
                            elif event.key == pygame.K_TAB:
                                gameState = "elementmenu"
                                buttonYOffset = 0
                                
                            elif event.key == pygame.K_F12:
                                unlockedElements = []
                                print("Oh dear, you unlocked ALL of the elements!")
                                for i in range(uniqueElements):
                                    unlockedElements.append(i)

            
            clock.tick(fps)
            if showfps and fps != int(clock.get_fps()):
                tempFps = int(clock.get_fps())
                print("fps:", tempFps)
            
            if live:
                if tutorial == 4 or tutorial == 7:
                    tutorialprogress += 1
                land = doing.doStuff(land,fliposwitch,werealsodoinglife)


            if fliposwitch and alive:
                fliposwitch = False
            else:
                fliposwitch = True

            if tutorial == 1:
                if yesbutton.tick(fire,mousePos):
                    tutorial = 2
                elif nobutton.tick(fire,mousePos):
                    tutorial = 0

            if wannaBreak:
                if yesbutton.tick(fire,mousePos):
                    gameState = "title"
                    titleState = 0
                    wannaBreak = False
                elif nobutton.tick(fire,mousePos):
                    wannaBreak = False
            
            if pickAnElement:
                texts = (
                        font[1].render("Enter the element's ID",1,Color(255,255,255)),
                        font[1].render(anElement,1,Color(255,255,255))
                        )
                if appendKey == "end":
                    if len(anElement) != 0:
                        element = int(anElement)
                        try:
                            print("Set element to", foreverglobals.elements[element].name)
                        except:
                            print("Set to an unknown element:", element)
                        pickAnElement = False
                    appendKey = ""
                elif appendKey == "escape":
                    print("Cancelling...")
                    pickAnElement = False
                elif appendKey == "back":
                    appendKey = ""
                    if len(anElement) > 0:
                        anElement = anElement[:-1]
                else:
                    anElement += appendKey
            
            #Where the mouse input matters!
            if (not (tap or tutorial == 1 or wannaBreak)) and fliposwitch:
                if tutorial == 2 or tutorial == 7:
                    tutorialprogress += 1
                elif tutorial == 3 and ice:
                    tutorialprogress += 1
                x = int(mousePos.x/landyx)
                mx = int((screenx-mousePos.x)/landyx)
                y = int(mousePos.y/landyy)
                if eyeDropper:
                    brushSize = 0
                for l in range(0-brushSize,1+brushSize):
                    for m in range(0-brushSize,1+brushSize):
                        t = 0
                        try:
                            if eyeDropper:
                                element = land[y+l][x+m][0]
                                print("Copied", end = " ")
                                eyeDropper = False
                                try:
                                    print(foreverglobals.elements[element].name, end = " ")
                                except:
                                    print("An unknown element", end = " ")
                                print("from the sandbox. (ID:", str(element)+")")
                                time.sleep(0.5)#To assure you don't accidentally screw something up (I had to import an entire library here just for this one command ;w;)
                            else:
                                if (not dither) or random.randint(1,5) == 1:
                                    if ice:
                                        land[y+l][x+m] = [0,0]
                                    else:
                                        if elementary:
                                            element = random.choice(elements)
                                        if element == 5:
                                            t = 100100100
                                        if element in (13, 30, 56,83):
                                            t = 5
                                        elif element in (19,93,103):
                                            t = random.randint(0,255)
                                        elif element == 54:
                                            t = random.randint(1,6)
                                        elif element == 61:
                                            t = 3
                                        elif element in (64, 65):
                                            t = 20
                                        elif element == 67:
                                            t = 10
                                        elif element == 87:
                                            t = random.randint(1,4)
                                        elif element == 89:
                                            t = 10
                                        land[y+l][x+m] = [element,t]
                                        if mirror:
                                            land[y+l][mx+m] = [element,t]
                        except IndexError:
                            oob += 1

            
            
            for i in doing.gimmeAllElms(land):
                if not i in unlockedElements:
                    unlockedElements.append(i)
            
            
            screen.fill((0,0,0))
            
            
            drawStuff(screen,land,landyx,landyy,smoothColors,gamma,fliposwitch)
            
            

            if tutorial != 0 or wannaBreak or pickAnElement:
                if tutorial == 9:
                    for l in range(len(texts)):
                        screen.blit(texts[l],Vector2(20, 10+20*l))
                else:
                    for l in range(len(texts)):
                        screen.blit(texts[l],Vector2(20, 10+40*l))
            
            #Render the yes and no buttons
            yn = False
            if tutorial == 1 or wannaBreak:
                yn = True
                yesbutton.render(screen)
                nobutton.render(screen)

            if not (tutorial == 1 or wannaBreak or yn or pickAnElement):
                pygame.draw.rect(screen,(255,255,255),(mousePos.x-(landyx/2)*(brushSize*2+1),mousePos.y-(landyy/2)*(brushSize*2+1),landyx*(brushSize*2+1),landyy*(brushSize*2+1)),(1+brushSize//5))

            if not alive:
                live = False
            #pygame.display.flip()
        
        elif gameState == "elementmenu":
            
            if changeScreen:
                screen = pygame.display.set_mode((650,450))
            
            for event in pygame.event.get(): #It's just your mouse and stuff!
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_TAB)):
                    gameState = "sandbox"
                    screen = pygame.display.set_mode((screenx,screeny))
                elif event.type == pygame.MOUSEBUTTONDOWN and tap:
                    if event.button in (1,3):
                        fire = True
                        tap = False
                        if event.button == 3:
                            ice = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    tap = True
                    ice = False
                elif event.type == pygame.MOUSEMOTION:
                    mousePos = Vector2(event.pos)
                elif event.type == pygame.MOUSEWHEEL:
                    wheeled = True
                    wheel = event.y
            clock.tick(fps)
            if gameState == "sandbox":
                continue
            
            if tutorial == 5:
                   texts = (
                        font[1].render("Welcome to the element menu, where",1,Color(255,255,255)),
                        font[1].render("You can find all of the elements you",1,Color(255,255,255)),
                        font[1].render("have unlocked. After the tutorial",1,Color(255,255,255)),
                        font[1].render("There are a bunch of elements that",1,Color(255,255,255)),
                        font[1].render("Will already be unlocked.",1,Color(255,255,255))
                   )
                   if continueButton.tick(fire,mousePos):
                       tutorial = 6
            elif tutorial == 6:
                   texts = (
                        font[1].render("Click on the element you want to use",1,Color(255,255,255)),
                        font[1].render("to draw.",1,Color(255,255,255))
                   )
                   if element != 1:
                       tutorial = 7
            elif tutorial == 7:
                   texts = (
                        font[1].render("Great! now go back into the sandbox",1,Color(255,255,255)),
                        font[1].render("by pressing TAB again and mess with",1,Color(255,255,255)),
                        font[1].render("these newfound elements!",1,Color(255,255,255))
                   )
            
            if wheeled:
                if wheelv < 16:
                    wheelv += 2
                else:
                    wheelv = 16
            else:
                if wheelv > 0:
                    wheelv -= 1
                else:
                    wheelv = 0
            buttonYOffset += wheel * wheelv
            
            if tutorial != 5:
                for yan in range(len(elementButtons)//eColumns):
                    for yin in range(eColumns):
                        elementButtons[yan*eColumns+yin].box.x = yin*50+5
                        elementButtons[yan*eColumns+yin].box.y = yan*50+5+buttonYOffset
                        
                        if elementButtons[yan*eColumns+yin].id in unlockedElements and elementButtons[yan*eColumns+yin].tick(fire,mousePos):
                            element = elementButtons[yan*eColumns+yin].id
                            if len(foreverglobals.elements[element].name) < 10:
                                elementNameText = font[0].render(foreverglobals.elements[element].name,1,Color(255,255,255))
                            elif len(foreverglobals.elements[element].name) < 12:
                                elementNameText = font[4].render(foreverglobals.elements[element].name,1,Color(255,255,255))
                            else:
                                elementNameText = font[5].render(foreverglobals.elements[element].name,1,Color(255,255,255))
                            if foreverglobals.elements[element].desc != None:
                                elt = foreverglobals.elements[element].desc.split("[n]")
                                elementText = []
                                for ttt in elt:
                                    elementText.append(font[6].render(ttt,1,Color(255,255,255)))
                            else:
                                elementText = [
                                    font[6].render("No description.",1,Color(255,255,255))
                                            ]
            
            
            
            
            
            
            
            
            
            
            
            
            
                    
            #Render the menu
            
            screen.fill((0,0,0))
            
            airdid = False
            
            
            pygame.draw.rect(screen,Color(30,30,30),Rect(eColumns*50,0,650-eColumns*50,450))
            if foreverglobals.elements[element].color != None:
                pygame.draw.rect(screen,foreverglobals.elements[element].color,Rect(eColumns*50+15,5,40,40))
            else:
                pygame.draw.rect(screen,foreverglobals.elements[element].mColors[0],Rect(eColumns*50+15,5,40,40))
            screen.blit(elementNameText,(eColumns*50+10,50))
            for ree in range(len(elementText)):
                screen.blit(elementText[ree],(eColumns*50+10,90+18*ree))
            
            for butt in elementButtons:
                if butt.id != 0:
                    if butt.id in unlockedElements:
                        butt.render(screen)
                    else:
                        pygame.draw.rect(screen,Color(0,0,0),butt.box)
                        pygame.draw.rect(screen,Color(20,20,20),butt.box,2)
                elif not airdid:
                    butt.render(screen)
                    airdid = True
            
            
            if tutorial == 5:
                continueButton.render(screen)
            if tutorialprogress == 0 and tutorial in (5,6,7):
                for l in range(len(texts)):
                    screen.blit(texts[l],Vector2(20, 10+40*l))
                    
                
        
        
        
        #Saving and loading files gamestate!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        elif "file" in gameState:
            tap = True
            appendKey = keyboard()
            clock.tick(fps)

            if appendKey != "":
                changeScreen = True
            
            if appendKey == "end":
                appendKey = ""
                doingafilething = True
            elif appendKey == "back":
                    appendKey = ""
                    if len(filename) > 0:
                        filename = filename[:-1]
            elif appendKey == "fullback":
                    appendKey = ""
                    filename = ""
            elif appendKey == "\"":
                appendKey = ""
            elif appendKey == "escape":
                appendKey = ""
                gameState = "sandbox"
                screen = pygame.display.set_mode((screenx,screeny))
                print("Saveing/Loading aborted!")
                continue


            if appendKey == "/" and ((len(filename) > 0 and filename[-1] == "/") or len(filename) <= 0):
                appendKey = ""

            filename += appendKey


            if "saving" in gameState:
                texts = (
                    font[1].render("What would you like to save your sandbox as?",1,Color(0,0,0)),
                    font[1].render(str(filename),1,Color(0,0,0))
                )
            elif "loading" in gameState:
                texts = (
                    font[1].render("What is the filename of the save you want to load?",1,Color(0,0,0)),
                    font[1].render("(You can load images too!)",1,Color(0,0,0)),
                    font[1].render(str(filename),1,Color(0,0,0))
                )
            else:
                gameState = "sandbox"            
            if doingafilething or gameState == "sandbox":
                if gameState != "sandbox":
                    fail = True
                    if "loading" in gameState:
                        tutorial = 0
                        if actualGame != "title":
                            undoList.append(deepcopy(land))
                            backupx = landx
                            backupy = landy
                            bacnupsx = screenx
                            backupsy = screeny
                            backupland = deepcopy(land)
                        
                        
                        try:
                            if filename[-4:] in (".png",".jpg"):
                                print("Loading", filename+ " from your saves folder...",end = " ")
                                res = 10
                                imagefile = loadImage(filename,res)
                                screenx = imagefile[0]
                                screeny = imagefile[1]
                                landx = screenx//res
                                landy = screeny//res
                                land = imagefile[2]
                            else:
                                print("Loading", filename+ ".txt",end = " ")
                                if usesavefolder:
                                    print("from your saves folder...")
                                    thefile = open('sandsaves/'+filename+'.txt', 'r')
                                else:
                                    print("from the game's directory...")
                                    thefile = open(filename+'.txt', 'r')
                                reading = thefile.read().split()
                                thefile.close()
                                print(filename, "read with", len(reading), "numbers!")
                                readed = []
                                for inny in range(len(reading)):
                                    readed.append(int(reading[inny]))
                                landx = readed[0]
                                landy = readed[1]
                                screenx = readed[2]
                                screeny = readed[3]
                                print("Grid size:", landx, "by", landy, "pixels on a", screenx, "by", screeny, "gaming window.")
                                land = []
                                for ay in range(landy):
                                    land.append([])
                                    for bx in range(landx):
                                        pxl = (bx+(landx*ay)) * 2 + 4
                                        land[ay].append([readed[pxl],readed[pxl+1]])
                            
                            screen = pygame.display.set_mode((screenx,screeny))
                            #The loading should go smoothly from here so we don't have to worry about these variables being screwed
                            landyx = (screenx/landx)
                            landyy = (screeny/landy)
                            fail = False
                            if (not werealsodoinglife) and (checkEverywhere(land,[26,0]) or checkEverywhere(land,[37,0])):
                                print("Warning! This save contains life particles and life isn't enabled. You should probably enable it for the intended experience!")
                            print("Load successful!")
                        except FileNotFoundError as e:
                            print(f'An error occured: {e}')
                            traceback.print_tb(e.__traceback__)
                            print("Try again with a file that exists. (Maybe you don't have any :/))")
                        except TypeError as e:
                            print(f'An error occured: {e}')
                            traceback.print_tb(e.__traceback__)
                            print("Your file might have more than just numbers in it.")
                        except IndexError as e:
                            print(f'An error occured: {e}')
                            traceback.print_tb(e.__traceback__)
                            print("It's possible your grid isn't matching up with the data in a way!")
                        except Exception as ler:
                            print(f'An error occured, but it\'s complicated: {ler}')
                            traceback.print_tb(ler.__traceback__)
                            print("Please contact the creator of this sandbox to see what the issue could be")
                        if fail and actualGame == "sandbox":
                            undoList.pop()
                            landx = backupx
                            landy = backupy
                            screenx = bacnupsx
                            screeny = backupsy
                            land = deepcopy(backupland)
                            
                            
                    else:
                        print("Saving", filename+ ".txt to your saves folder... (You better not close your program!)")
                        try:
                            if usesavefolder:
                                thefile = open('sandsaves/'+filename+'.txt', 'w')
                            else:
                                thefile = open(filename+'.txt', 'w')
                            data = []
                            data.append(str(landx))
                            data.append(str(landy))
                            data.append(str(screenx))
                            data.append(str(screeny))
                            for ay in range(len(land)):
                                for bx in range(len(land[0])):
                                    data.append(str(land[ay][bx][0]))
                                    data.append(str(land[ay][bx][1]))
                            writing = ' '.join(data)
                            thefile.write(writing)
                            thefile.close()
                            print("Save successful!")
                            fail = False
                            if tutorial == 8:
                                tutorial = 9
                        except FileNotFoundError as e:
                            print(f'An error occured: {e}')
                            print("Maybe you don't have a sandsaves folder for the saves to go to. (You'll have to make it manually)")
                        except:
                            print(f'An error occured, but we don\'t know how!')
                            print("Please contact the creator of this sandbox to see what the issue could be")
                    screen = pygame.display.set_mode((screenx,screeny))
                    if fail:
                        gameState = actualGame
                    else:
                        gameState = "sandbox"
                filename = ""
                continue
            
            if changeScreen:
                screen = pygame.display.set_mode((800,450))
            screen.fill((255,255,255))
            
            for l in range(len(texts)):
                screen.blit(texts[l],Vector2(10, 10+30*l))
            #pygame.display.flip()
        
        elif gameState == "terrarium":
            print("Coming soon(tm)")
            gameState = "title"

        #This code runs no matter the gamestate
        
        if changeScreen:
            changeScreen = False

        if loadState != gameState:
            changeScreen = True
            doingafilething = False
            appendKey = ""
            tap = True
            ice = False
            loadState = gameState
            if gameState in games:
                actualGame = gameState

        if pygame.key.get_pressed()[pygame.K_F12]:
            killOrder -= 1
            if killOrder < 0:
                print("Oh, I heard you like dividing by 0! (Crashing intentionally~)")
                rememberme = True
                #idc if I can force an exception just by using yet another boring function, I like to divide by 0
                sht = 1/0
        else:
            killOrder = 100
        if killOrder < 100:
            ohmy = font[1].render("Crashing in "+str(killOrder),1,Color(255,255,255))
            screen.blit(ohmy,(0,0))

        pygame.display.flip()
        fire = False
        wheeled = False
        wheel = 0









    pygame.quit()
    print("Process exit with code: \":)\"")
    print("You went out of bounds", oob, "times!")
    if oob == 0:
        print("Good job!")
    elif oob < 100:
        print("Almost good")
    elif oob < 200:
        print("Pls do better uwu")
    elif oob < 500:
        print("Trace in the screen next time!!")
    elif oob < 1000:
        print("You can only draw in the screen, please don't make me remind you again!")
    elif oob < 10000:
        print("Please stop going out of bounds so much, it's annoying")
    elif oob < 1000000:
        print("Please remain inside these boundaries.")
    else:
        print("Are you trying to enter the backrooms or something???")
except Exception as err:
    aSeriousError = True
    print("A fatal error occured durring the sandbox!")
    print(random.choice(foreverglobals.crashSplash))
    if rememberme:
        print("You caused it by hitting the F12 key, you silly billy")
    else:
        print("Here's what happened, share this for a bug fix maybe.")
        print(err)
        traceback.print_tb(err.__traceback__)
if aSeriousError:
    print("Saving your last instance to a backup file")
    t = time.localtime()
    h = []
    for _ in t:
        h.append(str(_))
    h = "-".join(h)
    try:
        try:
            os.mkdir('backups')
            print("Making a \"backups\" folder for our mess.")
        except:
            print("Backup folder spotted!")
        
        thefile = open('backups/'+actualGame+h+'.txt', 'w')
        data = []
        data.append(str(landx))
        data.append(str(landy))
        data.append(str(screenx))
        data.append(str(screeny))
        for ay in range(len(land)):
            for bx in range(len(land[0])):
                data.append(str(land[ay][bx][0]))
                data.append(str(land[ay][bx][1]))
        writing = ' '.join(data)
        thefile.write(writing)
        thefile.close()
        print("Save successful in file \"backups/"+h+".txt\"")
    except NameError:
        print("Oh wait, I guess you haven't even made a sandbox yet.\nThere's nothing here to back-up.")
    except Exception as berror:
        print(f'Oh great, another error: {berror}')
        traceback.print_tb(berror.__traceback__)
        print("Backup failed I guess")
    