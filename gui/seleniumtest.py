import sys
from selenium import webdriver
import gui.utility
from selenium.webdriver.common.keys import Keys
from PyQt5.QtWidgets import *

from gui import utility


class MainWin(QDialog):
    def __init__(self, parent=None):  # 初始化，主要负责各部分的布局结合与信号链接
        super(MainWin, self).__init__(parent)
        self.handle = ''  # 窗口句柄
        self.Test_handle = [u'{986c70e9-ef24-426b-8da0-3a948fd9d4f0}']  # 测试用窗口句柄
        self.Test = 1  # 桩

        self.Table_Column = 7  # 表格列数
        self.Table_Row = 0  # 表格行数，是到后面按下add会自动增加一行

        self.Data = []  # 表格数据记录list
        self.Data_Url = []

        self.Head()  # 头部的控件
        self.Body()  # 主体控件
        self.Table()  # 表格控件
        Layout_Main = QVBoxLayout()  # 主输出布局
        Layout_Main.addLayout(self.Layout_Head)  # 加入头部控件
        Layout_Main.addLayout(self.Layout_Body)  # 加入主体控件
        Layout_Main.addWidget(self.Table_Main)  # 加载表格
        self.setLayout(Layout_Main)  # 输出主布局
        #
        self.Button_Start.clicked.connect(self.Work_Start)
        # self.connect(self.Button_Start, SIGNAL('clicked()'), self.Work_Start)  # Start按钮的功能链接
        self.Button_GoOn.clicked.connect(self.Work_GoOn)
        # self.connect(self.Button_GoOn, SIGNAL('clicked()'), self.Work_GoOn)  # GOON按钮的功能链接
        self.Button_Add.clicked.connect(self.Work_Add)
        # self.connect(self.Button_Add, SIGNAL('clicked()'), self.Work_Add)  # 加入表格
        self.Button_Del.clicked.connect(self.Work_Del)
        # self.connect(self.Button_Del, SIGNAL('clicked()'), self.Work_Del)  # 删除最后一行
        self.Button_Data_Test.clicked.connect(self.Work_Data_Test)
        # self.connect(self.Button_Data_Test, SIGNAL('clicked()'), self.Work_Data_Test)  # 表格数据校验
        self.Button_Save.clicked.connect(self.Work_Save)
        # self.connect(self.Button_Save, SIGNAL('clicked()'), self.Work_Save)  # 数据保存按钮
        self.Button_Load.clicked.connect(self.Work_Load)
        # self.connect(self.Button_Load, SIGNAL('clicked()'), self.Work_Load)  # 数据读取按钮
        self.Button_Work_Test.clicked.connect(self.Just_Test)
        # self.Button_Work_Test.clicked.connect(self.Test)
        # self.connect(self.Button_Work_Test,SIGNAL('clicked()'),self.Test)#WORK测试按钮
        # self.connect(self.Button_Work_Test, SIGNAL('clicked()'), self.Just_Test)

        # 模式选择关闭不需要的输入栏
        # self.connect(self.ComboBox_Mode, SIGNAL("currentIndexChanged(int)"), self.Enable_LineEdit)

    # 头部UI
    def Head(self):
        Label_StartUrl = QLabel("Start Url :")
        self.LineEdit_StartUrl = QLineEdit()  # 输入地址
        if self.Test == 1:
            self.LineEdit_StartUrl.setText('www.baidu.com')

        self.Button_Start = QToolButton()
        self.Button_Start.setText('Start')  # Start按钮

        self.Button_GoOn = QToolButton()
        self.Button_GoOn.setText('GoOn')  # GOON按钮

        self.Button_Data_Test = QToolButton()
        self.Button_Data_Test.setText('Data Test')  # DATA TEST按钮

        self.Button_Save = QToolButton()  # Save按钮
        self.Button_Save.setText('Save')

        self.Button_Load = QToolButton()  # Load按钮
        self.Button_Load.setText('Load')

        self.Button_Work_Test = QToolButton()  # Work 功能测试按钮
        self.Button_Work_Test.setText('Work_Test')

        self.HTTP = QRadioButton('http://')  # 以下是3个单选框
        self.FTP = QRadioButton('ftp://')
        self.DIY = QRadioButton('DIY')
        x = 0
        y = 0
        self.Layout_Head = QGridLayout()
        self.Layout_Head.addWidget(Label_StartUrl, y, x)
        x += 1
        self.Layout_Head.addWidget(self.LineEdit_StartUrl, y, x)
        x += 1
        self.Layout_Head.addWidget(self.Button_Start, y, x)
        x += 1
        self.Layout_Head.addWidget(self.Button_GoOn, y, x)
        x += 1
        self.Layout_Head.addWidget(self.Button_Data_Test, y, x)

        x = 0
        y += 1
        self.Layout_Head.addWidget(self.Button_Save, y, x)
        x += 1
        self.Layout_Head.addWidget(self.Button_Load, y, x)
        x += 1
        self.Layout_Head.addWidget(self.Button_Work_Test, y, x)

        x = 0
        y += 1
        self.Layout_Head.addWidget(self.HTTP, y, x)
        x += 1
        self.Layout_Head.addWidget(self.FTP, y, x)
        x += 1
        self.Layout_Head.addWidget(self.DIY, y, x)

    # 主体UI
    def Body(self):
        self.ComboBox_Mode = QComboBox()
        self.ComboBox_Mode.addItem(self.tr('One'))
        self.ComboBox_Mode.addItem(self.tr('More'))
        self.ComboBox_Mode.addItem(self.tr('Frame'))
        self.ComboBox_Mode.addItem(self.tr('Go Back'))
        Lable_Findby = QLabel("Find by/GO:")
        self.LineEdit_Find_By = QLineEdit()
        Lable_Find_Value = QLabel("Value:")
        self.LineEdit_Find_Value = QLineEdit()
        Lable_Do_To = QLabel("Do/Back:")
        self.LineEdit_Do_To = QLineEdit()
        Lable_Do_Value = QLabel("Value:")
        self.LineEdit_Do_Value = QLineEdit()

        self.Button_Add = QToolButton()
        self.Button_Add.setText("Add")

        self.Button_Del = QToolButton()
        self.Button_Del.setText("Del")

        self.Layout_Body = QGridLayout()  # 布局主要的输入框，Y是行数，X是列数
        y = 0
        x = 0
        self.Layout_Body.addWidget(self.ComboBox_Mode, y, x)
        x += 1  # 同一行，跳转至后一格
        self.Layout_Body.addWidget(Lable_Findby, y, x)
        x += 1
        self.Layout_Body.addWidget(self.LineEdit_Find_By, y, x)
        x += 1
        self.Layout_Body.addWidget(Lable_Find_Value, y, x)
        x += 1
        self.Layout_Body.addWidget(self.LineEdit_Find_Value, y, x)
        x += 1
        self.Layout_Body.addWidget(Lable_Do_To, y, x)
        x += 1
        self.Layout_Body.addWidget(self.LineEdit_Do_To, y, x)
        x += 1
        self.Layout_Body.addWidget(Lable_Do_Value, y, x)
        x += 1
        self.Layout_Body.addWidget(self.LineEdit_Do_Value, y, x)
        x += 1
        self.Layout_Body.addWidget(self.Button_Add, y, x)
        x += 1
        self.Layout_Body.addWidget(self.Button_Del, y, x)

    # 表格--------------------------------------------------
    def Table(self):

        self.Table_Main = QTableWidget()  # 建立表格
        self.Table_Main.setColumnCount(self.Table_Column)  # 设置列
        self.Table_Main.setRowCount(self.Table_Row)  # 设置行
        # 表格列名
        self.Table_Main.setHorizontalHeaderLabels(['Mode', 'Find_by', 'Value', 'Do/List Name', 'Value1', 'GET', 'URL'])

    # 实际操作的执行前检验
    def Work_Inspection(self):
        Error_Mark = 0
        if self.Data:  # 检测到有数据
            if (utility.Data_Check(self.Data) == 'False'):  # 数据检验发现数据错误
                self.Error_Window('Error_Data')  # 报错
                Error_Mark = 1
        else:
            self.Error_Window('Error_No_Data')
            Error_Mark = 1
        if (Error_Mark != 1):
            self.Work()  # 一起正常，开始工作
            # 实际操作 Doing!!!!

    def Work(self):
        print
        'Start Work'
        DoThing = utility.DoThing()  # 实体化

        for i in range(0, len(self.Data), 5):
            # 主动作区
            if self.Data[i] == 'One':
                self.Data_Url.append(self.driver.current_url)
                d1 = DoThing.Find_One(self.driver, self.Data[i + 1], self.Data[i + 2])
                if d1[0] == 'Normal':
                    DoThing.Do_Thing(d1[1], self.Data[i + 3], self.Data[i + 4])
                else:
                    self.Error_Window(d1[0])
                    break  # 跳出本次工作
                    print
                    d1[0]

            elif self.Data[i] == 'More':
                self.Data_Url.append(unicode(self.driver.current_url))
                d1 = DoThing.Find_More(self.driver, self.Data[i + 1], self.Data[i + 2])
                if d1[0] == 'Normal' and d1[2] != 0:
                    DoThing.Do_Thing_More(d1[1], self.Data[i + 3], self.Data[i + 4])
                else:
                    self.Error_Window(d1[0])
                    print
                    d1[0]
                    break  # 跳出本次工作
                    # elif self.Data[i] == 'Go Back':
                    #   self.Data_Url.append(unicode(self.driver.current_url))
                    #  d1 = DoThing.


                    # if self.Data[i+3] == 'input_back' or self.Data[i+3] == 'click_back':
                    #   self.driver.get(self.Data_Url) GOBACK操作，暂时禁用。使用调用键盘操作的方式来实现

            self.Data_Url.append(unicode(self.driver.current_url))
            # 返回值显示区
            if self.Data[i] == 'One':
                self.Table_Main.setItem(i / 5, 6, QTableWidgetItem(unicode(self.driver.current_url)))
            elif self.Data[i] == 'More':
                self.Table_Main.setItem(i / 5, 5, QTableWidgetItem(unicode(d1[2])))




                # Start按钮功能……

    def Work_Start(self):
        Error_Mark = 0
        self.Start_Url = self.LineEdit_StartUrl.text()  # 首先得到新的URL
        if self.HTTP.isChecked():  # 3个单选框选择后对于输入的URL进行操作
            self.Start_Url = 'http://' + self.Start_Url
        if self.FTP.isChecked():
            self.Start_Url = 'ftp://' + self.Start_Url

        if (utility.Url_Test(self.Start_Url) == 'False'):  # 判断地址是否符合规则
            self.Error_Window('Error_Url')  # 报出URL错误警报
            Error_Mark = 1
        else:
            self.driver = webdriver.Firefox()
            self.driver.get(self.Start_Url)

        if Error_Mark == 0:
            self.Work_Inspection()
            self.handle = self.driver.window_handles  # 获得窗口句柄

            # GoOn按钮功能……

    def Work_GoOn(self):
        Error_Mark = 0
        if (self.handle == ''):  # 没有旧窗口报错
            self.Error_Window('Error_handle')
            Error_Mark = 1
        else:
            self.driver.switch_to_window(self.handle)  # 进入之前的窗口
        if Error_Mark == 0:
            self.Work_Inspection()


            # Add按钮功能

    def Work_Add(self):
        self.Table_Row += 1
        self.Table_Main.setRowCount(self.Table_Row)
        Find_by = self.LineEdit_Find_By.text()
        Value = self.LineEdit_Find_Value.text()
        Do = self.LineEdit_Do_To.text()
        Value1 = self.LineEdit_Do_Value.text()
        self.Button_Go = QToolButton()  # 输入栏-》表格
        x = 0
        self.Table_Main.setItem(self.Table_Row - 1, x, QTableWidgetItem(self.ComboBox_Mode.currentText()))
        x += 1
        self.Table_Main.setItem(self.Table_Row - 1, x, QTableWidgetItem(Find_by))
        x += 1
        self.Table_Main.setItem(self.Table_Row - 1, x, QTableWidgetItem(Value))
        x += 1
        self.Table_Main.setItem(self.Table_Row - 1, x, QTableWidgetItem(Do))
        x += 1
        self.Table_Main.setItem(self.Table_Row - 1, x, QTableWidgetItem(Value1))
        for i in range(self.Table_Column - 2):
            self.Data.append(self.Table_Main.item(self.Table_Row - 1, i).text())
            # if (self.LineEdit_StartUrl.text()!=''):
            # print self.LineEdit_StartUrl.text()
        if self.Test:
            print
            self.Data
            print
            self.Table_Row


            # Del按钮功能

    def Work_Del(self):
        if (self.Table_Row > 0):  # 判断是否到边界
            self.Table_Row -= 1  # 退行
            self.Table_Main.setRowCount(self.Table_Row)
            self.Data = self.Data[:-7]  # 删除数据
        if self.Test:
            print
            self.Data
            print
            self.Table_Row

            # Data Test按钮功能：

    def Work_Data_Test(self):
        if (utility.Data_Check(self.Data) == 'False'):
            self.Error_Window('Error_Data')
        elif (utility.Data_Check(self.Data) == 'Fuck'):
            self.Mes_Window('Mes_Data_Fuck')
        else:
            self.Mes_Window('Mes_Data')
            # Save按钮功能:

    def Work_Save(self):
        self.Data_Save = utility.Data_Change()
        f = open(".//data//22.txt", 'w')
        f_Show = open(".//data//22_Show.txt", 'w')
        f.write(self.Data_Save.List_To_String(self.Data))  # 写入数据，该处的数据可以直接通过Load调用的
        f_Show.write(self.Data_Save.List_To_String_Show(self.Data, self.Data_Url))

    # Load按钮功能
    def Work_Load(self):
        f = open("D://22.txt", 'r')
        self.Data_String = f.read()
        if self.Data:  # 是否有数据了。有则报错
            self.Error_Window('Error_Had_Data')
            return 'error'
        else:
            self.Data = self.Data_String.split('_._._')
        ddd = utility.Data_Change()
        print
        ddd.List_To_String_Show(self.Data)
        x = 0
        y = 0
        for a in range(len(self.Data)):
            # 设置表格行数
            self.Table_Main.setRowCount(a / 5 + 1)
            # 行数上传到总计数器
            self.Table_Row = (a / 5 + 1)
            if (a % 5 == 0):
                y += 1
                x = 0
            else:
                x += 1
            print
            self.Data[a], y, x
            self.Table_Main.setItem(y - 1, x, QTableWidgetItem(self.Data[a]))


            # 报错窗口调用……

    def Error_Window(self, Error):
        dialog = utility.Error_Window(parent=self)
        dialog.run(Error)  # 传入报错参数
        dialog.setWindowTitle('Error Window')  # 报错窗口名
        dialog.exec_()
        dialog.destroy()
        print
        Error + ' = error'

    # 一般信息窗口调用……
    def Mes_Window(self, Mes):
        dialog = utility.Mes_Window(parent=self)
        dialog.run(Mes)  # 传入报错参数
        dialog.setWindowTitle('Mes Window')  # 报错窗口名
        dialog.exec_()
        dialog.destroy()

    # 改变工作模式，某些输入框关闭----------------------------------------------------------------------
    def Enable_LineEdit(self):

        # 初始化输入栏状态
        self.LineEdit_Find_By.setEnabled(True)
        self.LineEdit_Find_Value.setEnabled(True)
        self.LineEdit_Do_To.setEnabled(True)
        self.LineEdit_Do_Value.setEnabled(True)

        # More模式
        if (self.ComboBox_Mode.currentText() == 'More'):
            # self.LineEdit_Find_Value.setEnabled(False)  #MORE 关闭VALUE的输入栏
            self.LineEdit_Find_Value.clear()  # 内容清理
        # Frame模式
        elif (self.ComboBox_Mode.currentText() == 'Frame'):
            self.LineEdit_Find_By.setEnabled(False)
            self.LineEdit_Do_To.setEnabled(False)
            self.LineEdit_Do_Value.setEnabled(False)

            self.LineEdit_Find_By.clear()  # 内容清理
            self.LineEdit_Do_To.clear()
            self.LineEdit_Do_Value.clear()
            # 返回功能
        elif (self.ComboBox_Mode.currentText() == 'Go Back'):
            self.LineEdit_Find_By.setEnabled(False)
            self.LineEdit_Find_Value.setEnabled(False)
            self.LineEdit_Do_To.setEnabled(False)
            self.LineEdit_Do_Value.setEnabled(False)  # 关闭所有选项

            self.LineEdit_Find_By.clear()
            self.LineEdit_Find_Value.clear()
            self.LineEdit_Do_To.clear()
            self.LineEdit_Do_Value.clear()  # 内容清理

            # 测试用的函数

    def Just_Test(self):
        utility.Key_Down(self.driver, Keys.BACKSPACE)
        utility.Key_Up(self.driver, Keys.BACKSPACE)


app = QApplication(sys.argv)
main = MainWin()
main.show()
app.exec_()