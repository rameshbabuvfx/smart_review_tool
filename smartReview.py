import os

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
    def __init__(self, image_path=None):
        """
        InIt method for Review tool class.

        :param Str image_path: Image path.
        """
        super(ReviewTool, self).__init__()
        self.setupUi(self)
        self.pixmap = None
        self.label_active = None
        self.text_label = None
        self.image_path = image_path
        self.text_label_status = None
        self.color_dialog = 000000
        self.setWindowTitle("Paint Tool")
        self.image_board = DrawingWidget()
        self.font_size_combox.addItems([str(size) for size in range(35)])
        self.font_size_combox.setCurrentIndex(8)
        self.verticalLayout_5.addWidget(self.image_board)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        icon_path = os.path.dirname(__file__)
        self.color_pushbutton.setIcon(QIcon(os.path.join(icon_path, "icons", "color_palette.png")))
        self.pen_button.setIcon(QIcon(os.path.join(icon_path, "icons", "sketch.png")))
        self.eraser_button.setIcon(QIcon(os.path.join(icon_path, "icons", "eraser.png")))
        self.bold_pushButton.setIcon(QIcon(os.path.join(icon_path, "icons", "bold.png")))
        self.connect_ui()
        if image_path:
            self.add_image_label(self.image_path)
        self.show()

    def connect_ui(self):
        """
        Connects Ui with custom methods.

        :return: None.
        """
        self.brush_size_slider.valueChanged.connect(self.set_pen_size)
        self.color_pushbutton.clicked.connect(self.open_color_panel)
        self.save_pushbutton.clicked.connect(lambda: self.save_image())
        self.import_pushbutton.clicked.connect(lambda: self.import_image())
        self.clear_pushbutton.clicked.connect(lambda: self.add_image_label(self.image_path))
        self.addtext_pushbutton.clicked.connect(self.launch_text_box)
        self.text_color_pushbutton.clicked.connect(lambda: self.set_text_style("pressed"))
        self.font_combo_box.currentFontChanged.connect(self.set_text_style)
        self.font_size_combox.currentIndexChanged.connect(self.set_text_style)
        self.bold_pushButton.clicked.connect(lambda: self.set_text_style(bold_button="pressed"))
        self.pen_button.clicked.connect(lambda: self.image_board.change_mode(eraser=False))
        self.eraser_button.clicked.connect(lambda: self.image_board.change_mode(eraser=True))
        self.add_palette_button()

    def add_palette_button(self):
        """
        Adds Palette buttons in window.

        :return: None.
        """
        for count, color in enumerate(COLORS):
            palette_button = QPaletteButton(color)
            self.connect_color_buttons(palette_button, color)
            if count == 1:
                self.palette_layout.addWidget(palette_button, 0, 1)
            else:
                self.palette_layout.addWidget(palette_button)

    def connect_color_buttons(self, palette_button, color):
        """
        Connects color button with custom menthods.

        :param palette_button: color button.
        :param color: color.
        :return: None.
        """
        palette_button.pressed.connect(lambda: self.image_board.set_pen_color(color))
        palette_button.pressed.connect(lambda: self.set_button_color(color))

    def import_image(self):
        """
        Imports images from file manager.

        :return: None.
        """
        self.image_path, _ = QFileDialog.getOpenFileName(self, "import image")
        if self.image_path:
            self.add_image_label(self.image_path)

    def add_image_label(self, image_path=None):
        """
        Adds image label in main widget.

        :param Str image_path: Path of image.
        :return: None.
        """
        self.pixmap = QPixmap(image_path)
        if self.pixmap.width() >= 1600 and self.pixmap.height() >= 850:
            self.pixmap = self.pixmap.scaled(1600, 850, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_board.set_image_label(self.pixmap)
        self.setMaximumSize(self.pixmap.size())

    def open_color_panel(self):
        """
        Opens color panel

        :return: None.
        """
        color_dialog = QColorDialog.getColor()
        self.image_board.set_pen_color(color_dialog)
        self.set_button_color(color_dialog.name())

    def set_button_color(self, hex):
        """
        Sets color for picker button.

        :param Str hex: Hexa color value.
        :return: None.
        """
        style_sheet = "background-color : {}".format(hex)
        self.color_pushbutton.setStyleSheet(style_sheet)

    def set_pen_size(self):
        """
        Sets pen size.

        :return: None.
        """
        pen_size = self.brush_size_slider.value()
        self.image_board.set_pen_size(pen_size)

    def save_image(self):
        """
        Saves imported image.

        :return: None.
        """
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*)"
        )
        pix = self.grab(self.image_board.geometry())
        pix.save(file_path, quality=-1)

    def launch_text_box(self):
        """
        Opens text box.

        :return: None.
        """
        if not self.text_label:
            self.text_label = QLabel(self)
            self.text_label.setGeometry(100, 100, 100, 10)
            self.text_label.setText("Add Text Here")
            self.text_label.show()
            self.text_label_status = True
            self.font_dialog()

    def font_dialog(self):
        """
        Opens font dialog box.

        :return: None.
        """
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
        """
        Adds text label on image label.

        :return: None.
        """
        label_text = self.text_widget.toPlainText()
        self.text_label.setText(label_text)
        self.text_label.adjustSize()

    def set_text_style(self, color_button="Not pressed", bold_button="Not pressed"):
        """
        Sets the stylesheet for color button.

        :param Str color_button: Status of button.
        :param Str bold_button: Status of Bold button.
        :return: None.
        """
        if color_button == "pressed":
            self.color_dialog = QColorDialog.getColor().name()
        font_family = self.font_combo_box.currentFont().family()
        font_size = self.font_size_combox.currentText()
        bold = 0
        if bold_button == "pressed":
            bold = 75
        style_sheet = """
            color : {};
            font: {} {}pt {};
        """.format(self.color_dialog, bold, font_size, font_family)
        try:
            self.text_label.setStyleSheet(style_sheet)
            self.text_label.adjustSize()
        except AttributeError as error:
            print(error)

    def set_font_label(self):
        """
        Sets font style.

        :return: None.
        """
        ok, font = QFontDialog.getFont()
        if ok:
            self.text_label.setFont(font)
            self.text_label.adjustSize()

    def enterEvent(self, event):
        """
        Changes cursor when mouse enters in text label.

        :param event: Event.
        :return: None.
        """
        try:
            self.text_label.setCursor(QCursor(Qt.OpenHandCursor))
        except:
            pass

    def mousePressEvent(self, event):
        """
        Sets cursor when mouse clicks on text label.

        :param event: Event.
        :return: None.
        """
        if event.button() == Qt.LeftButton and self.text_label_status:
            self.label_active = True
            self.text_label.setCursor(QCursor(Qt.ClosedHandCursor))
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """
        Moves text label as per mouse movement.

        :param event: Event.
        :return: None.
        """
        if self.label_active and self.text_label_status:
            self.text_label.move(event.pos())
        else:
            super().mouseMoveEvent(event)
        self.update()

    def mouseReleaseEvent(self, event):
        """
        Reverts the cursor type when mouse release.

        :param event: Event.
        :return: None.
        """
        if event.button() == Qt.LeftButton and self.text_label_status:
            self.text_label.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseDoubleClickEvent(self, event):
        """
        Opens the dialog box when double clicks on text label.

        :param event: Event.
        :return: None.
        """
        if event.button() == Qt.LeftButton and self.label_active:
            self.font_dialog()
        else:
            super().mouseDoubleClickEvent(event)

    def keyPressEvent(self, event):
        """
        Deletes the text label "Z" when key pressed.

        :param event: Event.
        :return: None.
        """
        if event.key() == Qt.Key_Delete:
            self.text_label.close()
            self.text_label = None
        else:
            super().keyPressEvent(event)


def main():
    review = ReviewTool()
    review.show()
