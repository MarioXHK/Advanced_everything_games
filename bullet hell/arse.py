#Short for arsenal
import pygame
from pygame import Vector2
import math

class orbiter:
    def __init__(self,centerPos: Vector2, size: int | float = 10, angle: int | float = 0, reach: int | float = 50, color: tuple[int,int,int] = (255,255,255)):
        self.size = size
        self.reach = reach
        self.cent = centerPos
        self.rotPos = centerPos
        self.angle = angle
        self.am = 2 #Angular momentum
        self.color = color
        self.rx = 0
        self.ry = 0
        self.rex = 0
        self.rey = 0
    def move(self) -> None:
        self.angle += self.am
        
        radians = self.angle*(3.14/180)
        
        self.rotPos = ((self.reach+self.rex)*math.cos(radians+self.rx)+self.cent.x, (self.reach+self.rey)*math.sin(radians+self.ry)+self.cent.y)
    def movetocent(self):
        self.rotPos = self.cent
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,self.rotPos,self.size)

class shield(orbiter):
    def __init__(self,centerPos: Vector2, size: int | float = 10, angle: int | float = 0, reach: int | float = 50, color: tuple[int,int,int] = (255,255,255), health: int = 3):
        super().__init__(centerPos,size, angle, reach,color)
        self.hp = health
        self.dhp = health
        self.healtime = 300
        self.fullhealtime = 900
        self.httimer = 0
        self.fhtimer = 0
    def healfromdamages(self):
        if self.hp <= 0:
            self.fhtimer += 1
            if self.fhtimer >= self.fullhealtime:
                self.fhtimer = 0
                self.hp = self.dhp//2
        elif self.hp < self.dhp:
            self.httimer += 1
            if self.httimer >= self.healtime:
                self.hp += 1
                self.httimer = 0
    def draw(self,screen):
        if self.hp <= 0:
            pygame.draw.circle(screen,(self.color[0]//4,self.color[1]//4,self.color[2]//4),self.rotPos,self.size*0.6)
        else:
            pygame.draw.circle(screen,self.color,self.rotPos,self.size)




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
    def __init__(self,centerPos: Vector2, size: int | float = 5,angle: int | float = -90,velocity: int | float = 10,vecvelocity: Vector2 | None = None, myColor: tuple = (255,255,255)):
        self.size = size
        self.color = myColor
        self.id = 0
        self.pos = centerPos
        self.vel = velocity
        self.angle = angle
        if vecvelocity == None:
            self.xyvel = Vector2(0,0)
            self.turn(angle)
        else:
            self.xyvel = vecvelocity
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
        pygame.draw.circle(screen,self.color,self.pos,self.size)