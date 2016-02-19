# -*- coding: utf-8 -*-

import sys
import time
from threading import Timer

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

from globalVars import *
from communicationObjs import *
from config import *
from tcpserver import *
from tableItem import *
from ui.mainWindow import *
from log import *

from sock import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Main(QMainWindow):

	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.StartBtn.clicked.connect(self.startServer)
		self.ui.StopBtn.clicked.connect(self.stopServer)
		self.ui.action.triggered.connect(self.showConfig)
		self.ui.StopBtn.setEnabled(False)
		self.timer = QTimer()

		self.timer.timeout.connect(self.updateRank)

		for x in range(1, g_config['tatolDoors']):
			newDoor = Door(x)
			g_doorArray.append(newDoor)

	def startServer(self):
		port = int(self.ui.PortTxt.text())
		self.ui.StartBtn.setEnabled(False)
		self.ui.PortTxt.setEnabled(False)
		self.ui.StopBtn.setEnabled(True)

		self.tcpServer = ServerThread(port,self)

		self.tcpServer.start()

		self.timer.start(1000)

		serverLog.debug("Start server.")
		
	def stopServer(self):
		self.emit(SIGNAL("ShutDown()"))

		self.tcpServer.quit()

		self.timer.stop();

		self.ui.StartBtn.setEnabled(True)
		self.ui.PortTxt.setEnabled(True)
		self.ui.StopBtn.setEnabled(False)

		serverLog.debug("Stop server.")

	def updateRank(self):
		pass
		
		teamRow = len(g_scoreRank.team)
		self.ui.TeamRankTb.setRowCount(teamRow)

		memRow = len(g_scoreRank.mem)
		self.ui.MemRankTbl.setRowCount(memRow)

		#为了不影响当前的报文解析,直接复制,可以一部分的避免加锁的情况
		i = int(0)
		team = g_scoreRank.getTeamScoreList()
		
		for t in team:
			self.ui.TeamRankTb.setItem(i,0,TableItem(str(i + 1)))
			self.ui.TeamRankTb.setItem(i,1,TableItem(str(t.name)))
			self.ui.TeamRankTb.setItem(i,2,TableItem(str(t.score)))	
			i += 1
		
		i = int(0)
		mem = g_scoreRank.getMemScoreList()

		for m in mem:
			self.ui.MemRankTbl.setItem(i,0,TableItem(str(i + 1)))
			self.ui.MemRankTbl.setItem(i,1,TableItem(str(m.ID + "(" + m.teamname + ")")))
			self.ui.MemRankTbl.setItem(i,2,TableItem(str(m.score)))	
			i += 1
		

	def showConfig(self):
		self.configWindow =  ConfigDialog()
		self.configWindow.setWindowModality(Qt.ApplicationModal)
		self.configWindow.show()

	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(self, _fromUtf8('退出'),
			_fromUtf8("确认退出?"), QtGui.QMessageBox.Yes |
			QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

app = QApplication(sys.argv)
main = Main()
main.show()
app.exec_()
