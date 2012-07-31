#!/usr/bin/env python2
from PIL import Image
import random

random.seed()

TILESIZE = 16

#images
filehandle = open("files", 'r')
images = []
for imgname in filehandle:
    images.append(Image.open(imgname.rstrip('\n')))
filehandle.close()
emptyimage = images.pop()
cornerimage = Image.open("corner-alpha.png")
cornerimage = cornerimage.convert("L")

#template for the image
filehandle = open("image", 'r')
imagetxt = filehandle.readlines();
filehandle.close()

#size
tilesy = len(imagetxt)
tilesx = len(imagetxt[0])-1

#new image
tiled = Image.new("RGBA",(TILESIZE*tilesx,TILESIZE*tilesy),(0,0,0,0))

for x in range(0,tilesx):
    for y in range(0,tilesy):
        if imagetxt[y][x] == ' ':
            tile = emptyimage
        else:
            tile = random.choice(images)
        tiled.paste(tile,(x*TILESIZE,y*TILESIZE,TILESIZE+x*TILESIZE,TILESIZE+y*TILESIZE))

tiled.paste((0,0,0,0),(0,0),cornerimage)
tiled.paste((0,0,0,0),(TILESIZE*tilesx-cornerimage.size[0],0),cornerimage.rotate(270))
tiled.paste((0,0,0,0),(TILESIZE*tilesx-cornerimage.size[0],TILESIZE*tilesy-cornerimage.size[1]),cornerimage.rotate(180))
tiled.paste((0,0,0,0),(0,TILESIZE*tilesy-cornerimage.size[1]),cornerimage.rotate(90))

tiled.save("output.png")
