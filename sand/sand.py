#Can someone please tell me how to give more resources to this app so I can throttle it and have a smooth 60 fps while my computer combusts into flames
#Some optimization help would be nice too
showfps = False
#the setting that controls if you'd like to do life or not (Experimental sorta)

oob = 0

import os
import pygame
from pygame import Vector2
from pygame.rect import Rect
from pygame.color import Color
#WHY DOES YOU NOT EVEN THE AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
from copy import deepcopy
from copy import copy
import random
import time
import foreverglobals
import buttons

#I caved
from physics import coinflip
from physics import checkEverywhere
from doing import doStuff
from inputkeys import keyboard

pygame.font.init()
font = (
    pygame.font.Font("PressStart2P.ttf", 30),
    pygame.font.SysFont('Comic Sans MS', 30),
    pygame.font.SysFont('Comic Sans MS', 15),
    pygame.font.SysFont('Comic Sans MS', 20)
    )

texts = []

doaflip = True

rememberme = False

#Save folder things

usesavefolder = True
if usesavefolder:
    print("Using the sandsaves folder as a save directory")
    try:
        os.mkdir('sandsaves')
        print("sandsave folder made automatically!")
    except:
        print("sandsave folder already in place (yippee!)")

pygame.init()
screen = pygame.display.set_mode((10,10))
pygame.display.set_caption("Sandbox game!")
playingMySandbox=True
clock = pygame.time.Clock()

#mouse variables--------------------------------
mousePos = Vector2(0,0)
fire = False
tap = True

#Element Variables

element = 1
brushsize = 0

testbutton = buttons.button(Color(255,255,0),Rect(200,200,100,100),None,"Test!")

werealsodoinglife = False
eyedropper = False
dither = False
elementary = False
elements = []
mirror = False

doingafilething = False


# ===============================================================================================
# ===================================== THE SETUP LOOP ==========================================
# ===============================================================================================


texts = [
    font[2].render("Setting up your sandbox (Preview mode)",1,Color(0,0,0)),
    font[2].render("The grid you see is what your sandbox",1,Color(0,0,0)),
    font[2].render("will look like in scale.",1,Color(0,0,0)),
    font[2].render("Press the arrow keys to change",1,Color(0,0,0)),
    font[2].render("the size of the sandbox space.",1,Color(0,0,0)),
    font[2].render("Press the WASD keys to change",1,Color(0,0,0)),
    font[2].render("the size of the sandbox's screen.",1,Color(0,0,0)),
    font[2].render("Once you're finished, press enter.",1,Color(0,0,0))
]

screenx: int = 500
screeny: int = 500

landx: int = 50
landy: int = 50

setup = True
filename = ""

texts.append(font[2].render((str("Current size: a " + str(landx) + " by " + str(landy) + " grid.")),1,Color(0,0,0)))
texts.append(font[2].render((str("On a " + str(screenx) + " by " + str(screeny) + " screen.")),1,Color(0,0,0)))


arrowkeys = [False,False,False,False]
delayme = [6,10]
changeScreen = True
shiftKey = False
dontgointothenegatives = [False,False]
wasdkeys = [False,False,False,False]

while playingMySandbox and setup:
    d = 0
    for event in pygame.event.get(): #Event Queue (or whatever it's called)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            playingMySandbox = False
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
    clock.tick(60)
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


    if changeScreen:
        screen.fill((0,0,0))
        texts[-2] = font[2].render((str("Current size: a " + str(landx) + " by " + str(landy) + " grid.")),1,Color(0,0,0))
        texts[-1] = font[2].render((str("On a " + str(screenx) + " by " + str(screeny) + " screen.")),1,Color(0,0,0))
        screen = pygame.display.set_mode((screenx,screeny))
        landyx = (screenx/landx)
        landyy = (screeny/landy)
        for i in range(landy):
            for j in range(landx):
                if True in dontgointothenegatives:
                    pygame.draw.rect(screen,(255,0,0),(j*landyx,i*landyy,landyx,landyy),1)
                else:
                    pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy),1)
        
        pygame.draw.rect(screen,(255,255,255),(0,0,300,230))
        for l in range(len(texts)):
            screen.blit(texts[l],Vector2(10, 10+20*l))
        pygame.display.flip()
    unanswered = True
    changeScreen = False


shiftKey = False

#Sandbox initialization!

land = [[[0,0] for _ in range(landx)] for i in range(landy)]
landyx = (screenx/landx)
landyy = (screeny/landy)

