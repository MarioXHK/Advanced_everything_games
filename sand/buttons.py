import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.color import Color
pygame.font.init()
font = (
    pygame.font.Font("PressStart2P.ttf", 30),
    pygame.font.SysFont('Comic Sans MS', 30),
    pygame.font.SysFont('Comic Sans MS', 15),
    pygame.font.SysFont('Comic Sans MS', 20),
    pygame.font.Font("PressStart2P.ttf", 20)
    )

class button:
    def __init__(self,color: Color,rectangle: Rect, boardercolor: Color | None = None, text: str | None = None,textcolor: Color = Color(0,0,0),whichfont: int = 1):
        self.color = color
        self.box = rectangle
        if text != None:
            self.text = font[whichfont].render(str(text), 1, textcolor)
        else:
            self.text = None
        if boardercolor == None:
            self.bc = color
        else:
            self.bc = boardercolor
        self.clicked = False
        self.hover = False
        self.moff = Vector2(0,0)
    def tick(self,mdown: bool,mousePos: Vector2) -> bool:
        if mousePos.x >= self.box[0] and mousePos.x <= self.box[0]+self.box[2] and mousePos.y >= self.box[1] and mousePos.y <= self.box[1]+self.box[3]:
            self.hover = True
            if mdown:
                if not self.clicked:
                    self.moff.x = mousePos.x - self.box.x
                    self.moff.y = mousePos.y - self.box.y
                self.clicked = True
                return True
        else:
            self.hover = False
        self.clicked = False
        return False
    def basicTick(self,mdown: bool,mousePos: Vector2) -> bool:
        #Tick without all the variable changing guff
        if mousePos.x >= self.box[0] and mousePos.x <= self.box[0]+self.box[2] and mousePos.y >= self.box[1] and mousePos.y <= self.box[1]+self.box[3]:
            if mdown:
                return True
        return False
    def drag(self,mousePos: Vector2):
        if self.clicked:
            self.box.x = mousePos.x - self.moff.x
            self.box.y = mousePos.y - self.moff.y
    def myPos(self,where: Vector2):
        self.box.x = where.x
        self.box.y = where.y
    def movePos(self,how: Vector2):
        self.box.x += how.x
        self.box.y += how.y
    def render(self,screen: pygame.Surface):
        pygame.draw.rect(screen,self.color,self.box)
        if self.hover:
            pygame.draw.rect(screen,self.bc,self.box,5)
        if self.text != None:
            screen.blit(self.text,Vector2(self.box.x, self.box.y) - Vector2(0,0))

class circleButton:
    def __init__(self,color: Color,position: Vector2, radius: float, bordercolor: Color | None = None, text: str = "", textcolor: Color = Color((0, 0, 0))):
        self.color = color
        self.rad = radius
        self.pos = position
        self.text = font.render(str(text), 1, textcolor)
        if bordercolor == None:
            self.bc = color
        else:
            self.bc = bordercolor
        self.clicked = False
        self.hover = False
        self.moff = Vector2(0,0)
    def tick(self,mdown: bool,mousePos: Vector2) -> bool:
        if self.rad > self.pos.distance_to(mousePos) or self.clicked:
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
    def basicTick(self,mdown: bool,mousePos: Vector2) -> bool:
        #Tick without all the variable changing guff
        if self.rad > self.pos.distance_to(mousePos) or self.clicked:
            if mdown:
                return True
        return False
    def drag(self,mousePos: Vector2):
        if self.clicked:
            self.pos = mousePos - self.moff
    def render(self,screen: pygame.Surface):
        pygame.draw.circle(screen,self.color,self.pos,self.rad)
        if self.hover:
            pygame.draw.circle(screen,self.bc,self.pos,self.rad,5)
        screen.blit(self.text,self.pos - Vector2(10,20))

class graphNode(circleButton):
    def __init__(self,color: Color,position: Vector2, radius: float, bordercolor: Color | None = None, text: str = "", textcolor: Color = Color((0, 0, 0))):
        super().__init__(color,position,radius,bordercolor,text,textcolor)
        self.connections = []
        self.weights = []
    def countNeighbors(self):
        return len(self.connections)

class elButton(button):
    def __init__(self,id: int, color: Color, elementcolor: Color,rectangle: Rect, boardercolor: Color | None = None,colorList: tuple[Color, ...] | None = None):
        super().__init__(color,rectangle, boardercolor)
        
        self.id = id
        self.ecolor = elementcolor
        self.clist = colorList
        self.rtimer = 120
        self.rticker = 120
        self.frame = 0
    def render(self,screen: pygame.Surface):
        if self.ecolor == None:
            self.rticker -= 1
            if self.rticker <= 0:
                self.rticker = self.rtimer
                if self.frame+1 < len(self.clist):
                    self.frame += 1
                else:
                    self.frame = 0
        if self.hover:
            pygame.draw.rect(screen,self.bc,self.box)
        else:
            pygame.draw.rect(screen,self.color,self.box)
        
        if self.ecolor != None:
            pygame.draw.rect(screen,self.ecolor,Rect(self.box.x+self.box.w/4,self.box.y+self.box.h/4,self.box.w/2,self.box.h/2))
        elif self.clist != None:
            pygame.draw.rect(screen,self.clist[self.frame],Rect(self.box.x+self.box.w/4,self.box.y+self.box.h/4,self.box.w/2,self.box.h/2))
            
        if not self.hover:
            pygame.draw.rect(screen,self.bc,self.box,2)
print("Beep boop!")