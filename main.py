import sys
import copy  
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from tcpserver import *

from globalVars import *
from communicationObjs import *

from ui.mainWindow import *
from config import *

class Main(QMainWindow):

	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.StartBtn.clicked.connect(self.startServer)
		self.ui.StopBtn.clicked.connect(self.stopServer)
		self.ui.action.triggered.connect(self.showConfig)

		#self.WorkThread = None

	def startServer(self):
		port = int(self.ui.PortTxt.text())

		for x in range(1, g_config['tatolDoors']):
			newDoor = Door(x)
			g_doorArray.append(newDoor)
		
		self.tcpServer = TcpServer("0.0.0.0", port)
		self.connect(self.tcpServer,SIGNAL("updateRank()"),self.updateRank)

		self.ui.StartBtn.setEnabled(False)
		self.ui.PortTxt.setEnabled(False)
		print("server started")

	def stopServer(self):
		#self.WorkThread.quit()
		self.tcpServer.close()
		
		del(self.tcpServer)

		self.ui.StartBtn.setEnabled(True)
		self.ui.PortTxt.setEnabled(True)
		print("server stoped")

	def updateRank(self):
		teamRow = len(g_TeamArray)
		self.ui.TeamRankTb.setRowCount(teamRow)

		memRow = len(g_memArray)
		self.ui.MemRankTbl.setRowCount(memRow)

		i = int(0)

		#为了不影响当前的报文解析,直接复制,可以一部分的避免加锁的情况
		memRLock.acquire()
		mem = copy.deepcopy(g_memArray)
		memRLock.release()

		teamRLock.acquire()
		team = copy.deepcopy(g_TeamArray)
		teamRLock.release()

		#更新排名
		mem.sort(key=lambda  x: x.score, reverse = True) 
		team.sort(key=lambda x: x.totalScore, reverse = True)


		for t in team:
			self.ui.TeamRankTb.setItem(i,0,QTableWidgetItem(str(i + 1)))
			self.ui.TeamRankTb.setItem(i,1,QTableWidgetItem(str(t.name)))
			self.ui.TeamRankTb.setItem(i,2,QTableWidgetItem(str(t.totalScore)))	
			i += 1

		i = 0

		for t in mem:
			self.ui.MemRankTbl.setItem(i,0,QTableWidgetItem(str(i + 1)))
			self.ui.MemRankTbl.setItem(i,1,QTableWidgetItem(str(t.id)))
			self.ui.MemRankTbl.setItem(i,2,QTableWidgetItem(str(t.score)))	
			i += 1

		del(team)
		del(mem)

	def showConfig(self):
		self.configWindow =  ConfigDialog()
		self.configWindow.setWindowModality(Qt.ApplicationModal)
		self.configWindow.show()

app = QApplication(sys.argv)
main = Main()
main.show()

app.exec_()
