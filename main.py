import os
import PIL
from PIL import Image


leftImgName = 'boxFront.png'
topImgName = 'boxFront.png'
bottomImgNames = ['marquee.png', 'cartridge.png', 'screenshot.png', 'Texture.png']

files = ['a', 'b']


inputFolderName = 'input'


def output(folder, topImgPath, bottomImgPath):
    print(topImgPath + ' ' + bottomImgPath)

    new_im = Image.new('RGBA', (640, 633))
    cover = Image.open(os.path.join('', leftImgName))

    topImg = Image.open(topImgPath)
    topImg.thumbnail((640, 316))
    new_im.paste(topImg, (132, 0))

    bottomImg = Image.open(bottomImgPath)
    bottomImg.thumbnail((640, 316))
    new_im.paste(bottomImg, (132, 317))

    new_im.paste(cover, (0,0), cover)

    new_im.save(folder + '/boxFront.png')


for filename in os.listdir(inputFolderName):
    folder = os.path.join(inputFolderName, filename)

    if os.path.isdir(folder):
        topImgPath = ''
        bottomImgPath = ''
        for imgName in os.listdir(folder):
            imgPath = os.path.join(folder, imgName)
            if os.path.isfile(imgPath):
                # print(imgPath)
                if (imgName == topImgName):
                    topImgPath = imgPath
              
        for cand in bottomImgNames:
            find = False 
            for imgName in os.listdir(folder):
                if (imgName == cand):
                    find = True 
                    print(cand, imgName)
                    imgPath = os.path.join(folder, imgName)
                    if os.path.isfile(imgPath):
                        bottomImgPath = imgPath
                        # print(cand)
                        if(topImgPath != ""):
                            output(folder, topImgPath, bottomImgPath)
                            break
                        # else:
                        #     continue
                        break
                    break
            if find: 
                break 


                     




exit()

