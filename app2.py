# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os,sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.path =""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(30, 80, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name.setObjectName("name")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(30, 180, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.email.setObjectName("email")
        self.mobile = QtWidgets.QLabel(self.centralwidget)
        self.mobile.setGeometry(QtCore.QRect(30, 240, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mobile.setFont(font)
        self.mobile.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mobile.setObjectName("mobile")
        self.dateofbirth = QtWidgets.QLabel(self.centralwidget)
        self.dateofbirth.setGeometry(QtCore.QRect(30, 310, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateofbirth.setFont(font)
        self.dateofbirth.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dateofbirth.setObjectName("dateofbirth")
        self.getpredict = QtWidgets.QPushButton(self.centralwidget)
        self.getpredict.setGeometry(QtCore.QRect(30, 360, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.getpredict.setFont(font)
        self.getpredict.setObjectName("getpredict")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(230, 360, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 420, 641, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 530, 461, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 90, 531, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 190, 531, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 250, 531, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 320, 531, 27))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 140, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.name_2 = QtWidgets.QLabel(self.centralwidget)
        self.name_2.setGeometry(QtCore.QRect(30, 130, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_2.setFont(font)
        self.name_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name_2.setObjectName("name_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 20, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 25))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chest Xray System"))
        self.name.setText(_translate("MainWindow", "Name of Patient"))
        self.email.setText(_translate("MainWindow", "Email Id"))
        self.mobile.setText(_translate("MainWindow", "MOBILE"))
        self.dateofbirth.setText(_translate("MainWindow", "Date of birth"))
        self.getpredict.setText(_translate("MainWindow", "Get Prediction"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "**Note no validations are encrypted so please input the correct info."))
        self.pushButton.setText(_translate("MainWindow", "Choose File"))
        self.name_2.setText(_translate("MainWindow", "Upload Chest-Xray image"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Chest X-Ray System Check</span></p></body></html>"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.pushButton.clicked.connect(self.choose_file)
        self.getpredict.clicked.connect(self.get_prediction)
        self.reset.clicked.connect(self.reset_values)

    def choose_file(self):
        print("1")
        self.open_dialog_box()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        #print(self.path + '1')
        #with open(path,'r') as f:
            #print(f.readlines())
    def load_path(self):
        print("Path of file-" + self.path)

    def get_prediction(self):
        self.load_path()
        self.show_name()

    def show_name(self):
        text="hi "+self.lineEdit.text()
        print(text)
        text2 = "Your email id is "+self.lineEdit_2.text()
        print(text2)
        text3 = "Your mobile No. is " + self.lineEdit_3.text()
        print(text3)
        text4 = "Your Date of Birth is" + self.lineEdit_4.text()
        print(text4)
        text5 = text + ' ' + text2 +' '+ text3 +' '+ text4
        self.textBrowser.setText(text5)
    
    def reset_values(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.textBrowser.setText("")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
