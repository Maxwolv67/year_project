import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QButtonGroup, QVBoxLayout
from PyQt5 import uic
from PyQt5.QtCore import Qt
from light import Light
import requests
#from auth import Authorization

class Admin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("admin.ui", self)
        self.setWindowTitle("Админка")
        self.initUI()

    def initUI(self):
        """инициализируем наш класс"""
        pass

    def authorization(self):
        """открывает окно входа"""
        if self.auth.text() == "Вход":
            self.hide()
            #self.x = Authorization(self)
            #self.x.show()
        else:
            self.name_label.setText("Неизвестный")
            self.auth.setText("Вход")

    def after_init(self):
        self.name_label.setText(self.name)
        self.auth.setText("Выход")

    def which_button(self, button):
        """Смотрит по названию, какая кнопка была нажата"""
        text = button.text()
        print(button.text())
        if text == "Освещение":
            self.l = Light(self)
            self.l.show()
            self.hide()


    def fill_in_hand(self):
        """Эта функция будет заполнять кнопками устройств, которые будут во вкладке с ручными режимами"""
        self.widget = QWidget()
        self.scroll_hand.setWidget(self.widget)
        self.layout_Area = QVBoxLayout(self.widget)

        for i in self.all_devices:
            self.button = QPushButton(i)
            self.button.setDisabled(False)
            self.button.setStyleSheet("""font-size: 25px;
                                        border-radius: 10px; 
                                        background-color: 
                                        rgb(150, 150, 255); 
                                        color: rgb(255, 255, 255)""")
            self.button.setMinimumHeight(40)

            self.group_buttons_hand.addButton(self.button)
            self.layout_Area.addWidget(self.button)

    def keyPressEvent(self, event):
        """Отслеживает нажатия клавиш"""
        if event.key() == Qt.Key_F:
            self.showFullScreen()
        if event.key() == Qt.Key_Escape:
            self.showNormal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Admin()
    ex.show()
    sys.exit(app.exec())
