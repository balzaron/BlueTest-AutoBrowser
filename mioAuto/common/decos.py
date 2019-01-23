import time
from functools import wraps
from pymongo import MongoClient

def dataProvider(fn_data_provider):
    """Data provider decorator, allows another callable to provide the data for the test"""
    def test_decorator(fn):
        @wraps(fn)
        def repl(self, *args):
            for i in fn_data_provider:
                try:
                    fn(self, *i)
                except AssertionError:
                    print("Assertion error caught with data set ", i)
                    raise
        return repl
    return test_decorator

def timeConsumer(timeout = 500):
    def deco_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            begin = time.time()*1000
            rt = func(*args, **kwargs)
            end = time.time()*1000
            consume = end - begin
            print('the %s consumed %d ms'%(func.__name__, consume))
            if consume >= timeout:
                raise TimeoutError('The method %s cost too much time!! It cost %d ms'%(func.__name__, consume))
            return rt

        return wrapper
    return deco_func


def mongoDataProvider(collection):
    """Data provider decorator, allows another callable to provide the data for the test"""
    fn_data_provider = collection.get('steps')
    def test_decorator(fn):
        @wraps(fn)
        def repl(self, *args):
            for i in fn_data_provider:
                try:
                    fn(self, *i)
                except AssertionError:
                    print("Assertion error caught with data set ", i)
                    raise

        return repl

    return test_decorator