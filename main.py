import sys
from PyQt4 import QtCore, QtGui
import os
# import klasy
from threading import Thread
from time import sleep
from PyQt4.QtGui import QMessageBox
import subprocess
from storjupload import Ui_Dialog
from storj_uploader_config import Ui_config
#from logs_standard import Ui_log_form
import urllib, urlparse, gzip
from StringIO import StringIO

#GUIs

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




class DoCommandThread(QtCore.QThread):
	def __init__(self, parent, cmd):
		super(DoCommandThread, self).__init__(parent)
		self.ui = parent.ui
		self.parent = parent
		self.cmd = cmd
	def run(self):
		p = subprocess.Popen(self.cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, env=os.environ, shell=True)


class Config_form(QtGui.QMainWindow, Ui_config):
    def __init__(self, parent=None):
        super(Config_form, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)

class Standard_logs_form(QtGui.QMainWindow, Ui_log_form):
    def __init__(self, parent=None):
        super(Standard_logs_form, self).__init__(parent)
        #QtGui.QWidget.__init__(self, parent)
        #self.ui_logs = self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.logs_ui = Ui_log_form()
        self.logs_ui.setupUi(self)


    def set_status_log_label (self,  text):
        #window3 = Ui_log_form()
        #self.logs_standard_ui.window3.close()
        #window3.retranslateUi(self)
        self.logs_ui.label_3.setText("dxsdgfg")



class StartQT4(QtGui.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        # nazwa klasy
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #self.config_ui = Ui_config()
        #self.config_ui.setupUi(self)
        self.logs_standard_ui = Ui_log_form()
        #self.logs_standard_ui.setupUi(self)
        QtCore.QObject.connect(self.ui.bt_file_select, QtCore.SIGNAL("clicked()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.bt_upload, QtCore.SIGNAL("clicked()"), self.upload_file)
        QtCore.QObject.connect(self.ui.toolButton, QtCore.SIGNAL("clicked()"), self.open_settings)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.open_standard_logs)
        self.updateGUIThread = Thread(target=self.updateGUI)

    def get_config_parametr_from_xml(self, parametr):
        from xml.dom import minidom

        # Open XML document using minidom parser
        DOMTree = minidom.parse('uploader_config.xml')

        # pobieramy elementy struktury dokumentu XML
        cNodes = DOMTree.childNodes
        for i in cNodes[0].getElementsByTagName("uploader_config"):
            # nazwa taga
            return i.getElementsByTagName(parametr)[0].nodeName


    def save_uploader_config_to_xml(self):
        import xml.etree.cElementTree as ET

        root = ET.Element("root")
        doc = ET.SubElement(root, "doc")

        ET.SubElement(doc, "field1", name="blah").text = "some value1"
        ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

        tree = ET.ElementTree(root)
        tree.write("uploader_config.xml")

    def updateGUI(self):
        while True:
            app.update()
            sleep(0.1)

    def file_dialog(self):
            # stworzenie obiektu QFileDialog
            fd = QtGui.QFileDialog(self)
            # pobranie nazwy wybranego pliku
            plik = fd.getOpenFileName()
            self.ui.lineEdit.setText(plik)



 
    def open_standard_logs (self):
        window3 = Standard_logs_form(self)
        window3.show()
        #window3.label_3.setText("test")

    def open_settings (self):
        window = Config_form(self)
        window.show()


           # print os.popen(storjcommand).read()

    def upload_file(self):

        #window3 = Standard_logs_form(self)
        #window3.close()
        #window3.show()
        #window3.setupUi(self);
        #self.z.setupUi(self)
        # self.z.label_3
        #QtGui.label_3.setText("aaaaaa")
        self.logs_ui_instance = Standard_logs_form(self)
        self.logs_ui_instance.logs_ui.label_3.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#d3980e;\">Generating encryption key</span></p></body></html>")
        #window3.label_3.setText()

        self.updateGUIThread = Thread(target=self.updateGUI)
        t1 = Thread(target=self.upload_in_thread, args=[])
        #signal1 = QtCore.pyqtSignal()
        #signal1.connect(lambda x: self.upload_in_thread)
        t1.start()
       # t1.wait()

    def progress_update(self, update_percent):
        """
        Update the progress bar
        """
        val = self.ui.progressBar.value() + update_percent
        if val <= 100:
            self.ui.progressBar.setValue(val)

    def upload_in_thread (self):
        path = '"'+self.ui.lineEdit.text()+'"'

        # QMessageBox.about(self, path, path);
    # os.system("storj -k koteczek7 upload-file ")
        storjcommand = str(' storj -k koteczek7 upload-file 57b4b6d7af035fde12cf544e ' + path)
        #storjcommand = u' '.join((' storj -k koteczek7 upload-file 57b4b6d7af035fde12cf544e ', path)).encode('utf-8').strip()

      #  p= os.Popen(storjcommand, stdout=subprocess.PIPE, shell=True)
    # (out, err) = proc.communicate()

        lineparsed = ""
        import os
        encrypting = 0;
        enc_key_generated = 0;
        enc_complete = 0;
        transfer_finished = 0;
        done = 0;
        ineparsed = "";
        p = os.popen(storjcommand)
        while 1:
            line = p.readline()
            if not line: break
            lineparsed = lineparsed + line
            print line
            if "Generating encryption key"  in lineparsed:
                if enc_key_generated != 1:
                    #self.ui.lineEdit.setText("text")
                    self.ui.progressBar.setValue(20)
                    self.ui.label_5.setText("Generating encryption key")
                    #self.logs_ui.label_3.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#d3980e;\">Generating encryption key</span></p></body></html>")
                    enc_key_generated = 1
                    #self.ui.progressBar.setValue(20)
            if "Encrypting"  in lineparsed:
                if encrypting != 1:
                    # self.ui.lineEdit.setText("text")
                    self.ui.progressBar.setValue(40)
                    self.ui.label_5.setText("Encrypting file...")
                    #window3.label_3.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#d3980e;\">Encrypting file...</span></p></body></html>")

                    encrypting = 1
                    #self.ui.progressBar.setValue(40)
            if "Encryption complete"  in lineparsed:
                if enc_complete != 1:
                    # self.ui.lineEdit.setText("text")
                    self.ui.progressBar.setValue(60)
                    self.ui.label_5.setText("Encryption completed. Beginning upload file...")
                    #window3.label_3.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#d3980e;\">Encryption completed. Beginning upload file...</span></p></body></html>")

                    enc_complete = 1
                    #self.ui.progressBar.setValue(60)
            if "Transfer finished"  in lineparsed:
                if transfer_finished != 1:
                    # self.ui.lineEdit.setText("text")
                    self.ui.progressBar.setValue(80)
                    self.ui.label_5.setText("File upload finished. Performing finalizing process...")
                    #window3.label_3.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#d3980e;\">File upload finished. Performing finalizing process...</span></p></body></html>")

                    transfer_finished = 1
                    #self.ui.progressBar.setValue(80)

            if "Done." in lineparsed:
                if done != 1:
                    # self.ui.lineEdit.setText("text")
                    self.ui.progressBar.setValue(100)
                    self.ui.label_5.setText("Done!")
                    #window3.label_3.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#d3980e;\">Idle</span></p></body></html>")

                    done = 1
                    #self.ui.progressBar.setValue(100)

            sleep(0.5)


           




        #self.runProcess(storjcommand)





if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    #app.deleteLater()
    sys.exit(app.exec_())
