from buttons import button
import random
from pygame.math import Vector2

class fish(button):
    def aftint(self):
        self.dir = (random.random()-0.5,random.random()-0.5)
        self.timetime = random.randint(30,300)
    def swim(self):
        self.timetime -= 1
        if self.clicked:
            return
        self.box[0] += self.dir[0]
        self.box[1] += self.dir[1]
        if self.timetime <= 0 or self.oob == True:
            self.dir = (random.random()-0.5,random.random()-0.5)
            self.timetime = random.randint(30,300)
    def oob(self) -> bool:
        return (self.box[0] < 0-self.box[2] or self.box[1] < 0-self.box[3] or self.box[0] > 1000 or self.box[1] > 800)