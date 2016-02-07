#!/usr/bin/env python
import PIL.Image

def bit_gen(fg):

    img = PIL.Image.open(fg)
    width,height = img.size

    for row in range(height):

        for col in range(width):

            fgr, fgg, fgb = img.getpixel((col,row))

            yield fgr & 1            
            yield fgg & 1            
            yield fgb & 1            
    

with open('new.png', 'rb') as fg:

    mybits = bit_gen(fg)
    done = False
    mess = 0
    n = 0
    mess_str = ''

    while not done:
        bit = mybits.next()
        mess = mess + bit * 2**n
        n += 1

        if n == 7:
            if mess == 0:
                done = True
            else:
                mess_str += chr(mess)
                mess = 0
                n = 0

    print str(mess_str)

