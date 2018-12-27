import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from mioAuto.expection.Expections import ElementNotFoundException

minus = bool(os.environ.get('minus'))

class BrowserCase(object):

    def isVisible(self, browser:WebDriver, locator:str, by='ID', timeout=10):

        ui.WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((eval('By.'+by), locator)))
        time.sleep(0.5)
        return True

    def isNotVisible(self,browser:WebDriver, locator, by='ID', timeout=10):
        ui.WebDriverWait(browser, timeout).until_not(EC.visibility_of_element_located((eval('By.'+by), locator)))
        time.sleep(0.5)
        return True

    def scrollToTarget(self,browser:WebDriver, target:str):
        target = browser.find_element_by_id(target)
        browser.execute_script("arguments[0].scrollIntoView();", target)

    def find_element_by_id(self,browser:WebDriver, id:str):
        if self.isVisible(browser, id):
            self.scrollToTarget(browser, target=id)
            return browser.find_element_by_id(id)
        else:
            raise ElementNotFoundException()

    def find_element(self,browser:WebDriver, by:str, e:str):
        by = by.upper()
        if self.isVisible(browser, e):
            self.scrollToTarget(browser,target=e)
            return browser.find_element(eval('By.'+by), e)
        else:
            raise ElementNotFoundException()

# browserInfo = Browser()
# browserInfo.type='chrome'
# browserInfo.cookie = 'no'
# browserInfo.initPage='https://www.baidu.com/'
# browserInfo.driverPath='/Users/miotech/opt/chromedriver'
#
# class bc(BrowserCase, TestCase):
#     browser = buildBrowser(browserInfo)
#
#
#     def testM1(self):
#         # self.browser.find_element_by_id('kw').send_keys('hello')
#         # self.browser.find_element_by_id('su').click()
#         self.find_element(self.browser, 'id', 'kw').send_keys('hello')
#         self.find_element(self.browser, 'id', 'su').click()