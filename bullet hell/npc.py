import pygame
from pygame import Vector2
import math
import random

class ship:
    def __init__(self,centerPos: Vector2, size: int | float = 20, velocity = Vector2(0,0), myColor: tuple = (255,255,255)):
        self.pos = centerPos
        self.size = size
        self.color = myColor
        self.vel = velocity
        self.alive = True
        self.dying = 25
        self.dead = False
    def move(self):
        self.pos += self.vel
    def dieplease(self):
        if self.alive:
            return
        self.dying -= 1
        if self.dying <= 0:
            self.dead = True
    def draw(self,screen):
        if self.alive:
            pygame.draw.circle(screen,self.color,self.pos,self.size)
        else:
            pygame.draw.circle(screen,(255,random.randint(0,255),0),self.pos,self.size*1.6)