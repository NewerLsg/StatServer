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

	def getTeamIn():
		return self.teamIn


class Member(object):
	"""docstring for Member"""
	def __init__(self, id, team):
		super(Member, self).__init__()	
		self.id 		= id
		self.team 		= team
		self.score 		= 0
	
	def getScore(self):
		return self.score

	def getTeamname(self):
		return self.teamName

	def getID(self):
		return self.id 

	def addScore(self, score):
		print("ID:%d get %d score!" % (self.id, score))
		self.score 	+= score    		 #队员积分
		self.team.score += score 		 #队伍积分			


class TeamObj(object):
	"""docstring for TeamObj"""
	def __init__(self, name):
		super(TeamObj, self).__init__()
		self.name = name
		self.score = 0
		self.mem = []

	def addMem(MID):
		newMem 	= Member(MID, self)
		self.mem.append(newMem)

	def getName():
		return self.name

	def getScore(self):
		return self.score