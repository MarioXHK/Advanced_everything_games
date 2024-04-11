from buttons import button
import random
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.color import Color


class fish(button):
    def __init__(self,color: Color,rectangle: Rect, boardercolor: Color | None = None):
        super().__init__(color,rectangle,boardercolor)
        self.dir = Vector2(random.random()-0.5,random.random()-0.5)
        self.timetime = random.randint(30,300)
    def swim(self):
        self.timetime -= 1
        if self.clicked:
            return
        self.box.topleft += self.dir
        if self.timetime <= 0 or self.oob == True:
            self.dir = Vector2(random.random()-0.5,random.random()-0.5)
            self.timetime = random.randint(30,300)
    def oob(self) -> bool:
        return (self.box[0] < 0-self.box[2] or self.box[1] < 0-self.box[3] or self.box[0] > 1000 or self.box[1] > 800)