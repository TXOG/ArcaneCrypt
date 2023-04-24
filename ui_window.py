# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowPMfHFp.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

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
        self.passwordInput.setStyleSheet(u"    QLineEdit {\n"
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
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.checkPasswordInput = QLineEdit(self.signupScreen)
        self.checkPasswordInput.setObjectName(u"checkPasswordInput")
        self.checkPasswordInput.setGeometry(QRect(560, 380, 271, 41))
        self.checkPasswordInput.setStyleSheet(u"    QLineEdit {\n"
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
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.createAccountButton.setFont(font3)
        self.createAccountButton.setMouseTracking(True)
        self.createAccountButton.setFocusPolicy(Qt.StrongFocus)
        self.createAccountButton.setStyleSheet(u"QPushButton {\n"
"    font-family: Segoe UI;\n"
"    font-size: 18pt;\n"
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
        self.createAccountErrorLabel = QLabel(self.signupScreen)
        self.createAccountErrorLabel.setObjectName(u"createAccountErrorLabel")
        self.createAccountErrorLabel.setGeometry(QRect(370, 600, 261, 41))
        self.createAccountErrorLabel.setFont(font2)
        self.createAccountErrorLabel.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.signupScreen)
        self.loginScreen = QWidget()
        self.loginScreen.setObjectName(u"loginScreen")
        self.title_2 = QLabel(self.loginScreen)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(0, 0, 971, 161))
        self.title_2.setFont(font)
        self.title_2.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.loginScreen)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 120, 971, 81))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.loginScreen)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 310, 191, 41))
        self.label_5.setFont(font2)
        self.loginInput = QLineEdit(self.loginScreen)
        self.loginInput.setObjectName(u"loginInput")
        self.loginInput.setGeometry(QRect(560, 310, 271, 41))
        self.loginInput.setStyleSheet(u"    QLineEdit {\n"
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
        self.loginInput.setEchoMode(QLineEdit.Password)
        self.loginButton = QPushButton(self.loginScreen)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(360, 480, 271, 111))
        self.loginButton.setFont(font3)
        self.loginButton.setMouseTracking(True)
        self.loginButton.setFocusPolicy(Qt.StrongFocus)
        self.loginButton.setStyleSheet(u"QPushButton {\n"
"    font-family: Segoe UI;\n"
"    font-size: 18pt;\n"
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
        self.loginErrorLabel = QLabel(self.loginScreen)
        self.loginErrorLabel.setObjectName(u"loginErrorLabel")
        self.loginErrorLabel.setGeometry(QRect(370, 600, 261, 41))
        self.loginErrorLabel.setFont(font2)
        self.loginErrorLabel.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.loginScreen)
        self.mainScreen = QWidget()
        self.mainScreen.setObjectName(u"mainScreen")
        self.menuWidget = QWidget(self.mainScreen)
        self.menuWidget.setObjectName(u"menuWidget")
        self.menuWidget.setGeometry(QRect(0, 0, 971, 51))
        self.vaultList = QComboBox(self.menuWidget)
        self.vaultList.setObjectName(u"vaultList")
        self.vaultList.setGeometry(QRect(10, 10, 191, 31))
        self.vaultList.setStyleSheet(u"/* Set the font family and size */\n"
"    QComboBox {\n"
"        font-family: Segoe UI;\n"
"        font-size: 9pt;\n"
"        font-weight: bold;\n"
"        color: #000000;\n"
"        border-radius: 4px;\n"
"        padding: 2px 20px 2px 6px;\n"
"        border: 1px solid #c9c9c9;\n"
"        background-color: #ffffff;\n"
"        selection-background-color: #0078d7;\n"
"        selection-color: #ffffff;\n"
"    }\n"
"    \n"
"    /* Set the background color and gradient */\n"
"    QComboBox::drop-down {\n"
"        background-color: #f2f2f2;\n"
"        border: 1px solid #c9c9c9;\n"
"        border-top-right-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        width: 20px;\n"
"    }\n"
"    \n"
"    /* Set the hover and focus background color */\n"
"    QComboBox:hover, QComboBox:focus {\n"
"        background-color: #f2f2f2;\n"
"        border: 1px solid #0078d7;\n"
"    }\n"
"    \n"
"    /* Set the background color and gradient of the dropdown menu */\n"
"    QComboBox QAbstractItemVi"
                        "ew {\n"
"        background-color: #ffffff;\n"
"        border: 1px solid #c9c9c9;\n"
"        selection-background-color: #0078d7;\n"
"        selection-color: #ffffff;\n"
"    }")
        self.createVaultButton = QPushButton(self.menuWidget)
        self.createVaultButton.setObjectName(u"createVaultButton")
        self.createVaultButton.setGeometry(QRect(224, 13, 131, 31))
        self.createVaultButton.setStyleSheet(u"QPushButton {\n"
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
        self.addVaultButton = QPushButton(self.menuWidget)
        self.addVaultButton.setObjectName(u"addVaultButton")
        self.addVaultButton.setGeometry(QRect(380, 13, 131, 31))
        self.addVaultButton.setStyleSheet(u"QPushButton {\n"
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
        self.vaultStack = QStackedWidget(self.mainScreen)
        self.vaultStack.setObjectName(u"vaultStack")
        self.vaultStack.setGeometry(QRect(0, 49, 971, 621))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, 290, 151, 61))
        self.vaultStack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(410, 320, 101, 51))
        self.vaultStack.addWidget(self.page_2)
        self.stackedWidget.addWidget(self.mainScreen)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.vaultStack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"ArcaneCrypt", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Looks like you haven't created an account yet, you can do that now", None))
        self.passwordInput.setInputMask("")
        self.passwordInput.setText("")
        self.checkPasswordInput.setInputMask("")
        self.checkPasswordInput.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Confirm Password:", None))
        self.createAccountButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.createAccountErrorLabel.setText("")
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"ArcaneCrypt", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Login to your account to view the contents of your Vaults", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.loginInput.setInputMask("")
        self.loginInput.setText("")
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.loginErrorLabel.setText("")
        self.vaultList.setCurrentText("")
        self.createVaultButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.addVaultButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Page1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"page2", None))
    # retranslateUi

