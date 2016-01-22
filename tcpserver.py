from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
from sock import *

MAX_CONNECTIONS = 60

class  TcpServer(QTcpServer):
	"""docstring for  TcpServer"""
	def __init__(self,addr, port, parent=None):
		super( TcpServer, self).__init__(parent)
		self.listen(QHostAddress(addr), port)
		self.setMaxPendingConnections(MAX_CONNECTIONS)
		self.conns = [] 			#需要保留这些sock，否则会被销毁

	def incomingConnection(self, descriptor):
		connSock = ClientSock(descriptor)
		self.conns.append(connSock)
