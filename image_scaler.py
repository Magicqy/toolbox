#!/usr/bin/python
from PIL import Image
import os, sys, argparse

# best down-sizing filter ANTIALIAS
def Resize(image, path, w, h, mode = Image.ANTIALIAS):
	path = os.path.abspath(os.path.expanduser(path))
	dir = os.path.dirname(path)
	if not os.path.isdir(dir):
		os.makedirs(dir)
	newimage = image.resize((w, h), mode)
	newimage.save(path)
pass

def MakeAndroidIcon(iconFile):
	im = Image.open(iconFile)
	Resize(im, "res/drawable-ldpi/app_icon.png", 36, 36)
	Resize(im, "res/drawable/app_icon.png", 48, 48)
	Resize(im, "res/drawable-hdpi/app_icon.png", 72, 72)
	Resize(im, "res/drawable-xhdpi/app_icon.png", 96, 96)
	Resize(im, "res/drawable-xxhdpi/app_icon.png", 144, 144)
	Resize(im, "res/drawable-xxxhdpi/app_icon.png", 192, 192)
pass

def MakeiOSIcon(iconFile):
	im = Image.open(iconFile)
	Resize(im, "AppIcon.appiconset/Icon.png", 57, 57)
	Resize(im, "AppIcon.appiconset/Icon@2x.png", 114, 114)
	Resize(im, "AppIcon.appiconset/Icon-72.png", 72, 72)
	Resize(im, "AppIcon.appiconset/Icon-76.png", 76, 76)
	Resize(im, "AppIcon.appiconset/Icon-120.png", 120, 120)
	Resize(im, "AppIcon.appiconset/Icon-144.png", 144, 144)
	Resize(im, "AppIcon.appiconset/Icon-152.png", 152, 152)
	Resize(im, "AppIcon.appiconset/Icon-180.png", 180, 180)
pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'icon image scaler')
    parser.add_argument('iconFile', help = 'origin icon image file')
    parser.add_argument('-android', action = 'store_true', help = 'make android icon image set')
    parser.add_argument('-ios', action = 'store_true', help = 'make ios icon image set')
    args = parser.parse_args()
    if os.path.isfile(args.iconFile):
        iconFile = os.path.abspath(args.iconFile)
        if args.android:
            MakeAndroidIcon(iconFile)
        if args.ios:
            MakeiOSIcon(iconFile)
    else:
        print('origin icon image file not exist')
    pass
