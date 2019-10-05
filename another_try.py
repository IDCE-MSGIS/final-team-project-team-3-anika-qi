# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'script2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_output_lable(object):
    def setupUi(self, output_lable):
        output_lable.setObjectName("output_lable")
        output_lable.resize(594, 905)
        font = QtGui.QFont()
        font.setPointSize(15)
        output_lable.setFont(font)
        self.input_location = QtWidgets.QLabel(output_lable)
        self.input_location.setGeometry(QtCore.QRect(30, 10, 431, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.input_location.setFont(font)
        self.input_location.setObjectName("input_location")
        self.input_button = QtWidgets.QPushButton(output_lable)
        self.input_button.setGeometry(QtCore.QRect(430, 100, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_button.setFont(font)
        self.input_button.setObjectName("input_button")
        self.cityname = QtWidgets.QTextEdit(output_lable)
        self.cityname.setGeometry(QtCore.QRect(50, 90, 321, 51))
        self.cityname.setObjectName("cityname")
        self.label_2 = QtWidgets.QLabel(output_lable)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(output_lable)
        self.textBrowser.setGeometry(QtCore.QRect(50, 210, 491, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(output_lable)
        self.label.setGeometry(QtCore.QRect(30, 640, 211, 51))
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(output_lable)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 700, 501, 151))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(output_lable)
        QtCore.QMetaObject.connectSlotsByName(output_lable)

    def retranslateUi(self, output_lable):
        _translate = QtCore.QCoreApplication.translate
        output_lable.setWindowTitle(_translate("output_lable", "Dialog"))
        self.input_location.setText(_translate("output_lable", "Please enter a city name："))
        self.input_button.setText(_translate("output_lable", "OK"))
        self.label_2.setText(_translate("output_lable", "Weather Today:"))
        self.label.setText(_translate("output_lable", "Clothes advice："))

