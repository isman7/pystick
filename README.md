# pystick
PyStick wants to be a Bot for upload bulks of images to the Telegram Sticker Bot. Now a couple of scripts. 

## Dependencies 

PyStick is developed in python2.7 (I'm wondering passing to python3) and based on [PyTg](https://github.com/luckydonald/pytg); a Python package that communicates with the [Telegram messenger CLI](https://github.com/vysheng/tg).

So, you have to install both in order to use **PyStick**.

## Use

I have made two script to easy deal with some image packages to made them Telegram Stickers. 

- *resizer.py*: asks for a folder. It resizes all .png to fit the 512x512 box.
- *pystick.py*: asks for a folder, with 512x512 fited .png images. Uploads them througth Telegram Cli.

## Future implementations

- Better app structure, not script.
- Better *emoji* implementation. **Now, are images are packaged into the same emoji. **
- Python3?
