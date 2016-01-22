from PyQt4.QtCore import *
from globalVars import *

def praseMsg(msg):
	print("%s" % msg)
	reply = QByteArray()
	wstream = QDataStream(reply, QIODevice.WriteOnly)
	wstream.setVersion(QDataStream.Qt_4_2)
	wstream.writeUInt32(0)
	wstream.writeQString(msg)
	wstream.device().seek(0)
	wstream.writeUInt32(reply.size() - 4)
	return reply