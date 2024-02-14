#Cookie variables (REALLY IMPORTANT)
#How many cookies you have
cookies: int = 0
#Cookies but float (If this hits more than 1, it'll do a cool)
precookies: float = 0

#Importing Libraries
import pygame
import random

#Vector 2 pogg
from pygame import Vector2

#My own libraries <3
import clickers
import workers
from workers import worker

#I blame declan for this conondrom
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.color import Color

#Initializing pygame variables
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Cookie Clicker 2: Cookie Haven")

#Loading music
music = pygame.mixer.music.load("click.mp3")
pygame.mixer.music.play(-1)

#While this is true, the game is gaming
cursoring = True

#Big cookie
big_cookie = clickers.cookie("cc",Vector2(200,400),150)

font = pygame.font.SysFont('Comic Sans MS', 30)

#CPS, cookies per second
cps = 0

cookieText = font.render("Cookies: " + str(cookies), False, (250,250,250),(85,51,17))
cpsText = font.render("Cookies Per Second: " + str(cps), False, (250,250,250),(85,51,17))


#Workers (autoclickers)
buildings = workers.default[:]

buildButtons = [clickers.button(Color(221,153,85),Rect(400,10+i*100,800,90),Color(85,51,17),str(buildings[i].count) + " " + buildings[i].name + "(s)    Cost: " + str(buildings[i].getPrice()),Color(255,255,255)) for i in range(len(buildings))]


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

    for b in range(len(buildButtons)):
        if buildButtons[b].tick(tap,mousePos):
            if buildings[b].getPrice() <= cookies:
   
                cookies -= buildings[b].buy()

                buildButtons[b].text = str(buildings[b].count) + " " + buildings[b].name + "(s)    Cost: " + str(buildings[b].getPrice())
            
    cps = 0
    for b in buildings:
        #Adding cookies from buildings to total
        cookies += int(b.giveCookies()/fps)
        #Makes it so that 0.1 cps works (Adds all the stuff after the . to a new variable)
        precookies += (b.giveCookies()/fps)%1
        #If that variable is greater than 1, then it will add an int version of itself to cookies
        if precookies >= 1:
            cookies += int(precookies)
            #Then it will go back to not having anything
            precookies -= int(precookies)
        cps += b.giveCookies()
    #print(cps)

    

    if big_cookie.tick(tap,mousePos):
        cookies += 1
        print("Clicked!")
    

    if wheeled:
        for bb in buildButtons:
            bb.box.topleft = (bb.box.topleft[0],bb.box.topleft[1]+wheel*20)



    #It's rendering time
    screen.fill((238,204,119))
    
    for bb in buildButtons:
        bb.render(screen)


    cookieText = font.render("Cookies: " + str(cookies), False, (250,250,250),(85,51,17))
    cpsText = font.render("Cookies Per Second: " + str(cps), False, (250,250,250),(85,51,17))
    screen.blit(cookieText, (50,50))
    screen.blit(cpsText, (50,100))

    big_cookie.render(screen)
    #Renders all over the place
    pygame.display.flip()
pygame.quit()