# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowrksKdr.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(971, 670)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 971, 671))
        self.signupScreen = QWidget()
        self.signupScreen.setObjectName(u"signupScreen")
        self.title = QLabel(self.signupScreen)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 0, 971, 161))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.signupScreen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 120, 971, 81))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.passwordInput = QLineEdit(self.signupScreen)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(560, 310, 271, 41))
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.checkPasswordInput = QLineEdit(self.signupScreen)
        self.checkPasswordInput.setObjectName(u"checkPasswordInput")
        self.checkPasswordInput.setGeometry(QRect(560, 380, 271, 41))
        self.checkPasswordInput.setEchoMode(QLineEdit.Password)
        self.label_2 = QLabel(self.signupScreen)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 310, 191, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.signupScreen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 380, 191, 41))
        self.label_3.setFont(font2)
        self.createAccountButton = QPushButton(self.signupScreen)
        self.createAccountButton.setObjectName(u"createAccountButton")
        self.createAccountButton.setGeometry(QRect(360, 480, 271, 111))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.createAccountButton.setFont(font3)
        self.createAccountButton.setMouseTracking(False)
        self.createAccountButton.setFocusPolicy(Qt.StrongFocus)
        self.createAccountErrorLabel = QLabel(self.signupScreen)
        self.createAccountErrorLabel.setObjectName(u"createAccountErrorLabel")
        self.createAccountErrorLabel.setGeometry(QRect(370, 600, 261, 41))
        self.createAccountErrorLabel.setFont(font2)
        self.createAccountErrorLabel.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.signupScreen)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"LockWarden", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Looks like you haven't created an account yet, you can do that now", None))
        self.passwordInput.setInputMask("")
        self.passwordInput.setText("")
        self.checkPasswordInput.setInputMask("")
        self.checkPasswordInput.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Confirm Password:", None))
        self.createAccountButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.createAccountErrorLabel.setText("")
    # retranslateUi

