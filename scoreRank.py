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
		tempMem = None
		for m in self.mem:
			if m.ID == member.ID:
				tempMem = m

		if tempMem is not None:
			self.mem.remove(tempMem)

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
	def __increaseTeamScore(self, ID, name, MID):
		
		self.tlock.acquire()

		for t in self.team:
			if ID == t.ID:
				t.increaseScore(MID)
				
				self.team.sort(key=lambda  x: x.score, reverse = True)
				self.tlock.release()
				return	t.score

		newTeamScoreEntity = teamScoreEntity(ID, name)
		newTeamScoreEntity.increaseScore(MID)

		self.team.append(newTeamScoreEntity)
		self.team.sort(key=lambda  x: x.score, reverse = True)
		self.tlock.release()

		return 1 


	def getTeamScore(self, ID):
		ret = int(0)

		self.tlock.acquire()

		for t in self.team:
			if t.ID == ID:
				ret =  t.score
				break

		self.tlock.release()

		return ret

	def updateTeamDoor(self, ID , doorID): #更新队伍所在关卡
		ret = int(0)

		self.tlock.acquire()

		for t in self.team:
			if t.ID == ID:
				t.curdoorID = doorID  
				break
				
		self.tlock.release()	

	def increaseScore(self, mem):
		#一个人只对自己的积分修改

		self.mlock.acquire()
		for m in self.mem:
			if mem.ID == m.ID:
				m.score += 1
				self.mem.sort(key=lambda  x: x.score, reverse = True)
				self.mlock.release()
				return self.__increaseTeamScore(mem.team.ID, mem.team.name, mem.ID)
				 	
		self.mem.append(memScoreEntity(mem.ID, mem.team.name))
		self.mem.sort(key=lambda  x: x.score, reverse = True)
		self.mlock.release()
		return self.__increaseTeamScore(mem.team.ID, mem.team.name, mem.ID)

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
		self.curdoorID	= int(0)

	def increaseScore(self, MID):

		self.score += 1 #总分增加

		for m in self.memscore:
			if m.ID == MID:
				m.score += 1
				return self.score

		self.memscore.append(memScoreEntity(MID, self.name))

		return self.score	

class memScoreEntity():
	"""docstring for scoreEntity"""
	def __init__(self, ID, teamname):
		self.ID 		= ID
		self.score 		= int(1)
		self.teamname 	= teamname