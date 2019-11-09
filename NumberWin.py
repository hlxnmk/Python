# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NumberWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(753, 533)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(90, 20, 541, 421))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.showpic = QtWidgets.QLabel(self.groupBox)
        self.showpic.setGeometry(QtCore.QRect(10, 50, 521, 361))
        self.showpic.setText("")
        self.showpic.setObjectName("showpic")
        self.okBtn = QtWidgets.QPushButton(Form)
        self.okBtn.setGeometry(QtCore.QRect(420, 460, 75, 23))
        self.okBtn.setObjectName("okBtn")
        self.numEdit = QtWidgets.QLineEdit(Form)
        self.numEdit.setGeometry(QtCore.QRect(140, 460, 41, 20))
        self.numEdit.setObjectName("numEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 460, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 460, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.wordEdit = QtWidgets.QLineEdit(Form)
        self.wordEdit.setGeometry(QtCore.QRect(250, 460, 113, 20))
        self.wordEdit.setObjectName("wordEdit")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(520, 460, 75, 23))
        self.clearBtn.setObjectName("clearBtn")

        self.retranslateUi(Form)
        self.clearBtn.clicked.connect(self.showpic.clear)
        self.clearBtn.clicked.connect(self.wordEdit.clear)
        self.okBtn.clicked.connect(Form.showpic)
        self.clearBtn.clicked.connect(Form.shownum)
        self.wordEdit.returnPressed.connect(self.okBtn.click)
        self.clearBtn.clicked.connect(Form.showword)
        self.numEdit.returnPressed.connect(self.okBtn.click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "数字密码图片"))
        self.okBtn.setText(_translate("Form", "确认"))
        self.label.setText(_translate("Form", "数字:"))
        self.label_2.setText(_translate("Form", "文字:"))
        self.clearBtn.setText(_translate("Form", "下一个"))
