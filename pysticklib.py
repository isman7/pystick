# -*- coding: utf-8 -*-
"""
Created on Tue May 26 09:31:50 2015

@author: isman7
"""

import os
import fnmatch
from pylab import *
from scipy.misc import imresize


defaultConfig = {'tg.target': 'Sticker_Bot', 
                 'tg.srvpub': '../tg/tg-server.pub',    
                 'tg.Path': '../tg/bin/telegram-cli', 
                 'tg.emoji': '24C2',
                 'stickers.path': './images'}

#### Sticker Bot Commands ####
# You should modify to point the correct Bot name, but it is supposed to be the same. 



newpack =  u'/newstickpack'
addsticker = u'/addsticker'
delsticker = u'/delsticker'
ordersticker= u'/ordersticker'
candel = u'/cancel'
publish = u'/publish'


def readConfig():
    
    config = {}
    
    try: 
        
        configFile = open('./config.txt')
        configStr = configFile.read()        
        configFile.close()
        
        optionLines = configStr.split('\n')
        for line in optionLines:
            option = line.split('=\t')        
            if len(option) == 2:             
                config[option[0]] = option[1]
            
    except IOError:
        print "Config file not found. Creating default one at: ./config.txt"    
        config = defaultConfig
        writeConfig(config)
        
    return config        

def writeConfig(config):
    
    try:
        
        configFile = open('./config.txt', 'w')        
        for option, value in config.iteritems():
            #print option+'=\t'+value            
            configFile.writelines(option+'=\t'+value+'\n')
        configFile.close()        
        return 1
    except IOError: 
        print "Config file not found"        
        return -1        
    
    
def resizeFolder(folderPath):
    
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
            


    