# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'uiGCFAZd.ui'
##
# Created by: Qt User Interface Compiler version 5.15.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.label)

        self.links = QLineEdit(self.centralwidget)
        self.links.setObjectName(u"links")

        self.horizontalLayout_2.addWidget(self.links)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setSizeIncrement(QSize(5, 0))
        self.line.setBaseSize(QSize(5, 0))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.min_size = QLineEdit(self.centralwidget)
        self.min_size.setObjectName(u"min_size")

        self.horizontalLayout.addWidget(self.min_size)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.start_scan = QPushButton(self.centralwidget)
        self.start_scan.setObjectName(u"start_scan")

        self.horizontalLayout.addWidget(self.start_scan)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate(
            "mainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("mainWindow", u"MD5", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate(
            "mainWindow", u"\u5927\u5c0f", None))
        self.label.setText(QCoreApplication.translate(
            "mainWindow", u"\u626b\u63cf\u8def\u5f84", None))
        self.label_2.setText(QCoreApplication.translate(
            "mainWindow", u"\u6700\u5c0f\u6587\u4ef6\u5927\u5c0f(M)", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "mainWindow", u"\u5feb\u901f\u626b\u63cf", None))
        self.start_scan.setText(QCoreApplication.translate(
            "mainWindow", u"\u5b8c\u6574\u626b\u63cf", None))
        self.pushButton.setText(QCoreApplication.translate(
            "mainWindow", u"\u5f00\u59cb\u94fe\u63a5", None))
    # retranslateUi
