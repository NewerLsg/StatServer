# -*- coding: utf-8 -*-

from globalVars import *
from threading import  RLock
from log import *


"""
通信对象：
	门、成员、组队靶
	(注：可以认为目标物帮助成员与服务器通信)
"""
class Door(object):
	"""docstring for Door"""

	def __init__(self, ID):
		super(Door, self).__init__()
		self.id 	 = ID 			#id
		self.teamIn	 = None			#内部队伍,为空表示没有
		self.time	 = 1			#队伍的进入时间
		self.targets = []

class Target(object):
	"""docstring for Target"""
	def __init__(self, ID, door, sock):
		super(Target, self).__init__()
		self.id   = ID
		self.door = door
		self.sock = sock 
		self.sock.peer = self

	def setStat(self, msg):
		self.sock.write(msg)

	def closeByAccient(self):
		for t in self.door.targets:
			if t == self:
				self.door.targets.remove(t)
			return
		

#成员对象:主要是存储自己的ID以及对应的组
class Member(object):
	"""docstring for Member"""

	def __init__(self, id, team):
		super(Member, self).__init__()	
		self.id 		= id 
		self.team 		= team
	
	def reset(self, team):
		self.team 		= team
		g_scoreRank.clearMemScore(self.id)

	def addScore(self, score):
		serverLog.debug("ID:[%s] get [%d] score!",self.id, score)
		g_scoreRank.updateScore(self, score)

#队伍对象，主要存储队名以及人数
class TeamObj(object):
	"""docstring for TeamObj"""
	
	def __init__(self, name):
		super(TeamObj, self).__init__()
		self.name 		= str(name)
		self.reg    	= int(0) 	#1:有队员,0：无队员
		self.num 		= int(0)
		self.curDoor	= None 		#当前所在关卡

	def addMem(self, MID):
		self.num += 1
		for m in g_memArray:
			if m.id == MID:
				m.reset(self)
				return

		serverLog.debug("ID[%s] added to team [%s].", MID, self.name)
		
		newMem 	= Member(MID, self)
		g_memArray.append(newMem)  