# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storjupload.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(666, 257)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 661, 71))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 351, 18))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.bt_upload = QtGui.QPushButton(Dialog)
        self.bt_upload.setGeometry(QtCore.QRect(10, 170, 191, 31))
        self.bt_upload.setObjectName(_fromUtf8("bt_upload"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(220, 170, 421, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.bt_cancel = QtGui.QPushButton(Dialog)
        self.bt_cancel.setGeometry(QtCore.QRect(510, 220, 131, 21))
        self.bt_cancel.setObjectName(_fromUtf8("bt_cancel"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 120, 501, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 111, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.bt_file_select = QtGui.QPushButton(Dialog)
        self.bt_file_select.setGeometry(QtCore.QRect(560, 120, 88, 34))
        self.bt_file_select.setObjectName(_fromUtf8("bt_file_select"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(230, 190, 61, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 190, 301, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(550, 10, 111, 41))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(550, 60, 111, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(160, 60, 351, 18))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("GUI for uploading files to Storj Network", "GUI for uploading files to Storj Network", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">GUI for uploading files to Storj Network</span></p><p><span style=\" font-size:11pt;\">(Alpha Version)</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ea0000;\">Currently only one file can be uploaded in the same time </span></p></body></html>", None))
        self.bt_upload.setText(_translate("Dialog", "Upload file!", None))
        self.bt_cancel.setText(_translate("Dialog", "Cancel", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Patch to file:</span></p></body></html>", None))
        self.bt_file_select.setText(_translate("Dialog", "Select file...", None))
        self.label_4.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Status:</span></p></body></html>",
                                        None))
        self.label_5.setText(
            _translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Idle</span></p></body></html>",
                       None))

        self.toolButton.setText(_translate("Dialog", "Settings", None))
        self.pushButton.setText(_translate("Dialog", "Logs", None))
        self.label_6.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" color:#ea0000;\">If upload seems stuck, please check detailed logs</span></p></body></html>",
                                        None))

