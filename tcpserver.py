# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
from sock import *

MAX_CONNECTIONS = 60

"""
将通信线程与UI线程分离以避免界面卡顿
"""
#监听线程
class ServerThread(QThread):
	"""docstring for ServerThread"""
	def __init__(self , port, parent=None):
		super(ServerThread, self).__init__()
		self.port = port

	def run(self):
		self.tcpServer = TcpServer(self.port)
		self.exec_()


#通信线程		
class WorkThread(QThread):
	def __init__(self, descriptor, parent=None):
		super(WorkThread, self).__init__(parent)
		self.descriptor = descriptor

	def run(self):
		self.sock = ClientSock(self.descriptor);
		self.connect(self.sock, SIGNAL("disconnected()"), self.quitThread)	
		self.connect(self.sock, SIGNAL("error()"), self.quitThread)			
		self.exec_()

	def quitThread(self):
		self.emit(SIGNAL("quitThread()"))

class  TcpServer(QTcpServer):
	"""docstring for  TcpServer"""
	def __init__(self, port, parent=None):
		super( TcpServer, self).__init__(parent)
		self.listen(QHostAddress("0.0.0.0"),port)
		self.setMaxPendingConnections(MAX_CONNECTIONS)
		self.conns = [] 	

	def incomingConnection(self, descriptor):
		work = WorkThread(descriptor,self)
		self.connect(work, SIGNAL("quitThread()"), self.removeWork)
		self.conns.append(work)
		work.start()
	
	def removeWork(self):
		work = self.sender()
		for w in self.conns:
			if w == work:
				w.quit()
				self.conns.remove(w)