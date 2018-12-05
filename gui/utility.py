# -*- coding: utf-8 -*-
import re
from PyQt5 import QtGui, QtCore

from PyQt5.QtWidgets import *
import copy
from selenium import webdriver
import time
from PyQt5.QtWidgets import QDialog


# Url_Test :检测地址是否符合规则

def Url_Test(url):
    rule1 = '(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?'
    rule2 = '^(http|https|ftp)\://([a-zA-Z0-9\.\-]+(\:[a-zA-Z0-9\.&amp;%\$\-]+)*@)?((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])|([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.[a-zA-Z]{2,4})(\:[0-9]+)?(/[^/][a-zA-Z0-9\.\,\?\'\\/\+&amp;%\$#\=~_\-@]*)*$'
    # rule3 = '^([a-zA-Z]\:|\\\\[^\/\\:*?"<>|]+\\[^\/\\:*?"<>|]+)(\\[^\/\\:*?"<>|]+)+(\.[^\/\\:*?"<>|]+)$'
    # rule4 = '^(http|https|ftp)\://([a-zA-Z0-9\.\-]+(\:[a-zA-Z0-9\.&amp;%\$\-]+)*@)*((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])|localhost|([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(\:[0-9]+)*(/($|[a-zA-Z0-9\.\,\?\'\\\+&amp;%\$#\=~_\-]+))*$'
    # rule5 = '^([a-zA-Z]\:)(\\[^\\/:*?<>"|]*(?<![ ]))*(\.[a-zA-Z]{2,6})$ '
    # rule6 = '^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$'
    # rule7 = '^(((ht|f)tp(s?))\://)?(www.|[a-zA-Z].)[a-zA-Z0-9\-\.]+\.(com|edu|gov|mil|net|org|biz|info|name|museum|us|ca|uk)(\:[0-9]+)*(/($|[a-zA-Z0-9\.\,\;\?\'\\\+&amp;%\$#\=~_\-]+))*$'
    # rule8 = '\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))'

    # RULE来自网络，亲自己百度吧,只开了规则1、2

    a1 = re.match(rule1, url)
    a2 = re.match(rule2, url)
    # a3 = re.match(rule3,url)
    # a4 = re.match(rule4,url)
    # a5 = re.match(rule5,url)
    # a6 = re.match(rule6,url)
    # a7 = re.match(rule7,url)
    # a8 = re.match(rule8,url)

    if a1 or a2:
        return 'Ture'
    else:
        return 'False'


# Data数据内容初步校验
def Data_Check(Data):
    Data_Len = len(Data)
    if Data_Len == 0:
        return 'Fuck'
    while Data_Len > 0:
        if Data[Data_Len - 5] == 'One':
            for a in (-4, -3, -2):
                if Data[Data_Len + a] == '':
                    return 'False'
        elif Data[Data_Len - 5] == '1More':  # 暂时关闭了。若打开更改为'More'
            if Data[Data_Len - 3] != '':
                return 'False'
            for a in (-4, -2):
                if Data[Data_Len + a] == '':
                    return 'False'
        elif Data[Data_Len - 5] == 'Frame':
            if Data[Data_Len - 3] == '':
                return 'False'
            if Data[Data_Len + a] != '':
                return 'False'
        elif Data[Data_Len - 5] == 'Go Back':
            for a in (-4, -3, -2, -1):
                if Data[Data_Len + a] != '':
                    return 'False'
        Data_Len -= 5


# 错误信息窗口
class Error_Window(QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.resize(200, 100)

        self.layout = QtGui.QGridLayout()
        self.Mes = QtGui.QLabel()  # 错误信息栏,由run函数根据入参选择输出语句

        self.Ok_Button =QToolButton()
        self.Ok_Button.setText('Ok I Know')

        self.layout.addWidget(self.Mes)
        self.layout.addWidget(self.Ok_Button)

        self.connect(self.Ok_Button, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))  # 关闭按钮

        self.setLayout(self.layout)
        self.setObjectName("MainWindow")

    def run(self, mes):
        if (mes == 'Error_Url'):
            self.Mes.setText('URL Error,Check The URL')
        elif (mes == 'Error_handle'):
            self.Mes.setText('No Old Window')
        elif (mes == 'Error_Test_handle'):
            self.Mes.setText('No Test Handle')
        elif (mes == 'Error_Data'):
            self.Mes.setText('Data wrong ,check data list')
        elif (mes == 'Error_Had_Data'):
            self.Mes.setText('Already have the data')
        elif (mes == 'Error_No_Data'):
            self.Mes.setText('No data run a fart')
        elif (mes == 'Not_Found'):
            self.Mes.setText('Not_Found Element')

        self.setLayout(self.layout)


# 一般消息窗口
class Mes_Window(QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.resize(200, 100)

        self.layout = QtGui.QGridLayout()
        self.Mes = QtGui.QLabel()  # 错误信息栏,由run函数根据入参选择输出语句

        self.Ok_Button = QToolButton()
        self.Ok_Button.setText('Ok I Know')

        self.layout.addWidget(self.Mes)
        self.layout.addWidget(self.Ok_Button)

        self.connect(self.Ok_Button, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))  # 关闭按钮

        self.setLayout(self.layout)
        self.setObjectName("MainWindow")

    def run(self, mes):
        if (mes == 'Mes_Data'):
            self.Mes.setText('Data ok,now do it')
        elif (mes == 'Mes_Data_Fuck'):
            self.Mes.setText('No Data , U Play Me?')
        elif (mes == 'Error_Test_handle'):
            self.Mes.setText('No Test Handle')
        elif (mes == 'Error_Data'):
            self.Mes.setText('Data wrong ,check data list')

        self.setLayout(self.layout)


