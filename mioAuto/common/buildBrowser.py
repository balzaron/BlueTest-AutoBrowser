# from mioAuto.common.config_center import globalconfig
# from cases.resource import CHROME_DRIVER_PATH,FIREFOX_DRIVER_PATH
import logging

from selenium import webdriver
from mioAuto.expection.Expections import NotSupportBrowserException
from mioAuto.model.BrowserObj import Browser

logger = logging.getLogger(__name__)

def buildBrowser(browserInfo:Browser):
    browser = None
    if browserInfo.type.lower() == 'chrome':
        try:
            browser = webdriver.Chrome(browserInfo.driverPath)
        except FileExistsError as e:
            logger.error(e)

    elif browser.type.lower() == 'firefox':
        try:
            browser = webdriver.Firefox(executable_path=browserInfo.driverPath)
        except FileExistsError as e:
            logger.error(e)

    elif browser.type.lower() == 'ie':
        try:
            browser = webdriver.Ie(browserInfo.driverPath)
        except FileExistsError as e:
            logger.error(e)
    else:
        logger.error("browser type of {} is not support now".format(browserInfo.type))
        raise NotSupportBrowserException(browser.type)

    # browser.add_cookie({
    #     'name': 'MIOYING_SESSION',
    #     'value': browserInfo.cookie,
    # })
    browser.get(browserInfo.initPage)

    browser.implicitly_wait(1)
    return browser

# def buildBrowser(domain='', driverPath='',browserType = 'chrome'):
#     # user = conf.get('userInfo')
#     # webdriver.Ie()
#     browser = None
#     if browserType.lower() == 'chrome':
#         try:
#             browser = webdriver.Chrome(driverPath)
#         except FileExistsError as e:
#             print(e)
#     elif browserType.lower() == 'firefox':
#         try:
#             browser = webdriver.Firefox(executable_path = driverPath)
#         except FileExistsError as e:
#             print(e)
#
#     elif browserType == 'ie':
#         try:
#             browser = webdriver.Ie(driverPath)
#         except FileExistsError as e:
#             print(e)
#     else:
#         raise NotSupportBrowserException(browserType)
#     # browser.maximize_window()
#     browser.get(domain)
#     browser.implicitly_wait(1)
#     return browser
