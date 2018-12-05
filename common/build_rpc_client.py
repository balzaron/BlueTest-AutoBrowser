import json

import grpc
from grpctest.generated.hello_pb2_grpc import helloStub
from grpctest.generated.hello_pb2 import response, request, sub

def build_rpc_client(host:str, port:int, stub):
    """
    :param host: server host
    :param port: port
    :param stub: grpc stub
    :return:
    """
    _stub = None
    try:
        channel = grpc.insecure_channel("{}:{}".format(host,str(port)))
        _stub = stub(channel)
        return _stub
    except Exception as e:
        pass
    finally:
        pass

from grpctest.generated.financial_instrument_service_pb2_grpc import FinancialInstrumentServiceStub
from grpctest.generated.financial_instrument_service_pb2 import *


if __name__ == '__main__':
    request1 ={

      "appId": "MioTech"

    }


    resp:AddAssetTagCategoryResult = build_rpc_client('18.182.39.102', 9221, FinancialInstrumentServiceStub).retrieveAllAssetTag(RetrieveAllAssetTagRequest(
        **request1
    ))
    print(resp)

    req = {'text':"jekki",
           'age':22,
           'sub1':{
               'sub1':'sub field 1',
               'sub2':2
           }
           }

    resp = build_rpc_client('localhost', 50051, helloStub).sayYo(request(**req))
    print(resp)

    req1 = {'text':"mona",
           'age':21,
           'sub1':{
               'sub1':'sub field 1',
               'sub2':2
           }
           }

    resp = build_rpc_client('localhost', 50051, helloStub).sayYo(request(**req1))
    print(resp)

