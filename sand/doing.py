# ======================================================================================
# ----------- The thing that makes all of this possible, it's DOSTUFF (Now in it's own file!)!!!! --------------
# ======================================================================================
from physics import coinflip
import physics
import random
from copy import deepcopy

def doLessStuff(plain: list[list[int]]) -> list[list[int]]:
    e = 0
    
    grid = deepcopy(plain)
    for a in range(len(plain)):
        for b in range(len(plain[0])):
            if coinflip():
                bb = len(plain[0])-b-1
            else:
                bb = b
            
            if plain[a][bb] != grid[a][bb]:
                continue
            
            e = plain[a][bb]
            
            au = False
            ad = False
            al = False
            ar = False
            
            if a + 1 < len(plain):
                ad = True
            if a - 1 > -1:
                au = True
            if bb + 1 < len(plain[0]):
                ar = True
            if bb - 1 > -1:
                al = True
            
            miniplain = []
            minigrid = []
            localPos = (1,1)
            
            if plain[a][bb] != 0:
                for i in range(0-int(au),1+int(ad)):
                    p = []
                    for j in range(0-int(al),1+int(ar)):
                        if (i,j) == (0,0):
                            p.append("self")
                            localPos = (1-int(not au),1-int(not al))
                            continue
                        p.append(plain[a+i][bb+j])
                    miniplain.append(tuple(p))
            
            if plain[a][bb] != 0:
                for i in range(0-int(au),1+int(ad)):
                    g = []
                    for j in range(0-int(al),1+int(ar)):
                        if (i,j) == (0,0):
                            g.append("self")
                            localPos = (1-int(not au),1-int(not al))
                            continue
                        g.append(grid[a+i][bb+j])
                    minigrid.append(tuple(g))
            
            miniplain = tuple(miniplain)
            minigrid = tuple(minigrid)
            
            #No need to try, there's no way it'll fail!
                
            #Air
            
            if e == 0:
                continue
            
            #Sand
            
            elif e == 1:
                c = physics.sandCheckLess(minigrid,localPos)
                if c == 0:
                    continue
                else:
                    grid[a][bb] = 0
                    grid[a+1][bb+(c-2)] = e

            #wall
            elif e == 4:
                continue
    return grid




