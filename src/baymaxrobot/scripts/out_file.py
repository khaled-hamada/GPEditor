# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baymaxGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(791, 648)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 140, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 190, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 230, 99, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 300, 99, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 140, 99, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 190, 99, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(240, 240, 99, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(40, 160, 131, 151))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 120, 161, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_8 = QtGui.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(240, 300, 99, 27))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(420, 260, 99, 27))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Form.update_position)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.home)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.stop_move)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cancel_goal)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.go_to_goal)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.run_robot)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.build_map)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.teleop)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.shutdown)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.save_map)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "run robot", None))
        self.pushButton_2.setText(_translate("Form", "build a map", None))
        self.pushButton_3.setText(_translate("Form", "move robot m.", None))
        self.pushButton_4.setText(_translate("Form", "shut down", None))
        self.pushButton_5.setText(_translate("Form", "go ", None))
        self.pushButton_6.setText(_translate("Form", "cancel", None))
        self.pushButton_7.setText(_translate("Form", "stop", None))
        self.label.setText(_translate("Form", "enter numbers from 1-5", None))
        self.pushButton_8.setText(_translate("Form", "Home", None))
        self.pushButton_9.setText(_translate("Form", "save map ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

