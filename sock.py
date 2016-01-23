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
		while self.canReadLine():
			rawMsg = self.readLine(128)   		#QBytesArray
			print("raw:%s,data:%s" % (rawMsg, rawMsg.decode()))
			resp = parseMsg(rawMsg.decode())

			if resp is not None:
				print("resp:%s" % resp)
				writen = self.write(resp)
				print("%d" % writen)
			continue
		
		"""
		rawMsg = self.readLine(128)   		#QBytesArray
		#print("%s" % bytes.decode(rawMsg)) #编码这里是个坑,不用这种
		data = QByteArray.fromRawData(rawMsg)
		stream = QDataStream(data, QIODevice.ReadOnly)
		msg = stream.readQString()
		resp = parseMsg(msg)
		"""""
		""""
		stream = QDataStream(self)
		stream.setVersion(QDataStream.Qt_4_2)
		rawMsg = stream.readQString()
		resp = parseMsg(rawMsg)
		"""""

	def sockErr(self):
		print("Error:%s" % format(self.errorString()))
		
	def disconnect(self):
		self.close()