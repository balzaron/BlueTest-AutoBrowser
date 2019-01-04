from mioAuto import imagePathPrefix
from mioAuto.common.utils import *



class fort(object):


    def saveImage(self, fn, index:int):
        folder = imagePathPrefix + self.__class__.__name__ + '/'
        assemble = folder+fn+ str(index)+'.png'
        print(assemble)

class fss(fort):

    def ff(self):
        i=0
        self.saveImage(get_current_function_name(), i)
        i+=1
        self.saveImage(get_current_function_name(),i)

if __name__ == '__main__':
    f=fss()
    f.ff()