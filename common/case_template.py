import os
import time
from unittest import TestCase

from selenium.webdriver.common.by import By
from common.config_center import globalconfig
from common.request import Request
from common.build_browser import build_a_browser
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from common.build_rpc_client import build_rpc_client

user = globalconfig().get('userInfo')
minus = bool(os.environ.get('minus')) or bool(globalconfig().get('minus'))
conf = globalconfig()

class BrowserCase(object):
    browser = build_a_browser('chrome')
    request = Request()

    # def __init__(self):
    browser.get(user['login_url'])
    # browser.maximize_window()

    browser.add_cookie({
        'name': 'MIOYING_SESSION',
        'value': user.get('cookie'),
    })
    browser.implicitly_wait(conf.get('wait'))


    def is_visible(self, locator, timeout=10):
        try:
            ui.WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
            time.sleep(0.5)
            return True
        except Exception as e:
            raise e

    def is_not_visible(self, locator, timeout=10):
        try:
            ui.WebDriverWait(self.browser, timeout).until_not(EC.visibility_of_element_located((By.ID, locator)))
            time.sleep(0.5)
            return True
        except Exception as e:
            raise e
    # def __del__(self):
    #     self.browser.close()

    def scroll_to_target(self, target:str):
        target = self.browser.find_element_by_id(target)
        self.browser.execute_script("arguments[0].scrollIntoView();", target)

    def find_element_by_id(self, id:str):
        if self.is_visible(id):
            self.scroll_to_target(target=id)
            return self.browser.find_element_by_id(id)


