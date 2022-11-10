from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(328, 285)
        MainWindow.setWindowOpacity(0.9)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 321, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 221, 31))

        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 10, 71, 31))

        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(20, 49, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)

        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 80, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)

        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 110, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)

        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 140, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 170, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_5.setFont(font)

        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 200, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_6.setFont(font)

        self.checkBox_6.setObjectName("checkBox_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 328, 26))

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CryptoPass"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.checkBox.setText(_translate("MainWindow", "ABC"))
        self.checkBox_2.setText(_translate("MainWindow", "abc"))
        self.checkBox_3.setText(_translate("MainWindow", "АБВ"))
        self.checkBox_4.setText(_translate("MainWindow", "абв"))
        self.checkBox_5.setText(_translate("MainWindow", "123"))
        self.checkBox_6.setText(_translate("MainWindow", "?%№"))
