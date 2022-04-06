from easygui import diropenbox
import PIL.Image as im
import PIL.ImageChops as ch
import os
import shutil as sh

def khiohpen(path):
    img = im.open(path)
    bg = im.new(img.mode, img.size, '#00000000')
    diff = ch.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        img.crop(bbox).save(path, quality=100)

d = diropenbox()
print(d)
listd = os.listdir(d)
for f in listd:
    if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.tif') or f.endswith('.webp') or f.endswith('.bmp'):
        sh.copyfile(f,f + '.bb')
        khiohpen(f)