# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class TableItem(QtGui.QTableWidgetItem):
	"""docstring for TableItem"""
	def __init__(self, arg):
		super(TableItem, self).__init__()
		self.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("宋体"))
		font.setPointSize(12)
		self.setFont(font)
		self.setText(arg)
		