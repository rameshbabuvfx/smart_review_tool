# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reviewMainUI.ui',
# licensing of 'reviewMainUI.ui' applies.
#
# Created: Tue Oct 12 23:29:51 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(494, 572)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.screen_grab_pushButton = QtWidgets.QPushButton(Form)
        self.screen_grab_pushButton.setMinimumSize(QtCore.QSize(0, 150))
        self.screen_grab_pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.screen_grab_pushButton.setObjectName("screen_grab_pushButton")
        self.gridLayout.addWidget(self.screen_grab_pushButton, 0, 0, 1, 1)
        self.launch_tool_pushButton = QtWidgets.QPushButton(Form)
        self.launch_tool_pushButton.setMinimumSize(QtCore.QSize(0, 150))
        self.launch_tool_pushButton.setObjectName("launch_tool_pushButton")
        self.gridLayout.addWidget(self.launch_tool_pushButton, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.screen_grab_pushButton.setText(QtWidgets.QApplication.translate("Form", "Screen Grab", None, -1))
        self.launch_tool_pushButton.setText(QtWidgets.QApplication.translate("Form", "Launch Paint", None, -1))

