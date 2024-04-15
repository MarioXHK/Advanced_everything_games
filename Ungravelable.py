import pygame
import random
from pygame.math import Vector2

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("gravel")
clock = pygame.time.Clock()

#create a buncha empty lists
sizes1 = []
positions1 = []
colors1 = []

class gravel:
    def __init__(self):
        self.pos = Vector2(random.randrange(0, 800),random.randrange(0, 800))
        self.size = random.randrange(5,10)
        self.alpha = random.randrange(100,255)
        self.color = [self.alpha,self.alpha,self.alpha]
        self.r = True
        self.g = True
        self.b = True
        self.dir = Vector2(random.random()-0.5,random.random()-0.5)
        self.timetime = random.randint(1,300)
    def shake(self,strength = 1):
        if strength == 0:
            return
        self.timetime -= 1
        for i in range(strength):
            rng = Vector2((random.random()-0.5)/2,(random.random()-0.5)/2)
            self.pos += self.dir + rng
        if self.timetime <= 0:
            self.dir = Vector2(random.random()-0.5,random.random()-0.5)
            self.timetime = random.randint(1,150)
    def killColors(self):
        self.r = False
        self.g = False
        self.b = False
    def checks(self, rects, color):
        for rectangle in rects:
            if self.pos[0] >= rectangle[0] and self.pos[0] <= rectangle[0]+rectangle[2] and self.pos[1] >= rectangle[1] and self.pos[1] <= rectangle[1]+rectangle[3]:
                if color == "r":
                    self.r = True
                    return
                elif color == "g":
                    self.g = True
                    return
                elif color == "b":
                    self.b = True
                    return
    def updateColor(self):
        if self.r:
            self.color[0] = self.alpha
        else:
            self.color[0] = 0
        if self.g:
            self.color[1] = self.alpha
        else:
            self.color[1] = 0
        if self.b:
            self.color[2] = self.alpha
        else:
            self.color[2] = 0
    def draw(self, box):
        pygame.draw.circle(box, self.color, self.pos, self.size)


gravelio = [gravel() for i in range(4000)]

ree = 1
shaking = False
sand = True
undate = False

while sand: #game loop###########################################################
    for event in pygame.event.get(): #Your input!
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sand = False
        if event.type == pygame.KEYDOWN:
            #Pressing the space will allow you to shake up the gravel
            if event.key == pygame.K_SPACE:
                shaking = True
            #Pressing left ctrl will allow you to see what happens if the gravel doesn't change colors
            if event.key == pygame.K_LCTRL:
                undate = True
            #Pressing a number from 1-9 changes the gravel's speed depending on what number you press
            if event.key == pygame.K_1:
                ree = 1
            if event.key == pygame.K_2:
                ree = 2
            if event.key == pygame.K_3:
                ree = 3
            if event.key == pygame.K_4:
                ree = 4
            if event.key == pygame.K_5:
                ree = 5
            if event.key == pygame.K_6:
                ree = 6
            if event.key == pygame.K_7:
                ree = 7
            if event.key == pygame.K_8:
                ree = 8
            if event.key == pygame.K_9:
                ree = 9
            if event.key == pygame.K_0:
                ree = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shaking = False
            if event.key == pygame.K_LCTRL:
                undate = False
    clock.tick(60)

    for i in gravelio:
        if shaking:
            i.shake(ree)
        if not undate:
            #The Gravel will update if you've pressed space and it will change by a small bit, always checking if it's in the lil zones if ctrl isn't pressed
            i.killColors()
            i.checks([[200,200,100,100],[300,300,100,100],[0,200,200,200],[0,0,200,200],[0,400,400,400]],"b")
            i.checks([[200,200,100,100],[300,300,100,100],[0,200,200,200],[200,0,200,200],[400,0,400,400]],"g")
            i.checks([[200,200,100,100],[300,300,100,100],[200,0,200,200],[0,0,200,200],[400,400,400,400]],"r")
            i.updateColor()
            #The gravel will change to different colors depending on where it is, and thus, the output is what you see visually


    #render section------------------------------
    
    screen.fill((0,0,0))# Clear the screen

    #draw the lines on the screen
    pygame.draw.line(screen, (100,100,100), (400, 0), (400, 800), 2)
    pygame.draw.line(screen, (100,100,100), (0, 400), (800, 400), 2)

    #draw the gravel
    for i in gravelio:
        i.draw(screen)
    
    pygame.display.flip()# Update the display

#end of game loop###################################################################
pygame.quit()