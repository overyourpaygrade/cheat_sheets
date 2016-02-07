#!/usr/bin/env python
import PIL.Image

with open('secret.png', 'rb') as fp:

    img = PIL.Image.open(fp)

    width,height = img.size

    #print("width: {} -- height: {}".format(width,height))

    newIm = PIL.Image.new("RGB", (width,height))

    for row in range(height):

        for col in range(width):

            fgr, fgg, fgb = img.getpixel((col,row))

            if fgr % 2 == 0:
                newIm.putpixel((col,row),(255,255,255))
            else:
                newIm.putpixel((col,row),(0,0,0))

    newIm.save('out.png')

