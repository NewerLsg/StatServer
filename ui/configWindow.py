# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created: Tue Feb 23 17:22:25 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(628, 121)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.TimeLimitLine = QtGui.QLineEdit(self.groupBox_4)
        self.TimeLimitLine.setStyleSheet(_fromUtf8("font: 12pt \"仿宋\";"))
        self.TimeLimitLine.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.TimeLimitLine.setMaxLength(3)
        self.TimeLimitLine.setObjectName(_fromUtf8("TimeLimitLine"))
        self.gridLayout_3.addWidget(self.TimeLimitLine, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.groupBox_7 = QtGui.QGroupBox(Dialog)
        self.groupBox_7.setTitle(_fromUtf8(""))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        spacerItem1 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_7)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.TotalLevels = QtGui.QLineEdit(self.groupBox_7)
        self.TotalLevels.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.TotalLevels.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.TotalLevels.setMaxLength(2)
        self.TotalLevels.setObjectName(_fromUtf8("TotalLevels"))
        self.gridLayout_6.addWidget(self.TotalLevels, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_7)
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.ScoreUnitLine = QtGui.QLineEdit(self.groupBox_5)
        self.ScoreUnitLine.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.ScoreUnitLine.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.ScoreUnitLine.setMaxLength(3)
        self.ScoreUnitLine.setObjectName(_fromUtf8("ScoreUnitLine"))
        self.gridLayout_4.addWidget(self.ScoreUnitLine, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem2 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 0, 0, 1, 1)
        self.ComfirmBtn = QtGui.QPushButton(Dialog)
        self.ComfirmBtn.setObjectName(_fromUtf8("ComfirmBtn"))
        self.gridLayout_9.addWidget(self.ComfirmBtn, 0, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem4, 0, 2, 1, 1)
        self.CancelBtn = QtGui.QPushButton(Dialog)
        self.CancelBtn.setObjectName(_fromUtf8("CancelBtn"))
        self.gridLayout_9.addWidget(self.CancelBtn, 0, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem5, 0, 4, 1, 1)
        self.ResetBtn = QtGui.QPushButton(Dialog)
        self.ResetBtn.setObjectName(_fromUtf8("ResetBtn"))
        self.gridLayout_9.addWidget(self.ResetBtn, 0, 5, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem6, 0, 6, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_9, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "关卡时限", None))
        self.label_5.setText(_translate("Dialog", "关卡数", None))
        self.label_3.setText(_translate("Dialog", "目标分值", None))
        self.ComfirmBtn.setText(_translate("Dialog", "完成", None))
        self.CancelBtn.setText(_translate("Dialog", "取消", None))
        self.ResetBtn.setText(_translate("Dialog", "重置", None))

