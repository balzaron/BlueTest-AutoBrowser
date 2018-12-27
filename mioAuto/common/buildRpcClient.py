import grpc

def buildRpcClient(host:str, port:int, stub):
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

