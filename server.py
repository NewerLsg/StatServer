import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

MAX_CONNECTIONS = 60

class Server(QPushButton):

	def __init__(self, parent=None):
		super(Server, self).__init__( "&Close Server", parent)
		self.conncArray = []
		sock = 0
		self.setWindowFlags(Qt.WindowStaysOnTopHint)

		self.connect(self, SIGNAL("clicked()"), self.close)
		font = self.font()
		font.setPointSize(24)
		self.setFont(font)
		self.setWindowTitle("Server")

	def init(self, addr,port):
		self.tcpServer = QTcpServer(self)

		self.tcpServer.setMaxPendingConnections(MAX_CONNECTIONS)
		#self.tcpServer.setProxy(QNetworkProxy::NoProxy)
		self.tcpServer.listen(QHostAddress(addr), port)

		self.connect(self.tcpServer, SIGNAL("newConnection()"), self.createNewConn)
		self.connect(self.tcpServer, SIGNAL("acceptError()"), self.acceptErr)

	def createNewConn(self):
		if self.tcpServer.hasPendingConnections():
			connSock = self.tcpServer.nextPendingConnection()
		else:
			return 

		self.connect(connSock, SIGNAL("readyRead()"), self.recv)
		self.connect(connSock, SIGNAL("disconnected()"), self.disconnect)
	
	def recv(self):
		sock = self.sender()

		if sock.bytesAvailable() > 4:
			rstream = QDataStream(sock)
			rstream.setVersion(QDataStream.Qt_4_2)

			msg 	= rstream.readQString()
			reply 	= QByteArray()
			wstream = QDataStream(reply, QIODevice.WriteOnly)

			wstream.setVersion(QDataStream.Qt_4_2)
			wstream.writeUInt32(0)
			wstream.writeQString(msg)
			wstream.device().seek(0)
			wstream.writeUInt32(reply.size() - 4)
			sock.write(reply)

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
