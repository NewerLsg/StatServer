import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

MAX_CONNECTIONS = 60

class Server(QDialog):

	def __init__(self, parent=None):
		super(Server, self).__init__(parent)
		self.conncArray = []
		self.txtBrowser = QTextBrowser()
		layout = QVBoxLayout()
		layout.addWidget(self.txtBrowser)
		self.setLayout(layout)
		self.setWindowTitle("Server")

	def init(self, addr,port):
		self.tcpServer = QTcpServer(self)

		self.tcpServer.setMaxPendingConnections(MAX_CONNECTIONS)

		self.tcpServer.listen(QHostAddress(addr), port)

		self.tcpServer.newConnection.connect(self.createNewConn)

	def createNewConn(self):
		if self.tcpServer.hasPendingConnections():
			connSock = self.tcpServer.nextPendingConnection()
		else:
			return 

		connSock.readyRead.connect(self.recv)
		connSock.disconnected.connect(self.disconnect)
	
	def recv(self):
		sock = self.sender()

		if sock.bytesAvailable() > 4:
			rstream = QDataStream(sock)
			rstream.setVersion(QDataStream.Qt_4_2)

			msg 	= rstream.readQString()

			print("%s" % msg);
			self.freshTxtBrowser(msg)
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

	def freshTxtBrowser(self,txt):
		self.txtBrowser.append(txt)

app = QApplication(sys.argv)
form = Server()
form.init("0.0.0.0",9999)
form.show()
form.move(0, 0)
app.exec_()
