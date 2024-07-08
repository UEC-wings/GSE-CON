# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SocketSettingsDialogPOGhjm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SocketSettingsDialog(object):
    def setupUi(self, SocketSettingsDialog):
        if not SocketSettingsDialog.objectName():
            SocketSettingsDialog.setObjectName(u"SocketSettingsDialog")
        SocketSettingsDialog.setEnabled(True)
        SocketSettingsDialog.resize(400, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SocketSettingsDialog.sizePolicy().hasHeightForWidth())
        SocketSettingsDialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u30e1\u30a4\u30ea\u30aa"])
        SocketSettingsDialog.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(SocketSettingsDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(SocketSettingsDialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"\u30e1\u30a4\u30ea\u30aa"])
        font1.setPointSize(9)
        self.label.setFont(font1)
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.addr_line_edit = QLineEdit(SocketSettingsDialog)
        self.addr_line_edit.setObjectName(u"addr_line_edit")

        self.horizontalLayout_2.addWidget(self.addr_line_edit)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(SocketSettingsDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.port_line_edit = QLineEdit(SocketSettingsDialog)
        self.port_line_edit.setObjectName(u"port_line_edit")

        self.horizontalLayout.addWidget(self.port_line_edit)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(SocketSettingsDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setFrameShape(QFrame.Shape.NoFrame)
        self.label_3.setFrameShadow(QFrame.Shadow.Plain)
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(0)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.socket_type_combo_box = QComboBox(SocketSettingsDialog)
        self.socket_type_combo_box.addItem("")
        self.socket_type_combo_box.addItem("")
        self.socket_type_combo_box.setObjectName(u"socket_type_combo_box")

        self.horizontalLayout_5.addWidget(self.socket_type_combo_box)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.apply_button = QPushButton(SocketSettingsDialog)
        self.apply_button.setObjectName(u"apply_button")

        self.horizontalLayout_3.addWidget(self.apply_button)

        self.cancel_button = QPushButton(SocketSettingsDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_3.addWidget(self.cancel_button)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(SocketSettingsDialog)

        QMetaObject.connectSlotsByName(SocketSettingsDialog)
    # setupUi

    def retranslateUi(self, SocketSettingsDialog):
        SocketSettingsDialog.setWindowTitle(QCoreApplication.translate("SocketSettingsDialog", u"TCP/IP", None))
        self.label.setText(QCoreApplication.translate("SocketSettingsDialog", u"IP Address", None))
        self.label_2.setText(QCoreApplication.translate("SocketSettingsDialog", u"Port", None))
        self.label_3.setText(QCoreApplication.translate("SocketSettingsDialog", u"Socket", None))
        self.socket_type_combo_box.setItemText(0, QCoreApplication.translate("SocketSettingsDialog", u"TCP", None))
        self.socket_type_combo_box.setItemText(1, QCoreApplication.translate("SocketSettingsDialog", u"UDP", None))

        self.apply_button.setText(QCoreApplication.translate("SocketSettingsDialog", u"Apply", None))
        self.cancel_button.setText(QCoreApplication.translate("SocketSettingsDialog", u"Cancel", None))
    # retranslateUi

