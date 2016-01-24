import sys
import copy  
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from tcpserver import *

from globalVars import *
from communicationObjs import *

from ui.mainWindow import *

class Main(QMainWindow):

	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.lineEdit.setText("9999")
		self.ui.pushButton.clicked.connect(self.startServer)
		self.ui.pushButton_2.clicked.connect(self.stopServer)
		#self.WorkThread = None

	def startServer(self):
		port = int(self.ui.lineEdit.text())

		for x in range(1, g_config['tatolDoors']):
			newDoor = Door(x)
			g_doorArray.append(newDoor)
		
		self.tcpServer = TcpServer("0.0.0.0", port)
		self.connect(self.tcpServer,SIGNAL("updateRank()"),self.updateRank)

		self.ui.pushButton.setEnabled(False)
		self.ui.lineEdit.setEnabled(False)
		print("server started")

	def stopServer(self):
		#self.WorkThread.quit()
		self.tcpServer.close()
		self.ui.pushButton.setEnabled(True)
		self.ui.lineEdit.setEnabled(True)
		print("server stoped")

	def updateRank(self):
		row = len(g_TeamArray)
		self.ui.tableWidget.setRowCount(row)

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
			self.ui.tableWidget.setItem(i,0,QTableWidgetItem(str(t.name)))
			self.ui.tableWidget.setItem(i,1,QTableWidgetItem(str(t.totalScore)))	
			i += 1

		del(team)
		del(mem)

app = QApplication(sys.argv)
main = Main()
main.show()

app.exec_()
