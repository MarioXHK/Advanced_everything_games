import pygame
import random
from physics import coinflip
from pygame.color import Color
def clamp(number:int,mina:int = 0,maxi:int = 255) -> int:
    if number > maxi:
        number = maxi
    elif number < mina:
        number = mina
    return number

def drawStuff(screen,plain: list[list[list[int]]],lyx: int,lyy: int, photo: bool = False, gamma: int | float = 100, switch: bool = True):
    for i in range(len(plain)):
        for j in range(len(plain[0])):
            
            el = plain[i][j][0]
            
            if el == 0:
                continue
            
            override = False
            et = plain[i][j][1]
            eColor = Color(255,0,255)
            #Sand
            
            if el == 1:
                eColor = Color(255,255,0)
            
            #Stone
            elif el == 2:
                eColor = Color(150,150,150)
            
            #Water
            elif el == 3:
                eColor = Color(0,0,255)
            
            #Sugar
            elif el == 4:
                eColor = Color(250,250,250)
            
            #Wall
            elif el == 5:
                coolr = et//1000000
                cool = et%1000000
                coolg = cool//1000
                coolb = cool%1000
                coolr = clamp(coolr)
                coolg = clamp(coolg)
                coolb = clamp(coolb)
                eColor = Color(coolr,coolg,coolb)
            
            #Dirt
            elif el == 6:
                eColor = Color(200,100,50)
            
            #Mud
            elif el == 7:
                eColor = Color(150,50,10)
            
            #Plant
            elif el == 8:
                eColor = Color(0,200,0)
            
            #Lava
            elif el == 9:
                #It gets darker when it's temp is lower
                if photo:
                    cool = 200+et*10
                else:
                    cool = 200+et*10+random.randint(0,50)
                cool = clamp(cool)
                if photo:
                    eColor = Color(cool,25,0)
                else:
                    eColor = Color(cool,random.randint(0,50),0)
            
            #Wet Sand
            elif el == 10:
                eColor = Color(200,200,50)
            
            #Gravel
            elif el == 11:
                eColor = Color(200,200,200)
            
            #Obsidian
            elif el == 12:
                eColor = Color(clamp(30+et),20,40)
            
            #Steam
            elif el == 13:
                eColor = Color(128,200,255)
            
            #Glass
            elif el == 14:
                eColor = Color(0,255,255)
            
            #Sugar Water
            elif el == 15:
                eColor = Color(0,128,255)
            
            #Cloud
            elif el == 16:
                eColor = Color(230,230,230)
            
            #Brick
            elif el == 17:
                eColor = Color(150,90,60)
            
            #Algae
            elif el == 18:
                eColor = Color(0,128,0)
            
            #Glass Shards
            elif el == 19:
                #This makes it so that while Glass Shards are randomly colored, unlike the others, they keep their colors (This is also laggy and why not many others use it)
                if photo:
                    eColor = Color(25,150,175)
                else:
                    random.seed(et)
                    eColor = Color(random.randint(0,50),50+random.randint(0,200),100+random.randint(0,150))
                    random.seed()
            
            #The Sun
            elif el == 20:
                if et == 1:
                    eColor = Color(255,255,128)
                else:
                    #Eclipsed Sun
                    override = True
                    pygame.draw.rect(screen,(1,1,1),(j*lyx,i*lyy,lyx,lyy))
                    pygame.draw.rect(screen,(255,255,200),(j*lyx,i*lyy,lyx,lyy),1)
            
            #The Moon
            elif el == 21:
                eColor = Color(10,60,180)
            
            #Snow
            elif el == 22:
                eColor = Color(240,250,255)
            
            #Ice
            elif el == 23:
                eColor = Color(200,255,255)
            
            #Sugar Crystals
            elif el == 24:
                eColor = Color(240,220,255)
            
            #Packed Ice
            elif el == 25:
                eColor = Color(100,200,230)
            
            #Precious, Precious Life
            elif el == 26:
                eColor = Color(255,255,255)
            
            #Sludge
            elif el == 27:
                eColor = Color(170,210,250)
            
            #Flower Stuff
            elif el == 28:
                #Flower Seed
                if et == 0:
                    eColor = Color(40,20,10)
                
                #Flower Stem
                else:
                    eColor = Color(0,255,0)
            
            #Oil
            elif el == 29:
                eColor = Color(24,24,24)
            
            #Fire!
            elif el == 30:
                if photo:
                    eColor = Color(255,200,0)
                else:
                    cool = 200+et*10
                    cooler = random.randint(50,100+et*random.randint(20,30))
                    eColor = Color(clamp(cool),clamp(cooler),0)
            
            #Wood
            elif el == 31:
                eColor = Color(140,70,30)
            
            #Ash
            elif el == 32:
                cool = clamp(100-et//2)
                eColor = Color(cool,cool,cool)
            
            #Cloner
            elif el == 33:
                cool = 0
                #Changes colors if it's in the process of cloning
                
                if et != 0:
                    cool = 100
                    if not photo:
                        cool += random.randint(-20,20)
                eColor = Color(clamp(100+cool),clamp(cool//2),255)
            
            #Clay
            elif el == 34:
                eColor = Color(160,170,180)
            
            #Void
            elif el == 35:
                eColor = Color(10,10,10)
            
            #Petal
            elif el == 36:
                eColor = Color(255,255,255)
                #Depending on it's temp, it'll be a different color
                if et == 1:
                    eColor = Color(255,0,0)
                elif et == 2:
                    eColor = Color(255,128,0)
                elif et == 3:
                    eColor = Color(255,255,0)
                elif et == 4:
                    eColor = Color(128,255,0)
                elif et == 5:
                    eColor = Color(0,255,0)
                elif et == 6:
                    eColor = Color(0,255,128)
                elif et == 7:
                    eColor = Color(255,255,255)
                elif et == 8:
                    eColor = Color(0,128,255)
                elif et == 9:
                    eColor = Color(0,0,255)
                elif et == 8:
                    eColor = Color(128,0,255)
                elif et == 9:
                    eColor = Color(255,0,255)
                elif et == 10:
                    eColor = Color(128,0,255)
                elif et == 11:
                    eColor = Color(128,128,128)
            
            #Cancer Particle
            elif el == 37:
                if photo:
                    eColor = Color(125,50,200)
                else:
                    eColor = Color(random.randint(0,250),random.randint(0,100),random.randint(150,250))
            
            #Iron
            elif el == 38:
                #Lights up at different states of electricity
                if et == 1:
                    eColor = Color(255,255,20)
                elif et == 2:
                    eColor = Color(230,230,100)
                else:
                    eColor = Color(180,180,170)
            
            #Iron Snad
            elif el == 39:
                if et == 1:
                    eColor = Color(255,255,20)
                else:
                    eColor = Color(200,200,190)
            
            #Iron Brick
            elif el == 40:
                if et == 1:
                    eColor = Color(255,255,20)
                else:
                    eColor = Color(200,200,150)
            
            #Smart Remover
            elif el == 41:
                cool = 0
                if not (et == 0 or photo):
                    cool = random.randint(-20,20)
                eColor = Color(100,20+cool//2,240)
            
            #Smart Converter
            elif el == 42:
                cool = 0
                if not (et == 0 or photo):
                    cool = random.randint(-50,50)
                eColor = Color(200+cool,50+cool,50+cool)
            
            #Electricity
            elif el == 43:
                if coinflip() or photo:
                    eColor = Color(255,255,0)
                else:
                    eColor = Color(255,255,128)
            
            #Rusted Iron (Doesn't show it's electrical current)
            elif el == 44:
                eColor = Color(180,130,100)
            
            #Rust
            elif el == 45:
                eColor = Color(60,30,15)
            
            #Salt
            elif el == 46:
                eColor = Color(255,255,255)
            
            #Salt Water
            elif el == 47:
                if random.randint(1,111) == 1 and et == 1 and not photo:
                    eColor = Color(255,255,0)
                else:
                    eColor = Color(128,128,255)
            
            #Salt Crystal
            elif el == 48:
                eColor = Color(200,230,255)
            
            #Leaf
            elif el == 49:
                if et < 0:
                    et = 0
                elif et > 10:
                    et = 10
                eColor = Color(clamp(et*20),clamp(150-et*10),0)
            
            #Jammer
            elif el == 50:
                if photo:
                    eColor = Color(255,128,127)
                else:
                    if switch:
                        eColor = Color(255,255,255)
                    else:
                        eColor = Color(255,0,0)
            
            #Antisand
            elif el == 51:
                eColor = Color(0,0,255)
            
            #Antistone
            elif el == 52:
                eColor = Color(105,105,105)
            
            #Antiwater
            elif el == 53:
                eColor = Color(255,255,0)
            
            #Identity Crisis
            elif el == 54:
                if photo:
                    eColor = Color(200,100,200)
                else:
                    #To look like sand
                    if et == 1:
                        eColor = Color(255,255,0)
                    #To look like stone
                    elif et == 2:
                        eColor = Color(150,150,150)
                    #To look like water
                    elif et == 3:
                        eColor = Color(0,0,255)
                    #To look like sugar
                    elif et == 4:
                        eColor = Color(250,250,250)
                    #To look like wall
                    elif et == 5:
                        eColor = Color(100,100,100)
                    #To look like dirt
                    elif et == 6:
                        eColor = Color(200,100,50)
                    #To look like something has went wrong
                    else:
                        eColor = Color(255,0,255)
            
            #Molten Salt
            elif el == 55:
                if photo:
                    eColor = Color(255,225,230)
                else:
                    eColor = Color(255,200+random.randint(0,55),200+random.randint(0,55))
            
            #Smoke
            elif el == 56:
                cool = clamp(et*5)
                eColor = Color(cool,cool,cool)
            
            #Virus
            elif el == 57:
                if photo:
                    eColor = Color(100,20,240)
                else:
                    eColor = Color(100,clamp(20+random.randint(-20,20)//2),240)
            
            #Gold
            elif el == 58:
                if et == 1:
                    eColor = Color(255,255,255)
                else:
                    eColor = Color(240,230,0)
            
            #Covered Wire
            elif el == 59:
                eColor = Color(25,25,30)
            
            #Strange Matter
            elif el == 60:
                if photo:
                    eColor = Color(20,200,25)
                else:
                    eColor = Color(random.randint(0,50),random.randint(25,255),random.randint(0,50))
            
            #Shockwave
            elif el == 61:
                cool = clamp(et*64)
                eColor = Color(cool,cool,cool)
            
            #Sapling
            elif el == 62:
                if et == 0:
                    eColor = Color(32,24,16)
                else:
                    eColor = Color(140,70,30)
            
            #Broken Brick
            elif el == 63:
                eColor = Color(130,80,60)
            
            #Acid Cloud
            elif el == 64:
                eColor = Color(170,250,190)
            
            #Acid
            elif el == 65:
                eColor = Color(0,255,0)
            
            #Acid Sludge
            elif el == 66:
                if photo:
                    eColor = Color(10,210,10)
                else:
                    pygame.draw.rect(screen,(random.randint(0,20),200+random.randint(0,20),random.randint(0,20)),(j*lyx,i*lyy,lyx,lyy))
            
            #Explosion
            elif el == 67:
                if photo:
                    eColor = Color(255,230,40)
                else:
                    pygame.draw.rect(screen,(random.randint(150,255),random.randint(50,230),random.randint(0,40)),(j*lyx,i*lyy,lyx,lyy))
            
            #TNT
            elif el == 68:
                eColor = Color(200,0,0)
            
            #C4
            elif el == 69:
                if et == 1:
                    if photo:
                        eColor = Color(255,200,0)
                    else:
                        pygame.draw.rect(screen,(255,random.randint(0,255),random.randint(0,255)),(j*lyx,i*lyy,lyx,lyy))
                else:
                    eColor = Color(200,180,150)
            
            #Nuke
            elif el == 70:
                eColor = Color(80,100,60)
            
            #Holy Water
            elif el == 71:
                if not (et == 0 or photo):
                    eColor = Color(200,255,230)
                else:
                    eColor = Color(200,200,255)
            
            #Dead Plant
            elif el == 72:
                eColor = Color(clamp(120-et),clamp(60-(et//5)),clamp(10-(et//10)))
            
            #Coal
            elif el == 73:
                eColor = Color(20,20,20)
            
            #Natural Gas
            elif el == 74:
                eColor = Color(60,30,15)
            
            #Polluted Water
            elif el == 75:
                if photo:
                    eColor = Color(0,150,75)
                else:
                    eColor = Color(0,random.randint(100,200),random.randint(30,100))
            
            #Greenhouse Sun
            elif el == 76:
                if et == 1:
                    eColor = Color(255,150,120)
                else:
                    #Eclipsed GreenhouseSun
                    override = True
                    pygame.draw.rect(screen,(10,0,0),(j*lyx,i*lyy,lyx,lyy))
                    pygame.draw.rect(screen,(255,0,0),(j*lyx,i*lyy,lyx,lyy),2)
            
            #Wax
            elif el == 77:
                
                eColor = Color(clamp(200+et*2),clamp(150+et*5),clamp(60+et*10))

            #Honeycomb
            elif el == 78:
                eColor = Color(230,200,70)
            
            #Honey
            elif el == 79:
                eColor = Color(160,100,23)
            
            #Bees
            elif el == 80:
                cool = clamp(230+(et//100)*10)
                override = True
                pygame.draw.rect(screen,(cool,cool,100),(j*lyx,i*lyy,lyx,lyy))
                #Wait...drawing more than just one thing? Only for lively creatures!
                pygame.draw.rect(screen,(23,23,23),(j*lyx+lyx/4,i*lyy,lyx/2,lyy))
            
            #Blood
            elif el == 81:
                if photo:
                    cool = 10
                else:
                    cool = random.randint(1,10)
                if et == 1:
                    cool *= 2
                elif et == 0:
                    cool = 0
                eColor = Color(255,cool,cool)

            #Red Sand
            elif el == 82:
                eColor = Color(200,128,0)

            #Good Smoke
            elif el == 83:
                if photo:
                    cool = 15
                else:
                    cool = et*random.randint(10,20)
                clamp(cool)
                eColor = Color(cool,cool,cool)
        
            #Acid Waste
            elif el == 84:
                if photo:
                    eColor = Color(5,180,5)
                else:
                    eColor = Color(random.randint(0,10),150+random.randint(0,60),random.randint(0,10))

            #Thick water
            elif el == 85:
                eColor = Color(40,60,255)

            #Filler
            elif el == 86:
                eColor = Color(100,0,240)
            
            #Snake
            elif el == 87:
                eColor = Color(0,128,0)

            #Tesla Coil
            elif el == 88:
                if et == 0:
                    eColor = Color(200,200,0)
                elif et == 1:
                    eColor = Color(255,255,255)
                else:
                    eColor = Color(255,255,0)

            #Battery
            elif el == 89:
                #Visual pulsing~
                if photo:
                    eColor = Color(55,55,55)
                else:
                    eColor = Color(clamp(60-et),clamp(60-et),clamp(60-et))

            #Thunder Clouds
            elif el == 90:
                if photo:
                    cool = 4
                else:
                    cool = random.randint(0,8)
                eColor = Color(clamp(120+cool),clamp(120+cool),clamp(120+cool))

            #Pollen
            elif el == 91:
                eColor = Color(255,230,128)
            
            #Flower bud
            #Petal
            elif el == 92:
                eColor = Color(255,255,255)
                #Depending on it's temp, it'll be a different color
                if et == 0:
                    eColor = Color(0,64,0)
                elif et == 1:
                    eColor = Color(255,0,0)
                elif et == 2:
                    eColor = Color(255,128,0)
                elif et == 3:
                    eColor = Color(255,255,0)
                elif et == 4:
                    eColor = Color(128,255,0)
                elif et == 5:
                    eColor = Color(0,255,0)
                elif et == 6:
                    eColor = Color(0,255,128)
                elif et == 7:
                    eColor = Color(255,255,255)
                elif et == 8:
                    eColor = Color(0,128,255)
                elif et == 9:
                    eColor = Color(0,0,255)
                elif et == 8:
                    eColor = Color(128,0,255)
                elif et == 9:
                    eColor = Color(255,0,255)
                elif et == 10:
                    eColor = Color(128,0,255)
                elif et == 11:
                    eColor = Color(128,128,128)

            #Feathers
            elif el == 93:
                #Read glass shards
                if photo:
                    eColor = Color(235,235,235)
                else:
                    random.seed(et)
                    cool = 200+random.randint(0,55)
                    eColor = Color(cool,cool,cool)
                    random.seed()

            

            #Molten Glass
            elif el == 95:
                if photo:
                    eColor = Color(127,244,244)
                else:
                    eColor = Color(random.randint(0,172),200+random.randint(0,55),200+random.randint(0,55))




            #Frosted Sand
            elif el == 101:
                eColor = Color(220,250,230)

            #Static
            elif el == 102:
                if photo:
                    eColor = Color(255,0,255)
                else:
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
                    eColor = Color(coolr,coolg,coolb)

            #TV Static
            elif el == 103:
                
                if photo:
                    eColor = Color(127,127,127)
                else:
                    if et > 255:
                        et = 255
                    elif et < 0:
                        et = 0
                    eColor = Color(et,et,et)

            #Redundancy ftw!
            eColor.r = clamp(int((eColor.r/100)*gamma))
            eColor.g = clamp(int((eColor.g/100)*gamma))
            eColor.b = clamp(int((eColor.b/100)*gamma))

            if not override:
                pygame.draw.rect(screen,eColor,(j*lyx,i*lyy,lyx,lyy))

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