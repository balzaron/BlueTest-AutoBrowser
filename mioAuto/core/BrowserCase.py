import os
import time
import re

from selenium.webdriver.common.keys import Keys
from mioAuto.config import getConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from mioAuto import imagePathPrefix
from mioAuto.log import logger
from mioAuto.expection.Expections import ElementNotFoundException, NotSupportObjYetExpection
from mioAuto.model.StepModel import *

minus = bool(os.environ.get('minus'))
param = getConfig().get('timeparameters')
wait = param.get('commonwait')
browserParam = param.get('browser')
timeout = browserParam.get('timeout')
scan = browserParam.get('scanStep')

class BrowserCase(object):

    def isVisible(self, browser:WebDriver,  by='ID', e:str='', timeout=timeout, scanStep=scan):
        if ':' in e:
            e = e.split(':')[0]
        locator = (eval('By.' + by.upper()), e)
        try:
            WebDriverWait(browser, timeout, scanStep).until(EC.visibility_of_element_located(locator))
            time.sleep(wait)
            return True
        except Exception as ec:
            # logger.error(ec)
            return False

    def isNotVisible(self,browser:WebDriver, e, by='ID', timeout=timeout, scanStep=scan):
        WebDriverWait(browser, timeout, scanStep).until_not(EC.visibility_of_element_located((eval('By.'+by), e)))
        time.sleep(wait)
        return True

    def scrollToTarget(self,browser:WebDriver,by='ID', e:str=''):
        if browser!=None and e != '':
            if ':' in e :
                e = e.split(':')[0]
            e = browser.find_element(eval('By.'+by),e)
            # browser.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", target)
            browser.execute_script("arguments[0].scrollIntoView();", e)

        else:
            raise ElementNotFoundException(e)

    def findElement(self, browser:WebDriver,  e:str='', by:str='id'):
        by = by.upper()
        if self.isVisible(browser, by=by, e = e):
        # if True:
            self.scrollToTarget(browser,by=by, e=e)
            return browser.find_element(eval('By.'+by), e)
        else:
            raise ElementNotFoundException(e)

    def saveImage(self, browser: WebDriver, fileName:str):
        folder = imagePathPrefix + self.__class__.__name__
        imgName = folder + fileName+'.png'
        # if os.path.exists(imgName)
        browser.save_screenshot()

    def __assertEqual(self, res, exp, reason:str=''):
        statement = 'self.assertEqual({res}, {exp}, \'{reason}\')'
        if res is not None and exp is not None:
            eval(statement.format(res=res, exp=exp, reason=reason))
            # assert res == exp
        else:
            raise AttributeError(str(res), str(exp))

    def __assert(self, res, exp=None, assertType:str='', reason:str=''):
        if isinstance(res, str):
            # statement1 = ''
            if isinstance(exp, str):
                statement1 = 'self.assert{type}(\'{res}\', \'{exp}\', \'{reason}\')'
            else:
                statement1 = 'self.assert{type}(\'{res}\', {exp}, \'{reason}\')'
            statement2 = 'self.assert{type}(\'{res}\', \'{reason}\')'
        else:
            statement1 = 'self.assert{type}({res}, {exp}, \'{reason}\')'
            statement2 = 'self.assert{type}({res}, \'{reason}\')'
        statement:str = ''

        if assertType in ('Equal', 'NotEqual', 'Greater', 'GreaterEqual',
                          'Less', 'LessEqual', 'AlmostEqual', 'NotAlmostEqual',
                          'In', 'NotIn'):
            statement = statement1.format(type=assertType, res=res, exp=exp, reason=reason)
        elif assertType in ('IsNone', 'IsNotNone', 'True', 'False'):
            statement = statement2.format(type = assertType, res=res, reason=reason)
        elif assertType is None:
            pass
        else:
            raise NotSupportObjYetExpection(assertType)

        eval(statement)

    def __assertion(self, expected, driver='browser'):
        """
        :param expected: expected output maybe restful response or element attribute.
        :return: boolean true or false
        """

        if expected not in ('skip', '', None):

            if isinstance(expected, BrowserExpectedResult):
                if not isinstance(expected.result, BrowserExpectedResult):

                    statement = 'self.findElement(self.{}, by=expected.by, e=expected.element).{}'
                    res = eval(statement.format(driver, expected.event))
                    assertType = expected.assertType
                    if isinstance(expected.result, int):
                        self.__assert(int(res.replace(',','')), int(expected.result), assertType)
            elif isinstance(expected, RestExpectedResult):
                pass
            elif isinstance(expected, RestFieldExpectedResult):
                statement = 'self.request.{}(\"{}\", {}).data.json()'.format(expected.method, expected.path, expected.parameter)
                tmp = eval(statement)
                res = self.__getValue(tmp, expected.valuePath)
                self.__assert(res=res,exp=expected.result, assertType=expected.assertType)
            else:
                raise NotSupportObjYetExpection(expected)

    def __getValue(self,obj:dict, vp:str, separator='|') -> object:
        layers:list = vp.split(separator)
        tmp = obj
        for i in layers:
            if isinstance(tmp, list):
                tmp = tmp[int(i)]
            elif isinstance(tmp, dict):
                tmp = tmp.get(i.strip())
        return tmp

    def doStep(self,browser:WebDriver, input, expected):
        """
        :param browser:
        :param input:
        :param expected:
        :return:
        """

        inputType, expType = None, None
        by, element, event = None, None, None
        method, path, parameter = None, None, None
        _expected = None
        #=========driverName 'None' should replaced by reflect name=====
        driverName = None or 'browser'
        #/========but i dont know how to change this reflect=====
        nulls = (None, 'skip', '')

        if input not in nulls:
            try:
                inputType = input.type
            except:
                inputType = input.get('type')
        else:
            self.__assertion(expected, driverName)

        if expected not in nulls:
            try:
                expType = expected.type
            except:
                expType = expected.get('type')
        else:
            pass

        if inputType == "BrowserStep":
            try:
                by, element, event = \
                    input.by, input.element, input.event
                _expected = expected
            except:
                by, element, event = \
                    input.get('by'), input.get('element'), input.get('event')
                _expected = expected.get('expected')

            e = self.findElement(browser, by=by, e=element)
            eval('e.'+event)

            self.__assertion(_expected, driverName)

        elif inputType == "RestStep" :
            try:
                method, path, parameter = \
                    input.method, input.path, input.parameter
                _expected = expected

            except:
                method, path, parameter = \
                    input.get('method'), input.get('path'), input.get('parameter')
                _expected = expected.get('expected')

            if expType == "BrowserExpectedResult":

                statement = 'self.request.{}(\"{}\", {})'
                result:dict = eval(statement.format(method, path, parameter))
                browser.refresh()
                self.__assertion(expected, driverName)

            elif expType == "RestExpectedResult":

                pass

            else:
                browser.refresh()
                time.sleep(10)




        elif inputType == "BrowserElementValue":

            try:
                by, element, position = \
                    input.by, input.element, input.position
            except:
                by, element, position = \
                    input.get('by'), input.get('element'), input.get('position')

            if expType == 'BrowserElementValue':


                ei = self.findElement(browser, by=by, e=element)
                vi = eval('ei.'+ position)

                ee = self.findElement(browser, by=by, e=element)
                ve = eval('ee.' + position)
                self.__assertEqual(vi, ve)

        elif inputType == 'RestField':

            mi, pi, parami, \
            mo, po, paramo, ato = \
                None, None, None, None, None, None, None
            try:
                mi, pi, parami, vpi = \
                    input.method, input.path, input.parameter, input.valuePath

            except:
                mi, pi, parami, vpi = \
                    input.get('method'), input.get('path'), input.get('parameter'), input.get('valuePath')
            try:
                mo, po, paramo, vpo, ato = \
                    expected.method, expected.path, expected.parameter, expected.valuePath, expected.assertType

            except:
                mo, po, paramo, vpo, ato = \
                    expected.get('method'), expected.get('path'), expected.get('parameter'), expected.get('valuePath'), \
                    expected.get('assertType')

            if expType == 'RestField':

                statement = 'self.request.{}(\"{}\", {})'
                ri:dict = eval(statement.format(mi, pi, parami))
                ro:dict = eval(statement.format(mo, po, paramo))
                f1 = self.__getValue(ri, vpi)
                f2 = self.__getValue(ro, vpo)
                self.__assert(f1, f2, ato)




