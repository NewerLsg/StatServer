# -*- coding: utf-8 -*-

from threading import  RLock
import copy  

#积分排序：包括所有队伍的分、个人的分
class ScoreRank():
	"""docstring for ScoreRank"""

	def __init__(self):
		self.mem = []
		self.team = []
		self.mlock = RLock()
		self.tlock = RLock()

	def getTeamScoreList(self):
		self.tlock.acquire()
		ret = copy.deepcopy(self.team)
		self.tlock.release()
		return ret

	def getMemScoreList(self):
		self.mlock.acquire()
		ret = copy.deepcopy(self.mem)
		self.mlock.release()
		return ret

	def clearMemScore(self, member):

		if member.team.numLeft == 0:	#所在队伍队员均重新分配了
			self.clearTeamSocre(member.team.ID, member.team.name)

		self.mlock.acquire()
		for m in self.mem:
			if m.ID == member.ID:
				m.score =  0

		self.mlock.release()

	def clearTeamSocre(self, ID ,name):

		self.tlock.acquire()

		tempteam = None
		for t in self.team:
			if t.ID == ID and t.name == name:
				tempteam = t
				break

		if tempteam is not None:
			self.team.remove(tempteam)

		self.tlock.release()


	#私有方法 更新队伍总分，并返回
	def __updateTeamScore(self, ID, name, MID, score):
		
		self.tlock.acquire()

		for t in self.team:
			if ID == t.ID:
				t.updateScore(MID, score)
				
				self.team.sort(key=lambda  x: x.score, reverse = True)
				self.tlock.release()
				return	t.score

		newTeamScoreEntity = teamScoreEntity(ID, name)
		newTeamScoreEntity.updateScore(MID, score)

		self.team.append(newTeamScoreEntity)
		self.team.sort(key=lambda  x: x.score, reverse = True)
		self.tlock.release()

		return score 


	def getTeamScore(self, ID):
		ret = int(0)

		self.tlock.acquire()

		for t in self.team:
			if t.ID == ID:
				ret =  t.score
				break

		self.tlock.release()

		return ret

	def updateScore(self, mem , score):
		#一个人只对自己的积分修改

		self.mlock.acquire()
		for m in self.mem:
			if mem.ID == m.ID:
				m.score += score
				self.mem.sort(key=lambda  x: x.score, reverse = True)
				self.mlock.release()
				return self.__updateTeamScore(mem.team.ID, mem.team.name, mem.ID, score)
				 	
		self.mem.append(memScoreEntity(mem.ID, score, mem.team.name))
		self.mem.sort(key=lambda  x: x.score, reverse = True)
		self.mlock.release()
		return self.__updateTeamScore(mem.team.ID, mem.team.name, mem.ID,score)

class scoreEntity():
	"""docstring for scoreEntity"""
	def __init__(self, ID, name , score):
		self.ID 	= ID
		self.name 	= name
		self.score 	= score

class teamScoreEntity():
	"""docstring for scoreEntity"""
	def __init__(self, ID, name):
		self.ID 		= ID
		self.name 		= name
		self.score 		= 0
		self.memscore 	= []

	def updateScore(self, MID, score):

		self.score += score #总分增加

		for m in self.memscore:
			if m.ID == MID:
				m.score += score
				return self.score

		self.memscore.append(memScoreEntity(MID, score, self.name))

		print("team name[%s] ID[%d] score[%d]" %(self.name, self.ID, self.score))

		for m in self.memscore:
			print("mem id[%s], mem score[%d] team name[%s]" %(m.ID, m.score, m.teamname))

		return self.score	

class memScoreEntity():
	"""docstring for scoreEntity"""
	def __init__(self, ID, score, teamname):
		self.ID 		= ID
		self.score 		= score
		self.teamname 	= teamname