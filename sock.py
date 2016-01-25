# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
from protocol import *

class ClientSock(QTcpSocket):
	"""docstring for ClientSock"""
	def __init__(self, descriptor,parent=None):
		super(ClientSock, self).__init__(parent)		
		self.setSocketDescriptor(descriptor)
		self.readyRead.connect(self.recv)

	def recv(self):
		while self.canReadLine():
			rawMsg = self.readLine(128)   		#QBytesArray
			print("raw:%s,data:%s" % (rawMsg, rawMsg.decode()))

			respv,updateRank = parseMsg(rawMsg.decode())

			print(" %s , %s" %(str(respv), str(updateRank)))
			if respv is not None:
				print("resp:%s" % str(respv))
				writen = self.write(str(respv))
				print("%d" % writen)

			continue