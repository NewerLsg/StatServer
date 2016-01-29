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

	def clearMemScore(self, name):
		self.mlock.acquire()
		for m in self.mem:
			if m.name == name:
				m.score =  0
		self.mlock.acquire()

	#私有方法 更新队伍总分，并返回
	def __updateTeamScore(self, name, score):
		#防止同一个对中的人同时修改
		self.tlock.acquire()

		for t in self.team:
			if name == t.name:
				t.score += score
				self.team.sort(key=lambda  x: x.score, reverse = True)
				self.tlock.release()
				return	t.score

		self.team.append(scoreEnpty(name, score))
		self.team.sort(key=lambda  x: x.score, reverse = True)
		self.tlock.release()

		return score 


	def getTeamScore(self,name):
		ret = int(0)

		self.tlock.acquire()

		for t in self.team:
			if t.name == name:
				ret =  t.score
				break

		self.tlock.release()

		return ret

	def updateScore(self, mem , score):
		#一个人只对自己的积分修改

		self.mlock.acquire()
		for m in self.mem:
			if mem.id == m.name:
				m.score += score
				self.mem.sort(key=lambda  x: x.score, reverse = True)
				self.mlock.release()
				return self.__updateTeamScore(mem.team.name, score)
				 	
		self.mem.append(scoreEnpty(mem.id, score))
		self.mem.sort(key=lambda  x: x.score, reverse = True)
		self.mlock.release()
		return self.__updateTeamScore(mem.team.name, score)

class scoreEnpty():
	"""docstring for scoreEnpty"""
	def __init__(self, name , score):
		self.name 	= name
		self.score 	= score
		