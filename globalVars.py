
#全局变量
from threading import  RLock

doorRLock  = RLock()
memRLock   = RLock()
teamRLock  = RLock()


g_doorArray = []
g_memArray 	= []
g_TeamArray = []

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

class SorceRank(object):
	"""docstring for SorceRank"""
	def __init__(self):
		super(SorceRank, self).__init__()
		self.mem = {}
		self.team = {}

	def setTeamScore(self, teamname, score):
		self.team[teamname] = score

	def setMemScore(self, memID, score):
		self.team[memID] = score
		