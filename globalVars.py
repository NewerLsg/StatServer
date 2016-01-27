# -*- coding: utf-8 -*-

#全局变量
from threading import  RLock
from scoreRank import *

memRLock   = RLock()
teamRLock  = RLock()

g_doorArray = []   #门设备
g_memArray 	= []   #成员
g_TeamArray = []   #队伍

g_scoreRank = ScoreRank()

#可变配置项
g_config = {'scoreUint': 10, 	#目标分值
			'nameSize':3,		#名字大小
			'targetUint':5,		#人均目标
			'tatolDoors':18,	#总门设备(关卡总数)
			'timeLimit':60}		#通关时限