# 列表数据转换
class Data_Change():
    # def __init__(self):

    def List_To_String_Show(self, Data, Data_Url):
        Data_New = copy.copy(Data)
        if Data_Url:
            for a in range(4, len(Data_New), 5):
                Data_New[a] = Data_New[a] + ':' + Data_Url[a / 5] + '\n'
        else:
            for a in range(4, len(Data_New), 5):
                Data_New[a] = Data_New[a] + '\n'
        string = '_._'.join(Data_New)
        string = '_._' + string
        return string

    def List_To_String(self, Data):
        string = '_._._'.join(Data)
        return string


# 主工作部分
class DoThing():
    # 查找单个元素-------------------------------------------------------
    def Find_One(self, driver, by, value):
        Error_Mark = 'Normal'
        # 根据class_name查找元素
        if (by == 'Class_name' or by == 'Class_Name' or by == 'class_name'):
            try:
                driver1 = driver.find_element_by_class_name(value)
            except:
                Error_Mark = 'Not_Found'
                # 根据css_selector查找元素
        elif (by == 'Css_selector' or by == 'Css_Selector' or by == 'css_selector'):
            try:
                driver1 = driver.find_element_by_css_selector(value)
            except:
                Error_Mark = 'Not_Found'
                # 根据id查找元素
        elif (by == 'ID' or by == 'Id' or by == 'id'):
            try:
                driver1 = driver.find_element_by_id(value)
            except:
                Error_Mark = 'Not_Found'
        # 根据link_text查找元素
        elif (by == 'Link_text' or by == 'Link_Text' or by == 'link_text'):
            try:
                driver1 = driver.find_element_by_link_text(value)
            except:
                Error_Mark = 'Not_Found'
                # 根据name查找元素
        elif (by == 'NAME' or by == 'Name' or by == 'name'):
            try:
                driver1 = driver.find_element_by_name(value)
            except:
                Error_Mark = 'Not_Found'
                # 根据partial_link_text找元素
        elif (by == 'Partial_link_text' or by == 'Partial_Link_Text' or by == 'partial_link_text'):
            try:
                driver1 = driver.find_element_by_partial_link_text(value)
            except:
                Error_Mark = 'Not_Found'
                # 根据tag_name查找元素
        elif (by == 'Tag_name' or by == 'Tag_Name' or by == 'tag_name'):
            try:
                driver1 = driver.find_element_by_tag_name(value)
            except:
                Error_Mark = 'Not_Found'
                # 根据xpath查找元素
        elif (by == 'XPATH' or by == 'Xpath' or by == 'xpath'):
            try:
                driver1 = driver.find_element_by_xpath(value)
            except:
                Error_Mark = 'Not_Found'
                # 啥都没有，报错吧亲
        else:
            Error_Mark = 'Mes_Data_Fuck'
        if Error_Mark != 'Normal':
            return Error_Mark, Error_Mark
        else:
            return Error_Mark, driver1

    # 查找多个元素-------------------------------------------------------
    def Find_More(self, driver, by, value):
        Error_Mark = 'Normal'
        # 根据class_name查找元素
        if (by == 'Class_name' or by == 'Class_Name' or by == 'class_name'):
            try:
                driver1 = driver.find_elements_by_class_name(value)
            except:
                Error_Mark = 'Not_Found'
                # 根据css_selector查找元素
        elif (by == 'Css_selector' or by == 'Css_Selector' or by == 'css_selector'):
            try:
                driver1 = driver.find_elements_by_css_selector(value)
            except:
                Error_Mark = 'Not_Found'
                # 根据id查找元素
        elif (by == 'ID' or by == 'Id' or by == 'id'):
            try:
                driver1 = driver.find_elements_by_id(value)
            except:
                Error_Mark = 'Not_Found'
                # 根据link_text查找元素
        elif (by == 'Link_text' or by == 'Link_Text' or by == 'link_text'):
            try:
                driver1 = driver.find_elements_by_link_text(value)
            except:
                Error_Mark = 'Not_Found'
                # 根据name查找元素
        elif (by == 'NAME' or by == 'Name' or by == 'name'):
            try:
                driver1 = driver.find_elements_by_name(value)
            except:
                Error_Mark = 'Not_Found'
                # 根据xpath查找元素
        elif (by == 'XPATH' or by == 'Xpath' or by == 'xpath'):
            try:
                driver1 = driver.find_elements_by_xpath(value)
            except:
                Error_Mark = 'Not_Found'
                # 啥都没有，报错吧亲
        else:
            Error_Mark = 'Mes_Data_Fuck'
        if Error_Mark != 'Normal':
            return Error_Mark, Error_Mark
        else:
            return (Error_Mark, driver1, len(driver1))

    # 输入数据,这个地方还可以改,延时1S-----------------------------------------------------------------
    def Do_Thing(self, driver, value1, value2):
        if value1 == 'input' or value1 == 'input':

            driver.send_keys(value2)

        elif value1 == 'click' or value1 == 'click_back':
            driver.click()
        time.sleep(1)

    # 调用方法（driver,元素集，何种动作，动作值）
    def Do_Thing_More(self, driver_eles, value1, value2):
        for driver_ele in driver_eles:
            self.Do_Thing(driver_ele, value1, value2)
            time.sleep(1)
            # def Go_Back(self,driver):


# send_F5 = webdriver.ActionChains(driver)
#                send_F5.key_down(Keys.F5).perform()
#                send_F5.key_up(Keys.F5).perform()#这步有时候会报错，逻辑似乎没问题，为什么会报错还不清楚

def Key_Down(driver, value):
    dd = webdriver.ActionChains(driver)
    dd.key_down(value).perform()


def Key_Up(driver, value):
    dd = webdriver.ActionChains(driver)
    dd.key_up(value).perform()




