screen = pygame.display.set_mode((screenx,screeny))

live = False
alive = False
ice = False
fps = 60

print("Welcome to the sandbox!")
print(random.choice(foreverglobals.splashes))
def remindMe() -> None:
    print("ELEMENTS: Press the keys for the element!  1: Sand  2: Stone  3: Water  4: Sugar  5: Wall  6: Dirt  7: Mud  8: Plant  9: Lava ")
    print("ELEMENTS: Q: Iron  W: Gravel  E: Obsidian  R: Steam  T: Glass  Y: Salt  U: Cloud  I: Brick O: Clay  P: Void  A: Algae")
    print("ELEMENTS: G: Snow  H: Ice  J: TNT  K: Sapling  L: Life particle (think the game of life, If turned off it will just be random)")
    print("ELEMENTS: Z: Electricity  X: Flower Seed  C: Oil  V: Fire N: Jammer (Screws stuff up)  M: Cloner  B: Smart Remover  S: Smart Converter  D: Sun  F: Moon")
    print("If you would like more information about how the smart remover/converter works, please visit https://www.youtube.com/watch?v=w_oNW7uHfcw")
    #I'm sure dr. mo wouldn't mind......
    print("PLACING CONTROLS: Left click to place down the element, Right click to use the eraser. You will have to discover the rest of the elements on your own through trial and error :)\nTo do multiple elements with a brush, press the comma for it to be random of some elements. To dither the brush, press the slash key.")
    print("ELEMENT CONTROLS: To get an element that's not on this list, press the Right Shift key then enter the element's ID (number) in the console.\nAlternatively, you can eyedrop (copy) an element from the sandbox by pressing period and then clicking the element")
    print("BRUSH CONTROLS: To enter/exit mirror mode, hit the backslash key. To undo an action, press the left square bracket, to redo said action, press the right square bracket ([ and ] respectively)")
    print("IMPORTANT: To start/pause the sandbox, press Left Ctrl. To go a single step in the sandbox, press Space.\nTo clear the sandbox, press the left Alt key. To clear the sandbox and have there be an ocean, hit the right Alt key.\nThere are several other kinds of oceans that can be created on the right hand side of the keyboard by pressing it's buttons.\nTo activate/deactivate the game of life and all it's whimsy, press the CAPS LOCK key. To change the brush size, hit up to grow it, hit down to shrink it.")
    print("SAVE/LOAD CONROLS: To save your sandbox, press either enter key. To load a sandbox, press the 0 key. To show this again, hit the backspace key")

# ===============================================================================================
# ====================================== THE GAME LOOP ==========================================
# ===============================================================================================

undoList = []
redoList = []

remindMe()

tutorial = 1
tutorialprogress = 0
gameState = "sandbox"
loadState = gameState
responded = False
fliposwitch = True

