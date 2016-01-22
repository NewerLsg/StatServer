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
		self.error.connect(self.sockErr)


	def recv(self):
		while not self.canReadLine():
				continue
		"""
		rawMsg = self.readLine(128)   #QBytesArray
		data = QByteArray.fromRawData(rawMsg)
		stream = QDataStream(data, QIODevice.ReadOnly)
		msg = stream.readQString()
		print("%s" % msg)

		"""""
		stream = QDataStream(self)
		stream.setVersion(QDataStream.Qt_4_2)
		rawMsg = stream.readQString()
		print("%s" % rawMsg)
		parseMsg()
	

	def sockErr(self):
		print("Error:%s" % format(self.errorString()))
		
	def disconnect(self):
		self.close()