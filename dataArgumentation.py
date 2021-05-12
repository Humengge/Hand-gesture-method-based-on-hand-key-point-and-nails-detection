import os
from PIL import Image


def argumanetation(path, name):
    label = name[-7:]
    id = str(int(name[:-7])+300)
    newName = id + label
    img = Image.open(path+name)
    img = img.transpose(Image.ROTATE_90)  # rotation 90
    #img = img.transpose(Image.ROTATE_180)  # rotation 180
    #img = img.transpose(Image.ROTATE_270)  # rotation 270
    # img.show("img/rotateImg.png")
    img.save(path+newName)

def mirror(path, name):
    label = name[-7:]
    id = str(int(name[:-7])+600)
    newName = id + label
    img = Image.open(path+name)
    img.transpose(Image.FLIP_LEFT_RIGHT).save(path+newName)

path = "./dataAndLabel/"
fileNames = os.listdir(path)
errorNames = ['117b33.jpg', '16b44.jpg', '171b55.jpg', '218g32.jpg', '254b11.jpg', '256b22.jpg', '267g23.jpg', '295g13.jpg', '37s23.jpg', '43g23.jpg', '56s23.jpg', '8g14.jpg']
rightNames = set(fileNames).difference(set(errorNames))
for name in rightNames:
    # argumanetation(path, name)
    mirror(path, name)


