# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ControlPanelhEiWlQ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_ControlPanel(object):
    def setupUi(self, ControlPanel):
        if not ControlPanel.objectName():
            ControlPanel.setObjectName(u"ControlPanel")
        ControlPanel.resize(640, 480)
        self.action_socket_settings = QAction(ControlPanel)
        self.action_socket_settings.setObjectName(u"action_socket_settings")
        self.action_connect = QAction(ControlPanel)
        self.action_connect.setObjectName(u"action_connect")
        self.action_disconnect = QAction(ControlPanel)
        self.action_disconnect.setObjectName(u"action_disconnect")
        self.action_help = QAction(ControlPanel)
        self.action_help.setObjectName(u"action_help")
        self.action_about_qt = QAction(ControlPanel)
        self.action_about_qt.setObjectName(u"action_about_qt")
        self.centralwidget = QWidget(ControlPanel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fill_button = QPushButton(self.centralwidget)
        self.fill_button.setObjectName(u"fill_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fill_button.sizePolicy().hasHeightForWidth())
        self.fill_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.fill_button)

        self.dump_button = QPushButton(self.centralwidget)
        self.dump_button.setObjectName(u"dump_button")
        sizePolicy.setHeightForWidth(self.dump_button.sizePolicy().hasHeightForWidth())
        self.dump_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.dump_button)

        self.purge_button = QPushButton(self.centralwidget)
        self.purge_button.setObjectName(u"purge_button")
        sizePolicy.setHeightForWidth(self.purge_button.sizePolicy().hasHeightForWidth())
        self.purge_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.purge_button)

        self.ignition_button = QPushButton(self.centralwidget)
        self.ignition_button.setObjectName(u"ignition_button")
        sizePolicy.setHeightForWidth(self.ignition_button.sizePolicy().hasHeightForWidth())
        self.ignition_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ignition_button)


        self.horizontalLayout.addLayout(self.verticalLayout)

        ControlPanel.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ControlPanel)
        self.statusbar.setObjectName(u"statusbar")
        ControlPanel.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(ControlPanel)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 22))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        ControlPanel.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSettings.addAction(self.action_socket_settings)
        self.menuSettings.addAction(self.action_connect)
        self.menuSettings.addAction(self.action_disconnect)
        self.menuHelp.addAction(self.action_about_qt)
        self.menuHelp.addAction(self.action_help)

        self.retranslateUi(ControlPanel)

        QMetaObject.connectSlotsByName(ControlPanel)
    # setupUi

    def retranslateUi(self, ControlPanel):
        ControlPanel.setWindowTitle(QCoreApplication.translate("ControlPanel", u"ControlPanel", None))
        self.action_socket_settings.setText(QCoreApplication.translate("ControlPanel", u"TCP/IP", None))
        self.action_connect.setText(QCoreApplication.translate("ControlPanel", u"connect", None))
        self.action_disconnect.setText(QCoreApplication.translate("ControlPanel", u"disconnect", None))
        self.action_help.setText(QCoreApplication.translate("ControlPanel", u"Help", None))
        self.action_about_qt.setText(QCoreApplication.translate("ControlPanel", u"About Qt", None))
        self.fill_button.setText(QCoreApplication.translate("ControlPanel", u"FILL", None))
        self.dump_button.setText(QCoreApplication.translate("ControlPanel", u"DUMP", None))
        self.purge_button.setText(QCoreApplication.translate("ControlPanel", u"PURGE", None))
        self.ignition_button.setText(QCoreApplication.translate("ControlPanel", u"IGNITION", None))
        self.menuSettings.setTitle(QCoreApplication.translate("ControlPanel", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("ControlPanel", u"Help", None))
    # retranslateUi

