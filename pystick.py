#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:37:29 2015

@author: isman7
"""


import os
import fnmatch
from pytg import Telegram
import pysticklib as ps

#### Loading config ####

config = ps.readConfig()

#### Treating images #### 

if 'stickers.path' in config: 
    ps.resizeFolder(config['stickers.path'])
    
#### Telegram object declaration ####

tg = Telegram(
    telegram=config['tg.Path'],
    pubkey_file=config['tg.srvpub'])
sender = tg.sender

#### Folder scanning ####

matches = []



try: 

    for root, dirnames, filenames in os.walk(config['stickers.path']):
        for filename in fnmatch.filter(filenames, '*.png'):
            matches.append(os.path.join(root, filename))
            
except IOError: 

    print "Folder not found. Using current directory: " + os.curdir 
    for root, dirnames, filenames in os.walk(os.curdir):
        for filename in fnmatch.filter(filenames, '*.png'):
            matches.append(os.path.join(root, filename))


#### Sticker pack creation ####

stickerbot = unicode(config['tg.target'])

packname = unicode(raw_input("Packname: "))
            
sender.send_msg(stickerbot, ps.newpack)

sender.send_msg(stickerbot, packname)

#TODO improve a lot emojis implementation 

emoji_number = 128059

#128512 grinning

#128048 #rabbit face!
    
#128059 bear face!

for stickers in matches: 
    
    sender.send_msg(stickerbot, unichr(emoji_number))
    sender.send_document(stickerbot, unicode(stickers))


sender.send_msg(stickerbot, ps.publish)

sender.send_msg(stickerbot, packname)    











