import os
from PIL import Image #pip install pillow

mypath =  os.getcwd()
im = Image.open(mypath + '/menu.png')

pix = im.load()
w, h = im.size
gfxbitty = ""

for y in range(0,h):
    for x in range(0, w):
        r,g,b,a = pix[x,y]					

        if(r == 255):
            gfxbitty = gfxbitty + "1"
        else:			
            gfxbitty = gfxbitty + "0"
        
        gfxbitty = gfxbitty + "\n"

text_file = open("menu.txt", "w")
text_file.write(gfxbitty)
text_file.close()



