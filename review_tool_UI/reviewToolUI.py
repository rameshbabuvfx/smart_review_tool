# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reviewToolUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(981, 644)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalFrame = QFrame(self.frame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.import_pushbutton = QPushButton(self.horizontalFrame)
        self.import_pushbutton.setObjectName(u"import_pushbutton")

        self.horizontalLayout.addWidget(self.import_pushbutton)

        self.save_pushbutton = QPushButton(self.horizontalFrame)
        self.save_pushbutton.setObjectName(u"save_pushbutton")

        self.horizontalLayout.addWidget(self.save_pushbutton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pen_icon_label = QLabel(self.horizontalFrame)
        self.pen_icon_label.setObjectName(u"pen_icon_label")

        self.horizontalLayout.addWidget(self.pen_icon_label)

        self.brush_size_slider = QSlider(self.horizontalFrame)
        self.brush_size_slider.setObjectName(u"brush_size_slider")
        self.brush_size_slider.setMaximumSize(QSize(100, 16777215))
        self.brush_size_slider.setMinimum(10)
        self.brush_size_slider.setMaximum(20)
        self.brush_size_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.brush_size_slider)

        self.addtext_pushbutton = QPushButton(self.horizontalFrame)
        self.addtext_pushbutton.setObjectName(u"addtext_pushbutton")

        self.horizontalLayout.addWidget(self.addtext_pushbutton)

        self.text_color_pushbutton = QPushButton(self.horizontalFrame)
        self.text_color_pushbutton.setObjectName(u"text_color_pushbutton")

        self.horizontalLayout.addWidget(self.text_color_pushbutton)

        self.font_combo_box = QFontComboBox(self.horizontalFrame)
        self.font_combo_box.setObjectName(u"font_combo_box")
        self.font_combo_box.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.font_combo_box)

        self.font_size_combox = QComboBox(self.horizontalFrame)
        self.font_size_combox.setObjectName(u"font_size_combox")

        self.horizontalLayout.addWidget(self.font_size_combox)

        self.bold_pushButton = QPushButton(self.horizontalFrame)
        self.bold_pushButton.setObjectName(u"bold_pushButton")
        self.bold_pushButton.setMinimumSize(QSize(40, 0))
        self.bold_pushButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.bold_pushButton)


        self.verticalLayout.addWidget(self.horizontalFrame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, -1, 10, -1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalFrame_2 = QFrame(self.frame)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setMaximumSize(QSize(120, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.pen_button = QPushButton(self.verticalFrame_2)
        self.pen_button.setObjectName(u"pen_button")
        self.pen_button.setMinimumSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.pen_button)

        self.eraser_button = QPushButton(self.verticalFrame_2)
        self.eraser_button.setObjectName(u"eraser_button")
        self.eraser_button.setMinimumSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.eraser_button)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(14, -1, 14, -1)
        self.clear_pushbutton = QPushButton(self.verticalFrame_2)
        self.clear_pushbutton.setObjectName(u"clear_pushbutton")
        self.clear_pushbutton.setMinimumSize(QSize(70, 0))
        self.clear_pushbutton.setMaximumSize(QSize(70, 16777215))

        self.verticalLayout_3.addWidget(self.clear_pushbutton)

        self.color_pushbutton = QPushButton(self.verticalFrame_2)
        self.color_pushbutton.setObjectName(u"color_pushbutton")
        self.color_pushbutton.setMinimumSize(QSize(70, 70))
        self.color_pushbutton.setMaximumSize(QSize(70, 16777215))
        self.color_pushbutton.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.color_pushbutton)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.palette_layout = QGridLayout()
        self.palette_layout.setObjectName(u"palette_layout")
        self.palette_layout.setHorizontalSpacing(10)
        self.palette_layout.setVerticalSpacing(5)
        self.palette_layout.setContentsMargins(0, 0, -1, 0)

        self.verticalLayout_6.addLayout(self.palette_layout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.verticalFrame_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.import_pushbutton.setText(QCoreApplication.translate("Form", u"Import", None))
        self.save_pushbutton.setText(QCoreApplication.translate("Form", u"save", None))
        self.pen_icon_label.setText(QCoreApplication.translate("Form", u"Size", None))
        self.addtext_pushbutton.setText(QCoreApplication.translate("Form", u"Add Text", None))
        self.text_color_pushbutton.setText(QCoreApplication.translate("Form", u"Text Color", None))
        self.bold_pushButton.setText("")
        self.pen_button.setText("")
        self.eraser_button.setText("")
        self.clear_pushbutton.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.color_pushbutton.setText(QCoreApplication.translate("Form", u"Picker", None))
    # retranslateUi

