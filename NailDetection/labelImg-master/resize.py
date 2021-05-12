from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir,width=3000,height=3000):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
for jpgfile in glob.glob("D:\\MasterThesis\\NailDetection\\nail_voc2007\\JPEGImages\\*.jpg"):
    convertjpg(jpgfile,"D:\\MasterThesis\\NailDetection\\nail_voc2007\\resize")
