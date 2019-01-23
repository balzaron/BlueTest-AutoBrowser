import inspect
import os
import csv, json
import time
from dataclasses import dataclass

import pandas as pd
from google.protobuf.json_format import MessageToJson
from google.protobuf.message import Message

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


class dict2obj(object):
    def __init__(self,dic):

        for a,b in dic.items():
            if isinstance(b,(list,tuple)):
                setattr(self,a,[x if isinstance(x,dict)else x for x in b])
            else:
                setattr(self,a,b if isinstance(b,dict)else b)

    # def toObj(self, obj):
    #     return obj(self(self.args, self.kwargs))


class DictObj(object):
    def __init__(self,map):
        self.map = map

    def __setattr__(self, name, value):
        if name == 'map':
             object.__setattr__(self, name, value)
             return
        self.map[name] = value

    def __getattr__(self,name):
        v = self.map[name]
        if isinstance(v,(dict)):
            return DictObj(v)
        if isinstance(v, (list)):
            r = []
            for i in v:
                r.append(DictObj(i))
            return r
        else:
            return self.map[name]

    def __getitem__(self,name):
        return self.map[name]

def wrapperLink(url:str):
    return "<a href=\"{}\", target=\"_blank\">{}</a>".format(url, url)

def getCurrentMillis():
    return int(time.time()*1000)

def get_request_timestamp(req_type=None, timestamp=getCurrentMillis()):
    """

    :param req_type: YTD, QTD, MTD, WTD, TODAY or None
    if None return first unix timestamp
    :return: unix timestamp
    """

    @dataclass
    class YTD(object):
        pass
    bench_date = pd.to_datetime(getUTCBeginDay(timestamp), unit='ms')
    if req_type not in (YTD, QTD, MTD, WTD, TODAY):
        return DAY_OF_MILLISECONDS
    if req_type == YTD:
        date = bench_date + pd.tseries.offsets.DateOffset(months=1 - bench_date.month, days=1 - bench_date.day)
    if req_type == QTD:
        date = bench_date + pd.tseries.offsets.DateOffset(months=-((bench_date.month - 1) % 3),
                                                          days=1 - bench_date.day)
    if req_type == MTD:
        date = bench_date + pd.tseries.offsets.DateOffset(days=1 - bench_date.day)
    if req_type == WTD:
        date = bench_date + pd.tseries.offsets.DateOffset(days=-bench_date.weekday())
    if req_type == TODAY:
        date = bench_date
    return getMillisSeconds(date) - DAY_OF_MILLISECONDS

