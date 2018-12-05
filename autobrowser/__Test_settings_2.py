# author: shanyue.gao
# datetime:2018/11/8 5:38 PM

import time
import unittest, os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.case_template import BrowserCase
from common.config_center import IDsConfig, minus
from common.utils import get_current_function_name
from common.log import miologging,errPath

# ===========common variables=================
IDs = IDsConfig()
logger = miologging()
png = '.png'

# ===========local variables==================
settings_page = 'https://release.miotech.com/super-admin/users/3292?from=https%3A%2F%2Frelease.miotech.com%2Fami'
change_password_section = 'https://release.miotech.com/super-admin/users/7?from=https%3A%2F%2Frelease.miotech.com%2Fcrm%2Fdetails%2F3284%3Ft%3Dbilling&section=accountSecurity'
innerSwitchCss = 'span[class="mio-switch-inner"]'
OFF = 'OFF'
ON = 'ON'
switchRevertURL = 'https://release.miotech.com/api/permission/user-app-edit'
enableAppsURL= 'https://release.miotech.com/super-admin/users/3292?from=https%3A%2F%2Frelease.miotech.com%2Fhome&section=enabledApps'


# minus test cases
class Test_settings_minus(unittest.TestCase, BrowserCase):

    @classmethod
    def setUpClass(cls):
        cls.browser.get(settings_page)
        # cls.browser.find_element_by_tag_name("html").send_keys(Keys.chord(Keys.COMMAND, Keys.ADD))


    def setUp(self):

        try:
            self.settingsConf:dict = IDs.get('super admin')
            self.browser.get(settings_page)
        except Exception as e:
            self.browser.save_screenshot(errPath+get_current_function_name()+'.png')
            logger.error(e)

    def test_sys_prefernces(self):

        # try:
        self.is_visible(self.settingsConf.get('System Preferences menu item'))
        self.browser.find_element_by_id(self.settingsConf.get('System Preferences menu item')).click()
        self.is_visible(self.settingsConf.get('System Preferences edit item'))
        self.browser.find_element_by_id(self.settingsConf.get('System Preferences edit item')).click()
        currencySelection = self.browser.find_element_by_id(self.settingsConf.get('System Preferences currency selection'))

        # select AUD currency.
        currencySelection.click()
        # currencySelection.send_keys(Keys.DOWN)
        # currencySelection.send_keys(Keys.RETURN)

        languageSelection = self.browser.find_element_by_id(self.settingsConf.get('System Preferences language selection'))

        # select Chinese option
        languageSelection.click()
        # languageSelection.send_keys(Keys.DOWN)
        # languageSelection.send_keys(Keys.DOWN)
        # languageSelection.send_keys(Keys.RETURN)

        self.is_visible(self.settingsConf.get('System Preferences update button'))
        self.browser.find_element_by_id(self.settingsConf.get('System Preferences update button')).click()
        self.request.post('https://release.miotech.com/api/user/preference/save',
                          {"currency": "AUD", "language": "zh-CN"})
        self.browser.refresh()

        # assertion
        text = self.browser.find_element_by_id(self.settingsConf.get('System Preferences edit item')).text
        print(text)
        self.assertEqual(text, "编辑")

    def test_enable_crm_apps(self):
        crmBar = self.settingsConf.get('Enabled apps Portx crm bar')
        crmAmdinSwitch = self.settingsConf.get('Portx crm admin switch')
        crmUserSwitch = self.settingsConf.get('Portx crm user switch')

        self.browser.get(enableAppsURL)
        # try:
        # click crm admin switch and assert status
        self.find_element_by_id(crmBar).click()

        switchAdmin = self.find_element_by_id(crmAmdinSwitch)
        switchAdmin.click()
        time.sleep(1)
        off = switchAdmin.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(off, OFF, 'click crm admin switch and assert status')

        # click crm user switch and assert status
        switchUser = self.find_element_by_id(crmUserSwitch)
        switchUser.click()
        time.sleep(1)
        off = switchUser.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(off, OFF, 'click crm user switch and assert status')

        # revert the status and assert
        switchUser.click()
        time.sleep(1)
        on = switchUser.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(on, ON, 'revert the status and assert')
        switchAdmin.click()
        time.sleep(1)
        on = switchAdmin.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(on, ON, 'revert the status and assert')

    def test_enable_portx_portfolio_app(self):
        portfolioBar = self.settingsConf.get('Portx portfolio bar')
        portfolioSwitch = self.settingsConf.get('Protx portfolio dashboard user switch')
        self.browser.get(enableAppsURL)
        # try:
        # portx portfolio check
        self.is_visible(portfolioBar)
        self.browser.find_element_by_id(portfolioBar).click()
        self.is_visible(portfolioSwitch)
        switch = self.browser.find_element_by_id(portfolioSwitch)
        switch.click()
        time.sleep(1)
        off = switch.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(off, OFF, 'portx portfolio check should be off')

        switch.click()
        time.sleep(1)
        on = switch.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(on, ON, 'portx portfolio check should be on')

    def test_enable_ami_app(self):
        amiBar = self.settingsConf.get('Ami bar')
        amiUserSwitch = self.settingsConf.get('Ami user switch')

        self.browser.get(enableAppsURL)
        self.find_element_by_id(amiBar).click()
        switch = self.find_element_by_id(amiUserSwitch)
        switch.click()
        time.sleep(1)
        off = switch.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(off, OFF)



    def test_enable_transaction_app(self):
        transactionBar = self.settingsConf.get('PortX - Transaction bar')
        adminSwitch = self.settingsConf.get('transaction admin switch')
        userSwitch = self.settingsConf.get('transaction user switch')
        omsSwitch= self.settingsConf.get('oms execution team')

        self.browser.get(enableAppsURL)

        # transaction admin assert
        self.find_element_by_id(transactionBar).click()
        switch = self.find_element_by_id(adminSwitch)
        switch.click()
        time.sleep(1)


        off = switch.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(off, OFF, 'transaction admin assert')


        # transaction user assert
        switch = self.find_element_by_id(userSwitch)
        switch.click()
        time.sleep(1)
        off = switch.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(off, OFF, 'transaction user assert')

        # transaction oms assert

        switch = self.find_element_by_id(omsSwitch)
        switch.click()
        time.sleep(1)
        off = switch.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(off, OFF, 'transaction omsSwitch assert')

    def test_enable_workflow_app(self):
        workflowBar = self.settingsConf.get('workflow bar')
        adminSwitch = self.settingsConf.get('workflow admin switch')
        userSwitch = self.settingsConf.get('workflow internal switch')
        clientSwitch= self.settingsConf.get('workflow client switch')

        self.browser.get(enableAppsURL)

        # workflow admin assert
        self.find_element_by_id(workflowBar).click()

        switch = self.find_element_by_id(adminSwitch)
        switch.click()
        time.sleep(1)
        off = switch.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(off, OFF, 'workflow admin assert')

        # workflow internal assert
        switch = self.find_element_by_id(userSwitch)
        switch.click()
        time.sleep(1)
        off = switch.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(off, OFF, 'workflow internal assert')

        # transaction oms assert
        switch = self.find_element_by_id(clientSwitch)
        switch.click()
        time.sleep(1)
        off = switch.find_element_by_css_selector(innerSwitchCss).text
        self.assertEqual(off, OFF, 'transaction omsSwitch assert')

    @classmethod
    def tearDownClass(cls):
        cls.request.post('https://release.miotech.com/api/user/preference/save', {"currency":"USD","language":"en-US"})
        cls.request.post(switchRevertURL,{"appDetailIds":[8,9,63,64,65],"userId":"3292","value":True})
        cls.request.post(switchRevertURL, {"appDetailIds":[10,11,12,13,14,15,16,17],"userId":"3292","value":True})
        cls.request.post(switchRevertURL, {"appDetailIds":[18,19,20,45,66],"userId":"3292","value":True})
        cls.request.post(switchRevertURL, {"appDetailIds":[24,69],"userId":"3292","value":True})
        cls.request.post(switchRevertURL, {"appDetailIds":[38,39,40],"userId":"3292","value":True})
        cls.request.post(switchRevertURL, {"appDetailIds":[41,42,43,44,62],"userId":"3292","value":True})
        cls.request.post(switchRevertURL, {"appDetailIds":[58,59],"userId":"3292","value":True})
        cls.request.post(switchRevertURL, {"appDetailIds":[28,29,30],"userId":"3292","value":True})
        cls.request.post(switchRevertURL, {"appDetailIds":[31,32],"userId":"3292","value":True})
        cls.request.post(switchRevertURL, {"appDetailIds":[33],"userId":"3292","value":True})
        cls.browser.close()


@unittest.skipIf(minus, 'minus')
class Test_settings(unittest.TestCase,BrowserCase):

    def setUp(self):
        pass

    def test_sys_preferences(self):
        pass