import random
from time import time
from unittest import TestCase, skip, skipIf

from common.build_rpc_client import build_rpc_client
from common.config_center import globalconfig
from common.decos import dataProvider, timeConsumer
from common.utils import get_csv_data, grpcObject2dict
from grpctest.generated.dmp_pb2 import *
from grpctest.generated.pikachu_pb2_grpc import DmpCharmanderServiceStub
from google.protobuf.json_format import MessageToJson

conf = globalconfig().get('grpc').get('pikachu')
data1 = get_csv_data(path = '/Users/miotech/PycharmProjects/auto_miotech/grpctest/data/DmpCharmanderServiceStub_queryAssetMarketDataSeries.csv')
data2 = get_csv_data('./data/DmpCharmanderServiceStub_retrieveAssetId.csv')
host = conf.get('host')
port = int(conf.get('port'))
stub = build_rpc_client(host, port, DmpCharmanderServiceStub)
endTime = int(time()*1000)
currentTimeStamp = endTime
gap = 150*24*86400*1000
startTime = endTime - gap
appleGlobalId = "ceaa2bced7ed36e9c71acc124218f9c8:0"
appleAssetId = 20736
globalId2 = '12345678'
dataQueryByAssetId =(
    ({"assetId": [appleAssetId],"startTime": startTime,"endTime": endTime}, True),
)
dataQueryByGlobalId = (
    ({
"startTime": startTime,
"endTime": endTime,
"globalId": [appleGlobalId]
}, True),
)

dataRetrieveAssetId= (
    ({
    "retrieveAssetId": [{
    "ticker": "AAPL",
    "currency": "USD",
    "marketSecotr": "EQUITY",
    "exchange": {
    "exchangeId": "NSQ"
    }
    }]
    },True),
)

myTicker = "GSY_TEST_TICKER"+str(random.randint(1000,500000))
userId = 'MioTech'
dataCreateUserProduct = (
        ({
    "asset": [{
    "assetIDGroup": {
    "ticker": myTicker
    },
    "marketSector": "EQUITY",
    "userId": userId,
    "currency": "USD",
    "exchange": {
    "exchangeId": "NSQ"
    }
    }]
    }, True),
    )
appId = 'MioTech'

dataListAllUserProduct = (
    ({'accountId': appId}, True),
)
dataListAllUserProductReturnEmpty = (
    ({'accountId': appId + str(random.randint(9999, 999999))}, True),
    # ({}, True),
)
dataListAllCountryInfo = (
    ({"needAll": True}, {}),
    ({'code':'USA'}, {})
)

dataListAllExchangeInfo = (
    ({"needAll": True}, {}),
    ({'code':'NSQ'}, {})
)


class Test_queryAssetMarketDataSeries(TestCase):

    @skip('config is not ready')
    @timeConsumer(2000)
    @dataProvider(dataQueryByAssetId)
    def test_1_queryAssetMarketDataSeries_assetId(self, input, expected):
        real = stub.queryAssetMarketDataSeries(AssetDataRequest(**input))
        # print(real)
        self.assertIsNotNone(real)

    @timeConsumer(2000)
    @dataProvider(dataQueryByGlobalId)
    def test_2_queryAssetMarketDataSeries_globalId(self, input, expected):
        real = stub.queryAssetMarketDataSeries(AssetDataRequest(**input))
        # print(real)
        self.assertIsNotNone(real)

    @timeConsumer()
    @dataProvider(dataRetrieveAssetId)
    def test_3_retrieveAssetId(self, input, expected):
        real = stub.retrieveAssetId(RetrieveAssetIdRequest(**input))
        self.assertIsNotNone(real)

    @timeConsumer(2000)
    @dataProvider(dataCreateUserProduct)
    def test_4_createUserProduct(self, input, expected):
        real = stub.createUserProduct(CreateUserProductRequest(**input))
        self.assertIsNotNone(real)
        global globalIdOfMyProduct
        global assetIdOfMyProduct
        reallist = list(real.createUserProduct)

        for i in reallist:
            globalIdOfMyProduct = i.globalId
            assetIdOfMyProduct = i.assetId

    @timeConsumer(2000)
    @dataProvider(dataCreateUserProduct)
    def test_4_createUserProduct(self, input, expected):
        real = stub.createUserProduct(CreateUserProductRequest(**input))
        self.assertIsNotNone(real)
        global globalIdOfMyProduct
        global assetIdOfMyProduct
        reallist = list(real.createUserProduct)

        for i in reallist:
            globalIdOfMyProduct = i.globalId
            assetIdOfMyProduct = i.assetId

    @skip('not ready')
    @timeConsumer()
    def test_5_updateUserProduct(self):
        input = {
                "updateAssetMarketData": [{
                "pricePoint": [{
                "timestamp": currentTimeStamp,
                "adjustedPrice": random.random()
                }, {
                "timestamp": currentTimeStamp,
                "adjustedPrice": random.random()
                }],
                "globalId": globalIdOfMyProduct
                }]
                }
        real = stub.updateUserProduct(UpdateUserProductRequest(**input)).success
        self.assertTrue(real)

    @timeConsumer()
    @dataProvider(dataListAllUserProduct)
    def test_6_listAllUserProduct(self,input, expected):
        real = stub.listAllUserProduct(ListAllUserProductRequest(**input))
        self.assertNotEqual(grpcObject2dict(real), {})


    @timeConsumer()
    @dataProvider(dataListAllUserProductReturnEmpty)
    def test_7_listAllUserProduct(self,input, expected):
        real = stub.listAllUserProduct(ListAllUserProductRequest(**input))
        self.assertEqual(grpcObject2dict(real), {})

    @timeConsumer()
    @dataProvider(dataListAllCountryInfo)
    def test_8_listAllCountryInfo(self, input, expected):
        real = stub.listAllCountryInfo(ListAllRequest(**input))
        self.assertNotEqual(grpcObject2dict(real), expected)

    @timeConsumer()
    @dataProvider(dataListAllExchangeInfo)
    def test_9_listAllExchangeInfo(self, input, expected):
        real = stub.listAllExchangeInfo(ListAllRequest(**input))
        print(real)
        self.assertNotEqual(grpcObject2dict(real), expected)

    # @classmethod
    # def tearDownClass(cls):
    #     data1 = {'globalId':[globalIdOfMyProduct]}
    #     data2 = {'assetId':[assetIdOfMyProduct]}
    #     stub.deleteUserProduct(DeleteUserProductRequest(**data1))
    #     stub.deleteUserProduct(DeleteUserProductRequest(**data2))

