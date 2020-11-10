#Created by AverellDev - https://github.com/AverellDev

#User dialog example : main.py

"""Class usage exemple :
    gen = ColorPxGenerator(1920, 1080, 10) 
    gen.smooth_diagonal_gen(2, "#afafaf")
    if(gen.save("colorpxtest.png")==1):
        print("An error has occured !")
    else:
        print("File generated successfully.")
"""
from PIL import Image, ImageDraw
import random

import rgbtools

class ColorPxGenerator:
    """Class for generating the image"""
    def __init__(self, imgX=640, imgY=480, sqC=5):
        """Class initialisation
        imgX (int): image width 
        imgY (int): image height
        sqC (int): square side in pixels"""
        self.imgX = imgX-imgX%sqC
        self.imgY = imgY-imgY%sqC
        self.sqC = sqC
        self.nbSquaresX = int(self.imgX/sqC)
        self.nbSquaresY = int(self.imgY/sqC)
        self.im = Image.new("RGB", (imgX, imgY))
        self.img = ImageDraw.Draw(self.im)
        self.img.rectangle(((0,0),(self.imgX, self.imgY)), fill="#000000", outline=None)
        
    def random_gen(self, cPal="rgb"):
        """Generate and draw an array of randomly colored squares
        cPal (str): desired color palette ("rgb" or "bw")
        """
        for y in range(0, self.nbSquaresY):
            for x in range(0, self.nbSquaresX):
                color = rgbtools.randomColorGen(cPal)
                self.img.rectangle(((self.sqC*x,self.sqC*y),(self.sqC*(x+1), self.sqC*(y+1))), fill=color, outline=None)
         
         
    def smooth_diagonal_gen(self, cDiff=10, seed=None):
        """Diagonally generating and drawing an array of smoothly colored squares (the color of a square whose position index is (x,y) will be the average color of the (x-1, y) square and (x, y-1) square.
        This average color will be more or less modified by a random addition or substraction of a number between 0 and cDiff to its red, green and blue value.
        cDiff (int): Maximum rgb difference between a color and its randomly modified instance (ex : if cDiff = 10: 140, 180, 120 --> 130~150, 170~190, 110~130)
        seed (str): hex value of the top left ((0,0) coordinates) square color. (ex : "#8ab57d"). If no seed is given or seed=None, this color will be random.
        """
        previousLineColorList = []
        for y in range(0, self.nbSquaresY):
            for x in range(0, self.nbSquaresX):
                if(x==0 and y==0):
                    if(seed==None):
                        color = rgbtools.randomColorGen("rgb")
                    else:
                        color = seed
                    self.img.rectangle(((self.sqC*x,self.sqC*y),(self.sqC*(x+1), self.sqC*(y+1))), fill=color, outline=None)
                    previousLineColorList.append(color)
                elif(x==0):
                    color = rgbtools.closeColorGen(previousLineColorList[x], cDiff)
                    self.img.rectangle(((self.sqC*x,self.sqC*y),(self.sqC*(x+1), self.sqC*(y+1))), fill=color, outline=None)
                    previousLineColorList[0] = color
                elif(y==0):
                    color = rgbtools.closeColorGen(color, cDiff)
                    self.img.rectangle(((self.sqC*x,self.sqC*y),(self.sqC*(x+1), self.sqC*(y+1))), fill=color, outline=None)
                    previousLineColorList.append(color)
                else:
                    avColor = rgbtools.rgbAverage(color, previousLineColorList[x])
                    color = rgbtools.closeColorGen(avColor, cDiff)
                    self.img.rectangle(((self.sqC*x,self.sqC*y),(self.sqC*(x+1), self.sqC*(y+1))), fill=color, outline=None)
                    previousLineColorList[x] = color            
    
    def save(self, fileName):
        """Save the image as a jpg or png file
        fileName (str): file name or relative path
        Returned value : 0 if the file has been saved successfully, 1 if an error has occured when saving"""
        ext = ["jpg", "jpeg", "png"]
        spl = fileName.split(".")
        if spl[len(spl)-1] in ext:
            try:
                self.im.save(fileName)
            except:
                print("An error has occured when saving "+fileName)
                return 1
            print(fileName+" has been generated successfully.")
            return 0
        else:
            print(spl[1]+" is not a valid extension")
            return 1
        
    def reset(self):
        """Reset the image"""
        del self.img
        del self.im
        self.im = Image.new("RGB", (self.imgX, self.imgY))
        self.img = ImageDraw.Draw(self.im)
        self.img.rectangle(((0,0),(self.imgX, self.imgY)), fill="#000000", outline=None)
        
