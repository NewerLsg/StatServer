# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(892, 534)
        MainWindow.setMinimumSize(QtCore.QSize(892, 534))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(250, 110))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.StartBtn = QtGui.QPushButton(self.groupBox)
        self.StartBtn.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.StartBtn.setObjectName(_fromUtf8("StartBtn"))
        self.horizontalLayout.addWidget(self.StartBtn)
        self.StopBtn = QtGui.QPushButton(self.groupBox)
        self.StopBtn.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.StopBtn.setObjectName(_fromUtf8("StopBtn"))
        self.horizontalLayout.addWidget(self.StopBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(53, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.PortTxt = QtGui.QLineEdit(self.groupBox)
        self.PortTxt.setMinimumSize(QtCore.QSize(81, 20))
        self.PortTxt.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.PortTxt.setObjectName(_fromUtf8("PortTxt"))
        self.horizontalLayout_2.addWidget(self.PortTxt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.TipTextArea = QtGui.QTextBrowser(self.centralwidget)
        self.TipTextArea.setMaximumSize(QtCore.QSize(250, 16000))
        self.TipTextArea.setObjectName(_fromUtf8("TipTextArea"))
        self.verticalLayout.addWidget(self.TipTextArea)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.TeamRankTbl = QtGui.QTableWidget(self.centralwidget)
        self.TeamRankTbl.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.TeamRankTbl.setAutoFillBackground(False)
        self.TeamRankTbl.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TeamRankTbl.setAutoScroll(False)
        self.TeamRankTbl.setObjectName(_fromUtf8("TeamRankTbl"))
        self.TeamRankTbl.setColumnCount(3)
        self.TeamRankTbl.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.TeamRankTbl.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.TeamRankTbl.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.TeamRankTbl.setHorizontalHeaderItem(2, item)
        self.TeamRankTbl.verticalHeader().setVisible(False)
        self.horizontalLayout_3.addWidget(self.TeamRankTbl)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.MemRankTbl = QtGui.QTableWidget(self.centralwidget)
        self.MemRankTbl.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.MemRankTbl.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MemRankTbl.setObjectName(_fromUtf8("MemRankTbl"))
        self.MemRankTbl.setColumnCount(3)
        self.MemRankTbl.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.MemRankTbl.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.MemRankTbl.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.MemRankTbl.setHorizontalHeaderItem(2, item)
        self.MemRankTbl.verticalHeader().setVisible(False)
        self.horizontalLayout_3.addWidget(self.MemRankTbl)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 892, 23))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.StartBtn.setText(_translate("MainWindow", "启动", None))
        self.StopBtn.setText(_translate("MainWindow", "停止", None))
        self.label.setText(_translate("MainWindow", "端口", None))
        self.PortTxt.setText(_translate("MainWindow", "9999", None))
        item = self.TeamRankTbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名次", None))
        item = self.TeamRankTbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "队名", None))
        item = self.TeamRankTbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "积分", None))
        item = self.MemRankTbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名次", None))
        item = self.MemRankTbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.MemRankTbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "积分", None))
        self.menu.setTitle(_translate("MainWindow", "设置", None))
        self.menu_2.setTitle(_translate("MainWindow", "帮助", None))
        self.action.setText(_translate("MainWindow", "属性", None))
        self.action_2.setText(_translate("MainWindow", "关于软件", None))

