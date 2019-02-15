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
    else:
        print("unknown pixel vals: " + str(rgb_in))
        rgb_out = (255, 255, 255, 255)
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
            outFile[h, w, :] = colorchanger((r, g, b, alpha), WasserK)
    misc.imsave(imFileOUT, outFile)
    return(outFile) # return png array for summing later


def main():
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
    
    
    RiskAdded = 0.5* WasserArr + 0.5* StrassenArr
    misc.imsave("/home/andre_eggli/Desktop/opendata_eniwa/Python/RisikoSumm.png", RiskAdded)
    
main()
        
        
         
        