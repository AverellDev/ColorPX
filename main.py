#Created by AverellDev - https://github.com/AverellDev

from colorpx import *

#User dialog example of ColorPxGenerator class

if __name__ == "__main__":
    genModes = ["smooth-diagonal", "random"]
    
    fileName = str(input("File name (without extension): "))
    fileExt = str(input("File type (jpg, jpeg or png) : "))
    genMode = str(input("Gen mode (random or smooth-diagonal) : "))
    if genMode in genModes:
        imgX = int(input("Image width : "))
        imgY = int(input("Image height : "))
        sqC = int(input("Side of the squares (in px) : "))
        times = int(input("Number of generations : "))
        if imgX > 0 and imgY > 0 and sqC > 0 and times > 0:
            generator = ColorPxGenerator(imgX, imgY, sqC)
            
            if genMode == "random":
                colorPal = str(input("Color palette (rgb or bw) : "))
                print("")
                if times == 1:
                    generator.random_gen(colorPal)
                    generator.save(fileName+"."+fileExt)
                else:
                    for i in range(1, times+1):
                        generator.random_gen(colorPal)
                        if(generator.save(fileName+str(i)+"."+fileExt)==1):
                            break
                        generator.reset()
                        
            elif genMode == "smooth-diagonal":
                colDiff = int(input("Max r, g and b difference between two squares in contact : "))
                sd = str(input("Hex color seed (ex : #f285a6), \"None\" for random : "))
                print("")
                if(sd == "None" or sd == "none" or sd == "" or (len(sd)==7 and sd[0]=='#')):
                    if(sd == "None" or sd == "none" or sd == ""):
                        seed=None
                    else:
                        seed=sd
                    
                    if times == 1:
                        generator.smooth_diagonal_gen(colDiff, seed)
                        generator.save(fileName+"."+fileExt)
                    else:
                        for i in range(1, times+1):
                            generator.smooth_diagonal_gen(colDiff, seed)
                            if(generator.save(fileName+str(i)+"."+fileExt)==1):
                                break
                            generator.reset()
                else:
                    print("\nERROR : Seed is invalid")
        else:
            print("\nERROR : These values can't be negative or null.")
    else:
          print("\nERROR : Gen mode is incorrect.")
