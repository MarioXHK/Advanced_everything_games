from buttons import graphNode
from pygame.math import Vector2
import pygame
import random
from pygame.color import Color

#As in the graphing calculator, my favorite :D

class graph:
    def __init__(self,points: list[graphNode] = []):
        self.nodes = points
        self.nvel = []
        self.nsize = []
        self.pullStrength = 1
        self.threshhold = 5 #The margin of error the points are allowed to be in while trying to be pulled
        for nn in range(len(self.nodes)):
            self.nvel.append(Vector2(0,0))
            self.nsize.append(25)
        self.connecting = False
        self.connectTo = 0
    def nodeAppend(self,pos: Vector2, size = 25):
        self.nodes.append(graphNode(Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)),pos,size,Color(255,255,255),str(len(self.nodes))))
        self.nvel.append(Vector2(0,0))
        self.nsize.append(size)
    def nodesAct(self,taken,fire,connect,mousePos):
        for n in self.nodes:
            if taken == None and n.tick(fire,mousePos):
                #Dragging nodes around via left click
                taken = n.color
            elif n.basicTick(connect,mousePos):
                #Connecting nodes to eachother via right click
                if not self.connecting:
                    print("Connecting started!")
                    self.connecting = True
                    self.connectTo = self.nodes.index(n)
                else:
                    self.connecting = False
                    if self.nodes.index(n) in self.nodes[self.connectTo].connections:
                        print(self.connectTo, "is already connected to", self.nodes.index(n))
                    else:
                        self.nodes[self.connectTo].connections.append(self.nodes.index(n))
                        print("Connected", self.connectTo, "to", self.nodes.index(n))
            if n.color == taken:
                n.drag(mousePos)
        return taken

    def moveNodes(self):
        for n in self.nodes:
            for j in n.connections:
                print("Fine")



    def draw(self,screen: pygame.Surface):
        for n in self.nodes:
            if len(n.connections) > 0:
                for c in n.connections:
                    
                    if c == self.nodes.index(n):
                        pygame.draw.circle(screen,n.color,n.pos,n.rad*1.5,8)
                    else:
                        weight = n.pos.distance_to(self.nodes[c].pos)
                        w = int(weight)//3
                        tw = int((weight*4)**0.5)
                        font = pygame.font.SysFont('Comic Sans MS', tw)
                        if w > 255:
                            w = 255
                        t = font.render(str(int(weight)), 1, Color(w,0,0))
                        if self.nodes.index(n) in self.nodes[c].connections:
                            pygame.draw.line(screen,(255,255,255),n.pos,self.nodes[c].pos,int(weight**0.5))
                        else:
                            pygame.draw.line(screen,n.color,n.pos,self.nodes[c].pos,int(weight**0.5))
                        m = Vector2((n.pos.x+self.nodes[c].pos.x)/2,(n.pos.y+self.nodes[c].pos.y)/2)
                        screen.blit(t,m - Vector2(tw,tw))
            n.render(screen)