from inspect import getargvalues

import pytesseract
from PIL import Image
import cv2, sys
import aircv as ac


def tesser(img='./test.png'):
    img = Image.open(img)
    # img = img.transpose(Image.ROTATE_180).transpose(Image.FLIP_LEFT_RIGHT)
    img.show()
    text = pytesseract.image_to_string(img)
    data = pytesseract.image_to_boxes(img)
    print(text)
    print(data)

def drawer(img:Image, pos, long, width):
    cv2.rectangle(img, ())

def isContain( imgSub:str=None, imgSrc:str=None):
    """
    :param imgSub: the image you need to find.
    :param imgSrc: the source image.
    :return:
    """
    # return ac.find_all_sift(imgSrc, imgSub)
    if imgSrc != '' and imgSub != '':
        sub,src = None, None
        try:
            sub = ac.imread(imgSub)
            src = ac.imread(imgSrc)
        except FileNotFoundError as e:
            print(e)
        if sub is not None and src is not None:
            expected = ac.find_all_template(sub, src)
            if expected is not None:
                print(expected)
                return True
            else:
                return False


class one(object):
    def __init__(self, **kwargs):
        self.frame = sys._getframe()


    def getKw(self):
        argsValue = getargvalues(self.frame)
        print(argsValue)

if __name__ == '__main__':
    # print(tesser())
    b = ac.find_all_template(ac.imread('./logo.png'), ac.imread('./src.png'))
    for i in b:
        print(b)
    b = isContain('./logo.png', './src.png')
    print(b)