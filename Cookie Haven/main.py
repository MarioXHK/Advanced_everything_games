#Cookie variables (REALLY IMPORTANT)
#How many cookies you have
cookies: int = 0
#Cookies but float (If this hits more than 1, it'll do a cool)
precookies: float = 0

#Importing Libraries
import pygame
import random
import clickers

#Vector 2 pogg
from pygame import Vector2
from workers import worker

#Initializing pygame variables
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Cookie Clicker 2: Cookie Haven")

#Loading music
music = pygame.mixer.music.load("Cookie Haven/click.mp3")
pygame.mixer.music.play(-1)

#While this is true, the game is gaming
cursoring = True

#Big cookie
big_cookie = clickers.cookie("cc",Vector2(200,400),150)

#Workers (autoclickers)
buildings = [
    worker(
        0.1,
        15,
        "Cursor",
        "Autoclicks once every 10 seconds (If you're using a real autoclicker that's cheating)"
        ),
    worker(
        1,
        100,
        "Grandparent",
        "Cooks cookies with love"
        ),
    worker(
        8,
        1100,
        "Garden",
        "Grows a variety cookie based plants from cookie seeds"
        ),
    worker(
        50,
        13000,
        "Mine",
        "Mines out cookie dough and chocolate chip deposits"
        ),
    worker(
        300,
        135000,
        "Factory",
        "Produces large quantities of cookies hot off the production line"
        ),
    worker(
        1400,
        1400000,
        "Bank",
        "Generates cookie equity from interest"
        ),
    worker(
        8000,
        21000000,
        "Monument",
        "Full of precious chocolate from times before even Grandparents"
        ),
    worker(
        45000,
        333000000,
        "Chemistry Lab",
        "Uses chemistry to artificially create cookies from strange chemicals that probably shouldn't be ingested"
        ),
    worker(
        250000,
        5000000000,
        "Magicworks",
        "Summons cookies with magical means"
        ),
    worker(
        1600000,
        75000000000,
        "Lunar Collector",
        "Brings in fresh cookies from cookie moons far far away"
        ),
    worker(
        10000000,
        1000000000000,
        "Cookie Accelerator",
        "Accelerates cookies into eachother very fast to create even more cookies"
        ),
    worker(
        65000000,
        14000000000000,
        "Wormhole",
        "Opens portals that lead to universes filled to the brim with cookies"
        ),
    worker(
        420000000,
        160000000000000,
        "Wishing Star",
        "Uses the power of wishes to wish cookies into existence"
        ),
    worker(
        3000000000,
        2300000000000000,
        "RNG Manipulation",
        "Generates cookies out of thin air through 'luck'"
        ),
    worker(
        21000000000,
        24500000000000000,
        "Fractal Engine",
        "Takes cookies and creates more cookies from those cookies"
        ),
    worker(
        150000000000,
        310000000000000000,
        "Time Machine",
        "Brings cookies from the past and future before they were eaten"
        ),
    worker(
        1000000000000,
        7000000000000000000,
        "Cortex Baker",
        "Planet sized beings that constantly imagine cookies into existence"
        ),
    worker(
        8700000000000,
        12000000000000000000,
        "Void Dimension",
        "A void dimension that can be used to store many more cookies, and in itself can make cookies"
        ),
    worker(
        64000000000000,
        1984000000000000000000,
        "Python Console",
        "Creates cookies from the very code this game was written in"
        ),
    worker(
        510000000000000,
        540000000000000000000000,
        "Clone Copy",
        "You alone are the reason behind all of these cookies, now imagine if there were more"
        ),
    worker(
        3400000000000000,
        340000000000000000000000000,
        "Idlemultiverse",
        "There's several other idle games running along side this one, and now you can hijack their multiverses and convert whatever they're making into cookies"
        ),
    worker(
        12345678900000000,
        999990000000000000000000000000,
        "Beyond",
        "An incomprehensible way to make even more cookies"
        ),
    worker(
        87000000000000000,
        6410000000000000000000000000000000,
        "Infinity Cookie",
        "Siphons cookies right out of infinity itself, making for an almost unlimited source of cookies"
        ),
    worker(
        922337203685477807,
        340282366920938463463374607431768211456,
        "Overflowinator",
        "Fills in all the empty spaces in existence with cookies, and then makes even more cookies"
        ),
    worker(
        79000000000000000000,
        100000000000000000000000000000000000000000000000000,
        "Omega Black Hole Bomb",
        "Takes full advantage of black holes with the mass of several multiverses and converts it all into cookies"
        ),
    worker(
        0,
        10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        "Zero",
        "The very final thing this game can give you. If you've managed to buy even at least one of these, then you win."
        )
    ]

#bool to hold if the mouse is held
held = False
#bool to hold if the mouse has been tapped
tap = False
#The mouse pos on the screen
mousePos = (0,0)
#bool to hold if the mouse has been tapped and hasn't been released
tapped = False
#mouse wheel scrolling direction
wheel = 0
#If the mouse wheel is being used
wheeled = False

#frames per second
fps = 60

print("Starting game")
while cursoring:
    #The input you have
    wheeled = False
    tap = False
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
        if event.type == pygame.MOUSEWHEEL:
            wheeled = True
            wheel = event.y
    
    #Adding cookies!
    
    
    
    clock.tick(fps)

    if big_cookie.tick(tap,mousePos):
        cookies += 1
        print("Clicked!")
    
    
    screen.fill((238,204,119))
    
    big_cookie.render(screen)

    pygame.display.flip()
pygame.quit()