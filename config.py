# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from globalVars import *
from ui.configWindow 	import *

class ConfigDialog(QDialog):
	"""docstring for ConfigDialog"""
	def __init__(self,parent=None):
		super(ConfigDialog, self).__init__(parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.ui.CancelBtn.clicked.connect(self.close)
		self.ui.ResetBtn.clicked.connect(self.reset)
		self.ui.ComfirmBtn.clicked.connect(self.comfirm)

		self.ui.TimeLimitLine.setText(str(g_config['timeLimit']))
		self.ui.ScoreUnitLine.setText(str(g_config['scoreUint']))
		self.ui.TargetUnitLine.setText(str(g_config['targetUint']))
		self.ui.TotalDoorLine.setText(str(g_config['tatolDoors']))

	def reset(self):
		self.ui.TimeLimitLine.setText('60')
		self.ui.ScoreUnitLine.setText('10')
		self.ui.TargetUnitLine.setText('5')
		self.ui.TotalDoorLine.setText('18')

	def comfirm(self):		
		g_config['timeLimit'] = self.ui.TimeLimitLine.text()
		g_config['scoreUnit'] = self.ui.ScoreUnitLine.text()
		g_config['targetUint'] = self.ui.TargetUnitLine.text()
		g_config['tatolDoors'] = self.ui.TotalDoorLine.text()
		self.close()
		