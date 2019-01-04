
class BrowserStep(object):

    """
    selenium operation now.
    """

    def __init__(self, by='id', element='', event=''):
        self._by = by
        self._element = element
        self._event = event

    @property
    def by(self):
        return self._by

    @by.setter
    def by(self, value:str):
        self._by = value

    @property
    def element(self):
        return self._element

    @element.setter
    def element(self, value:str):
        self._element = value

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value:str):
        self._event = value

    def __str__(self):
        return "find {} by {} and event is {}".format(self.element, self.by , self.event)

class RestStep(object):
    """
    only support restful api now.
    """
    def __init__(self, method, path, parameter):
        self._method = method
        self._path = path
        self._parameter = parameter

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value:str):
        self._method=value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, v:str):
        self._path = v

    @property
    def parameter(self):
        return self._parameter

    @parameter.setter
    def parameter(self, v:dict):
        self._parameter = v

    def __str__(self):
        return "rest api path is {} method {} parameter {}".format(self.path, self.method, self.parameter)



class BrowserExpectedResult(BrowserStep):
    """
    browser result object
    """

    def __init__(self, by, element, event, result):
        super().__init__(by, element, event)
        self._reuslt = result

    @property
    def result(self):
        return self._reuslt

    @result.setter
    def result(self, v):
        self._reuslt = v

    def __str__(self):
        return "find {} by {} i need field {} and result is {}".format(self.element, self.by, self.event, self.result)

class RestExpectedResult(object):
    """
    restful result object
    """

    def __init__(self,statusCode:int, body:dict):
        self._body = body
        self._statusCode = statusCode

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, v:dict):
        self._body = v

    @property
    def statusCode(self):
        return self._statusCode

    @statusCode.setter
    def statusCode(self, v:int):
        self._statusCode = v
