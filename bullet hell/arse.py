#Short for arsenal
import pygame
from pygame import Vector2
import math

class orbiter:
    def __init__(self,centerPos: Vector2, angle: int | float = 0, reach: int | float = 50) -> None:
        self.reach = reach
        self.cent = centerPos
        self.rotPos = centerPos
        self.angle = angle
        self.am = 2 #Angular momentum
        
        self.rx = 0
        self.ry = 0
        self.rex = 0
        self.rey = 0
    def move(self) -> None:
        self.angle += self.am
        
        radians = self.angle*(3.14/180)
        
        self.rotPos = ((self.reach+self.rex)*math.cos(radians+self.rx)+self.cent.x, (self.reach+self.rey)*math.sin(radians+self.ry)+self.cent.y)
    
    def draw(self,screen):
        pygame.draw.circle(screen,(255,0,0),self.rotPos,10)


class pickaxe(orbiter):
    def __init__(self,centerPos: Vector2, level: int = 0, angle: int | float = 0, reach: int | float = 50):
        super().__init__(centerPos, angle, reach)
        self.tier = level
        self.hp = 10*2**level
        self.atk = 2**(level*0.5)
        self.broken = False
    def using(self, dmg) -> int:
        self.hp -= dmg
        if self.hp <= 0:
            self.broken = True
        return int(self.atk)


class bullet:
    def __init__(self,centerPos: Vector2, angle: int | float = -90,velocity: int | float = 10):
        self.id = 0
        self.pos = centerPos
        self.vel = velocity
        self.xyvel = Vector2(0,0)
        self.angle = angle
        self.turn(angle)
    def turn(self,angle: int | float):
        self.angle = angle
        radians = angle*(3.14/180)
        self.xyvel.x = self.vel*math.cos(radians)
        self.xyvel.y = self.vel*math.sin(radians)
    def move(self,goawayoffscreen: bool = True):
        self.pos += self.xyvel
        if goawayoffscreen:
            if self.pos.x < -100 or self.pos.x > 1124 or self.pos.y < -100 or self.pos.y > 868:
                self.id = 0
    def draw(self,screen):
        pygame.draw.circle(screen,(0,0,0),self.pos,5)