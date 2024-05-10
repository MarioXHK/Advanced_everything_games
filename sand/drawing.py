import pygame
import random
from physics import coinflip

def drawStuff(screen,plain: list[list[list[int]]],lyx: int,lyy: int, switch: bool = True):
    for i in range(len(plain)):
        for j in range(len(plain[0])):
            el = plain[i][j][0]
            et = plain[i][j][1]
            #Sand
            if el == 1:
                pygame.draw.rect(screen,(255,255,0),(j*lyx,i*lyy,lyx,lyy))
            
            #Stone
            elif el == 2:
                pygame.draw.rect(screen,(150,150,150),(j*lyx,i*lyy,lyx,lyy))
            
            #Water
            elif el == 3:
                pygame.draw.rect(screen,(0,0,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Sugar
            elif el == 4:
                pygame.draw.rect(screen,(250,250,250),(j*lyx,i*lyy,lyx,lyy))
            
            #Wall
            elif el == 5:
                coolr = et//1000000
                cool = et%1000000
                coolg = cool//1000
                coolb = cool%1000
                if coolr > 255:
                    coolr = 255
                elif coolr < 0:
                    coolr = 0
                if coolg > 255:
                    coolg = 255
                elif coolg < 0:
                    coolg = 0
                if coolb > 255:
                    coolb = 255
                elif coolb < 0:
                    coolb = 0
                pygame.draw.rect(screen,(coolr,coolg,coolb),(j*lyx,i*lyy,lyx,lyy))
            
            #Dirt
            elif el == 6:
                pygame.draw.rect(screen,(200,100,50),(j*lyx,i*lyy,lyx,lyy))
            
            #Mud
            elif el == 7:
                pygame.draw.rect(screen,(150,50,10),(j*lyx,i*lyy,lyx,lyy))
            
            #Plant
            elif el == 8:
                pygame.draw.rect(screen,(0,200,0),(j*lyx,i*lyy,lyx,lyy))
            
            #Lava
            elif el == 9:
                #It gets darker when it's temp is lower
                cool = 200+et*10+random.randint(0,50)
                if cool > 255:
                    cool = 255
                elif cool < 0:
                    cool = 0
                pygame.draw.rect(screen,(cool,random.randint(0,50),0),(j*lyx,i*lyy,lyx,lyy))
            
            #Wet Sand
            elif el == 10:
                pygame.draw.rect(screen,(200,200,50),(j*lyx,i*lyy,lyx,lyy))
            
            #Gravel
            elif el == 11:
                pygame.draw.rect(screen,(200,200,200),(j*lyx,i*lyy,lyx,lyy))
            
            #Obsidian
            elif el == 12:
                if et > 225:
                    et = 225
                elif et < -30:
                    et = -30
                pygame.draw.rect(screen,(30+et,20,40),(j*lyx,i*lyy,lyx,lyy))
            
            #Steam
            elif el == 13:
                pygame.draw.rect(screen,(128,200,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Glass
            elif el == 14:
                pygame.draw.rect(screen,(0,255,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Sugar Water
            elif el == 15:
                pygame.draw.rect(screen,(0,128,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Cloud
            elif el == 16:
                pygame.draw.rect(screen,(230,230,230),(j*lyx,i*lyy,lyx,lyy))
            
            #Brick
            elif el == 17:
                pygame.draw.rect(screen,(150,90,60),(j*lyx,i*lyy,lyx,lyy))
            
            #Algae
            elif el == 18:
                pygame.draw.rect(screen,(0,128,0),(j*lyx,i*lyy,lyx,lyy))
            
            #Glass Shards
            elif el == 19:
                #This makes it so that while Glass Shards are randomly colored, unlike the others, they keep their colors (This is also laggy and why not many others use it)
                random.seed(et)
                pygame.draw.rect(screen,(random.randint(0,50),50+random.randint(0,200),100+random.randint(0,150)),(j*lyx,i*lyy,lyx,lyy))
                random.seed()
            
            #The Sun
            elif el == 20:
                if et == 1:
                    pygame.draw.rect(screen,(255,255,128),(j*lyx,i*lyy,lyx,lyy))
                else:
                    #Eclipsed Sun
                    pygame.draw.rect(screen,(1,1,1),(j*lyx,i*lyy,lyx,lyy))
                    pygame.draw.rect(screen,(255,255,200),(j*lyx,i*lyy,lyx,lyy),1)
            
            #The Moon
            elif el == 21:
                pygame.draw.rect(screen,(10,60,180),(j*lyx,i*lyy,lyx,lyy))
            
            #Snow
            elif el == 22:
                pygame.draw.rect(screen,(240,250,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Ice
            elif el == 23:
                pygame.draw.rect(screen,(200,255,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Sugar Crystals
            elif el == 24:
                pygame.draw.rect(screen,(240,220,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Packed Ice
            elif el == 25:
                pygame.draw.rect(screen,(100,200,230),(j*lyx,i*lyy,lyx,lyy))
            
            #Precious, Precious Life
            elif el == 26:
                pygame.draw.rect(screen,(255,255,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Sludge
            elif el == 27:
                pygame.draw.rect(screen,(170,210,250),(j*lyx,i*lyy,lyx,lyy))
            
            #Flower Stuff
            elif el == 28:
                #Flower Seed
                if et == 0:
                    pygame.draw.rect(screen,(40,20,10),(j*lyx,i*lyy,lyx,lyy))
                
                #Flower Stem
                else:
                    pygame.draw.rect(screen,(0,255,0),(j*lyx,i*lyy,lyx,lyy))
            
            #Oil
            elif el == 29:
                pygame.draw.rect(screen,(24,24,24),(j*lyx,i*lyy,lyx,lyy))
            
            #Fire!
            elif el == 30:
                cool = 200+et*10
                if cool > 255:
                    cool = 255
                cooler = random.randint(50,100+et*random.randint(20,30))
                if cooler > 255:
                    cooler = 255
                pygame.draw.rect(screen,(cool,cooler,0),(j*lyx,i*lyy,lyx,lyy))
            
            #Wood
            elif el == 31:
                pygame.draw.rect(screen,(140,70,30),(j*lyx,i*lyy,lyx,lyy))
            
            #Ash
            elif el == 32:
                cool = 100-et//2
                pygame.draw.rect(screen,(cool,cool,cool),(j*lyx,i*lyy,lyx,lyy))
            
            #Cloner
            elif el == 33:
                cool = 0
                #Changes colors if it's in the process of cloning
                if et != 0:
                    cool = 100+random.randint(-20,20)
                pygame.draw.rect(screen,(100+cool,cool//2,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Clay
            elif el == 34:
                pygame.draw.rect(screen,(160,170,180),(j*lyx,i*lyy,lyx,lyy))
            
            #Void
            elif el == 35:
                pygame.draw.rect(screen,(10,10,10),(j*lyx,i*lyy,lyx,lyy))
            
            #Petal
            elif el == 36:
                colour = (255,255,255)
                #Depending on it's temp, it'll be a different color
                if et == 1:
                    colour = (255,0,0)
                elif et == 2:
                    colour = (255,128,0)
                elif et == 3:
                    colour = (255,255,0)
                elif et == 4:
                    colour = (128,255,0)
                elif et == 5:
                    colour = (0,255,0)
                elif et == 6:
                    colour = (0,255,128)
                elif et == 7:
                    colour = (255,255,255)
                elif et == 8:
                    colour = (0,128,255)
                elif et == 9:
                    colour = (0,0,255)
                elif et == 8:
                    colour = (128,0,255)
                elif et == 9:
                    colour = (255,0,255)
                elif et == 10:
                    colour = (128,0,255)
                elif et == 11:
                    colour = (128,128,128)
                pygame.draw.rect(screen,colour,(j*lyx,i*lyy,lyx,lyy))
            
            #Cancer Particle
            elif el == 37:
                pygame.draw.rect(screen,(random.randint(0,250),random.randint(0,100),random.randint(150,250)),(j*lyx,i*lyy,lyx,lyy))
            
            #Iron
            elif el == 38:
                #Lights up at different states of electricity
                if et == 1:
                    pygame.draw.rect(screen,(255,255,20),(j*lyx,i*lyy,lyx,lyy))
                elif et == 2:
                    pygame.draw.rect(screen,(230,230,100),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(180,180,170),(j*lyx,i*lyy,lyx,lyy))
            
            #Iron Snad
            elif el == 39:
                if et == 1:
                    pygame.draw.rect(screen,(255,255,20),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(200,200,190),(j*lyx,i*lyy,lyx,lyy))
            
            #Iron Brick
            elif el == 40:
                if et == 1:
                    pygame.draw.rect(screen,(255,255,20),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(200,200,150),(j*lyx,i*lyy,lyx,lyy))
            
            #Smart Remover
            elif el == 41:
                cool = 0
                if et != 0:
                    cool = random.randint(-20,20)
                pygame.draw.rect(screen,(100,20+cool//2,240),(j*lyx,i*lyy,lyx,lyy))
            
            #Smart Converter
            elif el == 42:
                cool = 0
                if et != 0:
                    cool = random.randint(-50,50)
                pygame.draw.rect(screen,(200+cool,50+cool,50+cool),(j*lyx,i*lyy,lyx,lyy))
            
            #Electricity
            elif el == 43:
                if coinflip():
                    pygame.draw.rect(screen,(255,255,0),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(255,255,128),(j*lyx,i*lyy,lyx,lyy))
            
            #Rusted Iron (Doesn't show it's electrical current)
            elif el == 44:
                pygame.draw.rect(screen,(180,130,100),(j*lyx,i*lyy,lyx,lyy))
            
            #Rust
            elif el == 45:
                pygame.draw.rect(screen,(60,30,15),(j*lyx,i*lyy,lyx,lyy))
            
            #Salt
            elif el == 46:
                pygame.draw.rect(screen,(255,255,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Salt Water
            elif el == 47:
                if random.randint(1,111) == 1 and et == 1:
                    pygame.draw.rect(screen,(255,255,0),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(128,128,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Salt Crystal
            elif el == 48:
                pygame.draw.rect(screen,(200,230,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Leaf
            elif el == 49:
                if et < 0:
                    et = 0
                elif et > 10:
                    et = 10
                pygame.draw.rect(screen,(et*20,150-et*10,0),(j*lyx,i*lyy,lyx,lyy))
            
            #Jammer
            elif el == 50:
                if switch:
                    pygame.draw.rect(screen,(255,255,255),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(255,0,0),(j*lyx,i*lyy,lyx,lyy))
            
            #Antisand
            elif el == 51:
                pygame.draw.rect(screen,(0,0,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Antistone
            elif el == 52:
                pygame.draw.rect(screen,(105,105,105),(j*lyx,i*lyy,lyx,lyy))
            
            #Antiwater
            elif el == 53:
                pygame.draw.rect(screen,(255,255,0),(j*lyx,i*lyy,lyx,lyy))
            
            #Identity Crisis
            elif el == 54:
                #To look like sand
                if et == 1:
                    pygame.draw.rect(screen,(255,255,0),(j*lyx,i*lyy,lyx,lyy))
                #To look like stone
                elif et == 2:
                    pygame.draw.rect(screen,(150,150,150),(j*lyx,i*lyy,lyx,lyy))
                #To look like water
                elif et == 3:
                    pygame.draw.rect(screen,(0,0,255),(j*lyx,i*lyy,lyx,lyy))
                #To look like sugar
                elif et == 4:
                    pygame.draw.rect(screen,(250,250,250),(j*lyx,i*lyy,lyx,lyy))
                #To look like wall
                elif et == 5:
                    pygame.draw.rect(screen,(100,100,100),(j*lyx,i*lyy,lyx,lyy))
                #To look like dirt
                elif et == 6:
                    pygame.draw.rect(screen,(200,100,50),(j*lyx,i*lyy,lyx,lyy))
                #To look like something has went wrong
                else:
                    pygame.draw.rect(screen,(255,0,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Molten Salt
            elif el == 55:
                pygame.draw.rect(screen,(255,200+random.randint(0,55),200+random.randint(0,55)),(j*lyx,i*lyy,lyx,lyy))
            
            #Smoke
            elif el == 56:
                pygame.draw.rect(screen,(et*5,et*5,et*5),(j*lyx,i*lyy,lyx,lyy))
            
            #Virus
            elif el == 57:
                pygame.draw.rect(screen,(100,20+random.randint(-20,20)//2,240),(j*lyx,i*lyy,lyx,lyy))
            
            #Gold
            elif el == 58:
                if et == 1:
                    pygame.draw.rect(screen,(255,255,255),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(240,230,0),(j*lyx,i*lyy,lyx,lyy))
            
            #Covered Wire
            elif el == 59:
                pygame.draw.rect(screen,(25,25,30),(j*lyx,i*lyy,lyx,lyy))
            
            #Strange Matter
            elif el == 60:
                pygame.draw.rect(screen,(random.randint(0,50),random.randint(25,255),random.randint(0,50)),(j*lyx,i*lyy,lyx,lyy))
            
            #Shockwave
            elif el == 61:
                cool = et*64
                if cool > 255:
                    cool = 255
                elif cool < 0:
                    cool = 0
                pygame.draw.rect(screen,(cool,cool,cool),(j*lyx,i*lyy,lyx,lyy))
            
            #Sapling
            elif el == 62:
                if et == 0:
                    pygame.draw.rect(screen,(32,24,16),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(140,70,30),(j*lyx,i*lyy,lyx,lyy))
            
            #Broken Brick
            elif el == 63:
                pygame.draw.rect(screen,(130,80,60),(j*lyx,i*lyy,lyx,lyy))
            
            #Acid Cloud
            elif el == 64:
                pygame.draw.rect(screen,(170,250,190),(j*lyx,i*lyy,lyx,lyy))
            
            #Acid
            elif el == 65:
                pygame.draw.rect(screen,(0,255,0),(j*lyx,i*lyy,lyx,lyy))
            
            #Acid Sludge
            elif el == 66:
                pygame.draw.rect(screen,(random.randint(0,20),200+random.randint(0,20),random.randint(0,20)),(j*lyx,i*lyy,lyx,lyy))
            
            #Explosion
            elif el == 67:
                pygame.draw.rect(screen,(random.randint(150,255),random.randint(50,230),random.randint(0,40)),(j*lyx,i*lyy,lyx,lyy))
            
            #TNT
            elif el == 68:
                pygame.draw.rect(screen,(200,0,0),(j*lyx,i*lyy,lyx,lyy))
            
            #C4
            elif el == 69:
                if et == 1:
                    pygame.draw.rect(screen,(255,random.randint(0,255),random.randint(0,255)),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(200,180,150),(j*lyx,i*lyy,lyx,lyy))
            
            #Nuke
            elif el == 70:
                pygame.draw.rect(screen,(80,100,60),(j*lyx,i*lyy,lyx,lyy))
            
            #Holy Water
            elif el == 71:
                if et != 0:
                    pygame.draw.rect(screen,(200,255,230),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(200,200,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Dead Plant
            elif el == 72:
                pygame.draw.rect(screen,(120-et,60-(et//5),10-(et//10)),(j*lyx,i*lyy,lyx,lyy))
            
            #Coal
            elif el == 73:
                pygame.draw.rect(screen,(20,20,20),(j*lyx,i*lyy,lyx,lyy))
            
            #Natural Gas
            elif el == 74:
                pygame.draw.rect(screen,(60,30,15),(j*lyx,i*lyy,lyx,lyy))
            
            #Polluted Water
            elif el == 75:
                pygame.draw.rect(screen,(0,random.randint(100,200),random.randint(30,100)),(j*lyx,i*lyy,lyx,lyy))
            
            #Greenhouse Sun
            elif el == 76:
                if et == 1:
                    pygame.draw.rect(screen,(255,150,120),(j*lyx,i*lyy,lyx,lyy))
                else:
                    #Eclipsed GreenhouseSun
                    pygame.draw.rect(screen,(10,0,0),(j*lyx,i*lyy,lyx,lyy))
                    pygame.draw.rect(screen,(255,0,0),(j*lyx,i*lyy,lyx,lyy),2)
            
            #Wax
            elif el == 77:
                pygame.draw.rect(screen,(200+et*2,150+et*5,60+et*10),(j*lyx,i*lyy,lyx,lyy))

            #Honeycomb
            elif el == 78:
                pygame.draw.rect(screen,(230,200,70),(j*lyx,i*lyy,lyx,lyy))
            
            #Honey
            elif el == 79:
                pygame.draw.rect(screen,(160,100,23),(j*lyx,i*lyy,lyx,lyy))
            
            #Bees
            elif el == 80:
                pygame.draw.rect(screen,(230,230,100),(j*lyx,i*lyy,lyx,lyy))
            
            #Blood
            elif el == 81:
                cool = random.randint(1,10)
                if et == 1:
                    cool *= 2
                elif et == 0:
                    cool = 0
                pygame.draw.rect(screen,(255,cool,cool),(j*lyx,i*lyy,lyx,lyy))

            #Red Sand
            elif el == 82:
                pygame.draw.rect(screen,(200,128,0),(j*lyx,i*lyy,lyx,lyy))

            #Good Smoke
            elif el == 83:
                cool = et*random.randint(10,20)
                if cool > 255:
                    cool = 255
                elif cool < 0:
                    cool = 0
                pygame.draw.rect(screen,(cool,cool,cool),(j*lyx,i*lyy,lyx,lyy))
        
            #Acid Waste
            elif el == 84:
                pygame.draw.rect(screen,(random.randint(0,10),150+random.randint(0,60),random.randint(0,10)),(j*lyx,i*lyy,lyx,lyy))

            #Thick water
            elif el == 85:
                pygame.draw.rect(screen,(40,60,255),(j*lyx,i*lyy,lyx,lyy))

            #Filler
            elif el == 86:
                pygame.draw.rect(screen,(100,0,240),(j*lyx,i*lyy,lyx,lyy))
            
            #Snake
            elif el == 87:
                pygame.draw.rect(screen,(0,128,0),(j*lyx,i*lyy,lyx,lyy))

            #Tesla Coil
            elif el == 88:
                if et == 0:
                    pygame.draw.rect(screen,(200,200,0),(j*lyx,i*lyy,lyx,lyy))
                elif et == 1:
                    pygame.draw.rect(screen,(255,255,255),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(255,255,0),(j*lyx,i*lyy,lyx,lyy))

            #Battery
            elif el == 89:
                #Visual pulsing~
                pygame.draw.rect(screen,(60-et,60-et,60-et),(j*lyx,i*lyy,lyx,lyy))

            #Thunder Clouds
            elif el == 90:
                cool = random.randint(0,8)
                pygame.draw.rect(screen,(120+cool,120+cool,120+cool),(j*lyx,i*lyy,lyx,lyy))

            #Pollen
            elif el == 91:
                pygame.draw.rect(screen,(255,230,128),(j*lyx,i*lyy,lyx,lyy))






            #Frosted Sand
            elif el == 101:
                pygame.draw.rect(screen,(220,250,230),(j*lyx,i*lyy,lyx,lyy))

            #If all else fails...
            else:
                #Look magenta, no other element looks entirely magenta
                if el != 0:
                    pygame.draw.rect(screen,(255,0,255),(j*lyx,i*lyy,lyx,lyy))

def drawLessStuff(screen,plain: list[list[int]],lyx:int,lyy:int, ts: int = 0):
    for i in range(len(plain)):
        for j in range(len(plain[0])):
            rel = plain[i][j]

            #Basic sand
            if rel == 1:
                if ts in (2,3):
                    pygame.draw.rect(screen,(255,255,0),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(255,255,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Basic stone
            elif rel == 2:
                pygame.draw.rect(screen,(150,150,150),(j*lyx,i*lyy,lyx,lyy))
            
            #Basic water
            elif rel == 3:
                pygame.draw.rect(screen,(0,0,255),(j*lyx,i*lyy,lyx,lyy))
            
            #Basic wall
            elif rel == 4:
                if ts == 2:
                    pygame.draw.rect(screen,(255,255,255),(j*lyx,i*lyy,lyx,lyy))
                elif ts == 3:
                    pygame.draw.rect(screen,(random.randint(20,50),random.randint(20,50),random.randint(20,50)),(j*lyx,i*lyy,lyx,lyy))
                else:
                    pygame.draw.rect(screen,(0,0,0),(j*lyx,i*lyy,lyx,lyy))
            else:
                if rel != 0:
                    #Basic Error
                    pygame.draw.rect(screen,(255,0,255),(j*lyx,i*lyy,lyx,lyy))



print("I wonder how blind people play video games. (I don't think I can make it accessable to them here ,-_-,)")