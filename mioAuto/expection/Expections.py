
class ElementNotFoundException(Exception):
    def __init__(self, element='', err='The element {} is not found in current page!'):
        super().__init__()
        self.err = err
        self.element = element

    def __str__(self):
        return self.err.format(self.element)


class ImageNotFindException(Exception):
    def __init__(self, imgSub='', imgSrc='', err='The {} cannot be find in source image {}!'):
        super().__init__()
        self.err = err
        self.imgSub = imgSub
        self.imgSrc = imgSrc

    def __str__(self):
        return self.err.format(self.imgSub, self.imgSrc)

class NotSupportBrowserException(Exception):
    def __init__(self, browser:str, err = 'The browser {} is not support now!'):
        super().__init__()
        self.err = err
        self.browser = browser

    def __str__(self):
        return self.err.format(self.browser)