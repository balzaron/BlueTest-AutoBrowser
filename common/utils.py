import inspect
import os
import csv, json

from google.protobuf.json_format import MessageToJson


def get_current_function_name():
    return inspect.stack()[1][3]

def get_abs_path():
    return os.path.dirname(os.path.abspath(__file__))

def get_parent_abs_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def grpcObject2dict(obj):
    return json.loads(MessageToJson(obj))

def get_csv_data(path):
    with open(path, 'r',) as f:
        lines = csv.reader(f, delimiter='|',  quotechar='"')
        ret = []

        for line in lines:
            l=[]
            for e in line:
                if type(e) == str and is_json(e):
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