yesbutton = buttons.button(Color(0,255,0),Rect(0,0,100,70),None,"Yes")
nobutton = buttons.button(Color(255,0,0),Rect(0,0,100,70),None,"No")
wannaBreak = False
#this makes sure that the sand keeps going in a straight line while placing it when it's active, and also some other stuff
try:
    while playingMySandbox:
        yesbutton.box = Rect(screenx/2-110,screeny*0.6,100,70)
        nobutton.box = Rect(screenx/2+10,screeny*0.6,100,70)
        if gameState == "sandbox":
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
                    texts = [
                        font[1].render("Welcome to the sandbox!",1,Color(255,255,255)),
                        font[1].render("Would you like a tutorial?",1,Color(255,255,255))
                    ]
                elif tutorial == 2:
                    for event in pygame.event.get(): #Event Queue but it's heavily restricted and you can only do mouse stuff for now
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            tutorial = 0
                            print("Skipping Tutorial!")
                        if event.type == pygame.MOUSEBUTTONDOWN and tap:
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


                    texts = [
                        font[3].render("Time for the basics of the basics.",1,Color(255,255,255)),
                        font[3].render("Using your mouse, you can click",1,Color(255,255,255)),
                        font[3].render("down and draw on the screen of an",1,Color(255,255,255)),
                        font[3].render("element (You're currently on sand)",1,Color(255,255,255)),
                        font[3].render("Progress: " + str(tutorialprogress//3) + "%",1,Color(255,255,255))
                        
                    ]
                    if tutorialprogress >= 300:
                        tutorialprogress = 0
                        tutorial = 3
                        continue
                elif tutorial == 3:
                    for event in pygame.event.get(): #Event Queue to do very basic sandbox stuff
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            tutorial = 0
                            print("Skipping Tutorial!")
                        if event.type == pygame.MOUSEBUTTONDOWN and tap:
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
                    texts = [
                        font[3].render("Great, if you want to see the sand",1,Color(255,255,255)),
                        font[3].render("move, press the Left Ctrl Button!",1,Color(255,255,255)),
                        font[3].render("(Alternatively you can go single",1,Color(255,255,255)),
                        font[3].render("Steps forward by pressing Space.)",1,Color(255,255,255)),
                        font[3].render("Progress: " + str(tutorialprogress//6) + "%",1,Color(255,255,255))
                    ]
                    if tutorialprogress >= 600:
                        tutorialprogress = 0
                        tutorial = 3
                        continue
            else:
                for event in pygame.event.get(): #Event Queue (or whatever it's called)
                    if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)) and not wannaBreak:
                        texts = [
                            font[1].render("Are you sure you want to quit?",1,Color(255,255,255)),
                            font[3].render("(Be sure to save your sandbox if you haven't!)",1,Color(255,255,255)),
                        ]
                        alive = False
                        wannaBreak = True
                    if event.type == pygame.MOUSEBUTTONDOWN and tap:
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
                        elif event.key == pygame.K_UP:
                            brushsize += 1
                            print("brush size is now", (brushsize*2+1))
                        elif event.key == pygame.K_DOWN:
                            if 0 < brushsize:
                                brushsize -= 1
                                print("brush size is now", (brushsize*2+1))
                        elif event.key == pygame.K_BACKSPACE:
                            remindMe()
                        elif event.key == pygame.K_TAB:
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
                            element = 13
                        elif event.key == pygame.K_t:
                            element = 14
                        elif event.key == pygame.K_y:
                            element = 46
                        elif event.key == pygame.K_u:
                            element = 16
                        elif event.key == pygame.K_i:
                            element = 17
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
                            element = 23
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
                            element = 30
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
                            try:
                                element = int(input("Enter the element ID\n"))
                                try:
                                    print("Set element to", foreverglobals.elementNames[element])
                                except:
                                    print("Set to an unknown element:", element)
                            except:
                                print("THAT'S NOT A VALID NUMBER FOR AN ELEMENT!!!")
                        elif event.key == pygame.K_PERIOD:
                            eyedropper = True
                            print("Pick an element from the sandbox to copy")
                            alive = False
                        
                        
                        #The ultimate thing: SAVING!
                        elif event.key == pygame.K_LSHIFT:
                            gameState = "file saving"
                        #What's the use of saving if you can't LOAD?
                        elif event.key == pygame.K_0:
                            gameState = "file loading"
                                
                        elif event.key == pygame.K_F12:
                            print("Oh, I heard you like dividing by 0! (Crashing intentionally~)")
                            rememberme = True
                            sht = 1/0
            
            clock.tick(60)
            if showfps and fps != int(clock.get_fps()):
                fps = int(clock.get_fps())
                print("fps:", fps)
            
            if live:
                if tutorial == 3:
                    tutorialprogress += 1
                land = doStuff(land,fliposwitch,werealsodoinglife)


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
                    playingMySandbox = False
                elif nobutton.tick(fire,mousePos):
                    wannaBreak = False

            #Where the mouse input matters!
            if (not (tap or tutorial == 1 or wannaBreak)) and fliposwitch:
                if tutorial == 2:
                    tutorialprogress += 1
                x = int(mousePos.x/landyx)
                mx = int((screenx-mousePos.x)/landyx)
                y = int(mousePos.y/landyy)
                for l in range(0-brushsize,1+brushsize):
                    for m in range(0-brushsize,1+brushsize):
                        t = 0
                        try:
                            if eyedropper:
                                element = land[y+l][x+m][0]
                                print("Copied", end = " ")
                                eyedropper = False
                                try:
                                    print(foreverglobals.elementNames[element], end = " ")
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
                                        if element in (13, 30, 56):
                                            t = 5
                                        elif element == 19:
                                            t = random.randint(0,255)
                                        elif element == 54:
                                            t = random.randint(1,6)
                                        elif element == 61:
                                            t = 3
                                        elif element in (64, 65):
                                            t = 20
                                        elif element == 67:
                                            t = 10
                                        land[y+l][x+m] = [element,t]
                                        if mirror:
                                            land[y+l][mx+m] = [element,t]
                        except IndexError:
                            oob += 1

            fire = False
            screen.fill((0,0,0))
            for i in range(len(land)):
                for j in range(len(land[0])):
                    el = land[i][j][0]
                    et = land[i][j][1]
                    if el == 1:
                        pygame.draw.rect(screen,(255,255,0),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 2:
                        pygame.draw.rect(screen,(150,150,150),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 3:
                        pygame.draw.rect(screen,(0,0,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 4:
                        pygame.draw.rect(screen,(250,250,250),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 5:
                        pygame.draw.rect(screen,(100,100,100),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 6:
                        pygame.draw.rect(screen,(200,100,50),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 7:
                        pygame.draw.rect(screen,(150,50,10),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 8:
                        pygame.draw.rect(screen,(0,200,0),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 9:
                        cool = 200+et*10+random.randint(0,50)
                        if cool > 255:
                            cool = 255
                        elif cool < 0:
                            cool = 0
                        pygame.draw.rect(screen,(cool,random.randint(0,50),0),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 10:
                        pygame.draw.rect(screen,(200,200,50),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 11:
                        pygame.draw.rect(screen,(200,200,200),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 12:
                        pygame.draw.rect(screen,(30,20,40),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 13:
                        pygame.draw.rect(screen,(128,200,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 14:
                        pygame.draw.rect(screen,(0,255,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 15:
                        pygame.draw.rect(screen,(0,128,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 16:
                        pygame.draw.rect(screen,(230,230,230),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 17:
                        pygame.draw.rect(screen,(150,90,60),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 18:
                        pygame.draw.rect(screen,(0,128,0),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 19:
                        random.seed(et)
                        pygame.draw.rect(screen,(random.randint(0,50),50+random.randint(0,200),100+random.randint(0,150)),(j*landyx,i*landyy,landyx,landyy))
                        random.seed()
                    elif el == 20:
                        pygame.draw.rect(screen,(255,255,128),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 21:
                        pygame.draw.rect(screen,(10,60,180),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 22:
                        pygame.draw.rect(screen,(240,250,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 23:
                        pygame.draw.rect(screen,(200,255,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 24:
                        pygame.draw.rect(screen,(240,220,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 25:
                        pygame.draw.rect(screen,(100,200,230),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 26:
                        pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 27:
                        pygame.draw.rect(screen,(170,210,250),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 28:
                        if et == 0:
                            pygame.draw.rect(screen,(40,20,10),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(0,255,0),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 29:
                        pygame.draw.rect(screen,(24,24,24),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 30:
                        cool = 200+et*10
                        if cool > 255:
                            cool = 255
                        cooler = random.randint(50,100+et*random.randint(20,30))
                        if cooler > 255:
                            cooler = 255
                        pygame.draw.rect(screen,(cool,cooler,0),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 31:
                        pygame.draw.rect(screen,(140,70,30),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 32:
                        cool = 100-et//2
                        pygame.draw.rect(screen,(cool,cool,cool),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 33:
                        cool = 0
                        if et != 0:
                            cool = 100+random.randint(-20,20)
                        pygame.draw.rect(screen,(100+cool,cool//2,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 34:
                        pygame.draw.rect(screen,(160,170,180),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 35:
                        pygame.draw.rect(screen,(10,10,10),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 36:
                        colour = (255,255,255)
                        if et == 1:
                            colour = (255,0,0)
                        elif et == 2:
                            colour = (255,128,0)
                        elif et == 3:
                            colour = (255,255,0)
                        elif et == 4:
                            colour = (128,255,0)
                        elif et == 5:
                            colour = (0,255,0)
                        elif et == 6:
                            colour = (0,255,128)
                        elif et == 7:
                            colour = (255,255,255)
                        elif et == 8:
                            colour = (0,128,255)
                        elif et == 9:
                            colour = (0,0,255)
                        elif et == 8:
                            colour = (128,0,255)
                        elif et == 9:
                            colour = (255,0,255)
                        elif et == 10:
                            colour = (128,0,255)
                        elif et == 11:
                            colour = (128,128,128)
                        pygame.draw.rect(screen,colour,(j*landyx,i*landyy,landyx,landyy))
                    elif el == 37:
                        pygame.draw.rect(screen,(random.randint(0,250),random.randint(0,100),random.randint(150,250)),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 38:
                        if et == 1:
                            pygame.draw.rect(screen,(255,255,20),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(180,180,170),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 39:
                        if et == 1:
                            pygame.draw.rect(screen,(255,255,20),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(200,200,190),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 40:
                        if et == 1:
                            pygame.draw.rect(screen,(255,255,20),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(200,200,150),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 41:
                        cool = 0
                        if et != 0:
                            cool = random.randint(-20,20)
                        pygame.draw.rect(screen,(100,20+cool//2,240),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 42:
                        cool = 0
                        if et != 0:
                            cool = random.randint(-50,50)
                        pygame.draw.rect(screen,(200+cool,50+cool,50+cool),(j*landyx,i*landyy,landyx,landyy))
                    
                    elif el == 43:
                        if coinflip():
                            pygame.draw.rect(screen,(255,255,0),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(255,255,128),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 44:
                        pygame.draw.rect(screen,(180,130,100),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 45:
                        pygame.draw.rect(screen,(60,30,15),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 46:
                        pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 47:
                        if random.randint(1,111) == 1 and et == 1:
                            pygame.draw.rect(screen,(255,255,0),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(128,128,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 48:
                        pygame.draw.rect(screen,(200,230,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 49:
                        if et < 0:
                            et = 0
                        elif et > 10:
                            et = 10
                        pygame.draw.rect(screen,(et*20,150-et*10,0),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 50:
                        if fliposwitch:
                            pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(255,0,0),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 51:
                        pygame.draw.rect(screen,(0,0,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 52:
                        pygame.draw.rect(screen,(105,105,105),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 53:
                        pygame.draw.rect(screen,(255,255,0),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 54:
                        if et == 1:
                            pygame.draw.rect(screen,(255,255,0),(j*landyx,i*landyy,landyx,landyy))
                        elif et == 2:
                            pygame.draw.rect(screen,(150,150,150),(j*landyx,i*landyy,landyx,landyy))
                        elif et == 3:
                            pygame.draw.rect(screen,(0,0,255),(j*landyx,i*landyy,landyx,landyy))
                        elif et == 4:
                            pygame.draw.rect(screen,(250,250,250),(j*landyx,i*landyy,landyx,landyy))
                        elif et == 5:
                            pygame.draw.rect(screen,(100,100,100),(j*landyx,i*landyy,landyx,landyy))
                        elif et == 6:
                            pygame.draw.rect(screen,(200,100,50),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(255,0,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 55:
                        pygame.draw.rect(screen,(255,200+random.randint(0,55),200+random.randint(0,55)),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 56:
                        pygame.draw.rect(screen,(et*5,et*5,et*5),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 57:
                        pygame.draw.rect(screen,(100,20+random.randint(-20,20)//2,240),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 58:
                        if et == 1:
                            pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(240,230,0),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 59:
                        pygame.draw.rect(screen,(25,25,30),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 60:
                        pygame.draw.rect(screen,(random.randint(0,50),random.randint(25,255),random.randint(0,50)),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 61:
                        if et == 0:
                            pygame.draw.rect(screen,(64,64,64),(j*landyx,i*landyy,landyx,landyy))
                        elif et == 1:
                            pygame.draw.rect(screen,(128,128,128),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 62:
                        if et == 0:
                            pygame.draw.rect(screen,(32,24,16),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(140,70,30),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 63:
                        pygame.draw.rect(screen,(130,80,60),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 64:
                        pygame.draw.rect(screen,(170,250,190),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 65:
                        pygame.draw.rect(screen,(0,255,0),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 66:
                        pygame.draw.rect(screen,(random.randint(0,20),200+random.randint(0,20),random.randint(0,20)),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 67:
                        pygame.draw.rect(screen,(random.randint(150,255),random.randint(50,230),random.randint(0,40)),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 68:
                        pygame.draw.rect(screen,(200,0,0),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 69:
                        if et == 1:
                            pygame.draw.rect(screen,(255,random.randint(0,255),random.randint(0,255)),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(200,180,150),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 70:
                        pygame.draw.rect(screen,(80,100,60),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 71:
                        if et != 0:
                            pygame.draw.rect(screen,(200,255,230),(j*landyx,i*landyy,landyx,landyy))
                        else:
                            pygame.draw.rect(screen,(200,200,255),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 72:
                        pygame.draw.rect(screen,(120-et,60-(et//5),10-(et//10)),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 73:
                        pygame.draw.rect(screen,(20,20,20),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 74:
                        pygame.draw.rect(screen,(60,30,15),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 75:
                        pygame.draw.rect(screen,(0,random.randint(100,200),random.randint(30,100)),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 76:
                        pygame.draw.rect(screen,(255,150,120),(j*landyx,i*landyy,landyx,landyy))
                    elif el == 77:
                        pygame.draw.rect(screen,(200,150,60),(j*landyx,i*landyy,landyx,landyy))


                    else:
                        if el != 0:
                            pygame.draw.rect(screen,(255,0,255),(j*landyx,i*landyy,landyx,landyy))
            
            
            pygame.draw.rect(screen,(255,255,255),(mousePos.x-(landyx/2)*brushsize*2,mousePos.y-(landyy/2)*brushsize*2,landyx*(brushsize*2+1),landyy*(brushsize*2+1)),2)

            if tutorial != 0 or wannaBreak:
                for l in range(len(texts)):
                    screen.blit(texts[l],Vector2(20, 10+40*l))
            
            #Render the yes and no buttons
            if tutorial == 1 or wannaBreak:
                yesbutton.render(screen)
                nobutton.render(screen)


            if not alive:
                live = False
            pygame.display.flip()
        elif "file" in gameState:
            
            appendkey = keyboard()
            if appendkey != "":
                changeScreen = True
            
            if appendkey == "end":
                appendkey = ""
                doingafilething = True
            elif appendkey == "back":
                    appendkey = ""
                    if len(filename) > 0:
                        filename = filename[:-1]
            elif appendkey == "fullback":
                    appendkey = ""
                    filename = ""
            elif appendkey == "\"":
                appendkey = ""
            
            if appendkey == "/" and ((len(filename) > 0 and filename[-1] == "/") or len(filename) <= 0):
                appendkey = ""

            filename += appendkey


            if "saving" in gameState:
                texts = [
                    font[1].render("What would you like to save your sandbox as?",1,Color(0,0,0)),
                    font[1].render(str(filename),1,Color(0,0,0))
                ]
            elif "loading" in gameState:
                texts = [
                    font[1].render("What is the filename of the save you want to load?",1,Color(0,0,0)),
                    font[1].render(str(filename),1,Color(0,0,0))
                ]
            else:
                gameState = "sandbox"
                continue
            
            if doingafilething:
                if "loading" in gameState:
                    undoList.append(deepcopy(land))
                    backupx = landx
                    backupy = landy
                    bacnupsx = screenx
                    backupsy = screeny
                    backupland = deepcopy(land)
                    fail = True
                    print("Loading", filename+ ".txt from your saves folder...")
                    try:
                        if usesavefolder:
                            thefile = open('sandsaves/'+filename+'.txt', 'r')
                        else:
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
                        print("Try again with a file that exists. (Maybe you don't have any :/))")
                    except TypeError as e:
                        print(f'An error occured: {e}')
                        print("Your file might have more than just numbers in it.")
                    except IndexError as e:
                        print(f'An error occured: {e}')
                        print("It's possible your grid isn't matching up with the data in a way!")
                    except Exception as x:
                        print(f'An error occured, but it\'s complicated: {x}')
                        print("Please contact the creator of this sandbox to see what the issue could be")
                    if fail:
                        undoList.pop()
                        landx = backupx
                        landy = backupy
                        screenx = bacnupsx
                        screeny = backupsy
                        land = deepcopy(backupland)
                        screen = pygame.display.set_mode((screenx,screeny))
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
                    except FileNotFoundError as e:
                        print(f'An error occured: {e}')
                        print("Maybe you don't have a sandsaves folder for the saves to go to. (You'll have to make it manually)")
                    except:
                        print(f'An error occured, but we don\'t know how!')
                        print("Please contact the creator of this sandbox to see what the issue could be")
                gameState = "sandbox"
                filename = ""
                continue

            if changeScreen:
                screen = pygame.display.set_mode((600,450))
                
                screen.fill((255,255,255))
                
                for l in range(len(texts)):
                    screen.blit(texts[l],Vector2(10, 10+30*l))
                pygame.display.flip()
            changeScreen = False
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
except Exception as x:
    print("A fatal error occured durring the sandbox!")
    print(random.choice(foreverglobals.crashSplash))
    if rememberme:
        print("You caused it by hitting the F12 key, you silly billy")
    else:
        print("Here's what happened, share this for a bug fix maybe.")
        print(x)
    print("Saving your last instance to a backup file")
    t = time.localtime()
    h = []
    for _ in t:
        h.append(str(_))
    h = "".join(h)
    try:
        if usesavefolder:
            thefile = open('sandsaves/backup'+h+'.txt', 'w')
        else:
            thefile = open('backup'+h+'.txt', 'w')
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
    except:
        print("Oh great, another error! Backup failed I guess")
    