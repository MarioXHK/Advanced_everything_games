import pygame #bring in pygame library
import random
pygame.init #initialize pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 900)) #create game screen
pygame.display.set_caption("You had one job...") #window title
hello_world = True
class pineapple:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.spen = 1
    def draw(self,scren):
        for i in range(20):
            points = ((self.x-200-i*5,self.y-400+i*5), (self.x+200-i*15,self.y-400+i*15), (self.x+400-i*15,self.y-200+i*15), (self.x+400-i*5,self.y+200+i*5),(self.x+200+i*5,self.y+400-i*5),(self.x-200+i*15,self.y+400-i*15),(self.x-400+i*15,self.y+200-i*15),(self.x-400+i*5,self.y-200-i*5))
            if self.spen >= 3:
                self.spen = 0
            if i % 3 != self.spen:
                pygame.draw.polygon(scren, (10,170,10),points)
            else:
                pygame.draw.polygon(scren, (70,200,70),points)
        pygame.draw.circle(scren,(70,40,0),(self.x-300,self.y-300),20)
tree = pineapple(450,450)
print("Wait a minute, this isn't a pineapple. THIS IS A WATERMELON!")
while hello_world:
    #The little input you have
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            hello_world = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tree.spen += 1
    #Render the pinapple!
    screen.fill((0,0,0))
    tree.draw(screen)
    pygame.display.flip()