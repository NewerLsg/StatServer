# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
from protocol import *

#连接套接字，主要是读取消息、回复消息
class ClientSock(QTcpSocket):
	"""docstring for ClientSock"""

	def __init__(self, descriptor,parent=None):
		super(ClientSock, self).__init__(parent)		
		self.setSocketDescriptor(descriptor)
		self.readyRead.connect(self.recv)

	def recv(self):
		while self.canReadLine():
			#readline 返回的是bytes对象,需要decode转化为str
			rawMsg = self.readLine(128) 

			print("raw:%s,data:%s" % (rawMsg, rawMsg.decode()))

			#respv是回复信息,update
			respv = parseMsg(rawMsg.decode())

			print(" %s " %(str(respv)))

			if respv is not None:
				print("resp:%s" % str(respv))
				writen = self.write(str(respv))

			continue