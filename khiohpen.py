from easygui import fileopenbox, msgbox
from PIL import Image, ImageChops

def TrimImgEdge(inImgPath, outImgPath):
    imgIn = Image.open(inImgPath)
    # 创建一个边框颜色图片
    bg = Image.new(imgIn.mode, imgIn.size, '#00000000')
    diff = ImageChops.difference(imgIn, bg)
    # diff = ImageChops.add(diff, diff, 2.0, -10) # 可选，会去的更干净，副作用是误伤
    bbox = diff.getbbox()   # 返回左上角和右下角的坐标 (left, upper, right, lower)
    if bbox:
        imgIn.crop(bbox).save(outImgPath, quality=95)

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
    TrimImgEdge(f,f)