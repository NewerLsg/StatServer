import sys
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *

class Msg(QTcpSocket):
	"""docstring for Msg"""
	def __init__(self, parent=None):
		super(Msg, self).__init__(parent)
		print("init QTcpSocket")
		#if not self.connect(self, SIGNAL("readyRead()"), self.recv):
			#print("connect readyRead error.")

		#if not self.connect(self, SIGNAL("disconnected()"), self.disconnect):
		#	print("connect disconnected error")

		#print("init Qtcpsocket,%d",parent)
		#self.connect(self, SIGNAL("error()"), self.error)

	def recv(self):
		print("in recv")
		
		if self.bytesAvailable() > 0:
			data = QDataStream(self)
			data.setVersion(QDataStream.Qt_4_2)

			if self.nextBlockSize == 0:
				if self.bytesAvailable() < 4:
					return

				self.nextBlockSize = data.readUInt32()
			if self.bytesAvailable() < self.nextBlockSize:
				return

			resp = data.readQString()
			self.nextBlockSize = 0
			self.sendMessage(resp, self.socketDescriptor())
			self.nextBlockSize = 0
	
	def sendMessage(self, resp, sock):	
		message = "{}> {}".format(sock, resp)
		reply = QByteArray()
		stream = QDataStream(reply, QIODevice.WriteOnly)
		stream.setVersion(QDataStream.Qt_4_2)
		stream.writeUInt32(0)
		stream.writeQString(message)
		stream.device().seek(0)
		stream.writeUInt32(reply.size() - 4)
		self.write(reply)

	def praseMsg(self):
		print("get from msg.%10d", self)
		

	def	disconnect(self):
		print("disconnect")
		

	def error(self):
		print("error")