#Can someone please tell me how to give more resources to this app so I can throttle it and have a smooth 60 fps while my computer combusts into flames
#Some optimization help would be nice too
showfps = False
#the setting that controls if you'd like to do life or not (Experimental sorta)

oob = 0

import os
import pygame
from pygame import Vector2
#WHY DOES YOU NOT EVEN THE AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
from copy import deepcopy
import random
import time
import foreverglobals

#I caved
from physics import coinflip
from physics import checkEverywhere
from doing import doStuff


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
breaking=True
clock = pygame.time.Clock()

#mouse variables--------------------------------
mousePos = Vector2(0,0)
fire = False
tap = True

#Element Variables

element = 1
brushsize = 0



werealsodoinglife = False
eyedropper = False
dither = False
elementary = False
elements = []
mirror = False




# ===============================================================================================
# ===================================== THE SETUP LOOP ==========================================
# ===============================================================================================



yeses = ("y","yes","yeah","do it","sure","alright","ok","ig","i guess","yay","pull the lever, cronk!","alrighty then","whatever","heck yes","hell yes","probably","ye","yea","yeah!","oh yes","i don't see why not","i dont see why not","the opposite of no","yep","yes sir","yessir","please do","do","1","i'd love to","i'd love to try it out","let's see what you've got","let's-a go!","lets a go","let's a go","lets a go!","mushroom kingdom here we come","may","smash","yeah, sure","yesure","let's kick bubblegum","activate","throttle","upgrade","proceed","bb","shure","surry boi","surry","yes please","yes maam","yes hoobaab")
noes = ("n","no","nah","nay","nein","it's opposite day","don't you dare","poop","do not","do not the cat","perish","hell no","heck no","probably not","jumpscare","no!","no!!","no!!!","mmm...","how could you screw it up this badly?","the opposite of yes","nope","not even close","please don't","don't","0","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","unrun","kill","oh no","ho ho ho ho no","steamed hams","nada","nay","pass","t_t","i'm sick rn","not today","chewing bubblegum","deactivate","turn back","i said turn back","snowgrave","die","di","noooooooooo","b","lmao nah","nada","zilch","q","no please","no thank you","no thanks")

screenx: int = 500
screeny: int = 500

landx: int = 50
landy: int = 50

setup = True


unanswered = True
print("Would you like to setup your own sandbox space?")
while unanswered:
    unanswered = False
    answer = input().lower()
    if answer in noes:
        print("Alright, default sandbox it is.")
        setup = False
    elif answer in yeses:
        print("Alright, let's get to setting your sandbox up!")
        setup = True
    else:
        print("Answer unrecognized, try again")
        unanswered = True

if setup:
    print("Setup your sandbox! (You can skip this and be default by putting in junk values)")

while breaking and setup:
    d = 0
    for event in pygame.event.get(): #Event Queue (or whatever it's called)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            breaking = False
    
    #Screen variables
    
    try:
        screenx = int(input("What should the window's size be in pixels horizontally?\n"))
        screeny = int(input("What should the window's size be in pixels vertically?\n"))
    except:
        print("That's not a number! Setting window size to default!")
        screenx = 500
        screeny = 500

    try:
        landx = int(input("How long should the sandbox be in units?\n"))
        landy = int(input("How tall should the sandbox be in units?\n"))
    except:
        print("That's not a number! Setting sandbox size to default!")
        landx = screenx//10
        landy = screeny//10


    landyx = (screenx/landx)
    landyy = (screeny/landy)

    screen.fill((0,0,0))

    screen = pygame.display.set_mode((screenx,screeny))

    for i in range(landy):
        for j in range(landx):
            pygame.draw.rect(screen,(255,255,255),(j*landyx,i*landyy,landyx,landyy),1)

    pygame.display.flip()
    print("You should now see a preview of the sandbox that you're about to unfold.\nIs this ok?")
    unanswered = True
    while unanswered:
        unanswered = False
        answer = input().lower()
        if answer in noes:
            print("Alright, let's try again.")
        elif answer in yeses:
            print("Alright, creating the sandbox now!")
            setup = False
        else:
            print("Answer unrecognized, try again")
            unanswered = True




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

