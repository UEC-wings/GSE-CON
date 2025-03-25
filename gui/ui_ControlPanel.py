# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ControlPanelYWXZqL.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

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
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.current_connection_label = QLabel(self.centralwidget)
        self.current_connection_label.setObjectName(u"current_connection_label")
        self.current_connection_label.setFrameShape(QFrame.Shape.Box)
        self.current_connection_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.current_connection_label)

        self.current_status_label = QLabel(self.centralwidget)
        self.current_status_label.setObjectName(u"current_status_label")
        self.current_status_label.setFrameShape(QFrame.Shape.Box)
        self.current_status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.current_status_label)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.n2o_fill_button = QPushButton(self.centralwidget)
        self.n2o_fill_button.setObjectName(u"n2o_fill_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n2o_fill_button.sizePolicy().hasHeightForWidth())
        self.n2o_fill_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.n2o_fill_button)

        self.n2o_fill_label = QLabel(self.centralwidget)
        self.n2o_fill_label.setObjectName(u"n2o_fill_label")
        self.n2o_fill_label.setFrameShape(QFrame.Shape.Box)
        self.n2o_fill_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.n2o_fill_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.n2o_dump_button = QPushButton(self.centralwidget)
        self.n2o_dump_button.setObjectName(u"n2o_dump_button")
        sizePolicy.setHeightForWidth(self.n2o_dump_button.sizePolicy().hasHeightForWidth())
        self.n2o_dump_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.n2o_dump_button)

        self.n2o_dump_label = QLabel(self.centralwidget)
        self.n2o_dump_label.setObjectName(u"n2o_dump_label")
        self.n2o_dump_label.setFrameShape(QFrame.Shape.Box)
        self.n2o_dump_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.n2o_dump_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.o2_fill_button = QPushButton(self.centralwidget)
        self.o2_fill_button.setObjectName(u"o2_fill_button")
        sizePolicy.setHeightForWidth(self.o2_fill_button.sizePolicy().hasHeightForWidth())
        self.o2_fill_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.o2_fill_button)

        self.o2_fill_label = QLabel(self.centralwidget)
        self.o2_fill_label.setObjectName(u"o2_fill_label")
        self.o2_fill_label.setFrameShape(QFrame.Shape.Box)
        self.o2_fill_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.o2_fill_label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ignition_button = QPushButton(self.centralwidget)
        self.ignition_button.setObjectName(u"ignition_button")
        sizePolicy.setHeightForWidth(self.ignition_button.sizePolicy().hasHeightForWidth())
        self.ignition_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.ignition_button)

        self.ignition_label = QLabel(self.centralwidget)
        self.ignition_label.setObjectName(u"ignition_label")
        self.ignition_label.setFrameShape(QFrame.Shape.Box)
        self.ignition_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.ignition_label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        ControlPanel.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ControlPanel)
        self.statusbar.setObjectName(u"statusbar")
        ControlPanel.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(ControlPanel)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 33))
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
        self.current_connection_label.setText(QCoreApplication.translate("ControlPanel", u"DISCONNECT", None))
        self.current_status_label.setText(QCoreApplication.translate("ControlPanel", u"CURRENT STATUS", None))
        self.n2o_fill_button.setText(QCoreApplication.translate("ControlPanel", u"N2O_FILL", None))
        self.n2o_fill_label.setText(QCoreApplication.translate("ControlPanel", u"OPEN", None))
        self.n2o_dump_button.setText(QCoreApplication.translate("ControlPanel", u"N2O_DUMP", None))
        self.n2o_dump_label.setText(QCoreApplication.translate("ControlPanel", u"OPEN", None))
        self.o2_fill_button.setText(QCoreApplication.translate("ControlPanel", u"O2_FILL", None))
        self.o2_fill_label.setText(QCoreApplication.translate("ControlPanel", u"OPEN", None))
        self.ignition_button.setText(QCoreApplication.translate("ControlPanel", u"IGNITION", None))
        self.ignition_label.setText(QCoreApplication.translate("ControlPanel", u"OPEN", None))
        self.menuSettings.setTitle(QCoreApplication.translate("ControlPanel", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("ControlPanel", u"Help", None))
    # retranslateUi

