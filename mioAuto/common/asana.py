from unittest import TestCase


class parent(object):
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def printer(self):
        print(self.a, self.b)


class son(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.setuper()

    @classmethod
    def tearDownClass(cls):
        cls.destroyer()

    def destroyer(self):
        print('destroyer')
    def setuper(self):
        print('setup')

    def printer2(self):
        print('printer2')


class test_c(son):

    def test_a(self):
        print('hi')
        self.assertEqual('a', 'b')
