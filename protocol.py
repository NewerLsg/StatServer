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

DEST_LIGHT		=   '1'		#点亮
DEST_DOWN		=   '0'     #熄灭
	
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

	subtype = msgContent[0:SUBTYPE_LEN]
	content = msgContent[SUBTYPE_LEN:]

	#开门权限
	if subtype == MEN_AUTH_MSG:
		did = int(content[0:])  

		serverLog.debug("[%d] request open authority.",did)

		try:
			curDoor = g_doorArray[did]
			curTime = time.time()
	
			#门内无队伍:门内队伍过关 or 门内队伍挑战超时
			if curDoor.teamIn is None \
					or curDoor.time < curTime - g_config['timeLimit']:	

				serverLog.debug("prefix condition matched.")

				#第一道门--直接给权限
				if did == 1:	
					serverLog.debug("first door open")

					return  SERVER_TO_MEN + AUTH_ACCESS + MSG_END

				#其他门--前面门内有队伍且达到积分要求
				elif  g_doorArray[did - 1].teamIn is not None \
						and g_scoreRank.getTeamScore(g_doorArray[did - 1].teamIn.name)  > 0:

					serverLog.debug("score matched")		
					return  SERVER_TO_MEN + AUTH_ACCESS + MSG_END

			serverLog.debug("condition not matched")
			return SERVER_TO_MEN + AUTH_DENY + MSG_END

		except IndexError: 
			serverLog.debug("invalid door id [%d].", did)
			return SERVER_TO_MEN + AUTH_DENY + MSG_END 

	#开门
	elif subtype == MEN_OPEN_MSG:
		
		mid = content[0:g_config['nameSize']] 		#开门者ID
		did = int(content[g_config['nameSize']:])  	#门id

		try:
			curDoor = g_doorArray[did]		#门
			m  		= g_memArray[mid] 		#成员
			serverLog.debug("door open, door id[%d], mem id[%s]", did, mid)

		except (IndexError,KeyError):
			serverLog.debug("invalid msg, door id[%d], mem id[%s]", did, mid)
			return None

		curDoor.teamIn 	= m.team 		#当前门的队伍
		m.team.curDoor 	= curDoor		#当前队伍所在的门
		curDoor.time   	= time.time()
		count 			= int(m.team.num) * int(g_config['targetUint'])

		serverLog.debug("get team, team members[%s], [%d] targets will be light up.", int(m.team.num), count)

		for key in curDoor.targets.keys():
			if count > 0:
				#点亮
				serverLog.debug("[%s] light up", key)
				curDoor.targets[key].setStat(SERVER_TO_DEST + DEST_LIGHT + MSG_END)
				count -= 1
			else:
				#熄灭
				serverLog.debug("[%s] down", key)
				curDoor.targets[key].setStat(SERVER_TO_DEST + DEST_DOWN + MSG_END)		

		if count > 0:
			serverLog.debug("not enough targets.")

		return None
	

def parseTeamMsg(msgContent):
	
	subtype = msgContent[0:SUBTYPE_LEN]
	content = msgContent[SUBTYPE_LEN:]

	#名字
	if subtype == TEAM_NAEM_MSG:
		serverLog.debug("regist name.")

		if content in g_TeamArray.keys():
			#已存在
			serverLog.debug("invalid name.")
			return SERVER_TO_TEAM + NAME_UNAVAIL + MSG_END

		else:
			#创建新的队伍
			newTeam = TeamObj(content)
			g_TeamArray[content] = newTeam
			serverLog.debug("valid name.")
			return SERVER_TO_TEAM + NAME_AVAIL + MSG_END

	#队员ID列表
	elif subtype == TEAM_ID_MSG :

		num = int(content[0:2])		#ID个数

		serverLog.debug("send member IDs, num[%d]", num)

		if num <= 0:			#负数-非法
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
		try:
			team = g_TeamArray[teamName]  

			if team.reg ==  0:	#当前队伍没有发送名字
				pos = int(0)
				for x in range(0, num):
					end = int(pos + g_config['nameSize'])
					team.addMem(namelist[pos:end])
					pos += g_config['nameSize'] 

				team.reg = 1

		except KeyError:
			serverLog.debug("team[%s] not exist", teamName)

		return None

def parseDestMsg(msgContent, sock):
	serverLog.debug("msg from MS")

	subtype = msgContent[0:SUBTYPE_LEN]
	content = msgContent[SUBTYPE_LEN:]

	#初始化
	if subtype == DEST_INIT:
		serverLog.debug("target init.")

		if len(content) != 4:
			serverLog.debug("invalid req.")
			return 

		tid = content[0:2]
		did = int(content[2:])

		try:
			curDoor = g_doorArray[did]

			if tid in curDoor.targets.keys(): #门内目标物ID已存在
				target = curDoor.targets[tid];
				#target.reset(curDoor, sock)
				serverLog.debug("target[%s] in team[%d] already exist.", tid, did)

			else:							#目标物ID不存在需要初始化
				target =  Target(tid, g_doorArray[did], sock)
				curDoor.targets[tid] = target

				print("target{%s} in  door[%d]"% (str(curDoor.targets), did))
				serverLog.debug("target[%s] in team[%d] init succ.", tid, did)	

		except IndexError:			#门不存在
			serverLog.debug("invalid door id [%d].", did)
			return None	

	#被击中
	elif subtype == DEST_SHOOTED:
		serverLog.debug("target shooted.")

		if len(content) != int(g_config['nameSize']) :
			serverLog.debug("invalid MID:[%s], len don't matched", content)

		try:
			mem = g_memArray[content]
			teamTotalScore = mem.addScore(g_config['scoreUint']) 

		except KeyError:
			serverLog.debug("MID[%d] don't exist.", content)

	return None