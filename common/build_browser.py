from common.config_center import globalconfig
from resource.constant import CHROME_DRIVER_PATH,FIREFOX_DRIVER_PATH
from selenium import webdriver

def build_a_browser(browser_type = 'firefox'):
    conf = globalconfig()
    user = conf.get('userInfo')
    # webdriver.Ie()
    browser = None
    if browser_type == 'chrome':
        browser = webdriver.Chrome(CHROME_DRIVER_PATH)
    elif browser_type == 'firefox':
        browser = webdriver.Firefox(executable_path = FIREFOX_DRIVER_PATH)
    # browser.maximize_window()
    browser.get(user['login_url'])
    browser.implicitly_wait(conf.get('wait'))
    return browser
