import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from textWidget import TextLabelWidget


class TextDraw(QWidget):
    def __init__(self):
        super(TextDraw, self).__init__()
        self.setGeometry(100, 250, 500, 500)

        self.label = TextLabelWidget(self)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label_move = True

    def mouseMoveEvent(self, event):
        if self.label_move:
            self.label.move(event.pos())

        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = TextDraw()
    tool.show()
    sys.exit(app.exec_())