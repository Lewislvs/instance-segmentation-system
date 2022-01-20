# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'b.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import detectron2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import os, json, cv2, random


# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook




from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog


class jieguo_window(QMainWindow):
    def __init__(self):
        super().__init__()

        print("结果界面生成!")
        MainWindow = self
        self.i = 0
        self.imgName = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 60, 700, 700))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(800, 60, 700, 700))
        self.label_2.setObjectName("label_2")

        self.biaoti = QtWidgets.QLabel(self.centralwidget)
        self.biaoti.setGeometry(QtCore.QRect(450, 60, 700, 700))
        self.biaoti.setObjectName("biaoti")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 800, 150, 46))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openfile)


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 800, 150, 46))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.next_pic)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1100, 800, 150, 46))
        self.pushButton_3.setObjectName("pushButton_3")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setFont(QFont("宋体", 14, QFont.Bold))
        self.pushButton_2.setFont(QFont("宋体", 14, QFont.Bold))
        self.pushButton_3.setFont(QFont("宋体", 14, QFont.Bold))
        self.pushButton.setText(_translate("MainWindow", "展示识别结果"))
        self.pushButton_2.setText(_translate("MainWindow", "展示分割实例"))
        self.pushButton_3.setText(_translate("MainWindow", "返回主界面"))
        self.biaoti.setAlignment(Qt.AlignCenter)
        self.biaoti.setFont(QFont("宋体", 40, QFont.Bold))
        # self.biaoti.setText(_translate("MainWindow", "结 果 分 析"))


    def openfile(self):
        self.imgName = "666.jpg"
        # self.imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        print(self.imgName)
        jpg = QtGui.QPixmap(self.imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

    def next_pic(self):
        self.i += 1
        self.imgName = "result" + str(self.i) + ".jpg"
        jpg = QtGui.QPixmap(self.imgName).scaled(self.label.width(), self.label.height())
        self.label_2.setPixmap(jpg)


