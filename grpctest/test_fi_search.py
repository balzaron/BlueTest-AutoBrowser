# author: shanyue.gao
# datetime:2018/12/3 4:39 PM

import random
import time
from unittest import TestCase, skip

from common.build_rpc_client import build_rpc_client
from common.config_center import globalconfig
from common.decos import dataProvider, timeConsumer
from common.utils import grpcObject2dict
from grpctest.generated.dmp_pb2 import *
from grpctest.generated.financial_instrument_service_pb2_grpc import FinancialInstrumentServiceStub

conf = globalconfig().get('grpc').get('fi')
stub = build_rpc_client(host=conf.get('host'), port=conf.get('port'), stub=FinancialInstrumentServiceStub)


#==========data prepare==================
dataSearchABC = (
    ({"searchString":"aapl","userId":"MioTech","bankAccount":["1063","1062","590","592","750","596","752","598","510","632","1057","512","634","756","514","636","758","518","640","520","642","522","644","1067","766","646","768","526","648","528","492","650","772","530","774","532","654","778","536","658","780","660","782","540","662","784","542","940","786","544","666","700","546","668","702","548","704","706","708","790","670","550","672","794","552","674","554","676","556","712","558","714","716","718","680","560","682","684","564","1301","686","720","566","688","600","722","568","602","724","1309","606","728","608","1165","1164","1163","1162","1161","1160","690","692","572","694","574","696","730","576","1311","698","610","1310","732","578","612","734","614","736","738","618","1055","580","582","584","740","586","620","742","588","622","744","624","746","504","626","748","506"]}, True),
)
dataSearchNull =(
    ({"userId":"MioTech","bankAccount":["1063","1062","590","592","750","596","752","598","510","632","1057","512","634","756","514","636","758","518","640","520","642","522","644","1067","766","646","768","526","648","528","492","650","772","530","774","532","654","778","536","658","780","660","782","540","662","784","542","940","786","544","666","700","546","668","702","548","704","706","708","790","670","550","672","794","552","674","554","676","556","712","558","714","716","718","680","560","682","684","564","1301","686","720","566","688","600","722","568","602","724","1309","606","728","608","1165","1164","1163","1162","1161","1160","690","692","572","694","574","696","730","576","1311","698","610","1310","732","578","612","734","614","736","738","618","1055","580","582","584","740","586","620","742","588","622","744","624","746","504","626","748","506"],"hasAssetAliasId":True}, True),
)

dataSearchAAPL = (
    ({"searchString":"AAPL","userId":"MioTech","bankAccount":["1063","1062","590","592","750","596","752","598","510","632","1057","512","634","756","514","636","758","518","640","520","642","522","644","1067","766","646","768","526","648","528","492","650","772","530","774","532","654","778","536","658","780","660","782","540","662","784","542","940","786","544","666","700","546","668","702","548","704","706","708","790","670","550","672","794","552","674","554","676","556","712","558","714","716","718","680","560","682","684","564","1301","686","720","566","688","600","722","568","602","724","1309","606","728","608","1165","1164","1163","1162","1161","1160","690","692","572","694","574","696","730","576","1311","698","610","1310","732","578","612","734","614","736","738","618","1055","580","582","584","740","586","620","742","588","622","744","624","746","504","626","748","506"]}, True),
    ({"searchString":"AAPL","assetType":"EQUITY","userId":"MioTech","bankAccount":["1063","1062","590","592","750","596","752","598","510","632","1057","512","634","756","514","636","758","518","640","520","642","522","644","1067","766","646","768","526","648","528","492","650","772","530","774","532","654","778","536","658","780","660","782","540","662","784","542","940","786","544","666","700","546","668","702","548","704","706","708","790","670","550","672","794","552","674","554","676","556","712","558","714","716","718","680","560","682","684","564","1301","686","720","566","688","600","722","568","602","724","1309","606","728","608","1165","1164","1163","1162","1161","1160","690","692","572","694","574","696","730","576","1311","698","610","1310","732","578","612","734","614","736","738","618","1055","580","582","584","740","586","620","742","588","622","744","624","746","504","626","748","506"]},True),
    ({"searchString":"AAPL","assetType":"EQUITY","userId":"MioTech","bankAccount":["1063","1062","590","592","750","596","752","598","510","632","1057","512","634","756","514","636","758","518","640","520","642","522","644","1067","766","646","768","526","648","528","492","650","772","530","774","532","654","778","536","658","780","660","782","540","662","784","542","940","786","544","666","700","546","668","702","548","704","706","708","790","670","550","672","794","552","674","554","676","556","712","558","714","716","718","680","560","682","684","564","1301","686","720","566","688","600","722","568","602","724","1309","606","728","608","1165","1164","1163","1162","1161","1160","690","692","572","694","574","696","730","576","1311","698","610","1310","732","578","612","734","614","736","738","618","1055","580","582","584","740","586","620","742","588","622","744","624","746","504","626","748","506"],"productType":"USER_PRDT","hasAssetAliasId":True},True),
)

dataSearchEmpty = (
    ({"userId":"MioTech","bankAccount":["1063","1062","590","592","750","596","752","598","510","632","1057","512","634","756","514","636","758","518","640","520","642","522","644","1067","766","646","768","526","648","528","492","650","772","530","774","532","654","778","536","658","780","660","782","540","662","784","542","940","786","544","666","700","546","668","702","548","704","706","708","790","670","550","672","794","552","674","554","676","556","712","558","714","716","718","680","560","682","684","564","1301","686","720","566","688","600","722","568","602","724","1309","606","728","608","1165","1164","1163","1162","1161","1160","690","692","572","694","574","696","730","576","1311","698","610","1310","732","578","612","734","614","736","738","618","1055","580","582","584","740","586","620","742","588","622","744","624","746","504","626","748","506"]}, True),
)
#========================================


class test_fi_search(TestCase):

    # @skip('config is not ready')
    @timeConsumer(6000)
    @dataProvider(dataSearchABC)
    def test_1_searchABC(self, input, expected):
        real = stub.search(SearchRequest(**input))
        print(grpcObject2dict(real))
        self.assertIsNotNone(real)

    @timeConsumer(6000)
    @dataProvider(dataSearchNull)
    def test_2_searchNull(self, input, expected):
        real = stub.search(SearchRequest(**input))
        print(real)
        self.assertIsNotNone(real)

    @skip('config is not ready')
    @timeConsumer(6000)
    @dataProvider(dataSearchAAPL)
    def test_3_searchABC(self, input, expected):
        real = stub.search(SearchRequest(**input))
        print(real)
        self.assertIsNotNone(real)

    @timeConsumer(6000)
    @dataProvider(dataSearchEmpty)
    def test_4_searchEmpty(self, input, expected):
        real = stub.search(SearchRequest(**input))
        print(real)
        self.assertIsNotNone(real)


