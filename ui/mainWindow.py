# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Jan 24 21:08:15 2016
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(932, 505)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 881, 441))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 201, 411))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 181, 72))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.StopBtn = QtGui.QPushButton(self.groupBox)
        self.StopBtn.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.StopBtn.setObjectName(_fromUtf8("StopBtn"))
        self.gridLayout.addWidget(self.StopBtn, 0, 2, 1, 1)
        self.PortTxt = QtGui.QLineEdit(self.groupBox)
        self.PortTxt.setMinimumSize(QtCore.QSize(81, 20))
        self.PortTxt.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.PortTxt.setObjectName(_fromUtf8("PortTxt"))
   
        self.gridLayout.addWidget(self.PortTxt, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(53, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.StartBtn = QtGui.QPushButton(self.groupBox)
        self.StartBtn.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.StartBtn.setObjectName(_fromUtf8("StartBtn"))
        self.gridLayout.addWidget(self.StartBtn, 0, 0, 1, 2)
        self.TipTextArea = QtGui.QTextBrowser(self.groupBox_2)
        self.TipTextArea.setGeometry(QtCore.QRect(10, 90, 181, 311))
        self.TipTextArea.setObjectName(_fromUtf8("TipTextArea"))
        self.MemRankTbl = QtGui.QTableWidget(self.groupBox_3)
        self.MemRankTbl.setGeometry(QtCore.QRect(550, 10, 301, 411))
        self.MemRankTbl.setObjectName(_fromUtf8("MemRankTbl"))
        self.MemRankTbl.setColumnCount(3)
        self.MemRankTbl.setRowCount(0)
        self.MemRankTbl.verticalHeader().setVisible(False)
        self.MemRankTbl.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.MemRankTbl.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.MemRankTbl.horizontalHeader().resizeSections()
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("宋体"))
        font.setPointSize(12)
        item.setFont(font)
        self.MemRankTbl.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("宋体"))
        font.setPointSize(12)
        item.setFont(font)
        self.MemRankTbl.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("宋体"))
        font.setPointSize(12)
        item.setFont(font)
        self.MemRankTbl.setHorizontalHeaderItem(2, item)
        self.TeamRankTb = QtGui.QTableWidget(self.groupBox_3)
        self.TeamRankTb.setGeometry(QtCore.QRect(230, 10, 301, 411))
        self.TeamRankTb.setObjectName(_fromUtf8("TeamRankTb"))
        self.TeamRankTb.setColumnCount(3)
        self.TeamRankTb.setRowCount(0)
        self.TeamRankTb.verticalHeader().setVisible(False)
        self.TeamRankTb.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.TeamRankTb.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.TeamRankTb.horizontalHeader().resizeSections()
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("宋体"))
        font.setPointSize(12)
        item.setFont(font)
        self.TeamRankTb.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("宋体"))
        font.setPointSize(12)
        item.setFont(font)
        self.TeamRankTb.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("宋体"))
        font.setPointSize(12)
        item.setFont(font)
        self.TeamRankTb.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menubar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.label.setBuddy(self.PortTxt)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "服务器", None))
        self.StopBtn.setText(_translate("MainWindow", "停止", None))
        self.PortTxt.setText(_translate("MainWindow", "9999", None))
        self.label.setText(_translate("MainWindow", "端口", None))
        self.StartBtn.setText(_translate("MainWindow", "启动", None))
        item = self.MemRankTbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名次", None))
        item = self.MemRankTbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.MemRankTbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "积分", None))
        item = self.TeamRankTb.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名次", None))
        item = self.TeamRankTb.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "队名", None))
        item = self.TeamRankTb.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "积分", None))
        self.menu.setTitle(_translate("MainWindow", "设置", None))
        self.menu_2.setTitle(_translate("MainWindow", "帮助", None))
        self.action.setText(_translate("MainWindow", "属性", None))
        self.action_2.setText(_translate("MainWindow", "关于软件", None))

