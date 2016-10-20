# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storj_uploader_config.ui'
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

class Ui_config(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(835, 304)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(25, 255, 786, 34))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.RestoreDefaults|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 15, 521, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 331, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(375, 65, 126, 32))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 361, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.spinBox_2 = QtGui.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(405, 105, 96, 32))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 156, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(205, 145, 296, 32))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 175, 521, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 215, 131, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 210, 646, 32))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Storj Uploader Configuration", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Settings - program for uploading files to Storj Network</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Number of mirrors, which must be created:</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Number of active connections at the same time:</span></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Your Storj password:</span></p></body></html>", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Advanced</span></p></body></html>", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Storj command:</span></p></body></html>", None))
        self.lineEdit_2.setText(_translate("Dialog", "storj", None))
