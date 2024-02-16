# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

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
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.thrust_meter_view = PlotWidget(self.centralwidget)
        self.thrust_meter_view.setObjectName(u"thrust_meter_view")

        self.verticalLayout_3.addWidget(self.thrust_meter_view)

        self.thermometer_view = PlotWidget(self.centralwidget)
        self.thermometer_view.setObjectName(u"thermometer_view")

        self.verticalLayout_3.addWidget(self.thermometer_view)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.thrust_label = QLabel(self.centralwidget)
        self.thrust_label.setObjectName(u"thrust_label")
        self.thrust_label.setFrameShape(QFrame.Box)

        self.verticalLayout_2.addWidget(self.thrust_label)

        self.temp_label = QLabel(self.centralwidget)
        self.temp_label.setObjectName(u"temp_label")
        self.temp_label.setFrameShape(QFrame.Box)

        self.verticalLayout_2.addWidget(self.temp_label)

        self.pressure_label = QLabel(self.centralwidget)
        self.pressure_label.setObjectName(u"pressure_label")
        self.pressure_label.setFrameShape(QFrame.Box)

        self.verticalLayout_2.addWidget(self.pressure_label)

        self.fill_label = QLabel(self.centralwidget)
        self.fill_label.setObjectName(u"fill_label")
        self.fill_label.setFrameShape(QFrame.Box)

        self.verticalLayout_2.addWidget(self.fill_label)

        self.dump_label = QLabel(self.centralwidget)
        self.dump_label.setObjectName(u"dump_label")
        self.dump_label.setFrameShape(QFrame.Box)

        self.verticalLayout_2.addWidget(self.dump_label)

        self.ignition_label = QLabel(self.centralwidget)
        self.ignition_label.setObjectName(u"ignition_label")
        self.ignition_label.setFrameShape(QFrame.Box)

        self.verticalLayout_2.addWidget(self.ignition_label)

        self.purge_label = QLabel(self.centralwidget)
        self.purge_label.setObjectName(u"purge_label")
        self.purge_label.setFrameShape(QFrame.Box)

        self.verticalLayout_2.addWidget(self.purge_label)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fill_radio_button = QRadioButton(self.centralwidget)
        self.fill_radio_button.setObjectName(u"fill_radio_button")
        self.fill_radio_button.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Meiryo UI"])
        font1.setPointSize(32)
        font1.setBold(True)
        self.fill_radio_button.setFont(font1)

        self.verticalLayout.addWidget(self.fill_radio_button)

        self.dump_radio_button = QRadioButton(self.centralwidget)
        self.dump_radio_button.setObjectName(u"dump_radio_button")
        self.dump_radio_button.setMinimumSize(QSize(0, 30))
        self.dump_radio_button.setFont(font1)

        self.verticalLayout.addWidget(self.dump_radio_button)

        self.ignition_radio_button = QRadioButton(self.centralwidget)
        self.ignition_radio_button.setObjectName(u"ignition_radio_button")
        self.ignition_radio_button.setMinimumSize(QSize(0, 30))
        self.ignition_radio_button.setFont(font1)

        self.verticalLayout.addWidget(self.ignition_radio_button)

        self.purge_radio_button = QRadioButton(self.centralwidget)
        self.purge_radio_button.setObjectName(u"purge_radio_button")
        self.purge_radio_button.setMinimumSize(QSize(0, 30))
        self.purge_radio_button.setFont(font1)

        self.verticalLayout.addWidget(self.purge_radio_button)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.on_off_button = QPushButton(self.centralwidget)
        self.on_off_button.setObjectName(u"on_off_button")
        self.on_off_button.setFont(font1)

        self.verticalLayout_4.addWidget(self.on_off_button)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 23))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.thrust_label.setText(QCoreApplication.translate("MainWindow", u"thrust: 500N", None))
        self.temp_label.setText(QCoreApplication.translate("MainWindow", u"temp: 20\u2103", None))
        self.pressure_label.setText(QCoreApplication.translate("MainWindow", u"pressure: 1kPa", None))
        self.fill_label.setText(QCoreApplication.translate("MainWindow", u"FILL", None))
        self.dump_label.setText(QCoreApplication.translate("MainWindow", u"DUMP", None))
        self.ignition_label.setText(QCoreApplication.translate("MainWindow", u"IGNITION", None))
        self.purge_label.setText(QCoreApplication.translate("MainWindow", u"PURGE", None))
        self.fill_radio_button.setText(QCoreApplication.translate("MainWindow", u"FILL", None))
        self.dump_radio_button.setText(QCoreApplication.translate("MainWindow", u"DUMP", None))
        self.ignition_radio_button.setText(QCoreApplication.translate("MainWindow", u"IGNITION", None))
        self.purge_radio_button.setText(QCoreApplication.translate("MainWindow", u"PURGE", None))
        self.on_off_button.setText(QCoreApplication.translate("MainWindow", u"ON", None))
    # retranslateUi

