import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from review_tool_UI.reviewToolUI import Ui_Form
from drawingWidget import DrawingWidget
from paletteButton import QPaletteButton

COLORS = [
            '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
            '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
            '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff', '#ff0000',
        ]


class ReviewTool(Ui_Form, QWidget):
    def __init__(self):
        super(ReviewTool, self).__init__()
        self.setupUi(self)
        self.pixmap = None
        self.text_label = None
        self.label_active = None
        self.text_label_status = None
        self.image_board = DrawingWidget()
        self.font_size_combox.addItems([str(size) for size in range(25)])
        self.font_size_combox.setCurrentIndex(10)
        self.verticalLayout_5.addWidget(self.image_board)
        self.color_pushbutton.setIcon(QIcon(r"D:\PythonProjects\NukePython\smart_review_tool\icons\color_palette.png"))
        self.connect_ui()

    def connect_ui(self):
        self.brush_size_slider.valueChanged.connect(self.set_pen_size)
        self.color_pushbutton.clicked.connect(self.open_color_panel)
        self.save_pushbutton.clicked.connect(lambda: self.save_image())
        self.import_pushbutton.clicked.connect(lambda: self.import_image())
        self.clear_pushbutton.clicked.connect(lambda: self.add_image_label())
        self.addtext_pushbutton.clicked.connect(self.launch_text_box)
        self.text_color_pushbutton.clicked.connect(self.set_text_color)
        self.font_combo_box.currentFontChanged.connect(self.set_font_style)
        self.font_size_combox.currentIndexChanged.connect(self.set_font_style)
        self.add_palette_button()

    def add_palette_button(self):
        for count, color in enumerate(COLORS):
            palette_button = QPaletteButton(color)
            self.connect_color_buttons(palette_button, color)
            if count == 1:
                self.palette_layout.addWidget(palette_button, 0, 1)
            else:
                self.palette_layout.addWidget(palette_button)

    def connect_color_buttons(self, palette_button, color):
        palette_button.pressed.connect(lambda: self.image_board.set_pen_color(color))
        palette_button.pressed.connect(lambda: self.set_button_color(color))

    def import_image(self):
        self.image_path, _ = QFileDialog.getOpenFileName(self, "import image")
        if self.image_path:
            self.add_image_label()

    def add_image_label(self):
        self.pixmap = QPixmap(self.image_path)
        if self.pixmap.width() >= 1600 and self.pixmap.height() >= 850:
            self.pixmap = self.pixmap.scaled(1600, 850, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_board.set_image_label(self.pixmap)
        self.image_board.setFixedSize(self.pixmap.size())
        self.setMaximumSize(self.pixmap.size())

    def open_color_panel(self):
        color_dialog = QColorDialog.getColor()

        self.image_board.set_pen_color(color_dialog)
        self.set_button_color(color_dialog.name())

    def set_button_color(self, hex):
        style_sheet = "background-color : {}".format(hex)
        self.color_pushbutton.setStyleSheet(style_sheet)

    def set_pen_size(self):
        pen_size = self.brush_size_slider.value()
        self.image_board.set_pen_size(pen_size)

    def save_image(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*)"
        )
        pix = self.grab(self.image_board.geometry())
        pix.save(file_path, quality=-1)

    def launch_text_box(self):
        if not self.text_label:
            self.text_label = QLabel(self)
            self.text_label.setGeometry(100, 100, 100, 100)
            self.text_label.setText("Add Text Here")
            self.text_label.show()
            self.text_label_status = True
            self.font_dialog()

    def font_dialog(self):
        dialog = QDialog()
        self.text_widget = QTextEdit()
        font_button = QPushButton("Font")
        font_button.clicked.connect(self.set_font_label)
        text_layout = QVBoxLayout()
        text_layout.addWidget(self.text_widget)
        text_layout.addWidget(font_button)
        dialog.setLayout(text_layout)
        self.text_widget.textChanged.connect(self.add_text_label)
        dialog.exec_()

    def add_text_label(self):
        label_text = self.text_widget.toPlainText()
        self.text_label.setText(label_text)
        self.text_label.adjustSize()

    def set_text_color(self):
        color_dialog = QColorDialog.getColor()
        style_sheet = "color : {}".format(color_dialog.name())
        button_style_sheet = "background-color : {}".format(color_dialog.name())
        try:
            self.text_label.setStyleSheet(style_sheet)
        except AttributeError as error:
            print(error)
        self.text_color_pushbutton.setStyleSheet(button_style_sheet)

    def set_font_style(self):
        font_family = self.font_combo_box.currentFont().family()
        font_size = self.font_size_combox.currentText()
        try:
            self.text_label.setStyleSheet("font: {}pt {}".format(font_size, font_family))
        except AttributeError as error:
            print(error)
        self.text_label.adjustSize()

    def set_font_label(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.text_label.setFont(font)
            self.text_label.adjustSize()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.text_label_status:
            self.label_active = True
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.label_active and self.text_label_status:
            self.text_label.move(event.pos())
        else:
            super().mouseMoveEvent(event)
        self.update()

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton and self.label_active:
            self.font_dialog()
        else:
            super().mouseDoubleClickEvent(event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.text_label.close()
            self.text_label = None
        else:
            super().keyPressEvent(event)


def main():
    tool = ReviewTool()
    tool.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = ReviewTool()
    tool.show()
    sys.exit(app.exec_())