def doStuff(plain: list[list[list[int]]],switch: bool,lifeIG: bool = False) -> list[list[list[int]]]:
    e = 0
    t = 0
    #I'll take my small victories in optimization where I can
    
    #The tuple that holds the elements that are required to have a mini plane map
    requireminip = [1,2,3,4,6,7,8,9,10,11,14,15,16,17,18,19,20,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,53,54,55,56,58,59,60,62,65,66,68,69,70,71,72,73,74,75,77,78,79,80,81,82,83,84,85,88,89]
    if lifeIG:
        requireminip.append(0)
        requireminip.append(26)
    requireminip = tuple(requireminip)
    
    #The tuple that holds the elements that are required to have a mini grid map
    requireminig = (1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,22,23,24,25,27,28,29,30,32,34,36,39,40,41,42,43,44,45,46,47,48,49,51,52,53,54,55,56,57,58,60,62,63,64,65,66,68,70,71,72,73,74,75,77,78,79,80,81,82,83,84,85)
    
    
    waters = (3,15,47,71,75,85)
        
    goodFossilizers = (2,9,12,18,29,32,38,40,51,53,55,58,72,73)
    
    conductors = (38,39,40,44,47,55,58,59,69,81,88,89)

    acidImmune = (0,2,3,5,9,12,16,17,20,21,30,35,38,43,47,50,51,53,55,56,61,64,65,66,71,89)

    blastProof = (5,12,61,67)
    
    virusProof = (0,57,71)
    
    plantSustainers = (8,28,31,62)
    
    #Self explanitory
    supersun: bool = physics.checkEverywhere(plain,[76,0])
    sun: bool = (physics.checkEverywhere(plain,[20,0]) or supersun)
    moon: bool = physics.checkEverywhere(plain,[21,0])
    jam: bool = physics.checkAbsolutelyEverywhere(plain,50)
    grid = deepcopy(plain)
    for a in range(len(plain)):
        for b in range(len(plain[0])):
            if switch:
                bb = len(plain[0])-b-1
            else:
                bb = b
            
            if plain[a][bb] != grid[a][bb]:
                continue
            
            e = plain[a][bb][0]
            t = plain[a][bb][1]
            
            au = False
            ad = False
            al = False
            ar = False
            
            if a + 1 < len(plain):
                ad = True
            if a - 1 > -1:
                au = True
            if bb + 1 < len(plain[0]):
                ar = True
            if bb - 1 > -1:
                al = True
            
            miniplain = []
            minigrid = []
            localPos = (1,1)
            
            if plain[a][bb][0] in requireminip:
                for i in range(0-int(au),1+int(ad)):
                    p = []
                    for j in range(0-int(al),1+int(ar)):
                        if (i,j) == (0,0):
                            p.append(("self",e))
                            localPos = (1-int(not au),1-int(not al))
                            continue
                        p.append(tuple(plain[a+i][bb+j]))
                    miniplain.append(tuple(p))
            
            if plain[a][bb][0] in requireminig:
                for i in range(0-int(au),1+int(ad)):
                    g = []
                    for j in range(0-int(al),1+int(ar)):
                        if (i,j) == (0,0):
                            g.append(("self",e))
                            localPos = (1-int(not au),1-int(not al))
                            continue
                        g.append(tuple(grid[a+i][bb+j]))
                    minigrid.append(tuple(g))
            
            miniplain = tuple(miniplain)
            minigrid = tuple(minigrid)
            
            #Possibly my biggest try statement
            
            try:
                
                #Air
                
                if e == 0:
                    if not lifeIG:
                        continue
                    #I need to optimize this more it's laggy as hell currently :(
                    l = physics.neighborCount(miniplain,[37])
                    if l == 3:
                        grid[a][bb] = [37,0]
                        continue
                    else:
                        l = physics.neighborCount(miniplain,[26])
                        if l == 3:
                            grid[a][bb] = [26,0]
                            continue
                
                #Sand
                
                elif e == 1:
                    if physics.neighborCheck(miniplain,(9,30,55,67)):
                        e = 14
                        t = 2
                    elif random.randint(1,50) == 1:
                        if physics.neighborCheck(miniplain,(3,15,71)):
                            e = 10
                        elif physics.neighborCheck(miniplain,(79,81)):
                            e = 82
                    elif random.randint(1,42) == 1:
                        if physics.neighborCheck(miniplain,[53]):
                            e = 51
                    else:
                        n = physics.neighborTempCheck(miniplain,[14])
                        if n[0]:
                            e = 14
                            t = n[1]-1
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if e == 1:
                            continue
                        else:
                            grid[a][bb] = [e,t]
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Stone
                
                elif e == 2:
                    if random.randint(1,1000) == 1:
                        if physics.neighborCheck(miniplain,waters):
                            e = 11
                    elif coinflip():
                        if physics.neighborCheck(miniplain,(61,65,66)):
                            e = 11
                    elif physics.neighborCheck(miniplain,[67]):
                        e = 11
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Water
                
                elif e == 3:
                    if coinflip():
                        if (physics.neighborCheck(miniplain,(30,67)) or (sun and random.randint(1,20000) == 1)):
                            e = 13
                            t = 10
                        elif physics.neighborCount(miniplain,(22,23,27)) > 3:
                            e = 27
                        elif physics.neighborCount(miniplain,[71]) > 3:
                            e = 71
                            t = 0
                    if physics.neighborCheck(miniplain,(9,55)):
                        e = 13
                        t = 15
                    elif random.randint(1,10000) == 1:
                        if physics.neighborCheck(miniplain,[18]):
                            e = 18
                    elif (random.randint(1,101) == 1 and physics.neighborCheck(miniplain,(29,45,50))) or (random.randint(1,12) == 1 and physics.neighborCheck(miniplain,(56,64,65,66,84))):
                        e = 75
                    elif random.randint(1,500) == 1 and physics.neighborCheck(miniplain,(79,81)):
                        e = 85
                    c = physics.sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            if e == 3:
                                continue
                            else:
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [0,0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Sugar
                
                elif e == 4:
                    if physics.neighborCheck(miniplain,(9,20,21)):
                        e = 24
                    elif random.randint(1,5) == 1:
                        if physics.neighborCheck(miniplain,(30,67)):
                            e = 30
                            t = 5
                    
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if random.randint(1,100) == 1:
                            if physics.neighborCheck(miniplain,[3]):
                                e = 15
                        elif random.randint(1,5000) == 1:
                            if physics.neighborCheck(miniplain,[18]):
                                e = 18
                        if e == 4:
                            continue
                        else:
                            grid[a][bb] = [e,t] 
                    else:
                        if random.randint(1,10) == 1:
                            if physics.neighborCheck(miniplain,[3]):
                                e = 15
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = physics.lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a+1][bb] = [e,0]
                            else:
                                if d[1]:
                                    grid[a+1][bb+1] = [e,0]
                                else:
                                    grid[a+1][bb-1] = [e,0]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,0]
                
                #Wall
                
                elif e == 5:
                    continue          
                
                #Dirt
                
                elif e == 6:
                    if random.randint(1,900) == 1:
                        if sun and physics.neighborCheck(miniplain,[8]) and physics.neighborCount(miniplain,[8]) < 2:
                            e = 8
                    if random.randint(1,100) == 1:
                        if physics.neighborCheck(miniplain,(3,15,71)):
                            e = 7
                    c = physics.sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        if e == 6:
                            continue
                        else:
                            grid[a][bb] = [e,0]
                    else:
                        grid[a][bb] = [0,0]
                        grid[a+1][bb+(c[0]-2)] = [e,0]
                
                #Mud
                
                elif e == 7:
                    if random.randint(1,400) == 1:
                        if sun and physics.neighborCheck(miniplain,[8]) and physics.neighborCount(miniplain,[8]) < 4:
                            e = 8
                    if physics.neighborCheck(miniplain,(9,30,55,67)):
                        e = 6
                    elif random.randint(1,100) == 1:
                        if physics.neighborCheck(miniplain,(46,47,48)):
                            e = 6
                    elif random.randint(1,40) == 1:
                        if sun and physics.neighborCount(miniplain,(3,10,7,15,27)) < 3:
                            e = 6
                    if random.randint(1,5000) == 1:
                        if physics.neighborCheck(miniplain,[18]):
                            e = 18
                        elif physics.neighborCheck(miniplain,[8]):
                            e = 8
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        if e == 7:
                            continue
                        else:
                            grid[a][bb] = [e,0]
                
                #Plant
                
                elif e == 8:
                    
                    if (random.randint(1,30) == 1 and physics.neighborCheck(miniplain,(23,46,47,48,61))) or (supersun and random.randint(1,10000) == 1) or physics.neighborCheck(miniplain,(9,30,55,67)):
                        e = 72
                        t = 0
                    elif coinflip() and physics.neighborCheck(miniplain,[53]):
                        e = 57
                        t = 0
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Lava
                
                elif e == 9:
                    if physics.neighborCheck(miniplain,(3,7,10,13,15,18,22,23,25,27,47,71)):
                        t -= 2
                        if physics.neighborCheck(miniplain,(3,15,22,23,25,27,47,71)):
                            t -= 4
                    
                    if physics.neighborCheck(miniplain,[20]):
                        t = 10
                    elif physics.neighborCheck(miniplain,[21]):
                        t = -10
                    
                    if random.randint(1,10) == 1:
                        if moon:
                            t -= 1
                    if t <= -10:
                        
                        e = 12
                    
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if random.randint(1,25) != 1:
                            grid[a][bb] = [e,t]
                            continue
                        d = physics.lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            grid[a][bb] = [e,t]
                            continue
                        else:
                            grid[a][bb] = [c[1],0]
                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Wet Sand
                
                elif e == 10:
                    if physics.neighborCheck(miniplain,(9,30,55,67)):
                        e = 14
                        t = 1
                    elif random.randint(1,100) == 1:
                        if physics.neighborCheck(miniplain,(46,47,48)):
                            e = 1
                    elif random.randint(1,40) == 1:
                        if sun and physics.neighborCount(miniplain,(3,10,7,15,27)) < 3:
                            e = 1
                    else:
                        n = physics.neighborTempCheck(miniplain,[14])
                        if n[0]:
                            e = 14
                            t = n[1]-1
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        if e == 10:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                
                #Gravel
                
                elif e == 11:
                    if random.randint(1,42) == 1:
                        if physics.neighborCheck(miniplain,[53]):
                            e = 52
                        elif physics.neighborCheck(miniplain,[71]):
                            e = 2
                    elif random.randint(1,3333) == 1:
                        if physics.neighborCheck(miniplain,(3,15,47)):
                            e = 1
                            #It gets converted into sand after awhile! (You need a lot of erosion to do this)
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        continue
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [11,0]
                
                #Obsidian
                
                elif e == 12:
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [12,0]
                    else:
                        continue
                
                #Steam
                
                elif e == 13:
                    if random.randint(1,20) == 1 and t > 0:
                        t -= 1
                    if t <= 0 and random.randint(1,34) == 1:
                        e = 16
                    c = physics.sandCheck(minigrid,localPos,False,True,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos,False,False,True)
                        if not d[0]:
                            if e == 13:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [e,0]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]
                    else:
                        grid[a][bb] = [c[1],t]
                        if c[0] == 2:
                            d = physics.lrWanderCheck(minigrid,localPos,True,False,True)
                            if not d[0]:
                                grid[a-1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a-1][bb+1] = [e,t]
                                else:
                                    grid[a-1][bb-1] = [e,t]
                        else:
                            grid[a-1][bb+(c[0]-2)] = [e,t]
                        
                #Glass
                
                elif e == 14:
                    if coinflip() and t > 0:
                        t -= 1
                    elif physics.neighborCheck(miniplain,(61,67)):
                        e = 19
                        t = random.randint(1,6294)
                    o = physics.lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        continue
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                        
                #Sugar Water
                
                elif e == 15:
                    if sun and random.randint(1,25000) == 1:
                        e = 13
                        t = 8
                    elif physics.neighborCheck(miniplain,(9,55)) or (coinflip() and physics.neighborCheck(miniplain,(30,67))):
                        if coinflip():
                            e = 4
                        else:
                            e = 13
                    elif random.randint(1,2500) == 1:
                        if physics.neighborCheck(miniplain,[18]):
                            e = 18
                        elif physics.neighborCheck(miniplain,[24]):
                            e = 4
                    c = physics.sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos,False,True)
                        if not d[0]:
                            d = physics.udWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                if e == 15:
                                    grid[a][bb] = [e,t]
                                else:
                                    grid[a][bb] = [e,0]
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,0]
                                else:
                                    grid[a-1][bb] = [e,0]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,0]
                            else:
                                grid[a][bb-1] = [e,0]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,0]
                
                #Clouds
                
                elif e == 16:
                    if random.randint(1,800) == 1:
                        if moon:
                            e = 22 
                        else:
                            e = 3
                    elif physics.neighborCount(miniplain,(56,74)) > 6:
                        e = 64
                        t = 15
                    if random.randint(1,20) == 1:
                        if random.randint(1,4) != 1:
                            d = physics.lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]
                                
                                if d[1]:
                                    grid[a][bb+1] = [e,t]
                                else:
                                    grid[a][bb-1] = [e,t]
                        else:
                            d = physics.udWanderCheck(minigrid,localPos)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    grid[a-1][bb] = [e,t]
                    else:
                        continue
                
                #Brick
                
                elif e == 17:
                    if coinflip():
                        if physics.neighborCheck(miniplain,[61]):
                            e = 63
                    o = physics.lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        grid[a][bb] = [e,t]
                        continue
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Algae
                
                elif e == 18:
                    if (random.randint(1,30) == 1 and physics.neighborCheck(miniplain,(23,46,47,48,61))) or (supersun and random.randint(1,10000) == 1) or physics.neighborCheck(miniplain,(30,55,67)):
                        e = 72
                        t = 0
                    elif physics.neighborCheck(miniplain,(46,47,48)):
                        e = 0
                    o = physics.lrCheck(miniplain[localPos[0]],localPos[1],True)
                    if o:
                        continue
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t]
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,0]
                
                #Glass shards or dust or whatever you wanna see it as
                
                elif e == 19:
                    if physics.neighborCheck(miniplain,(9,55)):
                        e = 14
                        t = 3
                    elif coinflip() and physics.neighborCheck(miniplain,(30,71)):
                        e = 14
                        t = 0
                    else:
                        n = physics.neighborTempCheck(miniplain,[14])
                        if n[0]:
                            e = 14
                            t = n[1]-1
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if e == 19:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                #Sun
                
                elif e == 20:
                    if moon:
                        t = 0
                    else:
                        t = 1
                    if supersun or (random.randint(1,100) == 1 and physics.neighborCount(miniplain,[56]) >= 7): #Me when the runaway greenhouse effect
                        e = 76
                    grid[a][bb] = [e,t]
                #Moon
                
                elif e == 21:
                    if random.randint(1,100) == 1 and supersun:
                        grid[a][bb] = [2,0]
                    else:
                        continue
                
                #Snow
                
                elif e == 22:
                    if random.randint(1,100) == 1:
                        if sun:
                            e = 3
                    if random.randint(1,10) == 1:
                        if (not moon) and physics.neighborCheck(miniplain,(3,15)):
                            e = 3
                    if physics.neighborCheck(miniplain,(9,13,20,30,46,47,48,55,67)):
                        e = 3
                    if random.randint(1,5000) == 1:
                        e = 3
                    if random.randint(1,10000) == 1:
                        e = 23
                    if switch:
                        c = physics.sandCheck(minigrid,localPos,True)
                        if c[0] == 0:
                            if e == 22:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [e,0] 
                        else:
                            grid[a][bb] = [c[1],0]
                            if c[0] == 2:
                                d = physics.lrWanderCheck(minigrid,localPos, True)
                                if not d[0]:
                                    grid[a+1][bb] = [e,0]
                                else:
                                    if d[1]:
                                        grid[a+1][bb+1] = [e,0]
                                    else:
                                        grid[a+1][bb-1] = [e,0]
                            else:
                                grid[a+1][bb+(c[0]-2)] = [e,0]
                    else:
                        if e == 22:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                
                #Ice
                
                elif e == 23:
                    if random.randint(1,200) == 1:
                        if sun:
                            e = 3
                    if coinflip():
                        if physics.neighborCheck(miniplain,(13,20)):
                            e = 3
                    if physics.neighborCheck(miniplain,(9,30,46,47,48,55,67)):
                        e = 3
                    if random.randint(1,1000) == 1:
                        if physics.neighborCheck(miniplain,(3,15)):
                            e = 3
                    c = physics.stoneCheck(minigrid,localPos,True)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        if e == 2:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                
                #Sugar Crystal
                
                elif e == 24:
                    if random.randint(1,7000) == 1:
                        if physics.neighborCheck(miniplain,[18]):
                            e = 18
                    elif random.randint(1,5000) == 1:
                        if physics.neighborCheck(miniplain,[3,15]):
                            e = 4
                    elif random.randint(1,50) == 1:
                        if physics.neighborCheck(miniplain,(30,67)):
                            e = 30
                            t = 5
                    elif random.randint(1,8) > 3:
                        if physics.neighborCheck(miniplain,[61]):
                            e = 4
                    o = physics.lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        if e == 24:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        if e == 24:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                
                #Packed Ice
                
                elif e == 25:
                    if random.randint(1,5) == 1:
                        if physics.neighborCheck(miniplain,(9,48,55,71)) or supersun:
                            e = 23
                    o = physics.lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        continue
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        if e == 25:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                
                #Life WORKING?!!~?!?!?!@43TUHREGAGR\\\
                
                elif e == 26:
                    if lifeIG:
                        #Now life has a few more rules that tell it that it's neighbors don't have to be it's own kind of life, but can be of different kinds of life or things that allow for life! (This should have very interesting effects)
                        l = physics.neighborCount(miniplain,(4,8,15,21,24,26,28,31,37,71))
                        if jam or supersun:
                            if l < random.randint(0,10) or l > random.randint(0,10):
                                grid[a][bb] = [0,0]
                            else:
                                grid[a][bb] = [26,0]
                        else:
                            if l < 2 or l > 3:
                                grid[a][bb] = [0,0]
                            else:
                                grid[a][bb] = [26,0]
                        continue
                    else:
                        grid[a][bb] = physics.randomElement()
                        continue
                
                #Sludge
                
                elif e == 27:
                    if (sun and random.randint(1,50) == 1) or ((not moon) and random.randint(1,500) == 1) or physics.neighborCheck(miniplain,(3,15,46,47,48)):
                        e = 3
                    if coinflip():
                        if (not moon) and physics.neighborCheck(miniplain,(3,15)):
                            e = 3
                    if coinflip() and e != 27:
                        if physics.neighborCount(miniplain,[22,23,27]) > 3:
                            e = 27
                    if random.randint(1,20) == 1:
                        if physics.neighborCount(miniplain,[22,23,27]) > 4:
                            e = 23
                    if physics.neighborCheck(miniplain,(9,13,20,30,55,67)):
                        e = 13
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if e == 27:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            grid[a+1][bb] = [e,0]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,0]

                #Flower things
                
                elif e == 28:
                    if jam:
                        t = 1
                        continue
                    if random.randint(1,4) == 1:
                        if physics.neighborCheck(miniplain,(9,30,55,67)):
                            if coinflip():
                                e = 30
                                t = 5
                            else:
                                e = 32
                    #Seed
                    if plain[a][bb][1] == 0:
                        c = physics.sandCheck(minigrid,localPos)
                        if c[0] == 0:
                            if random.randint(1,100) == 1 and physics.neighborCheck(miniplain,(7,8,10,18,27,32,71)) and not physics.neighborCheck(miniplain,(46,47,48)):
                                grid[a][bb] = [e,random.randint(2,8)]
                            else:
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                    #Stem
                    elif plain[a][bb][1] > 1 and a - 1 != 0:
                        t -= 1
                        grid[a-1][bb] = [e,t]
                        t = -1
                        grid[a][bb] = [e,t]
                    #Bloom
                    elif plain[a][bb][1] != -1:
                        grid[a][bb] = [36,random.randint(0,11)]
                        c = random.randint(0,11)
                        if a + 1 != len(plain):
                            grid[a+1][bb] = [36,c]
                        if a - 1 != -1 and grid[a-1][bb][0] == 0:
                            grid[a-1][bb] = [36,c]
                        if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                            grid[a][bb+1] = [36,c]
                        if bb - 1 != -1 and grid[a][bb-1][0] == 0:
                            grid[a][bb-1] = [36,c]
                           
                #Oil (Pls don't take americuh)
                
                elif e == 29:
                    if random.randint(1,15) == 1:
                        if physics.neighborCheck(miniplain,(9,30,55,67)):
                            e = 30
                            t = 5
                    elif coinflip() and physics.neighborCheck(miniplain,[71]):
                        e = 7
                        t = 0
                    c = physics.sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos,False,True)
                        if not d[0]:
                            d = physics.udWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                if e == 29:
                                    grid[a][bb] = [e,t]
                                else:
                                    grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],t]

                                if d[1]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    grid[a-1][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,0]
                
                #Fire
                
                elif e == 30:
                    flame = False
                    superflame = False
                    if (random.randint(1,4) == 1 or moon or jam or physics.neighborCount(miniplain,[56]) > 3) and t > 0:
                        if not sun:
                            t -= 1
                        else:
                            if coinflip():
                                t -= 1
                    if physics.neighborCheck(miniplain,(4,8,15,18,20,24,28,29,31,36,49,53,57,72,73,74,76)):
                        if moon:
                            if (coinflip() or sun) and t < 2:
                                t = 2
                        else:
                            t = 5
                        flame = True
                        if physics.neighborCheck(miniplain,(29,53,73,74,76)):
                            superflame = True
                    elif physics.neighborCheck(miniplain,(33,59)) and t < 2:
                        t = 2
                    elif random.randint(1,10) == 1:
                        o = physics.neighborTempCheck(miniplain,[30],">",t)
                        if o[0]:
                            t = o[1] - 1
                    if physics.neighborCheck(miniplain,(3,15,47,71)):
                        e = 56
                        t *= 2
                    elif t <= 0:
                        e = 56
                        t = 10
                    if flame and (random.randint(1,15) != 1 or superflame):
                        c = [0]
                        if superflame and random.randint(1,5) == 2:
                            if coinflip() and a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                                grid[a+1][bb] = [56,10]
                            if coinflip() and a - 1 != -1 and grid[a-1][bb][0] == 0:
                                grid[a-1][bb] = [56,10]
                            if coinflip() and bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                                grid[a][bb+1] = [56,10]
                            if coinflip() and bb - 1 != -1 and grid[a][bb-1][0] == 0:
                                grid[a][bb-1] = [56,10]
                    else:
                        c = physics.sandCheck(minigrid,localPos,False,True,True)
                    if c[0] == 0:
                        if flame and random.randint(1,8) != 1:
                            d = [False]
                        else:
                            d = physics.lrWanderCheck(minigrid,localPos,False,False,True)
                        if not d[0]:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]
                    else:
                        grid[a][bb] = [c[1],t]
                        if c[0] == 2:
                            d = physics.lrWanderCheck(minigrid,localPos,True,False,True)
                            if not d[0]:
                                grid[a-1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a-1][bb+1] = [e,t]
                                else:
                                    grid[a-1][bb-1] = [e,t]
                        else:
                            grid[a-1][bb+(c[0]-2)] = [e,t]
                
                #Wood
                
                elif e == 31:
                    if coinflip():
                        if physics.neighborCount(miniplain,(9,30,55,67)) > random.randint(1,5):
                            e = 32
                    elif random.randint(1,20) == 1:
                        if physics.neighborCheck(miniplain,(30,67)):
                            e = 30
                            t = 5
                    elif random.randint(1,40) == 1:
                        if physics.neighborCheck(miniplain,(9,55)):
                            e = 30
                            t = 5
                    
                    if e != 31:
                        grid[a][bb] = [e,t]
                
                #Ash
                
                elif e == 32:
                    if random.randint(1,1000) == 1:
                        if physics.neighborCount(miniplain,goodFossilizers) > 3:
                            t += random.randint(1,2)
                    elif random.randint(1,100) == 1:
                        if physics.neighborCheck(miniplain,[3,15]):
                            e = 34
                        elif physics.neighborCheck(miniplain,[71]):
                            e = 8
                            t = 0
                    if t >= 100:
                        e = 29
                        t = 0
                    elif jam:
                        t = 0
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t] 
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = physics.lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a+1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a+1][bb+1] = [e,t]
                                else:
                                    grid[a+1][bb-1] = [e,t]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Cloner (Yes, I went there)
                
                elif e == 33:
                    if jam:
                        t = 0
                    elif plain[a][bb][1] == 0:
                        t = physics.myNeighbor(miniplain,[33])
                    else:
                        if a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                            grid[a+1][bb] = [plain[a][bb][1],0]
                        if a - 1 != -1 and grid[a-1][bb][0] == 0:
                            grid[a-1][bb] = [plain[a][bb][1],0]
                        if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                            grid[a][bb+1] = [plain[a][bb][1],0]
                        if bb - 1 != -1 and grid[a][bb-1][0] == 0:
                            grid[a][bb-1] = [plain[a][bb][1],0]
                    grid[a][bb] = [e,t]
                
                #Clay
                
                elif e == 34:
                    if physics.neighborCheck(miniplain,(9,30,55)):
                        e = 17
                    elif physics.neighborCheck(miniplain,[67]):
                        e = 63
                    
                    c = physics.sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        if random.randint(1,40) != 1:
                            if random.randint(1,10) == 1:
                                d = physics.udWanderCheck(minigrid,localPos,True)
                            else:
                                d = [False]
                            if not d[0]:
                                if e == 17:
                                    grid[a][bb] = [e,t]
                                    continue
                                else:
                                    grid[a][bb] = [e,0]
                                    continue
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,0]
                                else:
                                    grid[a-1][bb] = [e,0]
                                continue
                            
                        d = physics.lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            if e == 17:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [e,0]
                        else:
                            grid[a][bb] = [c[1],0]
                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #VOID
                
                elif e == 35:
                    if jam or physics.neighborCheck(miniplain,[71]):
                        continue
                    if a + 1 != len(plain) and grid[a+1][bb][0] != 35:
                        grid[a+1][bb] = [0,0]
                    if a - 1 != -1 and grid[a-1][bb][0] != 35:
                        grid[a-1][bb] = [0,0]
                    if bb + 1 != len(plain[0]) and grid[a][bb+1][0] != 35:
                        grid[a][bb+1] = [0,0]
                    if bb - 1 != -1 and grid[a][bb-1][0] != 35:
                        grid[a][bb-1] = [0,0]
                
                #Petal
                
                elif e == 36:
                    if random.randint(1,15) == 1:
                        if physics.neighborCheck(miniplain,(9,30,55,67)):
                            if coinflip():
                                e = 30
                                t = 5
                            else:
                                e = 32
                    if physics.neighborCheck(miniplain,plantSustainers):
                        c = [True]
                    else:
                        c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Cancer (Doesn't know how to die)
                
                elif e == 37:
                    if lifeIG:
                        if physics.neighborCheck(miniplain,[71]):
                            grid[a][bb] = [0,0]
                        elif jam:
                            #This makes it obey Life's rules
                            l = physics.neighborCount(miniplain,(4,8,15,21,24,26,28,31,37))
                            if l < 2 or l > 3:
                                grid[a][bb] = [0,0]
                            else:
                                grid[a][bb] = [37,0]
                        continue
                    else:
                        grid[a][bb] = physics.randomElement()
                
                #Iron
                
                elif e == 38:
                    if random.randint(1,1000) == 1:
                        if physics.neighborCheck(miniplain,(3,15,47)):
                            e = 44
                    if t == 1 or jam:
                        t = 2
                    elif (physics.neighborCheck(miniplain,[43]) or physics.neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    grid[a][bb] = [e,t] 
                
                #Iron Sand
                
                elif e == 39:
                    if random.randint(1,1000) == 1:
                        if physics.neighborCheck(miniplain,[3,15,47]):
                            e = 45
                    elif physics.neighborCheck(miniplain,(9,55)):
                        e = 38
                    
                    if t == 1 or jam:
                        t = 2
                    elif (physics.neighborCheck(miniplain,[43]) or physics.neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t]
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Iron Brick
                
                elif e == 40:
                    if random.randint(1,1000) == 1:
                        if physics.neighborCheck(miniplain,[3,15,47]):
                            e = 44
                    if t == 1 or jam:
                        t = 2
                    elif (physics.neighborCheck(miniplain,[43]) or physics.neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    o = physics.lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        grid[a][bb] = [e,t]
                        continue
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Smart Remover (Based on the bacteria mod from minecraft)
                
                elif e == 41:
                    if jam:
                        t = 0
                        if random.randint(1,4) == 1:
                            e = 0
                    elif t == 0:
                        if a + 1 != len(plain) and grid[a+1][bb][0] != 0 and plain[a+1][bb][1] != 41 and (physics.neighborCheck(miniplain,[43]) or physics.neighborTempCheck(miniplain,conductors,"==",1)[0]):
                            t = grid[a+1][bb][0]
                    elif t != 41:
                        if a + 1 != len(plain) and grid[a+1][bb][0] == t:
                            grid[a+1][bb] = [e,t]
                        if a - 1 != -1 and grid[a-1][bb][0] == t:
                            grid[a-1][bb] = [e,t]
                        if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == t:
                            grid[a][bb+1] = [e,t]
                        if bb - 1 != -1 and grid[a][bb-1][0] == t:
                            grid[a][bb-1] = [e,t]
                        if not physics.neighborCheck(miniplain,[t]) or physics.neighborCount(miniplain,[41]) == 0:
                            e = 0
                            t = 0
                    c = physics.stoneCheck(minigrid,localPos,True)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Smart Converter (Probably my most complicated element yet since it's temprature is off the charts!)
                
                elif e == 42:
                    if jam:
                        t = 0
                        if random.randint(1,4) == 1:
                            e = 0
                    elif t == 0:
                        if a + 1 != len(plain) and grid[a+1][bb][0] != 0 and grid[a+1][bb][1] != 42 and a - 1 != -1 and grid[a-1][bb][0] != 0 and grid[a-1][bb][1] != 42 and (physics.neighborCheck(miniplain,[43]) or physics.neighborTempCheck(miniplain,conductors,"==",1)[0]):
                            #This is complex, lemme explain
                            
                            t = grid[a-1][bb][0]*1000
                            #This gets the value of the pixel above it and multiplies it by 1000, so when we do our lil // later, we can get this element back
                            
                            t += grid[a+1][bb][0]
                            #This gets the value of the pixel below it and adds it to the temp, so when we can do our lil % later and get this element back too!
                    else:
                        rt = t//1000 #The element that's gonna REPLACE the converted element
                        ct = t%1000 #The element that's gonna get CONVERTED into the replaced element
                        if rt != 42 and ct != 42:
                            if a + 1 != len(plain) and grid[a+1][bb][0] == ct:
                                grid[a+1][bb] = [e,t]
                            if a - 1 != -1 and grid[a-1][bb][0] == ct:
                                grid[a-1][bb] = [e,t]
                            if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == ct:
                                grid[a][bb+1] = [e,t]
                            if bb - 1 != -1 and grid[a][bb-1][0] == ct:
                                grid[a][bb-1] = [e,t]
                            if not physics.neighborCheck(miniplain,[ct]) or physics.neighborCount(miniplain,[42]) == 0:
                                e = rt
                                t = 0
                    c = physics.stoneCheck(minigrid,localPos,True)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                
                #Electricity
                
                elif e == 43:
                    c = physics.sandCheck(minigrid,localPos,True)
                    if c[0] == 0 or jam:
                        grid[a][bb] = [0,0]
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = physics.lrWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                grid[a+1][bb] = [e,0]
                            else:
                                if d[1]:
                                    grid[a+1][bb+1] = [e,0]
                                else:
                                    grid[a+1][bb-1] = [e,0]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,0]
                
                #Rusted Iron
                
                elif e == 44:
                    if coinflip() and physics.neighborCheck(miniplain,[71]):
                            e = 38
                    elif random.randint(1,1000) == 1:
                        if physics.neighborCheck(miniplain,(3,15,47)):
                            e = 45
                    if t == 1 or jam:
                        t = 2
                    elif physics.neighborTempCheck(miniplain,conductors,"==",1)[0] and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    o = physics.lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        grid[a][bb] = [e,t]
                        continue
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Rust
                
                elif e == 45:
                    if coinflip() and physics.neighborCheck(miniplain,[71]):
                        e = 40
                    elif random.randint(1,6) == 1 and physics.neighborCheck(miniplain,[75]):
                        e = 75
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if e == 1:
                            continue
                        else:
                            grid[a][bb] = [e,t]
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Salt
                
                elif e == 46:
                    if physics.neighborCheck(miniplain,(9,55)):
                        e = 55
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if random.randint(1,100) == 1:
                            if physics.neighborCheck(miniplain,[3]):
                                e = 47
                        grid[a][bb] = [e,t]
                    else:
                        if random.randint(1,10) == 1:
                            if physics.neighborCheck(miniplain,[3]):
                                e = 47
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Salt Water
                
                elif e == 47:
                    if t == 1 or jam:
                        t = 2
                    elif (physics.neighborCheck(miniplain,[43]) or physics.neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    if sun and random.randint(1,10000) == 1:
                        e = 13
                        t = 12
                    elif physics.neighborCheck(miniplain,(9,55)) or (coinflip() and physics.neighborCheck(miniplain,(30,67))):
                        if coinflip():
                            e = 46
                        else:
                            e = 13
                    elif random.randint(1,100) == 1 and physics.neighborCheck(miniplain,(4,15)):
                        e = 71
                    c = physics.sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos,False,True)
                        if not d[0]:
                            d = physics.udWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    grid[a-1][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Salt Crystal
                
                elif e == 48:
                    if physics.neighborCheck(miniplain,(9,55)):
                        e = 55
                    elif random.randint(1,5000) == 1:
                        if physics.neighborCheck(miniplain,[3,47]):
                            e = 46
                    elif random.randint(1,3):
                        if physics.neighborCheck(miniplain,[61]):
                            e = 46
                    
                    o = physics.lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        grid[a][bb] = [e,t]
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        if e == 24:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,0]
                
                #leaf
                
                elif e == 49:
                    if t > 9 or random.randint(1,10-t) == 1:
                        if (random.randint(1,10) == 1 and physics.neighborCheck(miniplain,(23,46,47,48,61))) or (supersun and random.randint(1,10000) == 1) or physics.neighborCheck(miniplain,(30,55,67)):
                            e = 72
                            t = 0
                    if physics.neighborCheck(miniplain,[71]):
                        t = 0
                        if random.randint(1,14) == 1:
                            e = 36
                            t = random.randint(0,11)
                    
                    if coinflip() or (physics.neighborCheck(miniplain,plantSustainers) and not (((random.randint(1,400) == 1 and moon)) or physics.neighborCheck(miniplain,[61]) or t == 1)):
                        grid[a][bb] = [e,t]
                        continue
                    if t == 0:
                        t = 1
                    elif random.randint(1,200) == 1 and t < 8:
                        t += 1
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t] 
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = physics.lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a+1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a+1][bb+1] = [e,t]
                                else:
                                    grid[a+1][bb-1] = [e,t]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                
                
                #Antisand
                
                elif e == 51:
                    c = physics.sandCheck(minigrid,localPos,False,True)
                    if c[0] == 0:
                        grid[a][bb] = [e,t]
                        continue
                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a-1][bb+(c[0]-2)] = [e,t]
                
                #Antistone
                
                elif e == 52:
                    c = physics.stoneCheck(minigrid,localPos,False,True)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a-1][bb] = [e,0]
                    else:
                        grid[a][bb] = [e,0]
                
                #Antiwater
                
                elif e == 53:
                    if (physics.neighborCheck(miniplain,(30,67)) or (sun and random.randint(1,20000) == 1)):
                            e = 25
                    elif (moon and random.randint(1,20000) == 1):
                            e = 13
                            t = 5
                    c = physics.sandCheck(minigrid,localPos,True,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos,False,True,True)
                        if not d[0]:
                            if e == 3:
                                continue
                            else:
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [0,0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a-1][bb+(c[0]-2)] = [e,t]
                
                #IDENTITY NOT FOUND =( https://www.youtube.com/watch?v=4bLf2wDJA5s
                elif e == 54:
                    
                    idk = random.randint(1,6)
                    t = idk
                    if jam or physics.neighborCheck(miniplain,[71]):
                        e = idk
                    
                    #Sandbit
                    
                    if idk == 1:
                        if physics.neighborCheck(miniplain,(9,30,55,67)):
                            e = 14
                            t = 2
                        else:
                            n = physics.neighborTempCheck(miniplain,[14])
                            if n[0]:
                                e = 14
                                t = n[1]-1
                            elif random.randint(1,50) == 1:
                                if physics.neighborCheck(miniplain,(3,15)):
                                    e = 10
                        c = physics.sandCheck(minigrid,localPos)
                        if c[0] == 0:
                            if e == 1:
                                continue
                            else:
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                    
                    #Stonebit
                    
                    elif idk == 2:
                        if random.randint(1,1000) == 1:
                            if physics.neighborCheck(miniplain,[3,15,47]):
                                e = 11
                        c = physics.stoneCheck(minigrid,localPos)
                        if not c[0]:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,t]
                    
                    #Waterbit
                    
                    elif idk == 3:
                        if coinflip():
                            if physics.neighborCheck(miniplain,[30]):
                                e = 13
                                t = 10
                            elif physics.neighborCount(miniplain,[22,23,27]) > 3:
                                e = 27
                        if physics.neighborCheck(miniplain,(9,55)):
                            e = 13
                            t = 15
                        elif random.randint(1,10000) == 1:
                            if physics.neighborCheck(miniplain,[18]):
                                e = 18
                        elif random.randint(1,20000) == 1:
                            if sun:
                                e = 13
                                t = 10
                        c = physics.sandCheck(minigrid,localPos,True)
                        if c[0] == 0:
                            d = physics.lrWanderCheck(minigrid,localPos)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [0,0]

                                if d[1]:
                                    grid[a][bb+1] = [e,t]
                                else:
                                    grid[a][bb-1] = [e,t]

                        else:
                            grid[a][bb] = [0,0]

                            grid[a+1][bb+(c[0]-2)] = [e,t]
                    
                    #Sugarbit
                    
                    elif idk == 4:
                        if physics.neighborCheck(miniplain,(9,20,21)):
                            e = 24
                        elif random.randint(1,5) == 1:
                            if physics.neighborCheck(miniplain,[30]):
                                e = 30
                                t = 5
                        
                        c = physics.sandCheck(minigrid,localPos)
                        if c[0] == 0:
                            if random.randint(1,100) == 1:
                                if physics.neighborCheck(miniplain,[3]):
                                    e = 15
                            elif random.randint(1,5000) == 1:
                                if physics.neighborCheck(miniplain,[18]):
                                    e = 18
                            grid[a][bb] = [e,t] 
                            continue
                        else:
                            if random.randint(1,10) == 1:
                                if physics.neighborCheck(miniplain,[3]):
                                    e = 15
                            grid[a][bb] = [c[1],0]
                            if c[0] == 2:
                                d = physics.lrWanderCheck(minigrid,localPos, True)
                                if not d[0]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    if d[1]:
                                        grid[a+1][bb+1] = [e,t]
                                    else:
                                        grid[a+1][bb-1] = [e,t]
                            else:
                                grid[a+1][bb+(c[0]-2)] = [e,t]
                    
                    #Wallbit
                    
                    elif idk == 5:
                        continue          
                    
                    #Dirtbit
                    
                    elif idk == 6:
                        if random.randint(1,900) == 1:
                            if physics.neighborCheck(miniplain,[8]) and sun:
                                e = 8
                        if random.randint(1,100) == 1:
                            if physics.neighborCheck(miniplain,[3]):
                                e = 7
                        c = physics.sandCheck(minigrid,localPos,True)
                        if c[0] == 0:
                            grid[a][bb] = [e,t]
                            continue
                        else:
                            grid[a][bb] = [0,0]
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Jammer
                
                elif e == 50:
                    o = 0
                    t += 1
                    if supersun:
                        t += 2
                        o = -10
                    n = physics.neighborCheck(miniplain,[71])
                    if t <= 50 and not n:
                        grid[a][bb] = [e,t]
                    else:
                        if random.randint(1,20-o) == 1 or n:
                            grid[a][bb] = [61,3]
                        else:
                            grid[a][bb] = [0,0]

                #Molten Salt (Yes, it's a thing)
                
                elif e == 55:
                    if t == 1 or jam:
                        t = 2
                    elif (physics.neighborCheck(miniplain,[43]) or physics.neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    if random.randint(1,25) == 1 or ((not sun) and physics.neighborCheck(miniplain,[8])):
                        e = 46
                    #Too salty to just go away without holyness...
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if random.randint(1,25) != 1:
                            if e == 9:
                                grid[a][bb] = [e,t]
                                continue
                            else:
                                grid[a][bb] = [e,t]
                                continue
                        d = physics.lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            if e == 9:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [c[1],0]
                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Smoke
                
                elif e == 56:
                    if (random.randint(1,10) == 1 and not (moon or sun)) or (random.randint(1,6) == 1 and moon and not sun) or (random.randint(1,12) == 1 and sun and not supersun) or (random.randint(1,20) == 1 and supersun):
                        t -= 1
                    if t <= 0 or physics.neighborCheck(miniplain,[71]):
                        e = 0
                    else:
                        o = physics.neighborTempCheck(miniplain,[56], ">", 5)
                        oo = physics.neighborTempCheck(miniplain,[56], ">", 10)
                        if (not (moon or oo[0])) and ((not sun and random.randint(1,70000) == 1) or (sun and random.randint(1,7000) == 1)) and physics.neighborCount(miniplain,[56]) >= 8 and o[0]:
                            e = 64
                            t = 15
                    c = physics.sandCheck(minigrid,localPos,False,True,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos,False,False,True)
                        if not d[0]:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = physics.lrWanderCheck(minigrid,localPos,True,False,True)
                            if not d[0]:
                                grid[a-1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a-1][bb+1] = [e,t]
                                else:
                                    grid[a-1][bb-1] = [e,t]
                        else:
                            grid[a-1][bb+(c[0]-2)] = [e,t]
                
                
                #Virus
                
                elif e == 57:
                    n = physics.neighborCheck(miniplain,[71])
                    if not (jam or n):
                        if a + 1 != len(plain) and not grid[a+1][bb][0] in virusProof:
                            grid[a+1][bb] = [e,grid[a+1][bb][0]]
                        if a - 1 != -1 and not grid[a-1][bb][0] in virusProof:
                            grid[a-1][bb] = [e,grid[a-1][bb][0]]
                        if bb + 1 != len(plain[0]) and not grid[a][bb+1][0] in virusProof:
                            grid[a][bb+1] = [e,grid[a][bb+1][0]]
                        if bb - 1 != -1 and not grid[a][bb-1][0] in virusProof:
                            grid[a][bb-1] = [e,grid[a][bb-1][0]]
                    if n:
                        if t == 57:
                            e = 0
                        else:
                            e = t
                        t = 0
                    c = physics.stoneCheck(minigrid,localPos,True)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Gold
                
                elif e == 58:
                    if t == 1 or jam:
                        t = 2
                    elif (physics.neighborCheck(miniplain,[43]) or physics.neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    o = physics.lrCheck(miniplain[localPos[0]],localPos[1])
                    if o:
                        grid[a][bb] = [e,t]
                        continue
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Wire
                
                elif e == 59:
                    if coinflip():
                        if physics.neighborCheck(miniplain,(9,30,55,67)):
                            e = 38
                    if t == 1 or jam:
                        t = 2
                    elif physics.neighborTempCheck(miniplain,conductors,"==",1)[0] and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    grid[a][bb] = [e,t]
                
                #Strange Matter (Fun fact: You can't obtain this without disabling life and getting it by random chance since there's no natural process that creates it!)
                
                elif e == 60:
                    n = physics.neighborCheck(miniplain,[71])
                    if not (moon or n):
                        if a + 1 != len(plain) and not grid[a+1][bb][0] in (0,71):
                            grid[a+1][bb] = [e,t]
                        if a - 1 != -1 and not grid[a-1][bb][0] in (0,71):
                            grid[a-1][bb] = [e,t]
                        if bb + 1 != len(plain[0]) and not grid[a][bb+1][0] in (0,71):
                            grid[a][bb+1] = [e,t]
                        if bb - 1 != -1 and not grid[a][bb-1][0] in (0,71):
                            grid[a][bb-1] = [e,t]
                    elif n:
                        e = 0
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        if random.randint(1,25) != 1:
                            grid[a][bb] = [e,t]
                            continue
                        d = physics.lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            grid[a][bb] = [e,t]
                            continue
                        else:
                            grid[a][bb] = [c[1],0]
                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Shockwave
                
                elif e == 61:
                    if t <= 0:
                        e = 0
                    else:
                        if t > 2:
                            if a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                                grid[a+1][bb] = [e,t]
                            if a - 1 != -1 and grid[a-1][bb][0] == 0:
                                grid[a-1][bb] = [e,t]
                            if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                                grid[a][bb+1] = [e,t]
                            if bb - 1 != -1 and grid[a][bb-1][0] == 0:
                                grid[a][bb-1] = [e,t]
                    t -= 1
                    grid[a][bb] = [e,t]
                    
                #Sapling into tree!
                
                elif e == 62:
                    if jam:
                        t = 1
                        continue
                    if random.randint(1,4) == 1:
                        if physics.neighborCheck(miniplain,(9,30,55,67)):
                            if coinflip():
                                e = 30
                                t = 5
                            else:
                                e = 32
                    #Sapling
                    if t == 0:
                        c = physics.stoneCheck(minigrid,localPos)
                        if not c[0]:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb] = [e,t]
                        else:
                            if random.randint(1,100) == 1 and physics.neighborCheck(miniplain,(7,8,10,18,27,32,71)) and not physics.neighborCheck(miniplain,(46,47,48)):
                                grid[a][bb] = [e,3]
                            else:
                                grid[a][bb] = [e,t]
                    #Stem
                    elif t == 3:
                        if random.randint(1,6) == 1 or a - 1 == 0:
                            t = 1
                            grid[a][bb] = [e,t]
                            continue
                        grid[a-1][bb] = [e,t]
                        grid[a][bb] = [31,0]
                        if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                            if random.randint(1,3) == 1:
                                grid[a][bb+1] = [e,2]
                            else:
                                grid[a][bb+1] = [49,0]
                        if bb - 1 != -1 and grid[a][bb-1][0] == 0:
                            if random.randint(1,3) == 1:
                                grid[a][bb-1] = [e,2]
                            else:
                                grid[a][bb-1] = [49,0]
                    #Branch
                    
                    elif t == 2:
                        if random.randint(1,4) == 1 or bb - 1 == 0 or bb + 1 == len(plain[0])-1:
                            t = 1
                            grid[a][bb] = [e,t]
                            continue
                        if grid[a][bb+1][0] != 31:
                            grid[a][bb+1] = [e,t]
                        else:
                            grid[a][bb-1] = [e,t]
                        grid[a][bb] = [31,0]
                            
                        if a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                            grid[a+1][bb] = [49,0]
                        if a - 1 != -1 and grid[a-1][bb][0] == 0:
                            grid[a-1][bb] = [49,0]
                    
                    #Finished
                    elif t == 1:
                        grid[a][bb] = [31,random.randint(0,11)]
                        if a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                            grid[a+1][bb] = [49,0]
                        if a - 1 != -1 and grid[a-1][bb][0] == 0:
                            grid[a-1][bb] = [49,0]
                        if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                            grid[a][bb+1] = [49,0]
                        if bb - 1 != -1 and grid[a][bb-1][0] == 0:
                            grid[a][bb-1] = [49,0]
                
                #Broken Brick
                
                elif e == 63:
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,t]
                    else:
                        grid[a][bb] = [e,t]
                
                #Acid Clouds
                
                elif e == 64:
                    if random.randint(1,800) == 1:
                        e = 65
                        t = 20
                    elif coinflip() and t <= 0:
                        e = 0
                    elif physics.neighborCheck(miniplain,[71]):
                        e = 16
                    
                    if not jam:
                        if a + 1 != len(plain) and not grid[a+1][bb][0] in acidImmune:
                            t -= 1
                            grid[a+1][bb] = [66,0]
                        if a - 1 != -1 and not grid[a-1][bb][0] in acidImmune:
                            t -= 1
                            grid[a-1][bb] = [66,0]
                        if bb + 1 != len(plain[0]) and not grid[a][bb+1][0] in acidImmune:
                            t -= 1
                            grid[a][bb+1] = [66,0]
                        if bb - 1 != -1 and not grid[a][bb-1][0] in acidImmune:
                            t -= 1
                            grid[a][bb-1] = [66,0]
                    
                    if random.randint(1,20) == 1:
                        if random.randint(1,4) != 1:
                            d = physics.lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]
                                
                                if d[1]:
                                    grid[a][bb+1] = [e,t]
                                else:
                                    grid[a][bb-1] = [e,t]
                        else:
                            d = physics.udWanderCheck(minigrid,localPos)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    grid[a-1][bb] = [e,t]
                    
                
                #Acid (Acid rain ig lol)

                elif e == 65:
                    if physics.neighborCheck(miniplain,(21,53)):
                        e = 3
                    elif coinflip() and t <= 0:
                        e = 0
                    elif random.randint(1,13) == 1 and physics.neighborCheck(miniplain,waters):
                        e = 75
                    elif physics.neighborCheck(miniplain,[71]):
                        e = 66
                    
                    if not jam:
                        if a + 1 != len(plain) and not grid[a+1][bb][0] in acidImmune:
                            t -= 1
                            grid[a+1][bb] = [66,0]
                        if a - 1 != -1 and not grid[a-1][bb][0] in acidImmune:
                            t -= 1
                            grid[a-1][bb] = [66,0]
                        if bb + 1 != len(plain[0]) and not grid[a][bb+1][0] in acidImmune:
                            t -= 1
                            grid[a][bb+1] = [66,0]
                        if bb - 1 != -1 and not grid[a][bb-1][0] in acidImmune:
                            t -= 1
                            grid[a][bb-1] = [66,0]
                    
                    c = physics.sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [0,0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]
                        grid[a+1][bb+(c[0]-2)] = [e,t]

                #Acid Sludge
                
                elif e == 66:
                    if (not moon) and random.randint(1,13) == 1:
                        if random.randint(1,10) == 1:
                            e = 84   
                        else:
                            e = 0
                        t = 0
                    elif physics.neighborCheck(miniplain,[71]):
                        e = 74
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t]
                    else:
                        grid[a][bb] = [c[1],t]
                        if c[0] == 2:
                            grid[a+1][bb] = [e,t]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,t]

                #Explosion
                
                elif e == 67:
                    t -= 1
                    if t <= 0:
                        e = 30
                        t = 4
                    else:
                        if a + 1 != len(plain) and not grid[a+1][bb][0] in blastProof:
                            grid[a+1][bb] = [e,t]
                        if a - 1 != -1 and not grid[a-1][bb][0] in blastProof:
                            grid[a-1][bb] = [e,t]
                        if bb + 1 != len(plain[0]) and not grid[a][bb+1][0] in blastProof:
                            grid[a][bb+1] = [e,t]
                        if bb - 1 != -1 and not grid[a][bb-1][0] in blastProof:
                            grid[a][bb-1] = [e,t]
                    grid[a][bb] = [e,t]

                #TNT
                
                elif e == 68:
                    if physics.neighborCheck(miniplain,[71]):
                        e = 31
                    elif physics.neighborCheck(miniplain,(9,30,67)):
                            e = 67
                            t = 8
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        grid[a][bb] = [e,t]
                
                
                #C4
                
                elif e == 69: #Not a word
                    if physics.neighborCheck(miniplain,[71]):
                        e = 31
                    elif physics.neighborCheck(miniplain,(9,67)):
                            e = 67
                            t = 4
                    
                    if t == 1 or jam:
                        t = 2
                    elif (physics.neighborCheck(miniplain,[43]) or physics.neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    if t == 2 and not jam:
                        e = 67
                        t = 10
                    grid[a][bb] = [e,t] 
                
                #Nuke (Mandatory when there are explosions in the game)
                
                elif e == 70:
                    if jam:
                        t = -1
                    if t == 0 and physics.neighborCheck(miniplain,(43,67)):
                            e = 67
                            t = random.randint(40,60)
                    if physics.neighborCheck(miniplain,[71]):
                        e = 31
                    
                    c = physics.stoneCheck(minigrid,localPos)
                    if not c[0]:
                        grid[a][bb] = [c[1],0]
                        grid[a+1][bb] = [e,0]
                    else:
                        grid[a][bb] = [e,t]
                
                #Holy Water
                
                elif e == 71:
                    if physics.neighborCheck(miniplain,[55]):
                        if coinflip():
                            e = 53
                        else:
                            e = 13
                    elif random.randint(1,9) == 1:
                        if physics.neighborCheck(miniplain,[31]):
                            e = 49
                    if coinflip():
                        if  bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 71:
                            t = grid[a][bb+1][1]
                        if bb - 1 != -1 and grid[a][bb-1][0] == 71:
                            t = grid[a][bb-1][1]
                    else:
                        if t == 0 and random.randint(1,555) == 1:
                            if coinflip():
                                t = 1
                            else:
                                t = 2
                        elif t != 0 and coinflip():
                            t = 0
                    
                    
                    c = physics.sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos,False,True)
                        if not d[0]:
                            d = physics.udWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                if e == 15:
                                    grid[a][bb] = [e,t]
                                else:
                                    grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    grid[a-1][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Dead Plants
                
                elif e == 72:
                    if coinflip():
                        if physics.neighborCheck(miniplain,(9,30,55,67)):
                            if coinflip():
                                e = 30
                                t = 5
                            else:
                                e = 32
                    elif random.randint(1,500) == 1:
                        if physics.neighborCount(miniplain,goodFossilizers) > 3:
                            t += random.randint(1,2)
                    elif physics.neighborCheck(miniplain,[71]):
                        e = 8
                        t = 0
                    if t >= 100:
                        e = 73
                        t = 0
                    elif jam:
                        t = 0
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t] 
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = physics.lrWanderCheck(minigrid,localPos, True)
                            if not d[0]:
                                grid[a+1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a+1][bb+1] = [e,t]
                                else:
                                    grid[a+1][bb-1] = [e,t]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Coal (Oh boy time to ruin the environment)
                
                elif e == 73:
                    if random.randint(1,120) == 1:
                        if physics.neighborCheck(miniplain,(9,30,55,67)):
                            e = 30
                            t = 5
                    elif physics.neighborCheck(miniplain,[71]):
                        e = 8
                        t = 0
                    if coinflip():
                        c = physics.stoneCheck(minigrid,localPos)
                        if not c[0]:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,t]
                    else:
                        c = physics.sandCheck(minigrid,localPos)
                        if c[0] == 0:
                            if e == 1:
                                continue
                            else:
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Natural Gas (If it's so natural then why is it hecking with the environment?)
                
                elif e == 74:
                    if random.randint(1,10) == 1:
                        if physics.neighborCheck(miniplain,(9,30,55,67)):
                            e = 30
                            t = 5
                    elif physics.neighborCheck(miniplain,[71]):
                        e = 16
                        t = 0
                    c = physics.sandCheck(minigrid,localPos,False,True,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos,False,False,True)
                        if not d[0]:
                            if e == 13:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [e,0]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]
                    else:
                        grid[a][bb] = [c[1],t]
                        if c[0] == 2:
                            d = physics.lrWanderCheck(minigrid,localPos,True,False,True)
                            if not d[0]:
                                grid[a-1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a-1][bb+1] = [e,t]
                                else:
                                    grid[a-1][bb-1] = [e,t]
                        else:
                            grid[a-1][bb+(c[0]-2)] = [e,t]
                
                #Polluted Water
                
                elif e == 75:
                    if sun and random.randint(1,30000) == 1:
                        e = 65
                        t = 10
                    c = physics.sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos,False,True)
                        if not d[0]:
                            d = physics.udWanderCheck(minigrid,localPos,True)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [d[2],0]

                                if d[1]:
                                    grid[a+1][bb] = [e,t]
                                else:
                                    grid[a-1][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Greenhouse sun
                
                elif e == 76:
                    if moon:
                        t = 0
                    else:
                        t = 1
                    if jam and random.randint(1,1000) == 1:
                        e = 20
                    grid[a][bb] = [e,t]
                
                #Wax

                elif e == 77:
                    l = [False,False]
                    if physics.neighborCheck(miniplain,(9,30,55,67)):
                        l[0] = True
                        if t < 15:
                            t += 1
                    else:
                        if t > 0 and random.randint(1,5) == 1:
                            t -= 1
                        if physics.neighborCount(miniplain, (0,13,16,64)) > 6:
                            l[1] = True
                    c = physics.sandCheck(minigrid,localPos,True)
                    if l[0] or (t > 0 and (t > 10 or random.randint(1,101-t*10)) == 1):
                        if c[0] == 0:
                            d = physics.lrWanderCheck(minigrid,localPos)
                            if not d[0]:
                                if e == 3:
                                    continue
                                else:
                                    grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [0,0]

                                if d[1]:
                                    grid[a][bb+1] = [e,t]
                                else:
                                    grid[a][bb-1] = [e,t]

                        else:
                            grid[a][bb] = [0,0]

                            grid[a+1][bb+(c[0]-2)] = [e,t]
                    elif l[1] or random.randint(1,123) == 1:
                        if coinflip():
                            c = physics.sandCheck(minigrid,localPos)
                            if c[0] == 0:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [c[1],0]
                                grid[a+1][bb+(c[0]-2)] = [e,t]
                        else:
                            c = physics.stoneCheck(minigrid,localPos)
                            if not c[0]:
                                grid[a][bb] = [c[1],0]
                                grid[a+1][bb] = [e,t]
                            else:
                                grid[a][bb] = [e,t]
                
                #Honeycomb

                elif e == 78:
                    l = False
                    if physics.neighborCount(miniplain, (0,13,16,64)) > 6:
                        l = True
                    elif physics.neighborCheck(miniplain,(61,67)):
                        if coinflip():
                            e = 77
                            t = 10
                        else:
                            e = 79
                    o = physics.lrCheck(miniplain[localPos[0]],localPos[1])
                    if l and not o:
                        c = physics.stoneCheck(minigrid,localPos)
                        if not c[0]:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,t]
                
                #Honey
                
                elif e == 79:
                    if sun and random.randint(1,25000) == 1:
                        e = 13
                        t = 8
                    elif physics.neighborCheck(miniplain,(9,55)) or (coinflip() and physics.neighborCheck(miniplain,(30,67))):
                        if coinflip():
                            e = 4
                        else:
                            e = 13
                    elif random.randint(1,2500) == 1:
                        if physics.neighborCheck(miniplain,[18]):
                            e = 18
                        elif physics.neighborCheck(miniplain,[24]):
                            e = 4
                    if random.randint(1,333) == 1 or not physics.neighborCheck(miniplain,[78]):
                        c = physics.sandCheck(minigrid,localPos)
                        if c[0] == 0:
                            if random.randint(1,25) != 1:
                                grid[a][bb] = [e,t]
                                continue
                            d = physics.lrWanderCheck(minigrid,localPos)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                                continue
                            else:
                                grid[a][bb] = [c[1],0]
                                if d[1]:
                                    grid[a][bb+1] = [e,t]
                                else:
                                    grid[a][bb-1] = [e,t]

                        else:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Bees!
                
                elif e == 80:
                    if physics.neighborCheck(miniplain,(9,20,30,35,53,57,60,61,66)) or (random.randint(1,20000) == 1 and not physics.neighborCheck(miniplain,(0,77,78,79))):
                        e = 81
                    if physics.neighborCount(miniplain,(3,10,13,16,21,22,27,29,32,34,37,39,43,45,46,47,48,51,52,54,56,73,74,75,78)) > random.randint(2,4):
                        t = 1
                    if t <= 0:
                        
                        if random.randint(1,5) == 1:
                            if random.randint(1,4) != 1:
                                d = physics.lrWanderCheck(minigrid,localPos, True)
                                if not d[0]:
                                    grid[a][bb] = [e,t]
                                else:
                                    grid[a][bb] = [d[2],0]
                                    
                                    if d[1]:
                                        grid[a][bb+1] = [e,t]
                                    else:
                                        grid[a][bb-1] = [e,t]
                            else:
                                d = physics.udWanderCheck(minigrid,localPos)
                                if not d[0]:
                                    grid[a][bb] = [e,t]
                                else:
                                    grid[a][bb] = [d[2],0]

                                    if d[1]:
                                        grid[a+1][bb] = [e,t]
                                    else:
                                        grid[a-1][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,t]
                    else:
                        if physics.neighborCheck(miniplain,(77,78,79)):
                            if random.randint(1,100):
                                t = 0
                            elif random.randint(1,1000):
                                r = random.randint(1,4)
                                if r == 1 and a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                                    grid[a+1][bb] = [random.randint(78,80),0]
                                if r == 2 and a - 1 != -1 and grid[a-1][bb][0] == 0:
                                    grid[a-1][bb] = [random.randint(78,80),0]
                                if r == 3 and bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                                    grid[a][bb+1] = [random.randint(78,80),0]
                                if r == 4 and bb - 1 != -1 and grid[a][bb-1][0] == 0:
                                    grid[a][bb-1] = [random.randint(78,80),0]
                        else:
                            if random.randint(1,50) == 1:
                                t += 1
                            if t == 25 or random.randint(1,500-20*t) == 1:
                                t = 0
                            c = physics.sandCheck(minigrid,localPos)
                            if c[0] == 0:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [c[1],0]
                                grid[a+1][bb+(c[0]-2)] = [e,t]
                
                #Blood!

                elif e == 81:
                    
                    if t == 1 or jam:
                        t = 2
                    elif (physics.neighborCheck(miniplain,[43]) or physics.neighborTempCheck(miniplain,conductors,"==",1)[0]) and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    
                    if coinflip():
                        if (physics.neighborCheck(miniplain,(30,67))):
                            e = 13
                            t = 10
                        elif physics.neighborCount(miniplain,(22,23,27)) > 3:
                            e = 27
                    if physics.neighborCheck(miniplain,(9,55)):
                        e = 13
                        t = 15
                    elif physics.neighborCount(miniplain,[71]) > 3:
                            if coinflip():
                                e = 79
                            else:
                                e = 3
                            t = 0
                    elif random.randint(1,2000) == 1:
                        if physics.neighborCheck(miniplain,[18]):
                            e = 18
                    elif (random.randint(1,20) == 1 and t != 0) or (sun and (random.randint(1,10101) == 1 and physics.neighborCheck(miniplain,waters))):
                        e = 75
                    
                    
                    
                    c = physics.sandCheck(minigrid,localPos,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos)
                        if not d[0]:
                            if e == 3:
                                continue
                            else:
                                grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [0,0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]

                    else:
                        grid[a][bb] = [0,0]

                        grid[a+1][bb+(c[0]-2)] = [e,t]

                #Red Sand

                elif e == 82:
                    if physics.neighborCheck(miniplain,(9,30,55,67)):
                        e = 14
                        t = 2
                    elif physics.neighborCheck(miniplain,[71]):
                        e = 1
                    if coinflip():
                        c = physics.sandCheck(minigrid,localPos)
                        if c[0] == 0:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb+(c[0]-2)] = [e,t]
                    else:
                        c = physics.stoneCheck(minigrid,localPos)
                        if not c[0]:
                            grid[a][bb] = [c[1],0]
                            grid[a+1][bb] = [e,t]
                        else:
                            grid[a][bb] = [e,t]

                #Good Smoke

                elif e == 83:
                    if (random.randint(1,10) == 1 and not (moon or sun)) or (random.randint(1,6) == 1 and moon and not sun) or (random.randint(1,12) == 1 and sun and not supersun) or (random.randint(1,20) == 1 and supersun):
                        t -= 1
                    if t <= 0 or physics.neighborCheck(miniplain,[71]):
                        e = 0
                    else:
                        o = physics.neighborTempCheck(miniplain,[83], ">", 5)
                        oo = physics.neighborTempCheck(miniplain,[83], ">", 10)
                        if (not (moon or oo[0])) and ((not sun and random.randint(1,70000) == 1) or (sun and random.randint(1,7000) == 1)) and physics.neighborCount(miniplain,[56]) >= 8 and o[0]:
                            e = 16
                    c = physics.sandCheck(minigrid,localPos,False,True,True)
                    if c[0] == 0:
                        d = physics.lrWanderCheck(minigrid,localPos,False,False,True)
                        if not d[0]:
                            grid[a][bb] = [e,t]
                        else:
                            grid[a][bb] = [d[2],0]

                            if d[1]:
                                grid[a][bb+1] = [e,t]
                            else:
                                grid[a][bb-1] = [e,t]
                    else:
                        grid[a][bb] = [c[1],0]
                        if c[0] == 2:
                            d = physics.lrWanderCheck(minigrid,localPos,True,False,True)
                            if not d[0]:
                                grid[a-1][bb] = [e,t]
                            else:
                                if d[1]:
                                    grid[a-1][bb+1] = [e,t]
                                else:
                                    grid[a-1][bb-1] = [e,t]
                        else:
                            grid[a-1][bb+(c[0]-2)] = [e,t]
                
                #Acid Waste
                
                elif e == 84:
                    if (sun or moon) and random.randint(1,1337) == 1:
                        e = 0
                        t = 0
                    elif physics.neighborCheck(miniplain,[71]):
                        e = 74
                    c = physics.sandCheck(minigrid,localPos)
                    if c[0] == 0:
                        grid[a][bb] = [e,t]
                    else:
                        grid[a][bb] = [c[1],t]
                        if c[0] == 2:
                            grid[a+1][bb] = [e,t]
                        else:
                            grid[a+1][bb+(c[0]-2)] = [e,t]

                #Thick water

                elif e == 85:
                    if coinflip():
                        if (physics.neighborCheck(miniplain,(30,67)) or (sun and random.randint(1,20000) == 1)):
                            e = 13
                            t = 10
                        elif physics.neighborCount(miniplain,(22,23,27)) > 3:
                            e = 27
                        elif physics.neighborCount(miniplain,[71]) > 3:
                            e = 71
                            t = 0
                    if physics.neighborCheck(miniplain,(9,55)):
                        e = 13
                        t = 15
                    elif random.randint(1,10000) == 1:
                        if physics.neighborCheck(miniplain,[18]):
                            e = 18
                    
                    if physics.neighborCount(miniplain, (0,85)) > 7:
                        c = physics.sandCheck(minigrid,localPos,True)
                        if c[0] == 0:
                            d = physics.lrWanderCheck(minigrid,localPos)
                            if not d[0]:
                                grid[a][bb] = [e,t]
                            else:
                                grid[a][bb] = [0,0]

                                if d[1]:
                                    grid[a][bb+1] = [e,t]
                                else:
                                    grid[a][bb-1] = [e,t]

                        else:
                            grid[a][bb] = [0,0]

                            grid[a+1][bb+(c[0]-2)] = [e,t]
                    else:
                        grid[a][bb] = [e,t]


                #Filler! (It's most of TV)
                
                elif e == 86:
                    if a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                        grid[a+1][bb] = [e,t]
                    if a - 1 != -1 and grid[a-1][bb][0] == 0:
                        grid[a-1][bb] = [e,t]
                    if bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                        grid[a][bb+1] = [e,t]
                    if bb - 1 != -1 and grid[a][bb-1][0] == 0:
                        grid[a][bb-1] = [e,t]
                    grid[a][bb] = [e,t]
                
                #Snake
                
                elif e == 87:
                    if random.randint(1,15) == 1 and t != 0:
                        tm = random.randint(1,4)
                        if (t == 1 and tm != 2) and (t == 2 and tm != 2) and (t == 3 and tm != 4) and (t == 4 and tm != 3):
                            t = random.randint(1,4)
                    if t == 1 and a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                        grid[a+1][bb] = [e,t]
                    if t == 2 and a - 1 != -1 and grid[a-1][bb][0] == 0:
                        grid[a-1][bb] = [e,t]
                    if t == 3 and bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                        grid[a][bb+1] = [e,t]
                    if t == 4 and bb - 1 != -1 and grid[a][bb-1][0] == 0:
                        grid[a][bb-1] = [e,t]
                    grid[a][bb] = [e,0]

                #Tesla Coil
                
                elif e == 88:
                    
                    if t == 1 or jam:
                        t = 2
                    elif physics.neighborTempCheck(miniplain,conductors,"==",1)[0] and t == 0:
                        t = 1
                    elif t == 2:
                        t = 0
                    
                    if t == 1:
                        if a + 1 != len(plain) and grid[a+1][bb][0] == 0:
                            #Electricity loves going down ngl
                            grid[a+1][bb] = [43,0]
                        else:
                            cd = 0
                            if (bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0) and (bb - 1 != -1 and grid[a][bb-1][0] == 0):
                                cd = random.randint(1,2)
                            elif bb + 1 != len(plain[0]) and grid[a][bb+1][0] == 0:
                                cd = 1
                            elif bb - 1 != -1 and grid[a][bb-1][0] == 0:
                                cd = 2
                            if cd == 1:
                                grid[a][bb+1] = [43,0]
                            elif cd == 2:
                                grid[a][bb-1] = [43,0]

                    grid[a][bb] = [e,t] 

                #Battery
                
                elif e == 89:
                    
                    t -= 1
                    if t <= 0 or jam:
                        t = 10
                    
                    if coinflip() and physics.neighborCheck(miniplain,(64,65)):
                        e = 65
                        t = 10-t

                    grid[a][bb] = [e,t] 





            except IndexError:
                print("Error in doing element", grid[a][bb], "index out of range (Did you remember to put the element ID in the corisponding mini-allowed tuple?)")
    return grid

def gimmeAllElms(plain: list[list[list[int]]]) -> list[int]:
    elements = []
    for a in plain:
        for b in a:
            if not b[0] in elements:
                elements.append(b[0])
    return elements

print("I'm doing it!")