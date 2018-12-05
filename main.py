from common.UserEntity import User
from common.request import Request

import  BlueTest

# with open('./srcdata/test.json.postman_collection', 'r') as f:
#     print(f.readlines())

BlueTest.initPostMan("test")
BlueTest.testByCsvData("test",mkpy=True)