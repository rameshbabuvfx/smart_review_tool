from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class QPaletteButton(QPushButton):
    def __init__(self, color):
        """
        Creates the palette buttons.

        :param color: Color of button.
        """
        super(QPaletteButton, self).__init__()
        self.setFixedSize(QSize(35, 35))
        self.color = color
        self.setStyleSheet("background-color: {};".format(color))
