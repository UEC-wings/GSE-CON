# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowZFJgIu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        font = QFont()
        font.setFamilies([u"Meiryo UI"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.thrust_meter_view = PlotWidget(self.centralwidget)
        self.thrust_meter_view.setObjectName(u"thrust_meter_view")

        self.verticalLayout_3.addWidget(self.thrust_meter_view)

        self.thermometer_view = PlotWidget(self.centralwidget)
        self.thermometer_view.setObjectName(u"thermometer_view")

        self.verticalLayout_3.addWidget(self.thermometer_view)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.thrust_label = QLabel(self.centralwidget)
        self.thrust_label.setObjectName(u"thrust_label")
        self.thrust_label.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout.addWidget(self.thrust_label)

        self.temp_label = QLabel(self.centralwidget)
        self.temp_label.setObjectName(u"temp_label")
        self.temp_label.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout.addWidget(self.temp_label)

        self.pressure_label = QLabel(self.centralwidget)
        self.pressure_label.setObjectName(u"pressure_label")
        self.pressure_label.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout.addWidget(self.pressure_label)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 9)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.thrust_label.setText(QCoreApplication.translate("MainWindow", u"thrust: 500N", None))
        self.temp_label.setText(QCoreApplication.translate("MainWindow", u"temp: 20\u2103", None))
        self.pressure_label.setText(QCoreApplication.translate("MainWindow", u"pressure: 1kPa", None))
    # retranslateUi

