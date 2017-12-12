from MergePng import *
from Generate_Number import *
import random
import os

def Generate_Numbers_to_dir(counts=1,max_number=2000,outdir='./numberImg'):
    '''
    used for recognization task
    :param counts: number you want to generate
    :param max_number: max value you want to generate
    :param outdir: root of img
    :return:
    '''

    if os.path.exists(outdir)==False:
        os.mkdir(outdir)
    for i in range(counts):
        while True:
            try:
                num = random.randint(0,max_number)
                color=(random.random(),random.random(),random.random())
                GenerateNumberPic(text=str(num),font='Vera.ttf',textsize=100,color=color,outPath=os.path.join(outdir,str(i)+'_'+str(num)+'.png'))
                break
            except Exception as e:
                continue

def Generate_Num_Detection_Dataset(bgroot,outimgroot,outlabelroot,counts=100,min_num_of_text=4,max_num_of_text=7):
    '''

    :param bgroot: Background image used for synthesize
    :param outimgroot: Output image root dir
    :param outlabelroot: Output label root dir
    :param counts: the number of data to synthesize
    :return: None
    '''
    fontlist=['./fonts/Vera.ttf']
    if os.path.exists(bgroot)==False:
        raise Exception("bgroot is not existed...")
    bgdirlist = os.listdir(bgroot)
    if os.path.exists(outimgroot)==False:
        os.mkdir(outimgroot)
    if os.path.exists(outlabelroot)==False:
        os.mkdir(outlabelroot)
    for i in range(counts):
        # Get Background image
        while True:
            bgname = random.choice(bgdirlist)
            bgpath=os.path.join(bgroot,bgname)
            try:
                bgimg = Image.open(bgpath)
                break
            except Exception as e:
                continue
        imglist=[]
        for k in range(random.randint(min_num_of_text, max_num_of_text)):
            while True:
                try:
                    text = str(random.randint(0,1000))
                    color=(random.random(),random.random(),random.random())
                    font=random.choice(fontlist)
                    imglist.append((text,GenerateNumberPic(text=text,textsize=100,color=color,font=font)))
                    break
                except Exception as e:
                    continue
        (outimg, labels)=merge_Background_text(bgimg, imglist)
        outimgpath=os.path.join(outimgroot,'%d.jpg'%i)
        outlabelpath=os.path.join(outlabelroot,'%d.txt'%i)
        outimg.save(outimgpath,'JPEG')
        fw = open(outlabelpath,'w')
        for text,box in labels:
            fw.write('%d %d %d %d %s\n'%(box[0],box[1],box[2],box[3],text))
        fw.close()

if __name__=='__main__':
    Generate_Num_Detection_Dataset('./bg','./outimg','./outlabel',30)