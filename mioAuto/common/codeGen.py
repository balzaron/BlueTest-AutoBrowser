import os
from collections import OrderedDict

CODE_TEMPLATE_AUTO_BROWSER =  \
"""
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.case_template import Case
from common.utils import get_current_function_name
from common.config_center import IDsConfig, minus
from common.log import logger

IDs = IDsConfig()

# minus regression test cases of {CLASS_NAME}
class {CLASS_NAME}_minus(unittest.TestCase, Case):

    def setUp(self):
        self.browser.get({PRECONDITION_URL})
    
   
    
    def tearDown(self):
        self.browser.close()
    
    
# full regression without minus cases of {CLASS_NAME}
@unittest.skipIf(minus, 'minus')
class {CLASS_NAME}(unittest.TestCase, Case):

    def setUp(self):
        self.browser.get({PRECONDITION_URL})
    
    
    
    def tearDown(self):
        self.browser.close()
"""


CASE_TEMPLATE = \
"""
def test_{FUNC}(self):
    self.browser.find_element(
"""

obj = {'CLASS_NAME': 'hi',
       'PRECONDITION_URL' : 'test'}

def code_gen(filename):
    if not os.path.exists(filename):

        with open(filename, 'w') as f:
            f.writelines(CODE_TEMPLATE_AUTO_BROWSER.format(**obj))

