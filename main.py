# -*- coding: utf-8 -*-

import sys
import time
from threading import Timer

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from tcpserver import *

from globalVars import *
from communicationObjs import *

from ui.mainWindow import *
from config import *
from tableItem import *

class Main(QMainWindow):

	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.StartBtn.clicked.connect(self.startServer)
		self.ui.StopBtn.clicked.connect(self.stopServer)
		self.ui.action.triggered.connect(self.showConfig)

		self.timer = None

	def startServer(self):
		port = int(self.ui.PortTxt.text())

		self.timer = QTimer()
		self.timer.timeout.connect(self.updateRank)
		self.timer.start(1000)

		for x in range(1, g_config['tatolDoors']):
			newDoor = Door(x)
			g_doorArray.append(newDoor)
		
		self.ui.StartBtn.setEnabled(False)
		self.ui.PortTxt.setEnabled(False)
		self.tcpServer = ServerThread(port)
		self.tcpServer.start()

	def stopServer(self):

		self.ui.StartBtn.setEnabled(True)
		self.ui.PortTxt.setEnabled(True)
		self.timer.stop();

	def updateRank(self):
		teamRow = len(g_scoreRank.team)
		self.ui.TeamRankTb.setRowCount(teamRow)

		memRow = len(g_scoreRank.mem)
		self.ui.MemRankTbl.setRowCount(memRow)

		i = int(0)

		#为了不影响当前的报文解析,直接复制,可以一部分的避免加锁的情况
		team = g_scoreRank.getTeamScoreList()
		mem = g_scoreRank.getMemScoreList()
			
		for t in team:

			self.ui.TeamRankTb.setItem(i,0,TableItem(str(i + 1)))
			self.ui.TeamRankTb.setItem(i,1,TableItem(str(t.name)))
			self.ui.TeamRankTb.setItem(i,2,TableItem(str(t.score)))	
			i += 1

		i = 0

		for t in mem:
			self.ui.MemRankTbl.setItem(i,0,TableItem(str(i + 1)))
			self.ui.MemRankTbl.setItem(i,1,TableItem(str(t.name)))
			self.ui.MemRankTbl.setItem(i,2,TableItem(str(t.score)))	
			i += 1

	def showConfig(self):
		self.configWindow =  ConfigDialog()
		self.configWindow.setWindowModality(Qt.ApplicationModal)
		self.configWindow.show()

app = QApplication(sys.argv)
main = Main()
main.show()

app.exec_()
