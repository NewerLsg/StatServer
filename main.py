import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from tcpserver import *

from globalVars import *
from door import *

class Main(QDialog):

	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.txtBrowser = QTextBrowser()
		layout = QVBoxLayout()
		layout.addWidget(self.txtBrowser)
		self.setLayout(layout)
		self.setWindowTitle("Main")

	def startServer(self, addr, port):
		for x in range(1,20):
			newDoor = Door(x)
			g_doorArray.append(newDoor)

		self.tcpServer = TcpServer(addr, port)

		print("start server.")

app = QApplication(sys.argv)
main = Main()

main.startServer("0.0.0.0",9999)

main.show()

main.move(0, 0)

app.exec_()
