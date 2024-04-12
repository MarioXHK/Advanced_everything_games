from buttons import graphNode
import pygame
#As in the graphing calculator, my favorite :D
class graph:
    def __init__(self,points: list[graphNode] = []):
        self.nodes = points
        self.connecting = False
        self.connectTo = 0
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

    def draw(self,screen: pygame.Surface):
        for n in self.nodes:
            if len(n.connections) > 0:
                for c in n.connections:
                    if c == self.nodes.index(n):
                        pygame.draw.circle(screen,n.color,n.pos,n.rad*1.5,8)
                    else:
                        weight = n.pos.distance_to(self.nodes[c].pos)
                        if self.nodes.index(n) in self.nodes[c].connections:
                            pygame.draw.line(screen,(255,255,255),n.pos,self.nodes[c].pos,int(weight**0.5))
                        else:
                            pygame.draw.line(screen,n.color,n.pos,self.nodes[c].pos,int(weight**0.5))
            n.render(screen)