# -*- coding: utf-8 -*-
"""
Created on Tue May 26 09:31:50 2015

@author: isman7
"""

import os
import fnmatch
from pylab import *
from scipy.misc import imresize
from pytg import Telegram


def readConfig():
    
    config = {}
    
    
    return config

def writeConfig():
    
    
    config = {}
    
    return config



def resizefolder(folderPath):
    
    try: 
        for root, dirnames, filenames in os.walk(folderPath):
            for filename in fnmatch.filter(filenames, '*.png'):
                matches.append(os.path.join(root, filename))
            
    except IOError:     
        print "Folder not found. Using test directory: " + os.curdir 
        for root, dirnames, filenames in os.walk(os.curdir + '/test/images'):
            for filename in fnmatch.filter(filenames, '*.png'):
                matches.append(os.path.join(root, filename))
                
    
    for stickers in matches: 
    
        sticker = imread(stickers)
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
            imsave(stickers, new_sticker)
            
def telegram_init():

    #### Telegram object declaration ####
    
    
    
    tg = Telegram(telegram="../tg/bin/telegram-cli", pubkey_file="../tg/tg-server.pub")
    
    return tg

    