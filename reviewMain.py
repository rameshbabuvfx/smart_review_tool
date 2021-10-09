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

    def review_paint_tool(self):
        smartReview.main()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = ReviewWindow()
    tool.show()
    sys.exit(app.exec_())
