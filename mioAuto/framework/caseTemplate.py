import os
import time
from unittest import TestCase

from mioAuto.common.buildBrowser import buildBrowser
from mioAuto.model.BrowserObj import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from mioAuto import imagePathPrefix
from mioAuto.common.utils import get_current_function_name
from mioAuto.log import logger
from mioAuto.expection.Expections import ElementNotFoundException, NotSupportObjYetExpection
from mioAuto.model.StepObj import *

minus = bool(os.environ.get('minus'))
wait = 0.8

class BrowserCase(object):

    def isVisible(self, browser:WebDriver,  by='ID', e:str='', timeout=10, scanStep=0.5):
        locator = (eval('By.'+by), e)
        try:
            WebDriverWait(browser, timeout, scanStep).until(EC.visibility_of_element_located(locator))
            time.sleep(wait)
            return True
        except Exception as ec:
            logger.error(ec)
            pass

    def isNotVisible(self,browser:WebDriver, e, by='ID', timeout=10, scanStep=0.5):
        WebDriverWait(browser, timeout, scanStep).until_not(EC.visibility_of_element_located((eval('By.'+by), e)))
        time.sleep(wait)
        return True

    def scrollToTarget(self,browser:WebDriver,by='ID', target:str=''):
        if browser!=None and target != '':
            target = browser.find_element(eval('By.'+by),target)
            # browser.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", target)
            browser.execute_script("arguments[0].scrollIntoView();", target)

        else:
            raise ElementNotFoundException(target)

    def findElement(self, browser:WebDriver,  e:str='', by:str='id'):
        by = by.upper()
        if self.isVisible(browser, by=by, e = e):
            self.scrollToTarget(browser,by=by, target=e)
            return browser.find_element(eval('By.'+by), e)
        else:
            raise ElementNotFoundException(e)

    def saveImage(self, browser: WebDriver, fileName:str):
        folder = imagePathPrefix + self.__class__.__name__
        browser.save_screenshot(fileName)

    def __assertion(self, expected):
        """
        :param expected: expected output maybe restful response or element attribute.
        :return: boolean true or false
        """
        if expected != 'skip':
            if isinstance(expected, BrowserExpectedResult):
                statement = 'self.assertEqual(self.findElement(self.browser, by=expected.by, e=expected.element).{}, expected.result)'
                eval(statement.format(expected.event))
            elif isinstance(expected, RestExpectedResult):
                statement = 'self.assertEqual({})'
            else:
                raise NotSupportObjYetExpection(expected)

    def doStep(self,browser:WebDriver, input, expected):
        """
        :param browser:
        :param input:
        :param expected:
        :return:
        """

        if isinstance(input, BrowserStep):
            e = self.findElement(browser, by=input.by, e=input.element)
            eval('e.'+input.event)
            self.__assertion(expected)

        elif isinstance(input, RestStep):
            statement = 'self.request.{}(\"{}\", {})'
            result:dict = eval(statement.format(input.method, input.path, input.parameter))
            browser.refresh()
            self.__assertion(expected)



# class BrowserCase2(TestCase):
#
#     def buildBrowser(self, bi:Browser):
#         return buildBrowser(bi)
#
#     def isVisible(self, browser:WebDriver,  by='ID', e:str='', timeout=10, scanStep=0.5):
#         locator = (eval('By.'+by), e)
#         try:
#             WebDriverWait(browser, timeout, scanStep).until(EC.visibility_of_element_located(locator))
#             time.sleep(wait)
#             return True
#         except Exception as ec:
#             logger.error(ec)
#             pass
#
#     def isNotVisible(self,browser:WebDriver, e, by='ID', timeout=10, scanStep=0.5):
#         WebDriverWait(browser, timeout, scanStep).until_not(EC.visibility_of_element_located((eval('By.'+by), e)))
#         time.sleep(wait)
#         return True
#
#     def scrollToTarget(self,browser:WebDriver,by='ID', target:str=''):
#         if browser!=None and target != '':
#             target = browser.find_element(eval('By.'+by),target)
#             # browser.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", target)
#             browser.execute_script("arguments[0].scrollIntoView();", target)
#
#         else:
#             raise ElementNotFoundException(target)
#
#     def findElement(self, browser:WebDriver,  e:str='', by:str='id'):
#         by = by.upper()
#         if self.isVisible(browser, by=by, e = e):
#             self.scrollToTarget(browser,by=by, target=e)
#             return browser.find_element(eval('By.'+by), e)
#         else:
#             raise ElementNotFoundException(e)
#
#     def saveImage(self, browser: WebDriver, fileName:str):
#         folder = imagePathPrefix + self.__class__.__name__
#         browser.save_screenshot(fileName)
#
#     def case(self,browser:WebDriver, input, expected):
#         if isinstance(input, BrowserStep):
#             e = self.findElement(browser, by=input.by, e=input.element)
#             eval('e.'+input.event)
#             if expected != 'skip':
#                 self.assertEqual(self.findElement(browser, by=expected[0], e=expected[1]).text, expected[2])
