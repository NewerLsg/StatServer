class Member(object):
	"""docstring for Member"""
	def __init__(self, id, teamName):
		super(Member, self).__init__()	
		self.id 		= id
		self.teamName 	= name
		self.score 		= 0
		
	def addScore(self, score):
		self.score 	+= score	

class TeamObj(object):
	"""docstring for TeamObj"""
	def __init__(self, name):
		super(TeamObj, self).__init__()
		self.name = name
		self.score = 0
		self.mem = []

	def addMem(MID):
		newMem 	= Member(MID, self.name)
		self.mem.append(newMem)

	def addScore(MID, score):
		for m in self.mem:
			if m.id == MID
				m.addScore(score)

		self.score += score 