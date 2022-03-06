from easygui import fileopenbox, msgbox
import PIL.Image as im
f = fileopenbox()
print(f)
if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.tif'):
    end = -4
elif f.endswith('.webp') or f.endswith('.tiff'):
    end = -5
else:
    msgbox('格式错误！')
    end = 0
if end != 0:
    bs = im.open(f)
    w = bs.size[0] // 128
    h = bs.size[1] // 128
    print(w, h)
    for i in range(0,w):
        for j in range(0,h):
            plm = f[0:end] + str(i) + str(j) + '.png'
            bs.crop((i*128,j*128,(i+1)*128,(j+1)*128)).save(plm)


