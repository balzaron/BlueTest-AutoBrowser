import inspect
from dataclasses import dataclass, field

from mioAuto.model import *

@dataclass
class BrowserStep(BaseModel):
    by: str = field(hash=True)
    element: str = field(hash=True)
    event: str = field(hash=True)
    type: str = inspect.stack()[0][3]


@dataclass
class BrowserExpectedResult(BaseModel):
    by: str = field(hash=True)
    element: str = field(hash=True)
    event: str = field(hash=True)
    result: object
    assertType: str = 'Equal'
    type: str = inspect.stack()[0][3]



@dataclass
class RestStep(BaseModel):
    method: str
    path: str
    parameter: dict
    type: str = inspect.stack()[0][3]


@dataclass
class RestExpectedResult(BaseModel):
    body: dict
    statusCode: int=200
    assertType: str="Equal"
    type: str = inspect.stack()[0][3]


@dataclass
class BrowserElementValue(BaseModel):
    by: str = field(hash=True)
    element: str = field(hash=True)
    position: str
    type: str = inspect.stack()[0][3]


@dataclass
class RestField(BaseModel):
    method: str
    path: str
    parameter: dict
    valuePath:str
    # assertType:str=None
    # result = None
    type: str = inspect.stack()[0][3]


@dataclass
class RestFieldExpectedResult(BaseModel):
    method: str
    path: str
    parameter: dict
    valuePath: str
    assertType: str
    result: object
    type: str = inspect.stack()[0][3]


def getValue(obj:dict, vp:str, separator='') -> dict:
    layers:list = vp.split(separator)
    tmp = obj
    for i in layers:
        if isinstance(tmp, list):
            tmp = tmp[int(i)]
        elif isinstance(tmp, dict):
            tmp = tmp.get(i.strip())
    return tmp

