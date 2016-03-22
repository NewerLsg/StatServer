# -*- coding: utf-8 -*-

import globalVars 
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
		self.ID 	 = ID 			#ID
		self.teamIn	 = None			#内部队伍,为空表示没有
		self.time	 = 1			#队伍的进入时间
		self.targets = {}
		self.limit 	 = int(0)

class Target(object):
	"""docstring for Target"""
	def __init__(self, ID, door, sock):
		super(Target, self).__init__()
		self.ID   	= ID
		self.door 	= door
		self.sock 	= sock
		sock.src 	= self #通讯源,设备源

	def setStat(self, msg):
		print(msg)
		self.sock.write(msg)

	def reset(self,door,sock):
		self.sock =  sock
		self.door = door
		self.sock.src = self

	def closeByAccient(self):
		try:
			del self.door.targets[self.ID]
			serverLog.debug("target[%s] del from door[%d].", self.ID, int(self.door.ID))

		except KeyError:
			serverLog.debug("target[%s] not in door[%d]'s targets dict.", self.ID, str(self.door.ID))

		#except:
			#serverLog.debug("unexpect error")
					

#成员对象:主要是存储自己的ID以及对应的组
class Member(object):
	"""docstring for Member"""

	def __init__(self, ID, team):
		super(Member, self).__init__()	
		self.ID 		= ID 
		self.team 		= team
	
	def reset(self, team):
		self.team.numLeft -= 1	#原队伍人数减1

		if self.team.numLeft == 0: #队伍没有人
			self.team.curDoor = None
			globalVars.g_TeamArray.pop(self.team.ID)

		globalVars.g_scoreRank.clearMemScore(self)
		self.team 		= team

	def increaseScore(self):
		serverLog.debug("ID:[%s] get  score!",self.ID)
		self.team.increaseDoorScore();
		return globalVars.g_scoreRank.increaseScore(self)

#队伍对象，主要存储队名以及人数
class TeamObj(object):
	"""docstring for TeamObj"""

	def __init__(self, name): 
		super(TeamObj, self).__init__()
		self.name 		= str(name)
		self.ID 		= globalVars.g_teamNum 
		self.doorScore  = int(0) 	#当前关卡获得分数
		self.num 		= int(0)	#总人数
		self.numLeft	= int(0)	#剩余人数
		self.curDoor	= None 		#当前所在关卡
		globalVars.g_teamNum += 1

	def resetDoorScore(self):
		self.doorScore = 0

	def increaseDoorScore(self):
		self.doorScore += 1

	def addMem(self, MID):
		self.num += 1
		self.numLeft += 1
		try:
			mem =  globalVars.g_memArray[MID]
			mem.reset(self) #清理积分
			globalVars.g_memArray[MID] = Member(MID, self)
		except KeyError:
			#不存在则新建
			globalVars.g_memArray[MID] = Member(MID, self)

		#except:
			#serverLog.debug("unexpect error.")

		serverLog.debug("ID[%s] added to team name[%s], ID[%d].", MID, self.name, self.ID)		 