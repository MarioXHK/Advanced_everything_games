from PIL import Image

def loadImage(file:str,res:int = 10) -> tuple[int,int,list]:
    im = Image.open(file) # Can be many different formats.
    pix = im.load()
    lx = im.size[0]//res
    ly = im.size[1]//res
    sx = lx*res
    sy = ly*res
    imageLand = [[[5,0] for _ in range(lx)] for i in range(ly)]
    for y in range(len(imageLand)):
        for x in range(len(imageLand[0])):
            #print([x*res,y*res])
            color = pix[x*res,y*res]
            if color[0]+color[1]+color[2] == 0:
                imageLand[y][x] = [0,0]
            else:
                cr = color[0]*1000000
                cg = color[1]*1000
                cb = color[2]
                imageLand[y][x][1] = cr+cg+cb
    return (sx,sy,imageLand)

print("Bad apples are being thrown around!")

pen = loadImage("nyan cat.png")