# -*- coding: utf-8 -*-

from globalVars import *
from threading import  RLock


"""
通信对象：
	门、成员、组队靶
	(注：可以认为目标物帮助成员与服务器通信)
"""
class Door(object):
	"""docstring for Door"""
	def __init__(self, ID):
		super(Door, self).__init__()
		self.arg 	 = ID 			#id
		self.teamIn	 = None			#内部队伍,为空表示没有
		self.time	 = 1			#队伍的进入时间

	def getTeamIn():
		return self.teamIn


class Member(object):
	"""docstring for Member"""
	def __init__(self, id, team):
		super(Member, self).__init__()	
		self.id 		= id 
		self.team 		= team
	
	def reset(self, team):
		self.team 		= team
		g_scoreRank.clearMemScore(self.id)

	def getTeamname(self):
		return self.teamName

	def getID(self):
		return self.id 

	def addScore(self, score):
		print("ID:%s get %d score!" % (self.id, score))
		g_scoreRank.updateScore(self, score)


class TeamObj(object):
	"""docstring for TeamObj"""
	def __init__(self, name):
		super(TeamObj, self).__init__()
		self.name 		= name
		self.reg    	= 0 	#1:有队员,0：无队员
		self.num 		= 0
		self.curDoor	= None 	#当前所在关卡

	def addMem(self, MID):
		self.num += 1
		for m in g_memArray:
			if m.id == MID:
				m.reset(self)
				return

		print("new mem, %s" % MID)
		
		newMem 	= Member(MID, self)
		g_memArray.append(newMem)  

	def getName(self):
		return self.name