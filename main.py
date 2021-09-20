import sys

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class WhiteBoard(QLabel):
    def __init__(self):
        super().__init__()
        self.last_point = QPoint()
        self.drawing = None
        self.image = QPixmap(r"C:\Users\rames\Pictures\DBZ\dragonball-z-kakarot-vegeta-fight-cutscene-1.jpg")
        self.setPixmap(self.image)
        self.resize(self.image.width(), self.image.height())

    def paintEvent(self, event):
        self.painter = QPainter(self)
        self.painter.drawPixmap(self.rect(), self.image)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.drawing = True
            pos = event.pos()
            mp = self.mapToGlobal(pos)
            self.last_point = self.mapFromGlobal(mp)

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.drawing:
            print(event.x(), event.y())
            self.painter = QPainter(self.image)

            pen = QPen(Qt.red, 10.0,  Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            self.painter.setPen(pen)
            pos = event.pos()
            mp = self.mapToGlobal(pos)
            self.painter.drawLine(self.last_point,  self.mapFromGlobal(mp))
            self.last_point = self.mapFromGlobal(mp)
            self.update()

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.drawing = False


class ReviewTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 250, 750, 600)
        self.vlayout = QVBoxLayout()
        self.button = QPushButton("Click Here")
        self.button.setMinimumHeight(300)
        board = WhiteBoard()
        widget = QWidget()
        self.vlayout.addWidget(board)
        self.vlayout.addWidget(self.button)
        widget.setLayout(self.vlayout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication()
    window = ReviewTool()
    window.show()
    sys.exit(app.exec_())
