# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from globalVars import *
from communicationObjs import *

import time

#设备到服务器
MEN_TO_SERVER 	=  'DS'  	#门
TEAM_TO_SERVER  =  'TS'		#队伍
DEST_TO_SERVER  =  'MS'		#目标物

#服务器回复设备
SERVER_TO_MEN	=  'SD'  	#门
SERVER_TO_TEAM	=  'ST'  	#队伍
SERVER_TO_DEST	=  'SM'  	#目标物

#子类型
#门设备
MEN_AUTH_MSG	=  '00'		#请求开门权限

AUTH_ACCESS		=  '00'		#赋予权限
AUTH_DENY		=  '01'		#赋予权限

MEN_OPEN_MSG	=  '01'		#上传开门者ID

#组队靶
TEAM_NAEM_MSG	=  '00'		#上传队名
NAME_AVAIL		=  '01'		#名字可用
NAME_UNAVAIL	=  '00'		#名字被占用,不可用

TEAM_ID_MSG		=  '01'		#上传对内成员ID列表

MSG_END			=   '\n'

def parseMsg(rawMsg):
	resp = None

	if len(rawMsg) < 2 :
		return None

	msgType = rawMsg[0:2]
	msgContent = rawMsg[2:-1]

	print("%s" % rawMsg[0:2])
	print("%s" % rawMsg[2:-1])

	if msgType == MEN_TO_SERVER:
		return  parseMenMsg(msgContent)

	elif msgType == TEAM_TO_SERVER:
		return  parseTeamMsg(msgContent)

	elif msgType == DEST_TO_SERVER:
		return  parseDestMsg(msgContent)


def parseMenMsg(msgContent):
	print("msg from door")

	if len(msgContent) < 3:
		return None

	subtype = msgContent[0:2]
	content = msgContent[2:]

	#开门权限
	if subtype == MEN_AUTH_MSG:
		print("get auth")

		did = int(content[0:])  

		#超过门的权限
		if did > g_config['tatolDoors']:
			return SERVER_TO_MEN + AUTH_DENY + MSG_END #回复一个deny的报文
		
		#不需要锁，因为当前门只会请求自己的权限
		#获取上一个门的状态可能不对，但是由于会轮询，下一次就是准确的
		curDoor = g_doorArray[did]
		curTime = time.time()

		#门内物无队伍 or 门内队伍被淘汰了——给开门权限
			#当前门是第一道门，则直接给权限
			#其他门,前一个门有队伍且积分达到指标,给权限
		if curDoor.teamIn is None \
				or curDoor.time < curTime - g_config['timeLimit']:	

			print("prefix condition matched.")

			if did == 1:
				print("first door open")
				return  SERVER_TO_MEN + AUTH_ACCESS + MSG_END

			elif  g_doorArray[did - 1].teamIn is not None \
					and g_scoreRank.getTeamScore(g_doorArray[did - 1].teamIn.name)  > 0:
				print("score matched")			
				return  SERVER_TO_MEN + AUTH_ACCESS + MSG_END

		print("condition not matched")		
		return SERVER_TO_MEN + AUTH_DENY + MSG_END

	#开门
	elif subtype == MEN_OPEN_MSG:
		print("open door")
		mid = content[0:1] #取得开门者ID
		did = int(content[1:])  #门id

		print("menid:%d" % did)

		#不用锁，当前门只会改自己的状态，不会有其他门来改它不会冲突
		curDoor = g_doorArray[did] 		#当前请求的门

		if did > g_config['tatolDoors']:
			return ERVER_TO_MEN + '00' + MSG_END 		#这个队员不属于任何队伍，亮起0个目标物

		for m in g_memArray:
			if m.id == mid:
				print("find team:%s" % m.team.name)
				curDoor.teamIn = m.team
				curDoor.time   = time.time()
				count = str(m.team.num * g_config['targetUint'])
				return  SERVER_TO_MEN + count.rjust(2,'0') + MSG_END
				
		return SERVER_TO_MEN + '00' + MSG_END 		#这个队员不属于任何队伍，亮起0个目标物
	

def parseTeamMsg(msgContent):
	print("msg from TS")

	subtype = msgContent[0:2]
	content = msgContent[2:]

	print("subtype:%s, content:%s" %(subtype, content))

	#名字
	if subtype == TEAM_NAEM_MSG:
		for team in g_TeamArray:
			if team.name == content:
				return SERVER_TO_TEAM + NAME_UNAVAIL + MSG_END

		#创建新的队伍
		newTeam = TeamObj(content)
		g_TeamArray.append(newTeam)

		return SERVER_TO_TEAM + NAME_AVAIL + MSG_END

	#队员ID列表
	elif subtype == TEAM_ID_MSG :
		#将队员加入ID
		num = int(content[0:2])

		print("num:%d" % (num))
		if num <= 0:
			return None,

		#队名列表的结束位置
		#例：02ABHONGDUI -- 02为个数, A、B为ID，HONGDUI为队名
		#num = 2，则namelistEnd为 2 + 2 * 1 = 4，那在content位置5即为名字列表的结束 
		nameListEnd = 2 + num * g_config['nameSize']  

		#必须处理不合格的报文
		if len(content) < nameListEnd:
			return None

		namelist = content[2:nameListEnd]
		teamName = content[nameListEnd:]

		print("list:%s, teamname:%s" % (namelist, teamName))

		#将ID加入队伍
		for team in g_TeamArray:
			if team.name == teamName and team.reg == 0:
				pos = int(0)
				for x in range(1, num + 1):
					end = int(pos + g_config['nameSize'])
					print("ID[%d] :%s "  % (x, namelist[pos:end]))
					team.addMem(namelist[pos:end])
					pos += g_config['nameSize'] 
				team.reg = 1
				break

		return None

def parseDestMsg(msgContent):

	print("msg from MS")
	print("msglen:%d, nameSize:%d" % (len(msgContent) , int(g_config['nameSize'])))

	if len(msgContent) < int(g_config['nameSize']) :
		return None

	#目标物发送击中目标物的ID,
	mid = msgContent[0:g_config['nameSize']] 

	print("%s" % mid)

	#找出ID对应的组,并更新分数
	for m in g_memArray:
		if mid == m.id:
			m.addScore(g_config['scoreUint']) 
			break

	return None