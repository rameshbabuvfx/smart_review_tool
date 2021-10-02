import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class TextLabelWidget(QLabel):
    def __init__(self, parent):
        super(TextLabelWidget, self).__init__(parent)
        self.setGeometry(100, 250, 500, 500)
        self.setText("This looks odd change to the normal color and text this add thiss part  netrain nadakam ")
        self.setWordWrap(True)
        self.adjustSize()

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.label_move = True
    #
    # def mouseMoveEvent(self, event):
    #     if self.label_move and Qt.LeftButton:
    #         self.move(event.pos())
    #         print(event.pos())
    #
    # def mouseReleaseEvent(self, event):
    #     if self.label_move:
    #         self.label_move = False

