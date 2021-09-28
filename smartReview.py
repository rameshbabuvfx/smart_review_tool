import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from review_tool_UI.reviewToolUI import Ui_Form

COLORS = [
            '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
            '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
            '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff', '#ff0000',
        ]


class ImageBoard(QWidget):
    def __init__(self):
        super(ImageBoard, self).__init__()

        self.label = QLabel()
        self.image = QPixmap("review_image.jpg")
        self.label.setMaximumHeight(self.image.height())
        self.label.setMaximumWidth(self.image.width())
        self.label.setPixmap(self.image)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.last_point = None
        self.pen_color = "#000000"

    def set_pen_color(self, c):
        self.pen_color = c

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = self.label.mapFromParent(event.pos())

    def mouseMoveEvent(self, event):
        end_point = self.label.mapFromParent(event.pos())
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setColor(QColor(self.pen_color))
        painter.setPen(pen)
        line = QLine(self.last_point, end_point)
        painter.drawLine(line)
        self.last_point = end_point
        self.update()

    def mouseReleaseEvent(self, event):
        self.last_point = None


class QPaletteButton(QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QSize(35, 35))
        self.color = color
        self.setStyleSheet("background-color: {};".format(color))


class ReviewTool(Ui_Form, QWidget):
    def __init__(self):
        super(ReviewTool, self).__init__()
        self.setupUi(self)
        self.image_board = ImageBoard()
        self.resize(self.image_board.image.width(), self.image_board.image.height())
        self.verticalLayout_5.addWidget(self.image_board)
        self.color_pushbutton.clicked.connect(self.open_color_panel)
        self.add_palette_button()

    def add_palette_button(self):
        for count, color in enumerate(COLORS):
            palette_button = QPaletteButton(color)
            palette_button.pressed.connect(lambda c=color: self.image_board.set_pen_color(c))
            if count == 1:
                self.palette_layout.addWidget(palette_button, 0, 1)
            else:
                self.palette_layout.addWidget(palette_button)

    def open_color_panel(self):
        color_dialog = QColorDialog.getColor()
        self.image_board.set_pen_color(color_dialog)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = ReviewTool()
    tool.show()
    sys.exit(app.exec_())
