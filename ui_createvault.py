# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createvaulttMhZoj.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(407, 314)
        self.title = QLabel(Dialog)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 0, 401, 71))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 50, 401, 61))
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 130, 201, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.createVaultNameInput = QLineEdit(Dialog)
        self.createVaultNameInput.setObjectName(u"createVaultNameInput")
        self.createVaultNameInput.setGeometry(QRect(200, 130, 181, 41))
        self.createVaultNameInput.setStyleSheet(u"    QLineEdit {\n"
"        font-family: Segoe UI;\n"
"        font-size: 9pt;\n"
"        border-radius: 4px;\n"
"    }\n"
"    \n"
"    QLineEdit {\n"
"        background-color: #ffffff;\n"
"    }\n"
"    \n"
"    QLineEdit {\n"
"        color: #000000;\n"
"    }\n"
"    \n"
"    QLineEdit {\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: #c9c9c9;\n"
"    }\n"
"    \n"
"    QLineEdit {\n"
"        padding-left: 4px;\n"
"        padding-right: 4px;\n"
"    }\n"
"\n"
"    QLineEdit:hover, QLineEdit:focus {\n"
"        background-color: #f2f2f2;\n"
"    }\n"
"\n"
"    QLineEdit::selection {\n"
"        background-color: #0078d7;\n"
"        color: #ffffff;\n"
"    }")
        self.createVaultNameInput.setEchoMode(QLineEdit.Normal)
        self.createVaultFinalButton = QPushButton(Dialog)
        self.createVaultFinalButton.setObjectName(u"createVaultFinalButton")
        self.createVaultFinalButton.setGeometry(QRect(120, 210, 171, 61))
        self.createVaultFinalButton.setStyleSheet(u"QPushButton {\n"
"    font-family: Segoe UI;\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"    color: #ffffff;\n"
"    background-color: #808080;\n"
"    background-image: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #808080, stop: 1 #4d4d4d);\n"
"    border-radius: 8px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #808080;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"    background-image: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 1 #2e2e2e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"    background-image: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2e2e2e, stop: 1 #1c1c1c);\n"
"}\n"
"\n"
"QPushButton:!hover:!pressed {\n"
"    background-color: #808080;\n"
"    background-image: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #808080, stop: 1 #4d4d4d);\n"
"}")
        self.createVaultErrorLabel = QLabel(Dialog)
        self.createVaultErrorLabel.setObjectName(u"createVaultErrorLabel")
        self.createVaultErrorLabel.setGeometry(QRect(0, 270, 401, 41))
        self.createVaultErrorLabel.setFont(font2)
        self.createVaultErrorLabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"ArcaneCrypt", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Create a new Vault here", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.createVaultNameInput.setInputMask("")
        self.createVaultNameInput.setText("")
        self.createVaultFinalButton.setText(QCoreApplication.translate("Dialog", u"Create", None))
        self.createVaultErrorLabel.setText("")
    # retranslateUi

