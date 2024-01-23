import pygame
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

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
    def tick(self,mdown: bool,mousePos: tuple) -> bool:
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
    def drag(self,mousePos: tuple):
        if self.clicked:
            self.box[0] = mousePos[0] - self.moff[0]
            self.box[1] = mousePos[1] - self.moff[1]
    def render(self,screen: pygame.surface):
        pygame.draw.rect(screen,self.color,self.box)
        if self.hover:
            pygame.draw.rect(screen,self.bc,self.box,5)
            