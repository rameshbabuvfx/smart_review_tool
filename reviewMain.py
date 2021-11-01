import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import smartReview
from review_tool_UI import reviewMainUI


class ReviewWindow(reviewMainUI.Ui_Form, QWidget):
    def __init__(self):
        super(ReviewWindow, self).__init__()
        self.setupUi(self)
        self.screen_grab_pushButton.clicked.connect(self.review_paint_tool)
        self.launch_tool_pushButton.clicked.connect(self.launch_review_tool)

    @staticmethod
    def review_paint_tool():
        """
        Runs Screenshot class.

        :return: None
        """
        ScreenShot()

    def launch_review_tool(self):
        """
        Runs Review tool class.

        :return:
        """
        smartReview.ReviewTool()


class ScreenShot(QWidget):
    def __init__(self):
        super(ScreenShot, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet('''background-color:white; ''')
        self.setWindowOpacity(0.7)
        self.showMaximized()
        self.isDrawing = False
        self.setCursor(Qt.CrossCursor)
        self.startPoint = QPoint()
        self.endPoint = QPoint()
        self.show()

    def paintEvent(self, event):
        """
        Paint Event draws the widget.

        :param event: Event.
        :return: None.
        """
        self.bmask = QBitmap(self.geometry().size())
        self.bmask.fill(Qt.black)
        self.mask = self.bmask.copy()
        mask_painter = QPainter(self.mask)
        pen = QPen()
        pen.setStyle(Qt.NoPen)
        mask_painter.setPen(pen)
        brush = QBrush(Qt.white)
        mask_painter.setBrush(brush)
        mask_painter.drawRect(QRect(self.startPoint, self.endPoint))
        self.setMask(QBitmap(self.mask))

    def mousePressEvent(self, event):
        """
        Enables the drawing mode.

        :param event: Event.
        :return: None.
        """
        if event.button() == Qt.LeftButton:

            self.startPoint = event.pos()
            self.endPoint = self.startPoint
            self.isDrawing = True

    def mouseMoveEvent(self, event):
        """
        Draws the rect on the widget.

        :param event: Event
        :return: None.
        """
        if self.isDrawing:
            self.endPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        """
        Saves the screenshots to given path.

        :param event: Event.
        :return: None.
        """
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            main_window_id = QApplication.desktop().winId()
            long_win_id = main_window_id
            screenshot = QPixmap.grabWindow(long_win_id)
            rect = QRect(self.startPoint, self.endPoint)
            output_region = screenshot.copy(rect)
            temp_path = os.path.dirname(__file__)
            temp_path = "{}/_cache/temp.png".format(temp_path)
            output_region.save(temp_path, format='JPG', quality=100)
            saved_image = (QPixmap(temp_path).scaled(1580, 1020, Qt.KeepAspectRatio))
            self.resize(saved_image.width(), saved_image.height())
            self.close()
            smartReview.ReviewTool(temp_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = ReviewWindow()
    tool.show()
    sys.exit(app.exec_())
