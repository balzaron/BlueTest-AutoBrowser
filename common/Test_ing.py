import unittest

from common.decos import dataProvider
from common.utils import get_csv_data
data = get_csv_data('grpcdata.csv')

add = lambda a,b: a+b
toBool = lambda x:bool(x)


class Test_ing(unittest.TestCase):

    def test_2(self):
        print(toBool(2))

    @dataProvider(data)
    def testing(self, input, expected, assertion, function):
        eval('self.%s(%s(**input))'%(assertion))
