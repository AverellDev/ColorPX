#Created by AverellDev - https://github.com/AverellDev

#Useful color handling functions

import random

def strhexToRgb(strhex):
    """strhex (str): hex value to be converted
    Returned values: r (int), b (int) and g (int) values""" 
    return int(strhex[1]+strhex[2], 16), int(strhex[3]+strhex[4], 16), int(strhex[5]+strhex[6], 16)
    
def rgbToStrhex(r, g, b):
    """r (int), g (int), b (int): rgb values to be converted
    Returned value (str): hex value of the color (ex: #7f866a""" 
    return '#%02x%02x%02x' % (r, g, b)
    
def rgbAverage(col1, col2):
    """col1 (str): hex value of color 1
    col2 (str): hex value of color 2
    Returned value (str): hex value of average color"""
    r1, g1, b1 = strhexToRgb(col1)
    r2, g2, b2 = strhexToRgb(col2)
    if(random.random()>=0.5):
        r = int((r1+r2)/2+0.5)
        g = int((g1+g2)/2+0.5)
        b = int((b1+b2)/2+0.5)
    else:
        r = int((r1+r2)/2)
        g = int((g1+g2)/2)
        b = int((b1+b2)/2)
    return rgbToStrhex(r,g,b)
    
def closeColorGen(baseCol, maxDiff):
    """baseCol (str): hex value of base color
    maxDiff (int): Maximum rgb difference between a color and its randomly modified instance (ex : if maxDiff = 10: 140, 180, 120 --> 130~150, 170~190, 110~130)
    Returned value (str): hex value of generated color
    """
    baseR, baseG, baseB = strhexToRgb(baseCol)
    r = baseR+random.randint(0-maxDiff, maxDiff)
    g = baseG+random.randint(0-maxDiff, maxDiff)
    b = baseB+random.randint(0-maxDiff, maxDiff)
    if(r>255):
        r = 255
    elif(r<0):
        r = 0
    if(g>255):
        g = 255
    elif(g<0):
        g = 0
    if(b>255):
        b = 255
    elif(b<0):
        b = 0
    return rgbToStrhex(r,g,b)

def randomColorGen(cPal):
    """cPal (str): desired color palette 
    Returned value (str): hex value of random color
    """
    if(cPal=="rgb"):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
    elif(cPal=="bw"):
        col = random.randint(0, 255)
        r = col
        g = col
        b = col
    else:
        r = 0
        g = 0
        b = 0
    return rgbToStrhex(r,g,b)
