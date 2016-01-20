import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

MAX_CONNECTIONS = 60

class Server(QPushButton):

	def __init__(self, parent=None):
		super(Server, self).__init__( "&Close Server", parent)
		self.conncArray = []
		self.currentsock = 0
		self.setWindowFlags(Qt.WindowStaysOnTopHint)

		self.connect(self, SIGNAL("clicked()"), self.close)
		font = self.font()
		font.setPointSize(24)
		self.setFont(font)
		self.setWindowTitle("Server")

	def init(self, addr,port):
		self.tcpServer = QTcpServer(self)

		self.tcpServer.setMaxPendingConnections(MAX_CONNECTIONS)
		#self.tcpServer.setProxy(QNetworkProxy:NoProxy)
		self.tcpServer.listen(QHostAddress(addr), port)

		self.connect(self.tcpServer, SIGNAL("newConnection()"), self.createNewConn)
		self.connect(self.tcpServer, SIGNAL("acceptError()"), self.acceptErr)

	def createNewConn(self):
		if self.tcpServer.hasPendingConnections():
			connSock = self.tcpServer.nextPendingConnection()
		else:
			return 
		connSock.nextBlockSize = 0	
		self.currentsock = connSock
		print("1231")
		self.connect(self.currentsock, SIGNAL("readyRead()"), self.recv)
		self.connect(self.currentsock, SIGNAL("disconnected()"), self.disconnect)
	
	def recv(self):
		print("in recv")
		if self.currentsock.bytesAvailable() > 0:
			rstream = QDataStream(self.currentsock)
			rstream.setVersion(QDataStream.Qt_4_2)
			if self.currentsock.nextBlockSize == 0:
				if self.currentsock.bytesAvailable < 4:
					return
				self.currentsock.nextBlockSize = rstream.readUInt32()

			if self.currentsock.bytesAvailable() < self.currentsock.nextBlockSize:
				return

			msg = rstream.readQString()
			print("%s",msg)
			self.currentsock.nextBlockSize = 0
			reply = QByteArray()
			wstream = QDataStream(reply, QIODevice.WriteOnly)
			wstream.setVersion(QDataStream.Qt_4_2)
			wstream.writeUInt32(0)
			wstream.writeQString(msg)
			wstream.device().seek(0)
			wstream.writeUInt32(reply.size() - 4)
			self.currentsock.write(reply)

	def disconnect(self):
		print("disconnect")

	def connerror(self):
		print("conn error")	

	def acceptErr(self):
		pass


app = QApplication(sys.argv)
form = Server()
form.init("0.0.0.0",9999)
form.show()
form.move(0, 0)
app.exec_()
