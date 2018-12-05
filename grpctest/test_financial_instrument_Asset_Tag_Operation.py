# author: shanyue.gao
# datetime:2018/12/1 3:54 PM

import random
import time
from unittest import TestCase

from common.build_rpc_client import build_rpc_client
from common.config_center import globalconfig
from common.decos import dataProvider, timeConsumer
from common.utils import grpcObject2dict
from grpctest.generated.dmp_pb2 import *
from grpctest.generated.financial_instrument_service_pb2_grpc import FinancialInstrumentServiceStub

conf = globalconfig().get('grpc').get('fi')
stub = build_rpc_client(host=conf.get('host'), port=conf.get('port'), stub=FinancialInstrumentServiceStub)

appId= "MioTech"
assetTagCategoryName = "JUST_FOR_GSY_TEST_assetTagCategoryName"+str(random.randint(1, 10000))
assetTagName = "JUST_FOR_GSY_TEST_assetTagName"+str(random.randint(1, 10000))
assetTagChoiceName1 = 'AUD'
assetTagChoiceName2 = 'BGN'
assetId = random.randint(1000000000,9000000000)
assetTagChoiceId1 = 858
assetTagChoiceId2 = 859
assetTagTypeId = 9

#==========data prepare==================
data1 = (
    ({'appId':appId}, True),
)
data2 = (
    ({'appId':appId},True),
)

data3 = (
    ({"appId":appId, 'assetTagCategoryName':assetTagCategoryName}, True),
)

data5 = (
    ({
  "appId": appId,
  "tagType": "INPUT_FIELD"
}, True),
)

data7 = (
    ({'appId': appId, 'assetId':assetId}, True),
)

#========================================

class test_financial_instrument_Asset_Tag_Operation(TestCase):

    @timeConsumer()
    @dataProvider(data1)
    def test_1_retrieveAllAssetTag(self, input, expected):
        real = stub.retrieveAllAssetTag(RetrieveAllAssetTagRequest(**input))
        self.assertEqual(real.success, expected)

    @timeConsumer()
    @dataProvider(data2)
    def test_2_retrieveAssetTagType(self, input, expected):
        real = stub.retrieveAssetTagType(RetrieveAssetTagTypeRequest(**input))
        self.assertTrue(real.success)
        print(real)
        self.assertIsNotNone(real.assetTagType)


    @timeConsumer()
    @dataProvider(data3)
    def test_3_addAssetTagCategory(self, input, expected):
        real = stub.addAssetTagCategory(AddAssetTagCategoryRequest(**input))
        self.assertTrue(real.success)
        global assetTagCategoryId
        assetTagCategoryId = real.assetTagCategoryId
        self.assertGreaterEqual(assetTagCategoryId, 0)

    @timeConsumer()
    def test_4_addAssetTag(self):
        data = {"appId": appId,
                  "assetTagCategoryId": assetTagCategoryId,
                  "assetTagData": {
                    "assetTagName": assetTagName,
                    "assetTagTypeId": assetTagTypeId,
                    "assetTagChoices": [{
                      "assetTagChoiceName":assetTagChoiceName1
                    }, {
                      "assetTagChoiceName": assetTagChoiceName2
                    }]
                  }
                }
        real = stub.addAssetTag(AddAssetTagRequest(**data))
        print(grpcObject2dict(real))
        self.assertTrue(real.success)
        global assetTagId
        assetTagId = real.assetTagId
        self.assertGreaterEqual(assetTagId, 0)

    @timeConsumer()
    @dataProvider(data5)
    def test_5_retrieveTagListByTagType(self, input, expected):
        real = stub.retrieveTaglistByTagType(RetrieveTaglistByTagTypeRequest(**input))
        self.assertEqual(real.success, expected)
        self.assertIsNot(real.assetTagData, [])

    @timeConsumer()
    def test_6_saveAssignedTag(self):
        data6 = {

                 "appId": appId,
                 "assetId": assetId,
                 "assetTagData": [{
                     "assetTagId": assetTagId,
                     "assetTagChoices": [{
                         "assetTagChoiceId": assetTagChoiceId1,
                         "assetTagChoiceName": assetTagChoiceName1
                     }, {
                         "assetTagChoiceId": assetTagChoiceId2,
                         "assetTagChoiceName": assetTagChoiceName2,
                         "selected": True
                     }]
                 }]
             }
        real = stub.saveAssignedTag(SaveAssignedTagRequest(**data6))
        print(grpcObject2dict(real))
        self.assertTrue(real.success)

    @timeConsumer()
    @dataProvider(data7)
    def test_7_retrieveAssignedTag(self, input, expected):
        real = stub.retrieveAssignedTag(RetrieveAssignedTagRequest(**input))
        self.assertEqual(real.success, expected)

    @classmethod
    def tearDownClass(cls):
        rtr = {'appId':appId, 'assetTagId':assetTagId}
        ratc = {'appId':appId, 'assetTagCategoryId': assetTagCategoryId}
        stub.removeAssetTag(RemoveAssetTagRequest(**rtr))
        stub.removeAssetTagCategory(RemoveAssetTagCategoryRequest(**ratc))
