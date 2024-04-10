import pygame
from pygame import Vector2
import math
import random

class ship:
    def __init__(self,centerPos: Vector2,health: int = 10, size: int | float = 20, velocity = Vector2(0,0), myColor: tuple = (255,255,255)):
        self.pos = centerPos
        self.size = size
        self.color = myColor
        self.vel = velocity
        self.alive = True
        self.dying = 25
        self.dead = False
        self.hp = health
        self.rhp = health
        self.inv = 10
        self.tinv = 0
    def move(self):
        self.pos += self.vel
    def dieplease(self):
        if self.hp <= 0:
            self.alive = False
        if self.alive:
            return
        self.dying -= 1
        if self.dying <= 0:
            self.dead = True
    def draw(self,screen):
        if self.alive:
            if self.tinv > 0:
                self.tinv -= 1
            if self.rhp == self.hp and self.tinv <= 0:
                
                pygame.draw.circle(screen,self.color,self.pos,self.size)
            else:
                if self.tinv <= 0:
                    self.tinv = self.inv
                pygame.draw.circle(screen,(255,random.randint(0,127),0),self.pos,self.size)
            self.rhp = self.hp
        else:
            pygame.draw.circle(screen,(255,random.randint(0,255),0),self.pos,self.size*1.6)