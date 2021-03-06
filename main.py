# -*- coding: utf-8 -*-

import sys
import os
import time
from threading import Timer

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

import globalVars 
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
		self.status = False
		self.ui.StopBtn.setEnabled(False)
		self.timer4Rank = QTimer()
		self.timer4Msg  = QTimer()

		self.timer4Rank.timeout.connect(self.updateRank)
		self.timer4Msg.timeout.connect(self.updateMsg)

		self.config()

	def startServer(self):
		port = int(self.ui.PortTxt.text())

		self.ui.StartBtn.setEnabled(False)
		self.ui.PortTxt.setEnabled(False)
		self.ui.StopBtn.setEnabled(True)

		self.tcpServer = ServerThread(port,self)

		self.tcpServer.start()

		self.timer4Rank.start(1000)
		self.timer4Msg.start(1000)

		self.status = True

		serverLog.debug("Start server.")
		
	def stopServer(self):
		self.emit(SIGNAL("ShutDown()"))

		self.tcpServer.quit()

		self.timer4Rank.stop();
		self.timer4Msg.stop();

		self.ui.StartBtn.setEnabled(True)
		self.ui.PortTxt.setEnabled(True)
		self.ui.StopBtn.setEnabled(False)


		self.status = False
		serverLog.debug("Stop server.")

	def updateRank(self):
		teamRow = len(globalVars.g_scoreRank.team)
		self.ui.TeamRankTbl.setRowCount(teamRow)

		memRow = len(globalVars.g_scoreRank.mem)
		self.ui.MemRankTbl.setRowCount(memRow)

		#为了不影响当前的报文解析,直接复制,可以一部分的避免加锁的情况
		i = int(0)
		team = globalVars.g_scoreRank.getTeamScoreList()
		
		for t in team:
			self.ui.TeamRankTbl.setItem(i,0,TableItem(str(i + 1)))
			self.ui.TeamRankTbl.setItem(i,1,TableItem(str(t.name)))
			self.ui.TeamRankTbl.setItem(i,2,TableItem(str(t.curdoorID )))
			self.ui.TeamRankTbl.setItem(i,3,TableItem(str(t.score * globalVars.g_config["scoreUint"])))	
			i += 1
		
		i = int(0)
		mem = globalVars.g_scoreRank.getMemScoreList()

		for m in mem:
			self.ui.MemRankTbl.setItem(i,0,TableItem(str(i + 1)))
			self.ui.MemRankTbl.setItem(i,1,TableItem(str(m.ID + "(" + m.teamname + ")")))
			self.ui.MemRankTbl.setItem(i,2,TableItem(str(m.score * globalVars.g_config["scoreUint"])))	
			i += 1
	
	def updateMsg(self):

		i = int(50)
		if globalVars.g_msque.empty() is not True:
			while globalVars.g_msque.empty() is not True and i > 0:
				msg = globalVars.g_msque.get()
				i -= 1
				self.ui.TipTextArea.append(msg)
			globalVars.g_msque.task_done()	
		

	def showConfig(self):
		self.configWindow =  ConfigDialog()
		self.connect(self.configWindow, SIGNAL("configChanged()"), self.config)
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

	def config(self):

		if os.path.exists(globalVars.g_configPath) is False:
			return 

		with open(globalVars.g_configPath,"r") as f:
			jsonStr = json.load(f)

		globalVars.g_config['tatolLevels'] = int(jsonStr['totallevels'])
		globalVars.g_config['timeLimit']  = int(jsonStr['timelimit'])	
		globalVars.g_config['scoreUint']  = int(jsonStr['scoreunit'])

		levelArray = jsonStr['levelArray']

		globalVars.g_doorArray = []

		for x in range(0, globalVars.g_config['tatolLevels']):
			newDoor = Door(x + 1)
			newDoor.limit = levelArray[x]
			globalVars.g_doorArray.append(newDoor)


		if self.status == True:
			self.stopServer()
			self.startServer()
		

app = QApplication(sys.argv)
main = Main()
main.show()
app.exec_()
