import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class TextDraw(QWidget):
    def __init__(self):
        super(TextDraw, self).__init__()
        self.label = QLabel()
        self.image = QPixmap("review_image.jpg")
        self.label.setPixmap(self.image)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.draw_text()

    def draw_text(self):
        painter = QPainter(self.image)
        painter.setPen(QPen(QColor(Qt.red), 5))
        painter.drawText(50, 50, "Kanna")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.move = True

    def mouseMoveEvent(self, event):


    def paintEvent(self, event):
        self.label.setPixmap(self.image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = TextDraw()
    tool.show()
    sys.exit(app.exec_())