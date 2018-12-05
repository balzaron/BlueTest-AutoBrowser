# author: shanyue.gao
# datetime:2018/11/8 5:38 PM

# import time
# import unittest, os
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from common.case_template import BrowserCase
# from common.config_center import IDsConfig, minus
# from common.utils import get_current_function_name
# from common.log import miologging,errPath
#
# # ===========common variables=================
# IDs = IDsConfig()
# logger = miologging()
# png = '.png'
#
# # ===========local variables==================
# settings_page = 'https://release.miotech.com/super-admin/users/3292?from=https%3A%2F%2Frelease.miotech.com%2Fami'
# change_password_section = 'https://release.miotech.com/super-admin/users/7?from=https%3A%2F%2Frelease.miotech.com%2Fcrm%2Fdetails%2F3284%3Ft%3Dbilling&section=accountSecurity'
# innerSwitchCss = 'span[class="mio-switch-inner"]'
# OFF = 'OFF'
# ON = 'ON'
# switchRevertURL = 'https://release.miotech.com/api/permission/user-app-edit'
# enableAppsURL= 'https://release.miotech.com/super-admin/users/3292?from=https%3A%2F%2Frelease.miotech.com%2Fhome&section=enabledApps'
#

# minus test cases
from unittest import TestCase


class Test_settings_minus(TestCase):



    def test_sys_prefernces(self):
        """
        System Preferences
        """
        self.assertTrue(True)


    def test_enable_crm_apps(self):
       """
       crm enable
       """
       self.assertTrue(True)

    def test_enable_portx_portfolio_app(self):
        """
        portfolio enable
        """
        self.assertTrue(True)

    def test_enable_ami_app(self):
        """
        ami enable
        """

        self.assertTrue(True)


    def test_enable_transaction_app(self):

        """
        transaction enable
        """
        self.assertTrue(True)