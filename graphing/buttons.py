import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.color import Color
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

class button:
    def __init__(self,color: Color,rectangle: Rect, boardercolor: Color | None = None, text: str = "",textcolor: Color = Color(0,0,0)):
        self.color = color
        self.box = rectangle
        self.text = font.render(str(text), 1, textcolor)
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
    def drag(self,mousePos: Vector2):
        if self.clicked:
            self.box.x = mousePos.x - self.moff.x
            self.box.y = mousePos.y - self.moff.y
    def render(self,screen: pygame.surface):
        pygame.draw.rect(screen,self.color,self.box)
        if self.hover:
            pygame.draw.rect(screen,self.bc,self.box,5)
            