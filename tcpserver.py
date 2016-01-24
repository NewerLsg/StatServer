from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
from sock import *

MAX_CONNECTIONS = 60


class WorkThread(QThread):
	def __init__(self, descriptor):
		super(WorkThread, self).__init__()
		self.tcpServer  =  None
		self.descriptor = descriptor
		self.sock 		= None
	def run(self):
		sock = ClientSock(self.descriptor, self);
		self.sock = sock
		self.connect(self.sock, SIGNAL("updateRank()"),self.updateRank)	
		self.exec()

	def updateRank(self):
		self.emit(SIGNAL("updateRank()"))

	def quit(self):
		print("thread quit")
		self.tcpServer.close()


class  TcpServer(QTcpServer):
	"""docstring for  TcpServer"""
	def __init__(self,addr, port, parent=None):
		super( TcpServer, self).__init__(parent)
		self.updateSignal = pyqtSignal()
		self.listen(QHostAddress(addr), port)
		self.setMaxPendingConnections(MAX_CONNECTIONS)
		self.conns = [] 			#不能删除，否则对象会被销毁

	def incomingConnection(self, descriptor):
		print("new connSock")
		work = WorkThread(descriptor)
		self.connect(work, SIGNAL("updateRank()"), self.updateRank)
		self.conns.append(work)
		work.start()
	
	def updateRank(self):
		self.emit(SIGNAL("updateRank()"))