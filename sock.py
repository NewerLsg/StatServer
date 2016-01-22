from PyQt4.QtCore import *
from PyQt4.QtNetwork import *

from protocol import *

class ClientSock(QTcpSocket):
	"""docstring for ClientSock"""
	def __init__(self, descriptor, parent=None):
		super(ClientSock, self).__init__(parent)		
		self.setSocketDescriptor(descriptor)
		self.readyRead.connect(self.recv)
		self.disconnected.connect(self.disconnect)

	def recv(self):
		if self.bytesAvailable() > 0:
			stream = QDataStream(self)
			stream.setVersion(QDataStream.Qt_4_2)
			msg = stream.readQString()
			resp = praseMsg(msg)
			self.write(resp)	

	def disconnect(self):
		print("disconnected")