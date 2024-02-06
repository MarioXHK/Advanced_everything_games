import pygame
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
import random
from pygame import Vector2

class button:
    def __init__(self,color: tuple[int],rectangle: list, boardercolor: tuple[int] = (256,-7,69), text: str = "",textcolor: tuple[int] = (0,0,0)):
        self.color = color
        self.box = rectangle
        self.text = font.render(str(text), 1, textcolor)
        if 256 in boardercolor:
            self.bc = color
        else:
            self.bc = boardercolor
        self.clicked = False
        self.hover = False
        self.moff = [0,0]
    def tick(self,mdown: bool,mousePos: Vector2) -> bool:
        if mousePos[0] >= self.box[0] and mousePos[0] <= self.box[0]+self.box[2] and mousePos[1] >= self.box[1] and mousePos[1] <= self.box[1]+self.box[3]:
            self.hover = True
            if mdown:
                if not self.clicked:
                    self.moff[0] = mousePos[0] - self.box[0]
                    self.moff[1] = mousePos[1] - self.box[1]
                self.clicked = True
                return True
        else:
            self.hover = False
        self.clicked = False
        return False
    def drag(self,mousePos: Vector2):
        if self.clicked:
            self.box[0] = mousePos[0] - self.moff[0]
            self.box[1] = mousePos[1] - self.moff[1]
    def render(self,screen: pygame.surface):
        pygame.draw.rect(screen,self.color,self.box)
        if self.hover:
            pygame.draw.rect(screen,self.bc,self.box,5)

class circleButton:
    def __init__(self,color: tuple[int],position: Vector2, radius: float, boardercolor: tuple[int] = (256,-7,69), text: str = "",textcolor: tuple[int] = (0,0,0)):
        self.color = color
        self.rad = radius
        self.pos = position
        self.text = font.render(str(text), 1, textcolor)
        if 256 in boardercolor:
            self.bc = color
        else:
            self.bc = boardercolor
        self.clicked = False
        self.hover = False
        self.moff = Vector2(0,0)
    def tick(self,mdown: bool,mousePos: Vector2) -> bool:
        if self.rad > self.pos.distance_to(mousePos):
            self.hover = True
            if mdown:
                if not self.clicked:
                    self.moff = mousePos - self.pos
                self.clicked = True
                return True
        else:
            self.hover = False
        self.clicked = False
        return False
    def drag(self,mousePos: Vector2):
        if self.clicked:
            self.pos = mousePos - self.moff
    def render(self,screen: pygame.surface):
        pygame.draw.circle(screen,self.color,self.pos)
        if self.hover:
            pygame.draw.rect(screen,self.bc,self.pos,5) 

class cookie(circleButton):
    def __init__(self,cookieType: str,position: Vector2, radius: float, seed = random.randint(0,1000000000)):
        self.seed = seed
        self.kind = cookieType.lower()
        self.rad = radius
        self.pos = position
        self.clicked = False
        self.hover = False
        self.moff = Vector2(0,0)
    def tellMeType(self,technical):
        print("I'm a", end = " ")
        if self.kind == "cc":
            print("Chocolate Chip")
        print(" Cookie.")
        if technical:
            print("("+self.kind+") technical ID")
    def render(self,screen: pygame.surface):
        tempRad = self.rad
        if self.hover:
            tempRad *= 0.95

        random.seed(self.seed)
        colors = [(200,200,200),(200,200,200),(200,200,200),(200,200,200),(200,200,200)]
        if self.kind == "cc":
            colors[0] = (187,136,85)
            colors[1] = (170,119,51)
            colors[2] = (85,51,17)

        pygame.draw.circle(screen,colors[0],self.pos,tempRad)
        pygame.draw.circle(screen,colors[1],self.pos,tempRad,10)
        
        if self.kind == "cc":
            for i in range(random.randint(1,10)):
                pygame.draw.circle(screen,colors[2],((random.random()-0.5)*(tempRad*1.1),(random.random()-0.5)*(tempRad*1.1))+self.pos,(random.randint(5,10)*tempRad)/50)


        random.seed()