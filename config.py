# -*- coding: utf-8 -*-

import sys
import json
import os
import string
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

		self.gridLayout = [0 for col in range(20)]
		self.label  	= [0 for col in range(20)]
		self.LevelEdit  = [0 for col in range(99)]
		self.num		= int(0)
		self.row 		= int(0)

		self.ui.TotalLevels.editingFinished.connect(self.levelChanged)
		self.ui.CancelBtn.clicked.connect(self.close)
		self.ui.ResetBtn.clicked.connect(self.reset)
		self.ui.ComfirmBtn.clicked.connect(self.comfirm)

		self.reset()

	def levelChanged(self):

		num = int(self.ui.TotalLevels.text())

		if num == self.num:
			return None

		self.num = num

		if self.num%5 != 0:
			self.row = 1 + int(self.num/5)
		else:
			self.row = int(self.num/5)


		#删除原有格子
 		for i in xrange(1, self.ui.verticalLayout.count()):
 			childLayout = self.ui.verticalLayout.takeAt(1)
 			for x in xrange(0, childLayout.count()):
 				item = childLayout.takeAt(0)
 				item.widget().deleteLater()
			childLayout.layout().deleteLater()


		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)		

		#增加新的格子
		for i in xrange(0, self.row):
			self.gridLayout[i] = QtGui.QGridLayout()
			self.gridLayout[i].setObjectName(_fromUtf8("gridLayout_" + str(i)))
		

			self.label[i] = QtGui.QLabel(self)
			self.label[i].setObjectName(_fromUtf8("lable_" + str(i)))
			self.label[i].setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))

			self.label[i].setText(_fromUtf8(string.zfill(str(i * 5 + 1),2) + "-" + string.zfill(str(i * 5 + 5),2) + "关"))

			self.label[i].setSizePolicy(sizePolicy)
			self.label[i].setMaximumHeight(50)

			self.gridLayout[i].addWidget(self.label[i], 0, 0, 1, 1)

			for j in xrange(0,5):
				self.LevelEdit[i * 5 + j] = QtGui.QLineEdit(self)
				self.LevelEdit[i * 5 + j].setText("0")
				self.LevelEdit[i * 5 + j].setObjectName(_fromUtf8("Level_" + str(j) +"_Edit"))
				self.LevelEdit[i * 5 + j].setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
				self.LevelEdit[i * 5 + j].setSizePolicy(sizePolicy)
				self.LevelEdit[i * 5 + j].setMaximumHeight(50)

				if i * 5 + j >= self.num:
					self.LevelEdit[i * 5 + j].setText("")
					self.LevelEdit[i * 5 + j].setEnabled(False)

				self.gridLayout[i].addWidget(self.LevelEdit[i * 5 + j], 0, j + 1, 1, 1,QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

			self.ui.verticalLayout.addLayout(self.gridLayout[i])

			self.adjustSize()

			self.resize(self.maximumWidth(), self.maximumHeight() + 50 * self.row)

	def reset(self):
		if os.path.exists(g_configPath) is False:
			return 

		with open(g_configPath,"r") as f:
			jsonStr = json.load(f)

		levelArray = jsonStr["levelArray"]

		self.num = len(levelArray)

		if self.num%5 != 0:
			self.row = 1 + int(self.num/5)
		else:
			self.row = int(self.num/5)

		#删除原有格子
 		for i in xrange(1, self.ui.verticalLayout.count()):
 			childLayout = self.ui.verticalLayout.takeAt(1)
 			for x in xrange(0, childLayout.count()):
 				item = childLayout.takeAt(0)
 				item.widget().deleteLater()

			childLayout.layout().deleteLater()

		#增加新的格子
		for i in xrange(0, self.row):
			self.gridLayout[i] = QtGui.QGridLayout()
			self.gridLayout[i].setObjectName(_fromUtf8("gridLayout_" + str(i)))
			self.label[i] = QtGui.QLabel(self)
			self.label[i].setObjectName(_fromUtf8("lable_" + str(i)))
			self.label[i].setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
			self.label[i].setText(_fromUtf8(string.zfill(str(i * 5 + 1),2) + "-" + string.zfill(str(i * 5 + 5),2) + "关"))

			self.gridLayout[i].addWidget(self.label[i], 0, 0, 1, 1)

			for j in xrange(0,5):
				self.LevelEdit[i * 5 + j] = QtGui.QLineEdit(self)

				if i * 5 + j >= self.num:
					self.LevelEdit[i * 5 + j].setText("")
					self.LevelEdit[i * 5 + j].setEnabled(False)
				else:
					self.LevelEdit[i * 5 + j].setText(str(levelArray[i * 5 + j]))
				
				self.LevelEdit[i * 5 + j].setObjectName(_fromUtf8("Level_" + str(j) +"_Edit"))
				self.LevelEdit[i * 5 + j].setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))

				self.gridLayout[i].addWidget(self.LevelEdit[i * 5 + j], 0, j + 1, 1, 1,QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

			self.ui.verticalLayout.addLayout(self.gridLayout[i])

		self.ui.TimeLimitLine.setText(str(jsonStr["timelimit"])) 	
		self.ui.ScoreUnitLine.setText(str(jsonStr["scoreunit"]))
		self.ui.TotalLevels.setText(str(jsonStr["totallevels"]))


	def comfirm(self):		

		jsonStr = {}
		levelArray = []

		for i in xrange(0, self.num):
			levelArray.append(int(self.LevelEdit[i].text()))

		jsonStr["timelimit"] = int(self.ui.TimeLimitLine.text())
		jsonStr["scoreunit"] = int(self.ui.ScoreUnitLine.text())
		jsonStr["totallevels"] = int(self.ui.TotalLevels.text())
		jsonStr["levelArray"]  = levelArray

		with open(g_configPath,"w") as f:
			json.dump(jsonStr, f)

		self.emit(SIGNAL("configChanged()"));

		self.close()

