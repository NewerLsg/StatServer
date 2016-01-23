from globalVars import *

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
		self.score 		= 0
	
	def reset(self, team):
		self.score  	= 0
		self.team 		= team
		
	def getScore(self):
		return self.score

	def getTeamname(self):
		return self.teamName

	def getID(self):
		return self.id 

	def addScore(self, score):
		print("ID:%s get %d score!" % (self.id, score))
		self.score 	+= score    		 	 		#队员积分
		self.team.totalSocre += score 		 		#队伍积分	
		#保留队员在当前队伍的历史积分，避免重新组队导致积分丢失
		self.team.memScore[self.id] = self.score    

class TeamObj(object):
	"""docstring for TeamObj"""
	def __init__(self, name):
		super(TeamObj, self).__init__()
		self.name 		= name
		self.totalSocre = 0
		self.reg    	= 0 	#1:有队员,0：无队员
		self.memScore 	= {}
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

	def getScore(self):
		return self.score