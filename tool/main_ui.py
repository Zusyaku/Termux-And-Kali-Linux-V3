# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Jun 16 11:44:54 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import webbrowser
import urllib2

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(320, 240)
        MainWindow.setMinimumSize(320, 240)
        MainWindow.setMaximumSize(320, 240)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.imageLabel = QtGui.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(0, 20, 320, 48))
        self.imageLabel.setText(_fromUtf8(""))
        self.imageLabel.setPixmap(QtGui.QPixmap(_fromUtf8("image.png")))
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.nameEdit = QtGui.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(55, 106, 265, 27))
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.nameLabel = QtGui.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(10, 110, 40, 17))
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.infoCombo = QtGui.QComboBox(self.centralwidget)
        self.infoCombo.setGeometry(QtCore.QRect(55, 135, 265, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoCombo.sizePolicy().hasHeightForWidth())
        self.infoCombo.setSizePolicy(sizePolicy)
        self.infoCombo.setObjectName(_fromUtf8("infoCombo"))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoCombo.addItem(_fromUtf8(""))
        self.infoLabel = QtGui.QLabel(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(10, 140, 40, 17))
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 180, 321, 40))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.doxButton = QtGui.QPushButton(self.layoutWidget)
        self.doxButton.setObjectName(_fromUtf8("doxButton"))
        self.horizontalLayout.addWidget(self.doxButton)
        self.quitButton = QtGui.QPushButton(self.layoutWidget)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.horizontalLayout.addWidget(self.quitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.doxButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.dox)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def dox(self):
	self.name = self.nameEdit.text()
	option = self.infoCombo.currentText()
	opt = str(option)
	if opt == "FaceBook":
	  self.facebook()
	elif opt == "Twitter":
	  self.twitter()
	elif opt == "MySpace":
	  self.myspace()
	elif opt == "Bebo":
	  self.bebo()
	elif opt == "Tagged":
	  self.tagged()
	elif opt == "Pipl":
	  self.pipl()
	elif opt == "Soundcloud":
	  self.soundcloud()
	elif opt == "Pictures":
	  self.pictures()
	elif opt == "Home Address":
	  self.address()
	elif opt == "Phone No":
	  self.phonenumber()
	elif opt == "Marriage Records":
	  self.marriage()
	elif opt == "Mugshots":
	  self.mugshots()
	elif opt == "Skype Resolve":
	  self.skyperesolve()
	elif opt == "Email Search":
	  self.emailsearch()
    
    def facebook(self):
	webbrowser.open('https://www.google.com/#output=search&sclient=psy-ab&q=facebook.com ' + self.name)

    def twitter(self):
	webbrowser.open('https://www.google.com/#output=search&sclient=psy-ab&q=twitter.com ' + self.name)

    def myspace(self):
	webbrowser.open('https://www.google.com/#output=search&sclient=psy-ab&q=myspace.com ' + self.name)

    def bebo(self):
	webbrowser.open('https://www.google.com/#output=search&sclient=psy-ab&q=bebo.com ' + self.name)

    def tagged(self):
	webbrowser.open('http://www.tagged.com/search_results.html?search_term= ' + self.name +'&search_type=keyword')

    def pipl(self):
	webbrowser.open('https://pipl.com/search/?q='+ self.name)

    def soundcloud(self):
	webbrowser.open('https://soundcloud.com/search?q=' + self.name)

    def pictures(self):
	webbrowser.open('https://www.google.com/search?site=&tbm=isch&source=hp&biw=1024&bih=581&q=' + self.name)

    def address(self):
	webbrowser.open('http://www.192.com/')

    def phonenumber(self):
	webbrowser.open('www.bt.com/directoryenquiries/')

    def marriage(self):
	webbrowser.open('http://www.findmypast.co.uk/search/all/marriages?gclid={SI:gclid}&gclid=CIavkOzr47cCFaXMtAodMgIAmQ')
		
    def mugshots(self):
	webbrowser.open('http://mugshots.com/search.html?q=' + self.name)


    def skyperesolve(self):
	resp = urllib2.urlopen('http://infernoapi.com/skype.php?apikey=c9f4bfc1d0d0a4eecff90c7839fd929cdfd79f45&user=' + str(self.name))
	d = resp.read()
	QtGui.QMessageBox.about(self.centralwidget, '^_^', d)
	print d
	resp = ''
	d = ''
	

    def emailsearch(self):
	webbrowser.open('https://www.google.co.uk/#sclient=psy-ab&q=' + self.name + ' @hotmail @gmail @yahoo')

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "VipVince - Dox Tool", None))
        self.nameLabel.setText(_translate("MainWindow", "Name:", None))
        self.infoCombo.setItemText(0, _translate("MainWindow", "FaceBook", None))
        self.infoCombo.setItemText(1, _translate("MainWindow", "Twitter", None))
        self.infoCombo.setItemText(2, _translate("MainWindow", "MySpace", None))
        self.infoCombo.setItemText(3, _translate("MainWindow", "Bebo", None))
        self.infoCombo.setItemText(4, _translate("MainWindow", "Tagged", None))
        self.infoCombo.setItemText(5, _translate("MainWindow", "Pipl", None))
        self.infoCombo.setItemText(6, _translate("MainWindow", "Soundcloud", None))
        self.infoCombo.setItemText(7, _translate("MainWindow", "Pictures", None))
        self.infoCombo.setItemText(8, _translate("MainWindow", "Home Address", None))
        self.infoCombo.setItemText(9, _translate("MainWindow", "Phone No", None))
        self.infoCombo.setItemText(10, _translate("MainWindow", "Marriage Records", None))
        self.infoCombo.setItemText(11, _translate("MainWindow", "Mugshots", None))
        self.infoCombo.setItemText(12, _translate("MainWindow", "Skype Resolve", None))
        self.infoCombo.setItemText(13, _translate("MainWindow", "Email Search", None))
        self.infoLabel.setText(_translate("MainWindow", "Info:", None))
        self.doxButton.setText(_translate("MainWindow", "Dox", None))
        self.quitButton.setText(_translate("MainWindow", "Quit", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
if __name__ == '__main__':
  	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
