from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class DrawingWidget(QWidget):
    def __init__(self):
        super(DrawingWidget, self).__init__()

        self.label = QLabel()
        self.image = QPixmap(800, 600)
        self.image.fill(Qt.transparent)
        self.label.setMaximumHeight(self.image.height())
        self.label.setMaximumWidth(self.image.width())

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.last_point = None
        self.pen_color = "#000000"
        self.pen_size = 2

    def set_image_label(self, image_path):
        self.image = image_path
        self.label.setPixmap(self.image)
        self.label.setMaximumHeight(self.image.height())
        self.label.setMaximumWidth(self.image.width())
        self.update()

    def set_pen_color(self, color):
        self.pen_color = color

    def set_pen_size(self, size):
        self.pen_size = size

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = self.label.mapFromParent(event.pos())
            self.drawing = True
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.drawing == True:
            end_point = self.label.mapFromParent(event.pos())
            painter = QPainter(self.image)
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
            print(line)
            painter.drawLine(line)
            self.last_point = end_point
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = None
            self.drawing = False
        else:
            super().mouseReleaseEvent(event)

    def keyPressEvent(self, event):
        print("this is")
        if event.key() == Qt.Key_Z:
            print("this is")

    def paintEvent(self, event):
        self.label.setPixmap(self.image)


# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     tool = DrawingWidget()
#     tool.show()
#     sys.exit(app.exec_())
