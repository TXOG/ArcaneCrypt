import os
import sys
from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtWebEngineCore import *
from PySide6.QtNetwork import QNetworkCookieJar, QNetworkCookie
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QPoint, QRect
import sys
from PySide6 import QtWidgets
import threading
from ui_window import Ui_MainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QByteArray

import hashlib
from os.path import exists


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs, parent=parent)
        self.setupUi(self)

        # Create an instance of the UI from ui_window.py
        self.ui = Ui_MainWindow()

        if exists('setupdone.ivd'):
            self.stackedWidget.setCurrentWidget(self.loginScreen)

        self.createAccountButton.clicked.connect(self.createAccount)

    def createAccount(self):
        if self.passwordInput.text() == self.checkPasswordInput.text():
            password = self.passwordInput.text()
            password = password.encode('utf-8')
            hashed = hashlib.sha512(password).hexdigest()
            file = open('password.ivp', 'w+')
            writehashed = str(hashed)
            file.write(writehashed)
            file.close()
            file = open('setupdone.ivd', 'w+')
            file.close()
            file = open('openfile.ivd', 'w+')
            file.write("NONE")
            file.close()
            self.stackedWidget.setCurrentWidget(self.loginScreen)
        else:
            self.createAccountErrorLabel.setText("Passwords don't match")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
