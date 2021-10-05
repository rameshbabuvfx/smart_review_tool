from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class DrawingWidget(QWidget):
    def __init__(self):
        super(DrawingWidget, self).__init__()

        self.label = QLabel()
        self.image = QPixmap("review_image.jpg")
        self.label.setPixmap(self.image)
        self.label.resize(self.image.width(), self.image.height())
        print(self.label.geometry())

        self.paint_image = QPixmap(self.image.size())
        self.paint_image.fill(Qt.transparent)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.last_point = None
        self.pen_color = "#000000"
        self.pen_size = 3
        self.change = False

        self.paint_label = QLabel(self)
        self.paint_label.setGeometry(self.label.geometry())
        # self.paint_label.setStyleSheet("background-color: red")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = self.label.mapFromParent(event.pos())
            self.drawing = True
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.drawing:
            end_point = self.label.mapFromParent(event.pos())
            painter = QPainter(self.paint_image)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(
                QPen(
                    QColor(self.pen_color),
                    self.pen_size,
                    Qt.SolidLine,
                    Qt.RoundCap,
                    Qt.RoundJoin
                )
            )
            line = QLine(self.last_point, end_point)
            painter.drawLine(line)
            self.last_point = end_point
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = None
            self.drawing = False
            painter = QPainter(self.paint_image)
            painter.save()
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.eraseRect(100, 100, 100, 100)
            painter.restore()
        else:
            super().mouseReleaseEvent(event)

    def paintEvent(self, event):
        self.paint_label.setPixmap(self.paint_image)

    def change_color(self):
        self.change = not self.change
        if self.change:
            pixmap = QPixmap(QSize(1, 1)*self._clear_size)
            pixmap.fill(Qt.transparent)
            painter = QPainter(pixmap)
            painter.setPen(QPen(Qt.black, 2))
            painter.drawRect(pixmap.rect())
            painter.end()
            cursor = QCursor(pixmap)
            QApplication.setOverrideCursor(cursor)
        else:
            QApplication.restoreOverrideCursor()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    tool = DrawingWidget()
    tool.show()
    sys.exit(app.exec_())
