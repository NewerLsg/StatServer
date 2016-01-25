# -*- coding: utf-8 -*-

#全局变量
from threading import  RLock
from scoreRank import *
import copy  

doorRLock  = RLock()
memRLock   = RLock()
teamRLock  = RLock()


g_doorArray = []
g_memArray 	= []
g_TeamArray = []

g_scoreRank = ScoreRank()

#可变配置项
g_config = {'scoreUint': 10,
			'nameSize':1,
			'targetUint':5,
			'tatolDoors':18,
			'timeLimit':60}

def setScoceUint(scoreUint):
    g_config['scoreUint'] = scoreUint

def setNameSize(nameSize):
    g_config['nameSize'] = nameSize

def setTargetUint(targetUint):
    g_config['targetUint'] = targetUint
