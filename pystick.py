#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:37:29 2015

@author: isman7
"""


import os
import fnmatch
from pytg import Telegram

#### Telegram object declaration ####
# You should modify to find the correct path. 
tg = Telegram(
    telegram="../tg/bin/telegram-cli",
    pubkey_file="../tg/tg-server.pub")


receiver = tg.receiver
sender = tg.sender

#### Sticker Bot Commands ####
# You should modify to point the correct Bot name, but it is supposed to be the same. 
stickerbot = u'Stickers_Bot'

newpack = u'/newstickerpack'
addsticker = u'/addsticker'
delsticker = u'/delsticker'
ordersticker= u'/ordersticker'
candel = u'/cancel'
publish = u'/publish'


#### Folder scanning ####

matches = []

dirname = str(raw_input("Introduce la dirección de la carpeta que contiene los stickers: "))

try: 

    for root, dirnames, filenames in os.walk(dirname):
        for filename in fnmatch.filter(filenames, '*.png'):
            matches.append(os.path.join(root, filename))
            
except IOError: 

    print "Folder not found. Using current directory: " + os.curdir 
    for root, dirnames, filenames in os.walk(os.curdir):
        for filename in fnmatch.filter(filenames, '*.png'):
            matches.append(os.path.join(root, filename))


#### Sticker pack creation ####

packname = unicode(raw_input("Packname: "))
            
sender.send_msg(stickerbot, newpack)

sender.send_msg(stickerbot, packname)

#TODO improve a lot emojis implementation 

emoji_number = 128059

#128512 grinning

#128048 #rabbit face!
    
#128059 bear face!

for stickers in matches: 
    
    sender.send_msg(stickerbot, unichr(emoji_number))
    sender.send_document(stickerbot, unicode(stickers))


sender.send_msg(stickerbot, publish)

sender.send_msg(stickerbot, packname)    











