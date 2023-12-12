# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowGBDdre.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(296, 455)
        font = QFont()
        font.setFamilies([u"Meiryo UI"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.status_text = QTextEdit(self.centralwidget)
        self.status_text.setObjectName(u"status_text")
        self.status_text.setMinimumSize(QSize(0, 60))
        self.status_text.setMaximumSize(QSize(16777215, 60))
        self.status_text.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.status_text)

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


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.on_off_button = QPushButton(self.centralwidget)
        self.on_off_button.setObjectName(u"on_off_button")
        self.on_off_button.setFont(font1)

        self.verticalLayout_2.addWidget(self.on_off_button)

        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 6)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 296, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.status_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Meiryo UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">STATUS</span></p></body></html>", None))
        self.fill_radio_button.setText(QCoreApplication.translate("MainWindow", u"FILL", None))
        self.dump_radio_button.setText(QCoreApplication.translate("MainWindow", u"DUMP", None))
        self.ignition_radio_button.setText(QCoreApplication.translate("MainWindow", u"IGNITION", None))
        self.purge_radio_button.setText(QCoreApplication.translate("MainWindow", u"PURGE", None))
        self.on_off_button.setText(QCoreApplication.translate("MainWindow", u"ON", None))
    # retranslateUi

