# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from globalVars import *
from communicationObjs import *
from log import *

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

AUTH_ACCESS		=  '01'		#赋予权限
AUTH_DENY		=  '00'		#不赋予权限

MEN_OPEN_MSG	=  '01'		#上传开门者ID

#组队靶
TEAM_NAEM_MSG	=  '00'		#上传队名
NAME_AVAIL		=  '01'		#名字可用
NAME_UNAVAIL	=  '00'		#名字被占用,不可用

TEAM_ID_MSG		=  '01'		#上传对内成员ID列表

#目标物
DEST_INIT		=  '00'		#目标物上传状态
DEST_SHOOTED	=  '01'		#目标物被击中

RESP_DEST_INIT  =   'TI'	#返回中携带的字段


#子类型长度,目前均为2字节
MSGTYEP_LEN		=   2
SUBTYPE_LEN 	= 	2		

#结束标志-换行
MSG_END			=  '\n'

def parseMsg(rawMsg, sock):
	resp = None

	if len(rawMsg) < 2 :
		return None

	msgType 	= rawMsg[0:MSGTYEP_LEN]
	msgContent 	= rawMsg[MSGTYEP_LEN:-1]

	print("%s" % msgType)
	print("%s" % msgContent)

	if msgType == MEN_TO_SERVER:
		return  parseMenMsg(msgContent)

	elif msgType == TEAM_TO_SERVER:
		return  parseTeamMsg(msgContent)

	elif msgType == DEST_TO_SERVER:
		return  parseDestMsg(msgContent, sock)


def parseMenMsg(msgContent):
	serverLog.debug("type:[DS]")

	if len(msgContent) < 3:
		return None

	subtype = msgContent[0:SUBTYPE_LEN]
	content = msgContent[SUBTYPE_LEN:]

	#开门权限
	if subtype == MEN_AUTH_MSG:
		did = int(content[0:])  

		serverLog.debug("[%d] request open authority.",did)

		#超过门数的限制
		if did > g_config['tatolDoors'] or did < 0:
			serverLog.debug("invalid door.")
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

			serverLog.debug("prefix condition matched.")

			if did == 1:
				serverLog.debug("first door open")

				return  SERVER_TO_MEN + AUTH_ACCESS + MSG_END

			elif  g_doorArray[did - 1].teamIn is not None \
					and g_scoreRank.getTeamScore(g_doorArray[did - 1].teamIn.name)  > 0:

				serverLog.debug("score matched")		
				return  SERVER_TO_MEN + AUTH_ACCESS + MSG_END

		serverLog.debug("condition not matched")

		return SERVER_TO_MEN + AUTH_DENY + MSG_END

	#开门
	elif subtype == MEN_OPEN_MSG:
		
		mid = content[0:g_config['nameSize']] #取得开门者ID
		did = int(content[g_config['nameSize']])  #门id

		serverLog.debug("door open, door id[%d], mem id[%s]", did, mid)

		#不用锁，当前门只会改自己的状态，不会有其他门来改它不会冲突
		curDoor = g_doorArray[did] 		#当前请求的门

		if did > g_config['tatolDoors']:
			serverLog.debug("mem id[%s] is not in any team.", mid)
			return None 		#这个队员不属于任何队伍，亮起0个目标物

		for m in g_memArray:
			if m.id == mid:
				curDoor.teamIn = m.team
				curDoor.time   = time.time()
				serverLog.debug("get team, team members[%s].", int(m.team.num))

				count = str(int(m.team.num) * int(g_config['targetUint']))

				for t in curDoor.targets:
					if count > 0:
						#点亮
						t.setStat("SM00\n")
					else:
						#熄灭
						t.setStat("SM001\n")	 	
				 	count -= 1

				
				return None
				
		return None 		#这个队员不属于任何队伍，亮起0个目标物
	

def parseTeamMsg(msgContent):
	
	subtype = msgContent[0:SUBTYPE_LEN]
	content = msgContent[SUBTYPE_LEN:]

	serverLog.debug("team request")

	#名字
	if subtype == TEAM_NAEM_MSG:
		serverLog.debug("regist name.")
		for team in g_TeamArray:
			if team.name == content:
				serverLog.debug("invalid name.")
				return SERVER_TO_TEAM + NAME_UNAVAIL + MSG_END

		#创建新的队伍
		newTeam = TeamObj(content)
		g_TeamArray.append(newTeam)

		serverLog.debug("valid name.")
		return SERVER_TO_TEAM + NAME_AVAIL + MSG_END

	#队员ID列表
	elif subtype == TEAM_ID_MSG :

		#将队员加入ID
		num = int(content[0:2])

		serverLog.debug("send member IDs, num[%d]", num)

		if num <= 0:
			return None,

		#队名列表的结束位置
		#例：02ABHONGDUI -- 02为个数, A、B为ID，HONGDUI为队名
		#num = 2，则namelistEnd为 2 + 2 * 1 = 4，那在content位置5即为名字列表的结束 
		nameListEnd = 2 + num * g_config['nameSize']  

		#必须处理不合格的报文
		if len(content) < nameListEnd:
			serverLog.debug("invalid name list.", num)
			return None

		namelist = content[2:nameListEnd]
		teamName = content[nameListEnd:]

		serverLog.debug("namelist:[%s], teamname:[%s]", namelist, teamName)

		#将ID加入队伍
		for team in g_TeamArray:
			if team.name == teamName and team.reg == 0:
				pos = int(0)
				for x in range(1, num + 1):
					end = int(pos + g_config['nameSize'])
					team.addMem(namelist[pos:end])
					pos += g_config['nameSize'] 
				team.reg = 1
				break

		return None

def parseDestMsg(msgContent, sock):
	serverLog.debug("msg from MS")

	subtype = msgContent[0:SUBTYPE_LEN]
	content = msgContent[SUBTYPE_LEN:]

	if subtype == DEST_INIT:
		serverLog.debug("target init.")

		if len(content) != 4:
			serverLog.debug("invalid req.")
			return 

		tid = int(content[0:2])
		did = int(content[2:])

		if did > g_config['tatolDoors']  or did < 0:
			serverLog.debug("door don't exist[%d].", did)
			return 

		for t in g_doorArray[id].targets:
			if t.id == tid:
				serverLog.debug("target[%d] already init.", tid)
				return

		g_doorArray[did].targets.append(Target(tid, g_doorArray[did], sock))

		serverLog.debug("target[%d] init succ.", tid)

		return 

	elif subtype == DEST_SHOOTED:
		serverLog.debug("target shooted.")

		if len(content) != int(g_config['nameSize']) :
			serverLog.debug("invalid ID:[%s], len don't matched", content)

		#找出ID对应的组,并更新分数
		for m in g_memArray:
			if content == m.id:
				m.addScore(g_config['scoreUint']) 
				return

	serverLog.debug("ID[%d] don't exist.", content)

	return None