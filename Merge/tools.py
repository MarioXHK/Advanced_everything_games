import pygame
from pygame import Vector2
import math

class pickaxe:
    def __init__(self,centerPos: Vector2, level: int = 0, angle: int | float = 0, reach: int | float = 50) -> None:
        self.tier = level
        self.reach = reach
        self.cent = centerPos
        self.rotPos = centerPos
        self.angle = angle
        self.am = 1 #Angular momentum
        self.hp = 10*2**level
        self.atk = 2**(level*0.5)
        self.broken = False
    def move(self) -> None:
        self.angle += self.am

        radians = self.angle*(3.14/180)
        
        self.rotPos = (self.reach*math.cos(radians)+self.cent.x, self.reach*math.sin(radians)+self.cent.y)
    def using(self, dmg) -> int:
        self.hp -= dmg
        if self.hp <= 0:
            self.broken = True
        return self.atk
    def draw(self,screen):
        pygame.draw.circle(screen,(255,0,0),self.rotPos,10)
    