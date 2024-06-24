# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controlDialoglDmitx.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_control_dialog(object):
    def setupUi(self, control_dialog):
        if not control_dialog.objectName():
            control_dialog.setObjectName(u"control_dialog")
        control_dialog.resize(434, 312)
        font = QFont()
        font.setFamilies([u"\u30e1\u30a4\u30ea\u30aa"])
        control_dialog.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(control_dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fill_button = QPushButton(control_dialog)
        self.fill_button.setObjectName(u"fill_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fill_button.sizePolicy().hasHeightForWidth())
        self.fill_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.fill_button)

        self.dump_button = QPushButton(control_dialog)
        self.dump_button.setObjectName(u"dump_button")
        sizePolicy.setHeightForWidth(self.dump_button.sizePolicy().hasHeightForWidth())
        self.dump_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.dump_button)

        self.purge_button = QPushButton(control_dialog)
        self.purge_button.setObjectName(u"purge_button")
        sizePolicy.setHeightForWidth(self.purge_button.sizePolicy().hasHeightForWidth())
        self.purge_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.purge_button)

        self.ignition_button = QPushButton(control_dialog)
        self.ignition_button.setObjectName(u"ignition_button")
        sizePolicy.setHeightForWidth(self.ignition_button.sizePolicy().hasHeightForWidth())
        self.ignition_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ignition_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(control_dialog)

        QMetaObject.connectSlotsByName(control_dialog)
    # setupUi

    def retranslateUi(self, control_dialog):
        control_dialog.setWindowTitle(QCoreApplication.translate("control_dialog", u"Control Dialog", None))
        self.fill_button.setText(QCoreApplication.translate("control_dialog", u"FILL", None))
        self.dump_button.setText(QCoreApplication.translate("control_dialog", u"DUMP", None))
        self.purge_button.setText(QCoreApplication.translate("control_dialog", u"PURGE", None))
        self.ignition_button.setText(QCoreApplication.translate("control_dialog", u"IGNITION", None))
    # retranslateUi

