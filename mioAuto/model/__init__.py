import inspect
from dataclasses import dataclass


class BaseObj(object):

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, v:object):
        self._type = v

class BaseModel(object):
    pass