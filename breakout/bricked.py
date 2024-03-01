import pygame
import random
from pygame import Vector2
from pygame.rect import Rect
from pygame.color import Color

class brick:
    def __init__(self, rectangle: Rect,color: Color | None = None):
        self.box = rectangle
        if color == None:
            self.color = Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        else:
            self.color = color
        self.alive = True
    def collision(self, x,y):
        if self.alive:
            return True
        return False
    def draw(self,screen):
        if not self.alive:
            return
        pygame.draw.rect(screen,self.color,self.box)
        pygame.draw.rect(screen,(255,255,255),self.box,5)
