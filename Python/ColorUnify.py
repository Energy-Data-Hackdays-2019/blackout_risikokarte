#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 17:39:08 2019

@author: andre_eggli
"""

from scipy import misc
import glob

def colorchanger(rgb_in, filenameId):
    if rgb_in == (255, 255, 255, 255): # weiss
        rgb_out = (0, 0, 0, 255)
        
    # mapping für WasserKarte
    elif rgb_in == (253, 117, 117, 255):#rot
        rgb_out = (250, 0, 0, 255)
    elif rgb_in == (105, 154, 254, 255):#blau
        rgb_out = (175, 0, 0, 255)     
    elif rgb_in == (253, 250, 90, 255):#gelb
        rgb_out = (125, 0, 0, 255)
    elif rgb_in == (255, 255, 90, 255):#schraffiert
        rgb_out = (75, 0, 0, 255)
        
    # mapping für lärmKarte
    elif rgb_in == (110, 110, 110, 255): # rand
        rgb_out = (75, 0, 0, 255) 
    elif rgb_in == (255, 0, 0, 255): # rot
        rgb_out = (175, 0, 0, 255)  
    elif rgb_in == (255, 255, 0, 255): # gelb
        rgb_out = (75, 0, 0, 255) 
        
    # mapping für netz_wichtigkeit.png:
        
    elif rgb_in == (5, 5, 5, 255):
        rgb_out = (0, 250, 0, 255) 
    elif rgb_in == (66, 66, 66, 255):
        rgb_out = (0, 200, 0, 255) 
    elif rgb_in == (128, 128, 128, 255):
        rgb_out = (0, 150, 0, 255) 
    elif rgb_in == (189, 189, 189, 255):
        rgb_out = (0, 100, 0, 255) 
    elif rgb_in == (250, 250, 250, 255):
        rgb_out = (0, 50, 0, 255) 
    else:
        #print("unknown pixel vals: " + str(rgb_in))
        rgb_out = (0, 0, 0, 255)
    return(rgb_out)



def imagechanger(imFileIN, imFileOUT):
    image = image = misc.imread(imFileIN)
    outFile = misc.imread(imFileOUT)
    print(image.shape)
    print(image.dtype)
    (hight, width, _) = image.shape
    for h in range(hight):
        for w in range(width):
            (r, g, b, alpha) = image[h, w, :]
            outFile[h, w, :] = colorchanger((r, g, b, alpha), imFileOUT)
    misc.imsave(imFileOUT, outFile)
    return(outFile) # return png array for summing later

def grid2color(imFileIN, imFileOUT):
    image = image = misc.imread(imFileIN)
    outFile = misc.imread(imFileOUT)
    print(image.shape)
    print(image.dtype)
    (hight, width, _) = image.shape
    for h in range(hight):
        for w in range(width):
            (r, g, b, alpha) = image[h, w, :]
            outFile[h, w, :] = colorchanger((r, g, b, alpha), imFileOUT)
    misc.imsave(imFileOUT, outFile)
    return(outFile) # return png array for summing later

def multiply(gridArr, RiskAdded, imFileOUT):
    outFile = misc.imread(imFileOUT)
    (hight, width, _) = outFile.shape
    for h in range(hight):
        for w in range(width):
            outFile[h, w, :] = (0, 0, round(gridArr[h, w, 1] * RiskAdded[h, w, 0] / 255), 255)
            if outFile[h, w, 2] == 0: # set unocupied to transparent: alpha = 0
                outFile[h, w, 3] = 0
    misc.imsave(imFileOUT, outFile)
    return(outFile)
 
    
def findMaxBlueValue(multResArr):
    tempHighest = 0
    (hight, width, _) = multResArr.shape
    for h in range(hight):
        for w in range(width):
            if tempHighest < multResArr[h, w, 2]:
                tempHighest = multResArr[h, w, 2]
    return(tempHighest)

# Wasser:
WasserK = "/home/andre_eggli/Desktop/opendata_eniwa/Python/gefahrenkarte.png"
WasserK_out = "/home/andre_eggli/Desktop/opendata_eniwa/Python/gefahrenkarte out.png"
WasserArr = imagechanger(WasserK, WasserK_out)
print("Wasser fertig")

# Chemie: = Strassenläem
StrasseK = "/home/andre_eggli/Desktop/opendata_eniwa/Python/strassenlaerm.png"
StrasseK_out = "/home/andre_eggli/Desktop/opendata_eniwa/Python/strassenlaerm out.png"
StrassenArr = imagechanger(StrasseK, StrasseK_out)
print("LärmStrasse ferig")

# kombinierte Risikokarte
RiskAdded = 0.5* WasserArr + 0.5* StrassenArr
misc.imsave("/home/andre_eggli/Desktop/opendata_eniwa/Python/RisikoSumm.png", RiskAdded)

# verwandle Graustufen-Netz in grünes Bild
gridK = "/home/andre_eggli/Desktop/opendata_eniwa/Python/netz_wichtigkeit.png"
gridK_out = "/home/andre_eggli/Desktop/opendata_eniwa/Python/netz_wichtigkeit out.png"
gridArr = grid2color(gridK, gridK_out)

# multipliziere RisikoSumme * Impact
MultBild = "/home/andre_eggli/Desktop/opendata_eniwa/Python/RisikoMap.png"
multRes = multiply(gridArr, RiskAdded, MultBild)
    
    
    

        
        
         
        