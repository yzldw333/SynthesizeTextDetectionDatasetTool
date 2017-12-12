from PIL import Image,ImageDraw
import numpy as np




def IOU(x1,y1,width1,height1,x2,y2,width2,height2):
    """
    Compute IOU
    """

    endx = max(x1+width1,x2+width2)
    startx = min(x1,x2)
    width = width1+width2-(endx-startx)

    endy = max(y1+height1,y2+height2)
    starty = min(y1,y2)
    height = height1+height2-(endy-starty)

    if width <=0 or height <= 0:
        ratio = 0 # 重叠率为 0
    else:
        Area = width*height
        Area1 = width1*height1
        Area2 = width2*height2
        ratio = Area*1./(Area1+Area2-Area)
    # return IOU
    return ratio
def merge_Background_text(bgimg,imgList):
    '''

    :param bgimg: <PIL.Image>
    :param imgList: [(str,PIL.Image)...]
    :return: (bgimg,pasteBoxes): (<PIL.Image>,[(text,BoundingBox)]
    '''
    import random
    bgwidth,bgheight = bgimg.size
    if bgimg.mode!='RGBA':
        bgimg = bgimg.convert('RGBA')
    pasteBoxes = []
    draw = ImageDraw.Draw(bgimg)
    for num,img in imgList:

        while True:
            width = random.random()*0.4+0.05 #random from 0.05~0.45 of image
            width*=bgwidth
            width = int(width)
            ratio = random.random()*1+0.5 #height/width random from 0.5~1.5
            height = width*ratio
            height = int(height)

            x = int(random.random()*(bgwidth-width))
            y = int(random.random()*(bgheight-height))
            if y+height>bgheight:
                continue
            valid = True
            for text,box in pasteBoxes:
                iou = IOU(box[0],box[1],box[2]-box[0],box[3]-box[1],x,y,x+width,y+height)
                if iou>0:
                    valid = False
                    break
            if valid:
                pasteBoxes.append((num,(x,y,x+width,y+height)))
                img = img.resize((width,height),Image.BILINEAR)
                bgimg.paste(img,(x,y),img)
                #visualize and debug
                #draw.rectangle([x,y,x+width,y+height])
                break
    #bgimg.show()
    return (bgimg,pasteBoxes)