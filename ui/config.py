# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created: Sun Jan 24 20:49:11 2016
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
        Dialog.resize(398, 251)
        self.groupBox_7 = QtGui.QGroupBox(Dialog)
        self.groupBox_7.setGeometry(QtCore.QRect(9, 9, 381, 231))
        self.groupBox_7.setTitle(_fromUtf8(""))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 1, 1, 1)
        self.TimeLimitLine = QtGui.QLineEdit(self.groupBox_4)
        self.TimeLimitLine.setStyleSheet(_fromUtf8("font: 12pt \"仿宋\";"))
        self.TimeLimitLine.setObjectName(_fromUtf8("TimeLimitLine"))
        self.gridLayout_3.addWidget(self.TimeLimitLine, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 1, 1, 2)
        self.gridLayout_6.addWidget(self.groupBox_4, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.ScoreUnitLine = QtGui.QLineEdit(self.groupBox_5)
        self.ScoreUnitLine.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.ScoreUnitLine.setObjectName(_fromUtf8("ScoreUnitLine"))
        self.gridLayout_4.addWidget(self.ScoreUnitLine, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem3 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 1, 1, 1, 2)
        self.gridLayout_6.addWidget(self.groupBox_5, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        spacerItem5 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 1, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem6, 0, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.groupBox_6)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.TargetUnitLine = QtGui.QLineEdit(self.groupBox_6)
        self.TargetUnitLine.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.TargetUnitLine.setObjectName(_fromUtf8("TargetUnitLine"))
        self.gridLayout_5.addWidget(self.TargetUnitLine, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem7 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem7, 2, 1, 1, 2)
        self.gridLayout_6.addWidget(self.groupBox_6, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.TotalDoorLine = QtGui.QLineEdit(self.groupBox_3)
        self.TotalDoorLine.setStyleSheet(_fromUtf8("font: 12pt \"宋体\";"))
        self.TotalDoorLine.setObjectName(_fromUtf8("TotalDoorLine"))
        self.gridLayout_2.addWidget(self.TotalDoorLine, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(17, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.groupBox = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 0, 4, 1, 1)
        self.CancelBtn = QtGui.QPushButton(self.groupBox)
        self.CancelBtn.setObjectName(_fromUtf8("CancelBtn"))
        self.gridLayout.addWidget(self.CancelBtn, 0, 3, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 0, 2, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 0, 0, 1, 1)
        self.ComfirmBtn = QtGui.QPushButton(self.groupBox)
        self.ComfirmBtn.setObjectName(_fromUtf8("ComfirmBtn"))
        self.gridLayout.addWidget(self.ComfirmBtn, 0, 1, 1, 1)
        self.ResetBtn = QtGui.QPushButton(self.groupBox)
        self.ResetBtn.setObjectName(_fromUtf8("ResetBtn"))
        self.gridLayout.addWidget(self.ResetBtn, 0, 5, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 0, 6, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem14, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "关卡时限", None))
        self.label_3.setText(_translate("Dialog", "目标分值", None))
        self.label_4.setText(_translate("Dialog", "人均目标", None))
        self.TotalDoorLine.setText(_translate("Dialog", "123", None))
        self.label.setText(_translate("Dialog", "关卡总数", None))
        self.CancelBtn.setText(_translate("Dialog", "取消", None))
        self.ComfirmBtn.setText(_translate("Dialog", "完成", None))
        self.ResetBtn.setText(_translate("Dialog", "恢复默认", None))

