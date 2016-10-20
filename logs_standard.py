# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logs_standard.ui'
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

class Ui_log_form(object):
    def setupUi(self, log_form):
        log_form.setObjectName(_fromUtf8("log_form"))
        log_form.resize(871, 328)
        self.buttonBox = QtGui.QDialogButtonBox(log_form)
        self.buttonBox.setGeometry(QtCore.QRect(30, 280, 821, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(log_form)
        self.label.setGeometry(QtCore.QRect(50, 20, 201, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.treeWidget = QtGui.QTreeWidget(log_form)
        self.treeWidget.setGeometry(QtCore.QRect(40, 70, 801, 192))
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.label_2 = QtGui.QLabel(log_form)
        self.label_2.setGeometry(QtCore.QRect(530, 20, 131, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(log_form)
        self.label_3.setGeometry(QtCore.QRect(670, 20, 131, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(log_form)
        self.pushButton.setGeometry(QtCore.QRect(40, 280, 88, 34))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(log_form)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 280, 88, 34))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(log_form)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 20, 141, 34))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(log_form)

        QtCore.QMetaObject.connectSlotsByName(log_form)

    def retranslateUi(self, log_form):
        log_form.setWindowTitle(_translate("log_form", "Standard logs - Storj Uploader", None))
        self.label.setText(_translate("log_form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Event log - standard</span></p></body></html>", None))
        self.treeWidget.headerItem().setText(0, _translate("log_form", "Date", None))
        self.treeWidget.headerItem().setText(1, _translate("log_form", "Event", None))
        self.label_2.setText(_translate("log_form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#298300;\">Current status:</span></p></body></html>", None))
        self.label_3.setText(_translate("log_form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#d3980e;\">Idle</span></p></body></html>", None))
        self.pushButton.setText(_translate("log_form", "Save logs", None))
        self.pushButton_2.setText(_translate("log_form", "Clear logs", None))
        self.pushButton_3.setText(_translate("log_form", "Open detailed log", None))
