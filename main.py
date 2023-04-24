import os
import sys
import time

from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtWebEngineCore import *
from PySide6.QtNetwork import QNetworkCookieJar, QNetworkCookie
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QDialog
from PySide6.QtCore import Qt, QPoint, QRect
from PySide6 import QtWidgets
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QByteArray
from PySide6.QtCore import QDir

from ui_window import Ui_MainWindow
from ui_createvault import Ui_Dialog

import hashlib
from os.path import exists
import threading


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs, parent=parent)
        self.setupUi(self)

        # Create an instance of the UI from ui_window.py
        self.ui = Ui_MainWindow()


        self.vaultStack.removeWidget(self.page)
        self.page.deleteLater()
        self.vaultStack.removeWidget(self.page_2)
        self.page_2.deleteLater()

        if exists('setupdone.ivd'):
            self.stackedWidget.setCurrentWidget(self.loginScreen)

        self.createAccountButton.clicked.connect(self.createAccount)
        self.loginButton.clicked.connect(self.login)
        self.createVaultButton.clicked.connect(self.openCreateVaultWindow)

        vault_dir = QDir.currentPath() + "/Vaults"
        vault_folders = [f for f in os.listdir(vault_dir) if os.path.isdir(os.path.join(vault_dir, f))]

        for folder_name in vault_folders:
            folder_path = os.path.join(vault_dir, folder_name)
            self.vaultList.addItem(folder_name)
            newPage = QWidget()
            newPage.setObjectName(f"{folder_name}")
            self.vaultStack.addWidget(newPage)
            newLabel = QLabel(folder_name, parent=newPage)
            newLabel.setGeometry(QRect(410, 320, 101, 51))
            layout = QVBoxLayout(newPage)
            layout.addWidget(newLabel)

    def createAccount(self):
        if not self.passwordInput.text():
            self.createAccountErrorLabel.setText("Password can't be empty")
            return
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

    def login(self):
        file = open('password.ivp', 'r')
        checkhash = file.read()
        file.close()
        passwordcheck = hashlib.sha512(self.loginInput.text().encode('utf-8')).hexdigest()
        if str(passwordcheck) == str(checkhash):
            checkVaultThread = threading.Thread(target=self.checkVaultChange)
            checkVaultThread.start()
            self.stackedWidget.setCurrentWidget(self.mainScreen)
        else:
            self.loginErrorLabel.setText("Incorrect password")

    def checkVaultChange(self):
        currentVault = self.vaultList.currentText()
        pages = [self.vaultStack.widget(i) for i in range(self.vaultStack.count())]
        while True:
            selectedVault = self.vaultList.currentText()
            if selectedVault != currentVault:
                for i, page in enumerate(pages):
                    if page.objectName() == selectedVault:
                        self.vaultStack.setCurrentIndex(i)
                        break
                currentVault = selectedVault
            else:
                pass
            time.sleep(0.2)



    def openCreateVaultWindow(self):
        global vaultWindow
        vaultWindow = CreateVault()
        vaultWindow.show()
        return vaultWindow


class CreateVault(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None, *args, obj=None, **kwargs):
        super(CreateVault, self).__init__(parent=parent, *args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("ArcaneCrypt")

        self.createVaultFinalButton.clicked.connect(self.createVault)

    def createVault(self):
        checkDir = ('Vaults/' + self.createVaultNameInput.text() + '/')
        if not os.path.isdir(checkDir):
            try:
                os.mkdir(checkDir)
                self.createVaultErrorLabel.setText('Vault "' + self.createVaultNameInput.text() + '" created')
            except Exception as e:
                self.createVaultErrorLabel.setText("Error " + e)
        else:
            self.createVaultErrorLabel.setText("Vault name already exists")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("ArcaneCrypt")
    window.show()
    sys.exit(app.exec())
