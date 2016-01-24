from PyQt4.QtCore import *
from PyQt4.QtNetwork import *

from protocol import *

class ClientSock(QTcpSocket):
	"""docstring for ClientSock"""
	def __init__(self, descriptor,parent=None):
		#def __init__(self, descriptor, tcpserver, parent=None):
		super(ClientSock, self).__init__(parent)		
		self.setSocketDescriptor(descriptor)
		self.readyRead.connect(self.recv)
		self.disconnected.connect(self.disconnect)
		self.error.connect(self.sockErr)


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

			if bool(updateRank) is True:
				self.emit(SIGNAL("updateRank()"))
				#self.tcpserver.updateRank()

			continue

	def sockErr(self):
		print("Error:%s" % format(self.errorString()))
		
	def disconnect(self):
		self.close()