from PyQt4.QtCore import *
from globalVars import *

def parseMsg(rawMsg):
	print("%s,%s" % (rawMsg, type(rawMsg)))


	print("%s" % msg);

	stream = QDataStream(msg, QIODevice.ReadOnly)

	print("%s" % stream.readQString());
	return rawMsg