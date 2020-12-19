# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'case.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import http.client
import hashlib
import json
import urllib
import random
from PyQt5.Qt import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication
import sys
import os
import time
import run_classifier as cf
import ggg as gg
import globalvar as gl
import re
import requests

class Ui_human_translation(object):
    def setupUi(self, human_translation):
        human_translation.setObjectName("human_translation")
        human_translation.resize(1060, 784)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(10)
        human_translation.setFont(font)
        self.centralwidget = QtWidgets.QWidget(human_translation)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(280, 415, 750, 330))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(280, 50, 750, 330))

        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.open_bt = QtWidgets.QPushButton(self.centralwidget)
        self.open_bt.setGeometry(QtCore.QRect(910, 10, 100, 25))
        self.open_bt.setFont(font)
        self.open_bt.setObjectName("open_bt")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("open_path")
        self.open_path = QtWidgets.QLineEdit(self.centralwidget)
        self.open_path.setGeometry(QtCore.QRect(280, 10, 600, 25))

        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.translation = QtWidgets.QPushButton(self.centralwidget)
        self.translation.setGeometry(QtCore.QRect(910, 320, 100, 40))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.translation.setFont(font)
        self.translation.setObjectName("translation")

        self.deal = QtWidgets.QPushButton(self.centralwidget)
        self.deal.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deal.setFont(font)
        self.deal.setObjectName("deal")

        self.huoqu = QtWidgets.QPushButton(self.centralwidget)
        self.huoqu.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.huoqu.setFont(font)
        self.huoqu.setObjectName("huoqu")

        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setObjectName("deal")

        self.human_translation_2 = QtWidgets.QPushButton(self.centralwidget)
        self.human_translation_2.setGeometry(QtCore.QRect(910, 680, 100, 40))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.human_translation_2.setFont(font)
        self.human_translation_2.setObjectName("human_translation_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 100, 201, 41))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(110, 40, 50, 50))
        self.logo.setObjectName("logo")
        self.bgcolor = QtWidgets.QLabel(self.centralwidget)
        self.bgcolor.setGeometry(QtCore.QRect(250, 0, 831, 791))
        self.bgcolor.setText("")
        self.bgcolor.setObjectName("bgcolor")
        self.logo1 = QtWidgets.QLabel(self.centralwidget)
        self.logo1.setGeometry(QtCore.QRect(60, 190, 30, 30))
        self.logo1.setObjectName("logo1")
        self.logo2 = QtWidgets.QLabel(self.centralwidget)
        self.logo2.setGeometry(QtCore.QRect(60, 260, 30, 30))
        self.logo2.setObjectName("logo2")
        self.logo4 = QtWidgets.QLabel(self.centralwidget)
        self.logo4.setGeometry(QtCore.QRect(60, 400, 30, 30))
        self.logo4.setObjectName("logo4")
        self.logo3 = QtWidgets.QLabel(self.centralwidget)
        self.logo3.setGeometry(QtCore.QRect(60, 330, 30, 30))
        self.logo3.setObjectName("logo3")
        self.logo5 = QtWidgets.QLabel(self.centralwidget)
        self.logo5.setGeometry(QtCore.QRect(60, 530, 150, 150))
        self.logo5.setObjectName("logo5")
        self.bgcolor1 = QtWidgets.QLabel(self.centralwidget)
        self.bgcolor1.setGeometry(QtCore.QRect(0, 245, 250, 60))
        self.bgcolor1.setText("")
        self.bgcolor1.setObjectName("bgcolor1")
        self.dictionary1 = QtWidgets.QPushButton(self.centralwidget)
        self.dictionary1.setGeometry(QtCore.QRect(110, 190, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dictionary1.setFont(font)
        self.dictionary1.setObjectName("dictionary1")

        self.dictionary3 = QtWidgets.QPushButton(self.centralwidget)
        self.dictionary3.setGeometry(QtCore.QRect(110, 330, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dictionary3.setFont(font)
        self.dictionary3.setObjectName("dictionary3")
        self.dictionary4 = QtWidgets.QPushButton(self.centralwidget)
        self.dictionary4.setGeometry(QtCore.QRect(110, 400, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dictionary4.setFont(font)
        self.dictionary4.setObjectName("dictionary3")


        self.dictionary2 = QtWidgets.QPushButton(self.centralwidget)
        self.dictionary2.setGeometry(QtCore.QRect(110, 260, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dictionary2.setFont(font)
        self.dictionary2.setObjectName("dictionary2")
        self.prompt = QtWidgets.QLabel(self.centralwidget)
        self.prompt.setGeometry(QtCore.QRect(280, 10, 340, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.prompt.setFont(font)
        self.prompt.setObjectName("prompt")
        self.bgcolor1.raise_()
        self.bgcolor.raise_()
        #self.label_4.raise_()
        self.textBrowser.raise_()
        self.textEdit.raise_()
        self.translation.raise_()
        self.deal.raise_()
        self.huoqu.raise_()
        self.clear.raise_()
        self.open_path.raise_()
        self.human_translation_2.raise_()
        self.label_5.raise_()
        self.open_bt.raise_()
        self.logo.raise_()
        self.logo1.raise_()
        self.logo4.raise_()
        self.logo3.raise_()
        self.logo5.raise_()
        self.logo2.raise_()
        self.dictionary1.raise_()
        self.dictionary2.raise_()
        self.dictionary3.raise_()
        self.dictionary4.raise_()
        self.prompt.raise_()
        human_translation.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(human_translation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 23))
        self.menubar.setObjectName("menubar")
        human_translation.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(human_translation)
        self.statusbar.setObjectName("statusbar")
        human_translation.setStatusBar(self.statusbar)

        self.retranslateUi(human_translation)
        QtCore.QMetaObject.connectSlotsByName(human_translation)

    def retranslateUi(self, human_translation):
        _translate = QtCore.QCoreApplication.translate
        human_translation.setWindowTitle(_translate("human_translation", "隐式情感分析系统"))
        self.setWindowIcon(QIcon('../img/icon.gif'))
        #self.label_4.setText(_translate("human_translation", "相关"))
        self.translation.setText(_translate("human_translation", "预 测"))
        self.human_translation_2.setText(_translate("human_translation", "保存结果"))
        self.open_path.setText(_translate("human_translation", "打开文件"))
        self.open_bt.setText(_translate("human_translation","浏 览"))
        self.label_5.setText(_translate("human_translation", "隐式情感分析系统"))
        self.logo.setText(_translate("human_translation", "logo"))
        self.logo1.setText(_translate("human_translation", "logo1"))
        self.logo2.setText(_translate("human_translation", "logo2"))
        self.logo4.setText(_translate("human_translation", "logo4"))
        self.logo3.setText(_translate("human_translation", "logo3"))
        self.logo5.setText(_translate("human_translation", "logo5"))
        self.dictionary1.setText(_translate("human_translation", "数据清洗"))
        self.dictionary2.setText(_translate("human_translation", "预测"))
        self.dictionary3.setText(_translate("human_translation", "数据处理"))
        self.dictionary4.setText(_translate("human_translation", "数据获取"))



class translation(QMainWindow, Ui_human_translation):

    def __init__(self, parent=None):
        super(translation, self).__init__(parent)
        self.setupUi(self)
        self.translation.clicked.connect(self.pridect)
        self.dictionary1.clicked.connect(self.diction1)
        self.dictionary2.clicked.connect(self.diction2)
        self.dictionary3.clicked.connect(self.diction3)
        self.dictionary4.clicked.connect(self.diction4)
        self.deal.clicked.connect(self.deal_data)
        self.human_translation_2.clicked.connect(self.saveas_event)
        self.open_bt.clicked.connect(self.open_event)
        self.clear.clicked.connect(self.frash)
        self.huoqu.clicked.connect(self.huoqushujv)
        self.dictionary2.setStyleSheet("color:red;")
        self.translation.setStyleSheet("background-color:rgb(242,58,58);color:white;")
        self.dictionary1.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.dictionary3.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.dictionary4.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.dictionary2.setStyleSheet("border-style:outset;border-width:0;color:red;")
        self.human_translation_2.setStyleSheet("background-color:white;")
        self.textEdit.setStyleSheet("background-color:#f0f0f0;border-width:0;border-style:outset")
        self.textBrowser.setStyleSheet("border-width:0;border-style:outset;background-color:#f0f0f0;")
        self.bgcolor.setStyleSheet("background-color:white;")
        self.bgcolor1.setStyleSheet("background-color:#ffeff2;")
        jpg = QtGui.QPixmap('../img/logo1.jpg')
        self.logo.setPixmap(jpg)
        jpg1 = QtGui.QPixmap('../img/A.png')
        self.logo1.setPixmap(jpg1)
        jpg2 = QtGui.QPixmap('../img/B.png')
        self.logo2.setPixmap(jpg2)
        jpg3 = QtGui.QPixmap('../img/c.png')
        self.logo3.setPixmap(jpg3)
        jpg4 = QtGui.QPixmap('../img/d.png')
        self.logo4.setPixmap(jpg4)
        jpg5 = QtGui.QPixmap('../img/photo.png')
        self.logo5.setPixmap(jpg5)
        self.textEdit.setPlaceholderText("请输入要预测的文字或内容（例：1  今天天真蓝）")
        self.index = 1

    def diction1(self):
        self.open_bt.setGeometry(QtCore.QRect(910, 10, 100, 25))
        self.open_bt.setObjectName("open_bt")
        self.textEdit.setGeometry(QtCore.QRect(280, 50, 750, 330))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser.setGeometry(QtCore.QRect(280, 10, 600, 25))
        self.textBrowser.setObjectName("open_path")
        self.textBrowser.setGeometry(QtCore.QRect(280, 415, 750, 330))
        self.textBrowser.setObjectName("textBrowser")
        self.bgcolor1.setGeometry(QtCore.QRect(0, 175, 250, 60))
        self.dictionary1.setStyleSheet("color:red;")
        self.deal.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.translation.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.deal.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.huoqu.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.human_translation_2.setGeometry(QtCore.QRect(910, 680, 100, 40))
        self.clear.setGeometry(QtCore.QRect(910, 320, 100, 40))
        self.dictionary1.setStyleSheet("border-style:outset;border-width:0;color:red;")
        self.dictionary2.setStyleSheet("border-style:outset;border-width:0;")
        self.dictionary3.setStyleSheet("border-style:outset;border-width:0;")
        self.dictionary4.setStyleSheet("border-style:outset;border-width:0;")
        self.clear.setText("数据清洗")
        self.open_bt.setText("浏览")
        self.dictionary3.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.dictionary2.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.dictionary4.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.open_path.setText("打开文件")
        self.textEdit.clear()
        self.textBrowser.clear()
        self.textEdit.setPlaceholderText("请输入要清洗的文字或内容")


    def diction2(self):
        self.open_bt.setGeometry(QtCore.QRect(910, 10, 100, 25))
        self.open_bt.setObjectName("open_bt")
        self.textEdit.setGeometry(QtCore.QRect(280, 50, 750, 330))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser.setGeometry(QtCore.QRect(280, 10, 600, 25))
        self.textBrowser.setObjectName("open_path")
        self.textBrowser.setGeometry(QtCore.QRect(280, 415, 750, 330))
        self.textBrowser.setObjectName("textBrowser")
        self.bgcolor1.setGeometry(QtCore.QRect(0, 245, 250, 60))
        self.deal.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.clear.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.huoqu.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.dictionary3.setStyleSheet("color:black;")
        self.dictionary1.setStyleSheet("color:black;")
        self.dictionary4.setStyleSheet("color:black;")
       # self.label_4.setStyleSheet("color:black;")
        self.translation.setGeometry(QtCore.QRect(910, 320, 100, 40))
        self.human_translation_2.setGeometry(QtCore.QRect(910, 680, 100, 40))
        self.dictionary1.setStyleSheet("border-style:outset;border-width:0;")
        self.dictionary2.setStyleSheet("border-style:outset;border-width:0;color:red;")
        self.dictionary3.setStyleSheet("border-style:outset;border-width:0;")
        self.dictionary4.setStyleSheet("border-style:outset;border-width:0;")
        self.translation.setText("预 测")
        self.open_bt.setText("浏览")
        self.dictionary1.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.dictionary3.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.dictionary4.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.open_path.setText("打开文件")
        self.textEdit.clear()
        self.textBrowser.clear()
        self.textEdit.setPlaceholderText("请输入要预测的文字或内容（例：1  今天天真蓝）")

    def diction3(self):
        self.open_bt.setGeometry(QtCore.QRect(910, 10, 100, 25))
        self.open_bt.setObjectName("open_bt")
        self.textEdit.setGeometry(QtCore.QRect(280, 50, 750, 330))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser.setGeometry(QtCore.QRect(280, 10, 600, 25))
        self.textBrowser.setObjectName("open_path")
        self.textBrowser.setGeometry(QtCore.QRect(280, 415, 750, 330))
        self.textBrowser.setObjectName("textBrowser")
        self.bgcolor1.setGeometry(QtCore.QRect(0, 315, 250, 60))
        self.dictionary1.setStyleSheet("color:black;")
        self.deal.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.translation.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.deal.setGeometry(QtCore.QRect(910, 320, 100, 40))
        self.human_translation_2.setGeometry(QtCore.QRect(910, 680, 100, 40))
        self.clear.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.huoqu.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.dictionary1.setStyleSheet("border-style:outset;border-width:0;")
        self.dictionary2.setStyleSheet("border-style:outset;border-width:0;")
        self.dictionary3.setStyleSheet("border-style:outset;border-width:0;color:red;")
        self.dictionary4.setStyleSheet("border-style:outset;border-width:0;")
        self.deal.setText("数据处理")
        self.open_bt.setText("浏览")
        self.dictionary1.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.dictionary2.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.dictionary4.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.open_path.setText("打开文件")
        self.textEdit.clear()
        self.textBrowser.clear()
        self.textEdit.setPlaceholderText("请输入要处理的文字或内容（例：1  东海大学，以路思易教堂和东海乳品小栈而出名）")
        self.textBrowser.setText("例子：\nguid: dev-1\ntokens: [CLS] 东 海 大 学 ， 以 路 思 易 教 堂 和 东 海 乳 品 小 栈 而 出 名 。 [SEP](分词处理）\ninput_ids: 101 691 3862 1920 2110 8024 809 6662 2590 3211 3136 1828 1469 691 3862 745 1501 2207 3404 5445 1139 1399 511 102 （id映射，不够补0）\n")

    def diction4(self):
        self.open_bt.setGeometry(QtCore.QRect(910, 10, 100, 25))
        self.open_bt.setObjectName("open_bt")
        self.textEdit.setGeometry(QtCore.QRect(280, 50, 750, 330))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser.setGeometry(QtCore.QRect(280, 10, 600, 25))
        self.textBrowser.setObjectName("open_path")
        self.textBrowser.setGeometry(QtCore.QRect(280, 415, 750, 330))
        self.textBrowser.setObjectName("textBrowser")
        self.bgcolor1.setGeometry(QtCore.QRect(0, 385, 250, 60))
        self.deal.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.clear.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.dictionary3.setStyleSheet("color:black;")
        self.dictionary1.setStyleSheet("color:black;")
        self.dictionary4.setStyleSheet("color:black;")
        # self.label_4.setStyleSheet("color:black;")
        self.translation.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.huoqu.setGeometry(QtCore.QRect(910, 320, 100, 40))
        self.human_translation_2.setGeometry(QtCore.QRect(910, 680, 100, 40))
        self.dictionary1.setStyleSheet("border-style:outset;border-width:0;")
        self.dictionary2.setStyleSheet("border-style:outset;border-width:0;")
        self.dictionary3.setStyleSheet("border-style:outset;border-width:0;")
        self.dictionary4.setStyleSheet("border-style:outset;border-width:0;color:red;")
        self.huoqu.setText("获 取")
        self.open_bt.setText("浏览")
        self.open_path.setText("打开文件")
        self.textEdit.clear()
        self.textBrowser.clear()
        self.textEdit.setPlaceholderText("请输入要获取评论的数据的网址如：https://weibo.cn/comment/J2GogpBZh?uid=1403915120&rl=1&page=")


    def deal_data(self):
        print("1")
        gl._init()
        ttt = self.open_path.text()
        gl.set_value('val_path', ttt)
        tt = self.textEdit.toPlainText()
        gl.set_value('val_text', tt)
        print(ttt)
        cf.runn()
        _translate = QtCore.QCoreApplication.translate
        path = r'D:\python\Bert_chinese_1\output\test_results_3.txt'
        if path is not None:
            with open(file=path, mode='r+', encoding='utf-8') as file:
                self.textBrowser.setPlainText(file.read())

    def open_event(self):
        _translate = QtCore.QCoreApplication.translate
        directory1 = QFileDialog.getOpenFileName(None, "选择文件", "H:/")
        print(directory1)  # 打印文件夹路径
        path = directory1[0]
        self.open_path.setText(_translate("Form", path))
        if path is not None:
            with open(file=path, mode='r+', encoding='utf-8') as file:
                text = file.read()
                self.textEdit.setText(text)

    def frash(self):
        path = self.open_path.text()
        if (path=='打开文件'):
            content = self.textEdit.toPlainText()
        else :
            file_path = os.path.join(path)  # 获取文件输入内容
            f = open(file_path, 'r', encoding='utf-8')
            content = f.read()
        rawResults = re.findall(">.*?<", content, re.S)
        firstStepResults = []
        for result in rawResults:
            # print(result)
            if ">\'][\'<" in result:
                continue
            if ">:<" in result:
                continue
            if ">回复<" in result:
                continue
            if "><" in result:
                continue
            if ">\', \'<" in result:
                continue
            if "@" in result:
                continue
            if "> <" in result:
                continue
            if "【" in result:
                continue
            if "】" in result:
                continue
            else:
                firstStepResults.append(result)
        subTextHead = re.compile(">")
        subTextFoot = re.compile("<")
        i = 0
        redd = ''
        for lastResult in firstStepResults:
            resultExcel1 = re.sub(subTextHead, '', lastResult)
            resultExcel = re.sub(subTextFoot, '', resultExcel1)
            print(i, resultExcel)
            i += 1
            redd = redd + str(i) +'\t'+resultExcel+'\n'
        self.textBrowser.setPlainText(str(redd))


    def pridect(self):
        gl._init()
        ttt = self.open_path.text()
        gl.set_value('val_path', ttt)
        tt=self.textEdit.toPlainText()
        gl.set_value('val_text', tt)
        print(ttt)
        cf.runn()
        _translate = QtCore.QCoreApplication.translate
        path=r'D:\python\Bert_chinese_1\output\test_results_1.txt'
        if path is not None:
            with open(file=path, mode='r+', encoding='utf-8') as file:
                self.textBrowser.setPlainText(file.read())

    def saveas_event(self):
        _translate = QtCore.QCoreApplication.translate
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "H:/")
        print(fileName2)  # 打印保存文件的全部路径（包括文件名和后缀名）
        save_path = fileName2
        if save_path is not None:
            with open(file=save_path, mode='a+', encoding='utf-8') as file:
                file.write(self.textBrowser.toPlainText())

    def huoqushujv(self):
        for i in range(10):
            url = self.textEdit.toPlainText() + str(i)
            headers = {
                'User-agent': 'your User-agent',
                'Host': 'weibo.cn',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Cookie': '_T_WM=77756778463; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W57QS6ZgyP0WI5q.QVBzS-z5JpX5KzhUgL.Fo-ceh-pShe4S0z2dJLoI0YLxK-LB.-L1h-LxK-L1hnLB-zLxKBLBonL1h.LxKqL1KMLBK-LxKBLBonLBoqLxKBLBonLBoqLxKBLBonLBoqt; H5_wentry=H5; backURL=https%3A%2F%2Fweibo.cn%2F; SCF=AofakrnaZb1BO2o2gVvvm2hwF61aP_CrgaXQaf-q0O8msW9g4IhnjkI_wQzycqKa_jRrHqUDhK95Ovzwok_DC58.; SUB=_2A25zW4gvDeRhGeBP61EV8SfNyDWIHXVQpyhnrDV6PUJbkdAKLRXNkW1NRZjQf2S7xgDtEaZ6HOsAL0xGlIXQXOoO; SUHB=0sqBqy-0iJRFht',
                'DNT': '1',
                'Connection': 'keep-alive'
            }  # 请求头的书写，包括User-agent,Cookie等
            response = requests.get(url, headers=headers, verify=False)  # 利用requests.get命令获取网页html
            html = response.text
            print(html)
            print('正在爬取第 %d 页评论' % (i + 1))
            pattern = re.compile('<span class="ctt">.*?</span>', re.S)
            items = re.findall(pattern, html)
            result = str(items)
            with open(r'D:\python\Bert_chinese_1\output\ttt.txt', 'w', encoding='utf-8') as fp:
                fp.write(result)
            time.sleep(1)
        path = r'D:\python\Bert_chinese_1\output\ttt.txt'
        if path is not None:
            with open(file=path, mode='r+', encoding='utf-8') as file:
                self.textBrowser.setPlainText(file.read())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = translation()
    window.show()
    sys.exit(app.exec_())