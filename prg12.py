# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prg12.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 404)
        MainWindow.setStyleSheet("background-color:rgb(43, 43, 43)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.passwordi = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordi.setGeometry(QtCore.QRect(130, 200, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordi.setFont(font)
        self.passwordi.setStyleSheet("border:solid rgb(175, 175, 175);\n"
"border-radius: 6px;\n"
"background-color: white;\n"
"color: black;\n"
"TextInput.Password")
        self.passwordi.setText("")
        self.passwordi.setObjectName("passwordi")
        self.pbtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn2.setGeometry(QtCore.QRect(140, 310, 181, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbtn2.setFont(font)
        self.pbtn2.setStyleSheet("QPushButton{\n"
"    background-color:rgba(95, 95, 95, 70)\n"
"}\n"
"QPushButton::hover{\n"
"    background-color:rgba(172, 115, 172, 80);\n"
"    color: white;\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgba(220, 109, 165, 80);\n"
"    color: black;\n"
"}")
        self.pbtn2.setObjectName("pbtn2")
        self.logini = QtWidgets.QLineEdit(self.centralwidget)
        self.logini.setGeometry(QtCore.QRect(130, 150, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.logini.setFont(font)
        self.logini.setStyleSheet("border:solid rgb(175, 175, 175);\n"
"border-radius: 6px;\n"
"background-color: white;\n"
"color: black;")
        self.logini.setText("")
        self.logini.setObjectName("logini")
        self.pbtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn1.setGeometry(QtCore.QRect(130, 250, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pbtn1.setFont(font)
        self.pbtn1.setStyleSheet("QPushButton{\n"
"    background-color:rgba(95, 95, 95, 70)\n"
"}\n"
"QPushButton::hover{\n"
"    background-color:rgba(172, 115, 172, 80);\n"
"    color: white;\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color:rgba(220, 109, 165, 80);\n"
"    color: black;\n"
"}")
        self.pbtn1.setObjectName("pbtn1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 105, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.passwordi.setPlaceholderText(_translate("MainWindow", "Пароль..."))
        self.pbtn2.setText(_translate("MainWindow", "Регистрация"))
        self.logini.setPlaceholderText(_translate("MainWindow", "Логин..."))
        self.pbtn1.setText(_translate("MainWindow", "Войти"))
        self.label_2.setText(_translate("MainWindow", "label_2"))
        self.label.setText(_translate("MainWindow", "label"))