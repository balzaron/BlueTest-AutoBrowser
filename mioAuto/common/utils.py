import inspect
import os
import csv, json

from google.protobuf.json_format import MessageToJson
from google.protobuf.message import Message
from collections import namedtuple

def get_current_function_name():
    return inspect.stack()[1][3]

def get_abs_path(file = __file__):
    return os.path.dirname(os.path.abspath(file))

def get_parent_abs_path(file = __file__):
    return os.path.dirname(os.path.dirname(os.path.abspath(file)))

def isJson(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

def grpcObject2dict(obj):
    return json.loads(MessageToJson(obj)) if Message in obj.__class__.__bases__ else False

def get_csv_data(path, delimter='|'):
    with open(path, 'r',) as f:
        lines = csv.reader(f, delimiter=delimter,  quotechar='"')
        ret = []

        for line in lines:
            l=[]
            for e in line:
                if type(e) == str and isJson(e):
                    dic = json.loads(e)
                    l.append(dic)
                elif (e.lower() =='none' or e.lower() == 'null'):
                    n = None
                    l.append(n)
                elif (e.lower() == '!none' or e.lower() == '!null'):
                    n = None
                    l.append(n)
                elif e.lower() == 'true':
                    n = True
                    l.append(n)
                elif e.lower() == 'false':
                    n = False
                    l.append(n)
                else:
                    l.append(e)
            l = tuple(l)
            ret.append(l)
        return ret

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

def _dict_to_object(policys):
    policys_length = len(policys['policys'])
    res = []
    for i in range(policys_length):
        policy = Struct(**policys['policys'][i])
        res.append(policy)
    return res

class dict2obj(object):
    def __init__(self,d):
        for a,b in d.items():
            if isinstance(b,(list,tuple)):
                setattr(self,a,[dict2obj(x) if isinstance(x,dict)else x for x in b])
            else:
                setattr(self,a,dict2obj(b) if isinstance(b,dict)else b)

def wrapperLink(url:str):
    return "<a href=\"{}\", target=\"_blank\">{}</a>".format(url, url)

if __name__ == '__main__':
    print(__file__)