import sys
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

	def startServer(self):
		port = int(self.ui.lineEdit.text())

		for x in range(1,20):
			newDoor = Door(x)
			g_doorArray.append(newDoor)

		self.tcpServer = TcpServer("0.0.0.0", port)	
		self.ui.pushButton.setEnabled(False)
		self.ui.lineEdit.setEnabled(False)
		print("server started")

	def stopServer(self):
		self.tcpServer.close()
		self.ui.pushButton.setEnabled(True)
		self.ui.lineEdit.setEnabled(True)
		print("server stoped")

app = QApplication(sys.argv)
main = Main()
main.show()

app.exec_()
