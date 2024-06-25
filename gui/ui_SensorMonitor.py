# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SensorMonitorSyVwOm.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateTimeEdit, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_SensorMonitor(object):
    def setupUi(self, SensorMonitor):
        if not SensorMonitor.objectName():
            SensorMonitor.setObjectName(u"SensorMonitor")
        SensorMonitor.resize(1280, 720)
        font = QFont()
        font.setFamilies([u"Meiryo UI"])
        SensorMonitor.setFont(font)
        self.centralwidget = QWidget(SensorMonitor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.thrust_view = PlotWidget(self.centralwidget)
        self.thrust_view.setObjectName(u"thrust_view")

        self.gridLayout.addWidget(self.thrust_view, 0, 0, 1, 1)

        self.pressure_view = PlotWidget(self.centralwidget)
        self.pressure_view.setObjectName(u"pressure_view")

        self.gridLayout.addWidget(self.pressure_view, 0, 1, 1, 1)

        self.thermo_view = PlotWidget(self.centralwidget)
        self.thermo_view.setObjectName(u"thermo_view")

        self.gridLayout.addWidget(self.thermo_view, 1, 0, 1, 1)

        self.thermo_view_2 = PlotWidget(self.centralwidget)
        self.thermo_view_2.setObjectName(u"thermo_view_2")

        self.gridLayout.addWidget(self.thermo_view_2, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setFrame(True)
        self.dateTimeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.verticalLayout.addWidget(self.dateTimeEdit)

        self.thrust_label = QLabel(self.centralwidget)
        self.thrust_label.setObjectName(u"thrust_label")
        self.thrust_label.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout.addWidget(self.thrust_label)

        self.temp_label = QLabel(self.centralwidget)
        self.temp_label.setObjectName(u"temp_label")
        self.temp_label.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout.addWidget(self.temp_label)

        self.temp_label_2 = QLabel(self.centralwidget)
        self.temp_label_2.setObjectName(u"temp_label_2")
        self.temp_label_2.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout.addWidget(self.temp_label_2)

        self.pressure_label = QLabel(self.centralwidget)
        self.pressure_label.setObjectName(u"pressure_label")
        self.pressure_label.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout.addWidget(self.pressure_label)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        SensorMonitor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SensorMonitor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 22))
        SensorMonitor.setMenuBar(self.menubar)

        self.retranslateUi(SensorMonitor)

        QMetaObject.connectSlotsByName(SensorMonitor)
    # setupUi

    def retranslateUi(self, SensorMonitor):
        SensorMonitor.setWindowTitle(QCoreApplication.translate("SensorMonitor", u"SensorMonitor", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("SensorMonitor", u"yyyy/MM/dd H:mm:ss", None))
        self.thrust_label.setText(QCoreApplication.translate("SensorMonitor", u"thrust: 500N", None))
        self.temp_label.setText(QCoreApplication.translate("SensorMonitor", u"temp: 20\u2103", None))
        self.temp_label_2.setText(QCoreApplication.translate("SensorMonitor", u"temp2: 20\u2103", None))
        self.pressure_label.setText(QCoreApplication.translate("SensorMonitor", u"pressure: 1kPa", None))
    # retranslateUi

