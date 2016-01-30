# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
from protocol import *
from log import *

#连接套接字，主要是读取消息、回复消息
class ClientSock(QTcpSocket):
	"""docstring for ClientSock"""

	def __init__(self, descriptor, parent=None):
		super(ClientSock, self).__init__(parent)
		self.setSocketDescriptor(descriptor)
		self.readyRead.connect(self.recv)
		self.src = None

	def recv(self):
		while self.canReadLine():
			#readline 返回的是bytes对象,需要decode转化为str并去掉后面的空格以及换行
			rawMsg = self.readLine(128).decode().rstrip()

			print("rep [%s], len[%d]" % (rawMsg, len(rawMsg)))

			serverLog.debug("req:[%s],len[%d]",rawMsg, len(rawMsg))

			#respv是回复信息,update
			respv = parseMsg(rawMsg, self)
			
			if respv is not None:
				serverLog.debug("resp [%s], len[%d](blank included)", respv.rstrip(), len(respv))

				print("respv[%s], len[%d]" %(respv.rstrip(), len(respv.rstrip())))
				
				writen = self.write(str(respv))

				serverLog.debug("resp sended,len[%d]",int(writen))
			else:

				serverLog.debug("no need to resp.")

			continue

	def clearSock(self):
		if self.src is not None:
			self.src.closeByAccient()
			del self.src 

		self.close()