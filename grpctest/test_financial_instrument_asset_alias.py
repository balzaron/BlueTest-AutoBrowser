# author: shanyue.gao
# datetime:2018/12/1 1:44 PM
import json
import random
import time
from unittest import TestCase

from common.build_rpc_client import build_rpc_client
from common.config_center import globalconfig
from common.decos import dataProvider, timeConsumer
from grpctest.generated.dmp_pb2 import *
from grpctest.generated.financial_instrument_service_pb2_grpc import FinancialInstrumentServiceStub

conf = globalconfig().get('grpc').get('fi')
stub = build_rpc_client(host=conf.get('host'), port=conf.get('port'), stub=FinancialInstrumentServiceStub)

assetId = random.randint(1000000000, 9000000000)
assetAlias = 'ASSET_NAME_JUST_FOR_GSY_TEST'+str(random.randint(1999990,9999990))
assetAliasEdited = 'ASSET_NAME_JUST_FOR_GSY_TEST_EDITED'+str(random.randint(1999990,9999990))
appId = "MioTech"
appleAssetId = 20736
# GlobalAssetAliasId = 0
#==========data prepare==================
data1 = (
    (  {"assetAliasData":{"assetId": appleAssetId,"assetAlias": assetAlias,"insertTime": int(time.time()),"appId": appId}}, True),
)

data2 = (
    ({"appId": appId,"assetId": appleAssetId, "retrieveAll": True}, True),
)

data3 = (
    ({"assetAliasData": {"assetAliasId": appleAssetId,"assetAlias": assetAliasEdited,
    "insertTime": int(time.time()),
    "appId":appId}}, True),
)
data4 = (
    ({
  "appId": appId,
  "assetId": appleAssetId,
  "retrieveAll": True}, True),
)

data5 = (
    ({'assetAliasId':assetId}, True),
)

#========================================

class Test_financial_instrument_asset_alias(TestCase):

    @dataProvider(data1)
    @timeConsumer()
    def test_1_addAssetAlias(self, input, expected):
        realObj = stub.addAssetAlias(AddAssetAliasRequest(**input))
        global GlobalAssetAliasId
        GlobalAssetAliasId = realObj.assetAliasId
        self.assertEqual(realObj.success, expected)
        self.assertGreaterEqual(realObj.assetAliasId, 0)

    @timeConsumer()
    @dataProvider(data2)
    def test_2_retrieveAssetAlias(self, input, expected):
        realObj = stub.retrieveAssetAlias(RetrieveAssetAliasRequest(**input))
        print(realObj)
        assetAliasData:AssetAliasData = realObj.assetAliasData
        print(assetAliasData)
        self.assertEqual(realObj.success, expected)
        # self.assertEqual(assetAliasData.assetId, appleAssetId)
        # self.assertEqual(assetAliasData.assetName, "Apple Inc")

    @timeConsumer()
    @dataProvider(data3)
    def test_3_editAssetAlias(self, input, expected):
        realObj = stub.editAssetAlias(EditAssetAliasRequest(**input))
        print()
        self.assertEqual(realObj.success, expected)

    @timeConsumer()
    @dataProvider(data4)
    def test_4_retrieveAssetAlias(self, input, expected):
        realObj = stub.retrieveAssetAlias(RetrieveAssetAliasRequest(**input))
        print(realObj)
        self.assertTrue(realObj.success)

    @timeConsumer()
    @dataProvider(data5)
    def test_5_removeAssetAlias(self, input, expected):
        realObj = stub.removeAssetAlias(RemoveAssetAliasRequest(**input))
        print(realObj)
        self.assertTrue(realObj.success)

    @classmethod
    def tearDownClass(cls):
        tearDownData = {'assetAliasId':GlobalAssetAliasId}
        stub.removeAssetAlias(RemoveAssetAliasRequest(**tearDownData))