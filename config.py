# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from globalVars import *
from ui.configWindow 	import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


#配置窗口
class ConfigDialog(QDialog):
	"""docstring for ConfigDialog"""

	def __init__(self,parent=None):
		super(ConfigDialog, self).__init__(parent)

		self.setObjectName(_fromUtf8("ConfigDialog"))
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.ui.TimeLimitLine.setText(str(g_config['timeLimit']))
		self.ui.ScoreUnitLine.setText(str(g_config['scoreUint']))
		self.ui.TargetUnitLine.setText(str(g_config['targetUint']))
		#self.ui.TotalDoorLine.setText(str(g_config['tatolDoors']))

		self.gridLayout = [0 for col in range(5)]
		self.label  	= [0 for col in range(5)]
		self.LevelEdit  = [0 for col in range(5 * 4)]
		self.num		= int(0)

		self.ui.comboBox.activated.connect(self.comboBoxActivated)
		self.ui.CancelBtn.clicked.connect(self.close)
		self.ui.ResetBtn.clicked.connect(self.reset)
		self.ui.ComfirmBtn.clicked.connect(self.comfirm)

	def comboBoxActivated(self, num):

		num += 1

		if num == self.num:
			return None


		if self.num%5 != 0:
			oldrow = 1 + int(self.num/5)
		else:
			oldrow = int(self.num/5)

		if num%5 != 0:
			row = 1 + int(num/5)
		else:
			row = int(num/5)

		print("old[%d], new[%d]" %(oldrow, row))

		if num > self.num: 
			for i in xrange(oldrow, row ):#增加缺少的
				print("i[%d]" %(i))
				start = 0
				if i != oldrow or self.num == 0: #此行不用增加
					print("new line[%d]" %(i))
					self.gridLayout[i] = QtGui.QGridLayout()
					self.gridLayout[i].setObjectName(_fromUtf8("gridLayout_" + str(i)))
					self.label[i] = QtGui.QLabel(self)
					self.label[i].setObjectName(_fromUtf8("lable_" + str(i)))
					self.label[i].setText(_fromUtf8(str(i * 5 + 1) + "-" + str(i  * 5 + 5) + "关"))
					self.gridLayout[i].addWidget(self.label[i], 0, 0, 1, 1)
				else:
					start = 5 - self.num%5


				for j in xrange(start,5):
					self.LevelEdit[i * 5 + j] = QtGui.QLineEdit(self)
					self.LevelEdit[i * 5 + j].setText("123")
					self.LevelEdit[i * 5 + j].setObjectName(_fromUtf8("Level_" + str(j) +"_Edit"))
					self.gridLayout[i].addWidget(self.LevelEdit[i * 5 + j], 0, j + 1, 1, 1)

				if i != oldrow or self.num == 0:
					self.ui.verticalLayout.addLayout(self.gridLayout[i])

		self.num = num


	def reset(self):
		self.ui.TimeLimitLine.setText('60')
		self.ui.ScoreUnitLine.setText('10')
		self.ui.TargetUnitLine.setText('5')
		#self.ui.TotalDoorLine.setText('18')

	def comfirm(self):		
		g_config['timeLimit'] = self.ui.TimeLimitLine.text()
		g_config['scoreUnit'] = self.ui.ScoreUnitLine.text()
		g_config['targetUint'] = self.ui.TargetUnitLine.text()
		#g_config['tatolDoors'] = self.ui.TotalDoorLine.text()
		self.close()
		