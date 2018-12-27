class Browser(object):

    @property
    def cookie(self):
        return self._cookie

    @cookie.setter
    def cookie(self, value: str):
        self._cookie = value

    @property
    def driverPath(self):
        return self._driverPath

    @driverPath.setter
    def driverPath(self, value: str):
        self._driverPath = value

    @property
    def initPage(self):
        return self._initPage

    @initPage.setter
    def initPage(self, value:str):
        self._initPage = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

if __name__ == '__main__':
    a = Browser()
    a.initPage = 'u'
    print(a.initPage)
    