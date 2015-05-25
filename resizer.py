# -*- coding: utf-8 -*-
"""
Created on Sun May 24 01:00:37 2015

@author: isman7
"""

import os
import fnmatch
from pylab import *
from scipy.misc import imresize

#### Folder scanning ####

matches = []

dirname = str(raw_input("Input the image to resize folder path: "))

try: 

    for root, dirnames, filenames in os.walk(dirname):
        for filename in fnmatch.filter(filenames, '*.png'):
            matches.append(os.path.join(root, filename))
            
except IOError: 

    print "Folder not found. Using current directory: " + os.curdir 
    for root, dirnames, filenames in os.walk(os.curdir):
        for filename in fnmatch.filter(filenames, '*.png'):
            matches.append(os.path.join(root, filename))
            
for stickers in matches: 
    
    sticker = imread(stickers)
    
    #print sticker.shape
    
    stshape = sticker.shape
    
    if stshape[0] > stshape[1]:
        
        new_width = int(512*stshape[1]/stshape[0])       
        
        new_stshape = ( 512, new_width, stshape[2])        
                
        new_sticker = imresize(sticker, new_stshape)
        
        imsave(stickers, new_sticker )
        
    elif stshape[0] < stshape[1]:
        
        new_height = int(512*stshape[0]/stshape[1])       
        
        new_stshape = ( new_height, 512, stshape[2])        
                
        new_sticker = imresize(sticker, new_stshape)
        
        imsave(stickers, new_sticker )
    
    elif stshape[0] == stshape[1]:
        
        
        
        new_stshape = (512, 512, stshape[2])        
                
        new_sticker = imresize(sticker, new_stshape)
        
        imsave(stickers, new_sticker )
    
        
            
    
