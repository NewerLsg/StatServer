# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
from sock import *
from protocol import *
import sys

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
		self.tcpServer = TcpServer(self.port) 		#parent不能填self,self在另一个线程的栈中
		self.connect(self.parent, SIGNAL("ShutDown()"),self.shutDown)
		self.connect(self.tcpServer, SIGNAL("error()"),self.shutDown)

		self.exec_()

	def shutDown(self):
		self.tcpServer.removeAllSock()
		self.tcpServer.close()


"""
#通信线程:接收通信套接字初始化TcpSocket,在线程中完成Tcpsocket的读写
#需要在门开后向目标物发送报文--但无法跨线程调用,放弃此部分
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
		self.connections = []
		self.listen(QHostAddress.Any,port)
		self.setMaxPendingConnections(MAX_CONNECTIONS)
		self.connect(self, SIGNAL("error()"), self.errorProcess)

	def incomingConnection(self, descriptor):
		print("new connect")
		sock = ClientSock(descriptor, self)#这里的self必带,否则关闭sock将异常退出
		self.connect(sock, SIGNAL("disconnected()"), self.removeSock)	
		self.connect(sock, SIGNAL("error()"), self.removeSock)	
		self.connections.append(sock)

		"""
		#暂时去掉这里的多线程
		work = WorkThread(descriptor,self)
		self.connect(work, SIGNAL("quitThread()"), self.removeWork)
		self.conns.append(work)		#1.为了保存管理;2.如为局部变量会造成线程闪退
		work.start()
		"""

	def errorProcess(self):
		self.removeAllSock()
		self.close()


	def removeAllSock(self):
		for sock in self.connections:
			sock.clearSock()
			sock.close()


	def removeSock(self):
		sock = self.sender()

		sock.clearSock()
		sock.close()

		if sock in self.connections:
			self.connections.remove(sock)