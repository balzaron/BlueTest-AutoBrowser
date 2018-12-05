import random
from unittest import TestCase

from common.build_rpc_client import build_rpc_client
from common.config_center import globalconfig
from common.decos import dataProvider
from grpctest.generated.dmp_pb2 import *
from grpctest.generated.financial_instrument_service_pb2_grpc import FinancialInstrumentServiceStub

#==========data prepare==================
# data2 = get_csv_data('./data/financial_instrument/addAssetTagCategory.csv')
appId = "MioTech"
assetTagCategoryName = "AssetTagCategoryName_Just_For_GSY_Test"+str(random.randint(0,1000))
GlobalAssetTagCategoryId = 0
assetTagCategoryNameEdited = 'AssetTagCategoryName_Just_For_GSY_Test_Edited'+str(random.randint(0,1000))

data1 = (
    ({"appId": appId, "assetTagCategoryName":assetTagCategoryName},True),
)

data2 = (
    ({'appId': appId}, True),
)

data3 = (
    ({'appId':appId, 'assetTagCategoryId':GlobalAssetTagCategoryId, 'assetTagCategoryName':assetTagCategoryNameEdited}, True),
)

data4 = (
    ({'appId':appId}, True),
)

data5 = (
    ({
      "appId": "MioTech",
      "assetTagCategoryId": GlobalAssetTagCategoryId
    }, True),
)
data6 = (
    ({'appId':'MioTech'},True),
)
conf = globalconfig().get('grpc').get('fi')
stub = build_rpc_client(host=conf.get('host'), port=conf.get('port'), stub = FinancialInstrumentServiceStub)
#========================================

class test_financial_instrument_Asset_Tag_Category(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @dataProvider(data1)
    def test_1_addAssetTagCategory(self,input, expected):
        real = stub.addAssetTagCategory(AddAssetTagCategoryRequest(**input))
        global GlobalAssetTagCategoryId
        GlobalAssetTagCategoryId = real.assetTagCategoryId
        self.assertEqual(real.success, expected)


    @dataProvider(data2)
    def test_2_retrieveAllAssetTag(self, input ,expected):
        real = stub.retrieveAllAssetTag(RetrieveAllAssetTagRequest(**input))
        self.assertEqual(real.success, expected)

    def test_3_editAssetTagCategory(self):
        data= {'appId': appId, 'assetTagCategoryId': GlobalAssetTagCategoryId,
         'assetTagCategoryName': assetTagCategoryNameEdited}
        real = stub.editAssetTagCategory(EditAssetTagCategoryRequest(**data))
        self.assertEqual(real.success, True)

    @dataProvider(data4)
    def test_4_retrieveAllAssetTag(self,input, expected):
        real = stub.retrieveAllAssetTag(RetrieveAllAssetTagRequest(**input))
        self.assertEqual(real.success, expected)

    def test_5_removeAssetTagCategory(self):
        input = {
              "appId": "MioTech",
              "assetTagCategoryId": GlobalAssetTagCategoryId
        }
        real = stub.removeAssetTagCategory(RemoveAssetTagCategoryRequest(**input))
        self.assertTrue(real.success)

    @dataProvider(data6)
    def test_6_retrieveAllAssetTag(self, input, expected):
        real = stub.retrieveAllAssetTag(RetrieveAllAssetTagRequest(**input))
        self.assertTrue(real.success)

    @classmethod
    def tearDownClass(cls):
        tearDownData = {'appId': appId, 'assetTagCategoryId': GlobalAssetTagCategoryId}
        stub.removeAssetTagCategory(RemoveAssetTagCategoryRequest(**tearDownData))
