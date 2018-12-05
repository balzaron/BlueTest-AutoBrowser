import json

from grpc_tools import protoc
import os

from common.utils import get_csv_data

template = \
    """
from unittest import TestCase
from common.build_rpc_client import build_rpc_client
from common.config_center import globalconfig
from common.dataprovider import dataProvider
from common.utils import get_csv_data
from grpctest.generated.dmp_pb2 import AssetDataRequest
from {stub_package}_ import {stub}

conf = globalconfig().get('grpc').get('{service_name}')

{datas}

class Test_queryAssetMarketDataSeries(TestCase):

    @classmethod
    def setUpClass(cls):
        host = conf.get('host')
        port = int(conf.get('port'))
        stub = {stub}
        cls.stub = build_rpc_client(host, port, stub)

    {methods}

    @classmethod
    def tearDownClass(cls):
        pass
    """

method_template=\
    """
@dataProvider({data})
def test_{rpc_method}(self, input, expected):
    self.{assert_function}(self.stub.{rpc_method}({request_object}(**input)), expected)
    """


class TestClassObj(object):

    def __init__(self, stub_package, stub, datas:list, methods:list):
        self.stub_package = stub_package
        self.stub = stub
        self.datas = datas
        self.methods = methods

class TestMethodObj(object):

    def __init__(self, data, rpc_method, assert_function, request_object):
        self.data = data
        self.rpc_method = rpc_method
        self.assert_function = assert_function
        self.request_object = request_object

def proto_gen(path):
    dirs = os.listdir(path)
    print(dirs)
    for f in dirs:
        protoc.main((
            '',
            '-I./protos/',
            '--python_out=./generated/',
            '--grpc_python_out=./generated/',
            './protos/%s'%f,
        ))

def code_gen(data_dir:str, output_dir:str):
    """
    :param output_dir:
    :return:
    """
    for file in os.listdir(data_dir):
        data_file_name = file.split('_')
        service_name = data_file_name[-1]



if __name__ == '__main__':
    proto_gen('./protos')
