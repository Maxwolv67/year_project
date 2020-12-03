import sys

from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt


class Light(QDialog):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("light.ui", self)
        self.par = parent
        self.initUI()


    def initUI(self):
        """инициализируем наш класс"""
        self.rejected.connect(self.to_main)
        self.accepted.connect(self.to_main)

    def to_main(self):
        self.hide()
        self.par.show()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F:
            self.showFullScreen()
        if event.key() == Qt.Key_Escape:
            self.showNormal()