sandstack = []
restack = []

remindMe()

fliposwitch = True
#this makes sure that the sand keeps going in a straight line while placing it when it's active, and also some other stuff

while breaking:
    d = 0
    for event in pygame.event.get(): #Event Queue (or whatever it's called)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            if input("Are you sure you want to quit?\n").lower() in yeses:
                breaking = False
        if event.type == pygame.MOUSEBUTTONDOWN and tap:
            sandstack.append(deepcopy(land))
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
                    sandstack.append(deepcopy(land))
                    restack = []
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
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
            elif event.key == pygame.K_RALT:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[3,0] for _ in range(landx)]
            elif event.key == pygame.K_RCTRL:
                sandstack.append(deepcopy(land))
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[15,0] for _ in range(landx)]
            elif event.key == pygame.K_END:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[9,0] for _ in range(landx)]
            elif event.key == pygame.K_DELETE:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[65,20] for _ in range(landx)]
            elif event.key == pygame.K_HOME:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[29,0] for _ in range(landx)]
            elif event.key == pygame.K_PAGEUP:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[71,0] for _ in range(landx)]
            elif event.key == pygame.K_PAGEDOWN:
                sandstack.append(deepcopy(land))
                restack = []
                land = [[[0,0] for _ in range(landx)] for i in range(landy)]
                for u in range(10):
                    land[u] = [[75,0] for _ in range(landx)]
            elif event.key == pygame.K_NUMLOCK:
                sandstack.append(deepcopy(land))
                restack = []
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
                
                if len(restack) > 0:
                    sandstack.append(deepcopy(land))
                    land = restack.pop()
            elif event.key == pygame.K_LEFTBRACKET:
                if len(sandstack) > 0:
                    restack.append(deepcopy(land))
                    land = sandstack.pop()
            
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
            elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                alive = False
                print("What would you like to name your file? (If it's a save that already exists, it will override the save)")
                filename = input()
                legal = True
                for char in foreverglobals.illegals:
                    if char in filename:
                        print("File cannot contain an illegal character!", foreverglobals.illegals)
                        legal = False
                        break
                if legal:
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
            #What's the use of saving if you can't LOAD?
            elif event.key == pygame.K_0:
                alive = False
                print("What file would you like to load?")
                filename = input()
                legal = True
                for char in foreverglobals.illegals:
                    if char in filename:
                        print("File cannot contain an illegal character!", foreverglobals.illegals)
                        legal = False
                        break
                if legal:
                    sandstack.append(deepcopy(land))
                    backupx = landx
                    backupy = landy
                    bacnupsx = screenx
                    backupsy = screeny
                    backupland = deepcopy(land)
                    backupscreen = screen
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
                    except:
                        print(f'An error occured, but we don\'t know how!')
                        print("Please contact the creator of this sandbox to see what the issue could be")
                    if fail:
                        sandstack.pop()
                        landx = backupx
                        landy = backupy
                        screenx = bacnupsx
                        screeny = backupsy
                        land = deepcopy(backupland)
                        screen = backupscreen
    
    clock.tick(60)
    if showfps and fps != int(clock.get_fps()):
        fps = int(clock.get_fps())
        print("fps:", fps)
    
    if live:
        land = doStuff(land,fliposwitch,werealsodoinglife)


    if fliposwitch and alive:
        fliposwitch = False
    else:
        fliposwitch = True

    if (not tap) and fliposwitch:
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
            
            else:
                if el != 0:
                    pygame.draw.rect(screen,(255,0,255),(j*landyx,i*landyy,landyx,landyy))
            
    if not alive:
        live = False
    pygame.display.flip()
pygame.quit()
print("Process exit with code: \"Pee pee poo poo caca do do fart we wa woooooo\"")
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