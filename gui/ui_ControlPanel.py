# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ControlPanelKtMPFJ.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateTimeEdit, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
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

        self.data_time_edit = QDateTimeEdit(self.centralwidget)
        self.data_time_edit.setObjectName(u"data_time_edit")
        self.data_time_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_time_edit.setReadOnly(True)
        self.data_time_edit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.data_time_edit.setCurrentSection(QDateTimeEdit.Section.YearSection)

        self.horizontalLayout_5.addWidget(self.data_time_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.open_n2o_fill_button = QPushButton(self.centralwidget)
        self.open_n2o_fill_button.setObjectName(u"open_n2o_fill_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_n2o_fill_button.sizePolicy().hasHeightForWidth())
        self.open_n2o_fill_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.open_n2o_fill_button)

        self.close_n2o_fill_button = QPushButton(self.centralwidget)
        self.close_n2o_fill_button.setObjectName(u"close_n2o_fill_button")
        sizePolicy.setHeightForWidth(self.close_n2o_fill_button.sizePolicy().hasHeightForWidth())
        self.close_n2o_fill_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.close_n2o_fill_button)

        self.n2o_fill_label = QLabel(self.centralwidget)
        self.n2o_fill_label.setObjectName(u"n2o_fill_label")
        self.n2o_fill_label.setFrameShape(QFrame.Shape.Box)
        self.n2o_fill_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.n2o_fill_label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.open_n2o_dump_button = QPushButton(self.centralwidget)
        self.open_n2o_dump_button.setObjectName(u"open_n2o_dump_button")
        sizePolicy.setHeightForWidth(self.open_n2o_dump_button.sizePolicy().hasHeightForWidth())
        self.open_n2o_dump_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.open_n2o_dump_button)

        self.close_n2o_dump_button = QPushButton(self.centralwidget)
        self.close_n2o_dump_button.setObjectName(u"close_n2o_dump_button")
        sizePolicy.setHeightForWidth(self.close_n2o_dump_button.sizePolicy().hasHeightForWidth())
        self.close_n2o_dump_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.close_n2o_dump_button)

        self.n2o_dump_label = QLabel(self.centralwidget)
        self.n2o_dump_label.setObjectName(u"n2o_dump_label")
        self.n2o_dump_label.setFrameShape(QFrame.Shape.Box)
        self.n2o_dump_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.n2o_dump_label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.open_o2_fill_button = QPushButton(self.centralwidget)
        self.open_o2_fill_button.setObjectName(u"open_o2_fill_button")
        sizePolicy.setHeightForWidth(self.open_o2_fill_button.sizePolicy().hasHeightForWidth())
        self.open_o2_fill_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.open_o2_fill_button)

        self.close_o2_fill_button = QPushButton(self.centralwidget)
        self.close_o2_fill_button.setObjectName(u"close_o2_fill_button")
        sizePolicy.setHeightForWidth(self.close_o2_fill_button.sizePolicy().hasHeightForWidth())
        self.close_o2_fill_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.close_o2_fill_button)

        self.o2_fill_label = QLabel(self.centralwidget)
        self.o2_fill_label.setObjectName(u"o2_fill_label")
        self.o2_fill_label.setFrameShape(QFrame.Shape.Box)
        self.o2_fill_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.o2_fill_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.on_ignition_button = QPushButton(self.centralwidget)
        self.on_ignition_button.setObjectName(u"on_ignition_button")
        sizePolicy.setHeightForWidth(self.on_ignition_button.sizePolicy().hasHeightForWidth())
        self.on_ignition_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.on_ignition_button)

        self.off_ignition_button = QPushButton(self.centralwidget)
        self.off_ignition_button.setObjectName(u"off_ignition_button")
        sizePolicy.setHeightForWidth(self.off_ignition_button.sizePolicy().hasHeightForWidth())
        self.off_ignition_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.off_ignition_button)

        self.ignition_label = QLabel(self.centralwidget)
        self.ignition_label.setObjectName(u"ignition_label")
        self.ignition_label.setFrameShape(QFrame.Shape.Box)
        self.ignition_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.ignition_label)


        self.verticalLayout.addLayout(self.horizontalLayout)


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
        self.data_time_edit.setDisplayFormat(QCoreApplication.translate("ControlPanel", u"yyyy/MM/dd H:mm:ss", None))
        self.open_n2o_fill_button.setText(QCoreApplication.translate("ControlPanel", u"N2O_FILL_OPEN", None))
        self.close_n2o_fill_button.setText(QCoreApplication.translate("ControlPanel", u"N2O_FILL_CLOSE", None))
        self.n2o_fill_label.setText(QCoreApplication.translate("ControlPanel", u"OPEN", None))
        self.open_n2o_dump_button.setText(QCoreApplication.translate("ControlPanel", u"N2O_DUMP_OPEN", None))
        self.close_n2o_dump_button.setText(QCoreApplication.translate("ControlPanel", u"N2O_DUMP_CLOSE", None))
        self.n2o_dump_label.setText(QCoreApplication.translate("ControlPanel", u"OPEN", None))
        self.open_o2_fill_button.setText(QCoreApplication.translate("ControlPanel", u"O2_FILL_OPEN", None))
        self.close_o2_fill_button.setText(QCoreApplication.translate("ControlPanel", u"O2_FILL_CLOSE", None))
        self.o2_fill_label.setText(QCoreApplication.translate("ControlPanel", u"OPEN", None))
        self.on_ignition_button.setText(QCoreApplication.translate("ControlPanel", u"IGNITION_ON", None))
        self.off_ignition_button.setText(QCoreApplication.translate("ControlPanel", u"IGNITION_OFF", None))
        self.ignition_label.setText(QCoreApplication.translate("ControlPanel", u"OPEN", None))
        self.menuSettings.setTitle(QCoreApplication.translate("ControlPanel", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("ControlPanel", u"Help", None))
    # retranslateUi

