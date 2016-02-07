#!/usr/bin/env python
import PIL.Image
import random

mess = "This is a random string of text"

def bit_generator(mess):
    for ch in mess:
        ascii = ord(ch)
        ct = 0
        while ct < 7:
            yield ascii & 1
            ascii = ascii >> 1
            ct += 1
    for i in range(7):
        yield 0
    while True:
        yield random.randrange(1) 

def setbit(oldbyte,newbit):
    if newbit:
        return oldbyte | newbit
    else:
        return oldbyte & 0b11111110

with open('ascii_secret.png','rb') as fg:

    bitstream = bit_generator(mess)

    img = PIL.Image.open(fg)

    width,height = img.size

    newIm = PIL.Image.new("RGB", (width,height))

    for row in range(height):

        for col in range(width):

            fgr, fgg, fgb = img.getpixel((col,row))
            
            redbit = bitstream.next()
            fgr = setbit(fgr,redbit)

            greenbit = bitstream.next()
            fgg = setbit(fgg,greenbit)

            bluebit = bitstream.next()
            fgb = setbit(fgb,bluebit)

            newIm.putpixel((col,row),(fgr,fgg,fgb))

    newIm.save('new.png')
