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
		super(ServerThread, self).__init__(parent)
		self.port 	= port
		self.parent = parent

	def run(self):
		#将变量初始化在这里很重要,因为在run函数中的变量为本线程的变量
		#否则会被当成初始化该线程的变量而造成跨线程访问对象的错误(栈内为私有变量)
		self.tcpServer = TcpServer(self.port)
		self.connect(self.parent, SIGNAL("ShutDown()"),self.shutDown)
		self.exec_()

	def shutDown(self):
		self.tcpServer.cleanAllSock()
		self.tcpServer.close()


"""
#通信线程:接收通信套接字初始化TcpSocket,在线程中完成Tcpsocket的读写	
class WorkThread(QThread):
	def __init__(self, descriptor, parent=None):
		super(WorkThread, self).__init__(parent)
		self.descriptor = descriptor

	def run(self):
		self.sock = ClientSock(self.descriptor);
		self.connect(self.sock, SIGNAL("disconnected()"), self.quitThread)	
		self.connect(self.sock, SIGNAL("error()"), self.quitThread)
		self.exec_()

	#套接字出现问题
	def quitThread(self):
		print("close client sock")
		self.clear()
		self.emit(SIGNAL("quitThread()"))

	#清理线程
	def clear(self):
		print("close by main thread")
		self.sock.close()
		self.quit()		
"""


#Tcpserver的包装:实现连接套接字的线程处理:包括初始化、退出管理
class  TcpServer(QTcpServer):
	"""docstring for  TcpServer"""

	def __init__(self, port, parent=None):
		super( TcpServer, self).__init__(parent)
		self.conns = [] 	

		self.listen(QHostAddress("0.0.0.0"),port)
		self.setMaxPendingConnections(MAX_CONNECTIONS)

		self.connect(self, SIGNAL("error()"), self.errorProcess)

		
	def incomingConnection(self, descriptor):
		sock = ClientSock(descriptor)

		self.connect(sock, SIGNAL("disconnected()"), self.clearSock)	
		self.connect(sock, SIGNAL("error()"), self.clearSock)

		self.conns.append(sock)

		"""
		#暂时去掉这里的多线程
		#work = WorkThread(descriptor,self)
		#self.connect(work, SIGNAL("quitThread()"), self.removeWork)
		#self.conns.append(work)		#1.为了保存管理;2.如为局部变量会造成线程闪退
		#work.start()
		"""

	"""
	#not used
	def removeWork(self):
		work = self.sender()
		for w in self.conns:
			if w == work:
				w.quit()
				self.conns.remove(w)
	#not used
	def cleanWork(self):
		for w in self.conns:
			print("removed")
			w.clear()
			self.conns.remove(w)
	"""

	def errorProcess(self):
		print("error occur.")
		self.cleanAllSock()
		self.close()


	def cleanAllSock(self):
		print("clear all sock.")
		for sock in self.conns:
			if sock.peer is not None:
				sock.peer.closeByAccient()

			sock.close()


	def clearSock(self):
		sock = self.sender()

		print("clear sock");

		for s in self.conns:
			if s == sock:
				print("sock found.");
				if sock.peer is not None:
					sock.peer.closeByAccient()
					sock.close()
				
				self.conns.remove(s)

				return 