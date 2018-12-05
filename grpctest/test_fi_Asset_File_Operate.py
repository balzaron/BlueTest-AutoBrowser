# author: shanyue.gao
# datetime:2018/12/3 10:20 AM

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
appleAssetId = 20736
currentTimeStamp = int(time.time()*1000)
fileId = random.randint(122222222, 922222222)
assetFileId = 0
#==========data prepare==================

data1 = (
    ({

  "assetFileData": {

    "assetId": appleAssetId,

    "fileId": fileId,

    "insertTime": currentTimeStamp,

    "appId": appId

  }

},
     {
         "success": True,
     }
    ),
)

data2 = (
    ({'appId': appId, 'assetId':appleAssetId},
     {'success':True}),
)

data3 = (
    ({"appId": appId,
      "retrieveAll": True
    }, True),
)

data4 = (
    ({"assetFileData": {
    "assetFileId": assetFileId,
    "assetId": appleAssetId,
    "fileId": fileId,
    "insertTime": currentTimeStamp,
    "appId": appId
  }
}, True),
)
#========================================

class test_fi_Asset_File_Operate(TestCase):

    @timeConsumer()
    @dataProvider(data1)
    def test_1_addAssetFile(self, input:dict, expected:dict):
        real = stub.addAssetFile(AddAssetFileRequest(**input))
        self.assertEqual(real.success, expected.get('success'))
        global  assetFileId
        assetFileId = real.assetFileId
        self.assertGreaterEqual(assetFileId, 0)

    @timeConsumer(2000)
    @dataProvider(data2)
    def test_2_retrieveAssetFile(self, input, expected):
        real = stub.retrieveAssetFile(RetrieveAssetFileRequest(**input))
        self.assertEqual(real.success, expected.get('success'))
        assetFileDataList = list(real.assetFileData)
        for i in assetFileDataList:
            if i.assetFileId == assetFileId:
                self.assertTrue(True)
            if i.assetId == appleAssetId:
                self.assertTrue(True)

    @timeConsumer()
    @dataProvider(data3)
    def test_3_retrieveAssetFile(self, input, expected):
        real = stub.retrieveAssetFile(RetrieveAssetFileRequest(**input))
        self.assertEqual(real.success, expected)
        assetFileDataList = list(real.assetFileData)
        for i in assetFileDataList:
            if i.assetFileId == assetFileId:
                self.assertTrue(True)
            if i.assetId == appleAssetId:
                self.assertTrue(True)

    @timeConsumer()
    @dataProvider(data4)
    def test_4_editAssetFile(self, input, expected):
        real = stub.editAssetFile(EditAssetFileRequest(**input))
        self.assertTrue(real.success)

    @timeConsumer()
    @dataProvider(data3)
    def test_5_retrieveAssetFile(self, input, expected):
        real = stub.retrieveAssetFile(RetrieveAssetFileRequest(**input))
        self.assertEqual(real.success, expected)
        assetFileDataList = list(real.assetFileData)
        for i in assetFileDataList:
            if i.assetFileId == assetFileId:
                self.assertTrue(True)
            if i.assetId == appleAssetId:
                self.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        stub.removeAssetFile(RemoveAssetFileRequest(**{'assetFileId': assetFileId}))