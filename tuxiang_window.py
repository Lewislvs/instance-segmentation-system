import sys
import cv2 as cv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox


class tuxiang_window(QMainWindow):
    def __init__(self):
        super().__init__()
        MainWindow = self
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
        self.pushButton.setGeometry(QtCore.QRect(300, 800, 150, 46))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openfile)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 800, 150, 46))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openfile_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(900, 800, 150, 46))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.baocun)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1200, 800, 150, 46))
        self.pushButton_4.setObjectName("pushButton_4")

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

        self.camera = cv.VideoCapture(0)
        self.is_camera_opened = False  # ??????????????????????????????

        # ????????????30ms????????????
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._queryFrame)
        self._timer.setInterval(30)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setFont(QFont("??????", 14, QFont.Bold))
        self.pushButton_2.setFont(QFont("??????", 14, QFont.Bold))
        self.pushButton_3.setFont(QFont("??????", 14, QFont.Bold))
        self.pushButton_4.setFont(QFont("??????", 14, QFont.Bold))
        self.pushButton.setText(_translate("MainWindow", "???????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "????????????"))
        self.pushButton_4.setText(_translate("MainWindow", "???????????????"))

        self.biaoti.setAlignment(Qt.AlignCenter)
        self.biaoti.setFont(QFont("??????", 40, QFont.Bold))
        self.biaoti.setText(_translate("MainWindow", "??? ??? ??? ???"))

    def openfile(self):
        self.imgName, imgType = QFileDialog.getOpenFileName(self, "????????????", "", "*.jpg;;*.png;;All Files(*)")
        print(self.imgName)
        jpg = QtGui.QPixmap(self.imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

    def openfile_2(self):
        jpg = QtGui.QPixmap(self.imgName).scaled(self.label.width(), self.label.height())
        self.label_2.setPixmap(jpg)

    def baocun(self):
        name, type = QFileDialog.getSaveFileName(self, '????????????')
        msg_box = QMessageBox(QMessageBox.Warning, '??????', '????????????')
        msg_box.exec_()

    def btnOpenCamera_Clicked(self):
        '''
        ????????????????????????
        '''
        self.is_camera_opened = ~self.is_camera_opened
        if self.is_camera_opened:
            self.btnOpenCamera.setText("???????????????")
            self._timer.start()
        else:
            self.btnOpenCamera.setText("???????????????")
            self._timer.stop()

    def btnCapture_Clicked(self):
        '''
        ????????????
        '''
        # ??????????????????????????????????????????
        if not self.is_camera_opened:
            return

        self.captured = self.frame
        rows, cols, channels = self.captured.shape
        bytesPerLine = channels * cols
        # Qt????????????????????????????????????QImgage??????
        QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
        self.labelCapture.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def btnReadImage_Clicked(self):
        '''
        ?????????????????????
        '''
        # ???????????????????????????
        filename, _ = QFileDialog.getOpenFileName(self, '????????????')
        if filename:
            self.captured = cv.imread(str(filename))
            # OpenCV?????????BGR?????????????????????????????????BGR??????RGB
            self.captured = cv.cvtColor(self.captured, cv.COLOR_BGR2RGB)

            rows, cols, channels = self.captured.shape
            bytesPerLine = channels * cols
            QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
            self.labelCapture.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def _queryFrame(self):
        '''
        ??????????????????
        '''
        ret, self.frame = self.camera.read()

        img_rows, img_cols, channels = self.frame.shape
        bytesPerLine = channels * img_cols

        cv.cvtColor(self.frame, cv.COLOR_BGR2RGB, self.frame)
        QImg = QImage(self.frame.data, img_cols, img_rows, bytesPerLine, QImage.Format_RGB888)
        self.labelCamera.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelCamera.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
