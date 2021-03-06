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
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox


class shibie_window(QMainWindow):
    def __init__(self):
        super().__init__()

        print("识别界面生成！")
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

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 800, 150, 46))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openfile)

        self.biaoti = QtWidgets.QLabel(self.centralwidget)
        self.biaoti.setGeometry(QtCore.QRect(450, 60, 700, 700))
        self.biaoti.setObjectName("biaoti")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 800, 150, 46))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.start)

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setFont(QFont("宋体", 14, QFont.Bold))
        self.pushButton_2.setFont(QFont("宋体", 14, QFont.Bold))
        self.pushButton_3.setFont(QFont("宋体", 14, QFont.Bold))
        self.pushButton_4.setFont(QFont("宋体", 14, QFont.Bold))
        self.pushButton.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_2.setText(_translate("MainWindow", "开始识别"))
        self.pushButton_3.setText(_translate("MainWindow", "保存图片"))
        self.pushButton_4.setText(_translate("MainWindow", "返回主界面"))

        self.biaoti.setAlignment(Qt.AlignCenter)
        self.biaoti.setFont(QFont("宋体", 40, QFont.Bold))
        # self.biaoti.setText(_translate("MainWindow", "图 像 识 别"))

    def openfile(self):
        self.imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        print(self.imgName)
        jpg = QtGui.QPixmap(self.imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        

    def start(self):
        im = cv2.imread(self.imgName)

        cfg = get_cfg()
        cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
        cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
        predictor = DefaultPredictor(cfg)
        outputs = predictor(im)

        print(outputs["instances"].pred_classes)
        print(outputs["instances"].pred_boxes)

        v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
        out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        out_image = out.get_image()[:, :, ::-1]
        cv2.imwrite('666.jpg', out_image)

        im2 = QtGui.QPixmap('./666.jpg').scaled(self.label.width(), self.label.height())
        self.label_2.setPixmap(im2)

        i=0
        for box in outputs["instances"].pred_boxes.to('cpu'):
            i += 1
            x0 = int(box[0].item())
            y0 = int(box[1].item())
            x1 = int(box[2].item())
            y1 = int(box[3].item())

            width = x1 - x0
            height = y1 - y0
            fig, ax = plt.subplots()
            img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            im1 = ax.imshow(img)
            patch = patches.Rectangle(
                (x0, y0),
                width,
                height,
                transform=ax.transData
            )
            im1.set_clip_path(patch)
            ax.axis('off')
            plt.savefig(fname="result"+str(i)+".jpg")




    def baocun(self):
        name,type = QFileDialog.getSaveFileName(self, '保存图片')
        msg_box = QMessageBox(QMessageBox.Warning, '提示', '保存成功')
        msg_box.exec_()



