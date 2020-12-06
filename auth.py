import sys

from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5 import uic
from PyQt5.QtCore import Qt

import requests


class Authorization(QDialog):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("auth.ui", self)
        self.par = parent
        self.setWindowTitle("Вход")
        self.initUI()

    def initUI(self):
        """инициализируем наш класс"""
        self.rejected.connect(self.to_main)
        self.accepted.connect(self.find_in_db)

    def find_in_db(self):
        """Делает запрос и считывает данные из бд"""
        self.login = self.login_label.text().strip()  # логин
        self.password = self.password_label.text().strip()  # пароль
        self.password_right = requests.get("http://localhost:8888/server.php", {'login': self.login, "mode": 'reg'})
        self.password_right = self.password_right.text
        if self.check_password():
            self.hide()
            self.par.show()
        else:
            self.show()

    def check_password(self):
        if not self.password_right:
            self.error_label.setText("Пользователь не найден")
            return False
        if self.password == self.password_right:
            self.par.login = self.login
            name = requests.get("http://localhost:8888/server.php", {'login': self.login, "mode": 'name'})
            self.par.name = name.text
            self.par.after_init()
            return True
        else:
            self.error_label.setText("Неверный пароль")
            return False


    def to_main(self):
        self.par.show()
        self.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F:
            self.showFullScreen()
        if event.key() == Qt.Key_Escape:
            self.showNormal()
