# author: shanyue.gao
# datetime:2018/12/3 2:07 PM

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
appId = "MioTech"
assetTagCategoryName = "TEST_CASE_TestCategoryName"+str(random.randint(0,20000))

#==========data prepare==================
data1 = (
    ({
    "appId": appId,
    "assetTagCategoryName": assetTagCategoryName
    }, True),
)
#========================================

class test_fi_old(TestCase):

    @timeConsumer()
    @dataProvider(data1)
    def test_1_addAssetTagCategory(self, input, expected):
        real = stub.addAssetTagCategory(AddAssetTagCategoryRequest(**input))
        global assetTagCategoryId
        assetTagCategoryId = real.assetTagCategoryId
        self.assertTrue(real.success)
        self.assertGreaterEqual(assetTagCategoryId, 0)

    @classmethod
    def tearDownClass(cls):
        input1 = {'appId':appId, 'assetTagCategoryId':assetTagCategoryId}
        stub.removeAssetTagCategory(RemoveAssetTagCategoryRequest(**input1))
