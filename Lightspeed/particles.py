import pygame
import random
from pygame import Vector2

class particle:
    def __init__(self,position: Vector2 = Vector2(random.random()*1000,random.random()*1000),radius: float = random.random()*20+1,direct: Vector2 = Vector2(random.random()-0.5,random.random()-0.5), speed = random.random() * 10,radioactive: bool = bool(random.getrandbits(1))):
        self.pos = position
        self.prepos = [position.copy() for x in range(int(speed*radius**0.5))]
        self.rad = radius
        self.dirr = direct
        self.vel = speed
        self.nuclear = radioactive
        if self.nuclear:
            self.decay = random.randint(30-int(self.rad),600//int(self.rad+1))
    def accel(self,by):
        self.vel += by
    def tick(self,particles):
        # for d in range(len(self.prepos)):
            # print(self.prepos[d])
            # if d == 0:
            #     self.prepos[0] = self.pos
            # else:
            #     self.prepos[d] = self.prepos[d-1]
        
        # shift the list, dropping the first element and appending the current position
        self.prepos.append(self.pos.copy()) # .copy() is very important! otherwise, it will pass by reference, and so it will update in real time rather than storing it for thr future
        self.prepos.pop(0)

        self.pos += self.dirr * self.vel
        if self.pos[0] < 0 or self.pos[0] > 1000:
            self.dirr[0] = -self.dirr[0]
        if self.pos[1] < 0 or self.pos[1] > 1000:
            self.dirr[1] = -self.dirr[1]
    def see(self,tank):
        # lines = []
        # for d in range(len(self.prepos)):
        #     if d == 0:
        #         pass
        #     else:
        #         lines.append((lines[d], lines[d-1]))
        if len(self.prepos) > 1:
            pygame.draw.lines(tank,(255,255,230),False,self.prepos,int(self.rad*2))
        pygame.draw.circle(tank, (255,255,255), self.pos, self.rad)