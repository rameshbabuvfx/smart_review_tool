from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        top, left, width, height = 400, 400, 800, 600
        self.setWindowTitle("MyPainter")
        self.setGeometry(top, left, width, height)

        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_ARGB32)
        self.image.fill(QtCore.Qt.white)
        self.imageDraw = QtGui.QImage(self.size(), QtGui.QImage.Format_ARGB32)
        self.imageDraw.fill(QtCore.Qt.transparent)

        self.drawing = False
        self.brushSize = 2
        self._clear_size = 20
        self.brushColor = QtGui.QColor(QtCore.Qt.black)
        self.lastPoint = QtCore.QPoint()

        self.change = False
        mainMenu = self.menuBar()
        changeColour = mainMenu.addMenu("changeColour")
        changeColourAction = QtWidgets.QAction("change", self)
        changeColour.addAction(changeColourAction)
        changeColourAction.triggered.connect(self.changeColour)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and QtCore.Qt.LeftButton and self.drawing:
            painter = QtGui.QPainter(self.imageDraw)
            painter.setPen(QtGui.QPen(
                self.brushColor,
                self.brushSize,
                QtCore.Qt.SolidLine,
                QtCore.Qt.RoundCap,
                QtCore.Qt.RoundJoin
            )
            )
            if self.change:
                r = QtCore.QRect(QtCore.QPoint(), self._clear_size*QtCore.QSize())
                r.moveCenter(event.pos())
                painter.save()
                painter.setCompositionMode(QtGui.QPainter.CompositionMode_Clear)
                painter.eraseRect(r)
                painter.restore()
            else:
                painter.drawLine(self.lastPoint, event.pos())
            painter.end()
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == QtCore.Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QtGui.QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
        canvasPainter.drawImage(self.rect(), self.imageDraw, self.imageDraw.rect())

    def changeColour(self):
        self.change = not self.change
        if self.change:
            pixmap = QtGui.QPixmap(QtCore.QSize(1, 1)*self._clear_size)
            pixmap.fill(QtCore.Qt.transparent)
            painter = QtGui.QPainter(pixmap)
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 2))
            painter.drawRect(pixmap.rect())
            painter.end()
            cursor = QtGui.QCursor(pixmap)
            QtWidgets.QApplication.setOverrideCursor(cursor)
        else:
            QtWidgets.QApplication.restoreOverrideCursor()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())