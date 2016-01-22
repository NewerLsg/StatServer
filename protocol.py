from PyQt4.QtCore import *
from globalVars import *

#消息类型
#设备到服务器
MEN_TO_SERVER 	=  'DS'  	#门
TEAM_TO_SERVER  =  'TS'		#队伍
DEST_TO_SERVER  =  'MS'		#目标物

#服务器回复设备
SERVER_TO_MEN	=  'SD'  	#门
SERVER_TO_TEAM	=  'DT'  	#队伍
SERVER_TO_DEST	=  'SM'  	#目标物

#子类型
#门设备
MEN_AUTH_MSG	=  '00'		#请求开门权限

AUTH_ACCESS		=  '00'		#赋予权限
AUTH_DENY		=  '01'		#赋予权限

MEN_OPEN_MSG	=  '01'		#上传开门者ID

#组队靶
TEAM_NAEM_MSG	=  '00'		#上传队名
NAME_AVAIL		=  '00'		#名字可用
NAME_UNAVAIL	=  '01'		#名字被占用,不可用

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
		resp = parseMenMsg(msgContent)

	elif msgType == TEAM_TO_SERVER:
		resp = parseTeamMsg(msgContent)

	elif msgType == DEST_TO_SERVER:
		resp = parseDestMsg(msgContent)

	return resp


def parseMenMsg(msgContent):
	print("msg from MS")


def parseTeamMsg(msgContent):
	print("msg from MS")

	subtype = msgContent[0:2]
	content = msgContent[2:-1]

	#名字
	if subtype == TEAM_NAEM_MSG :
		for team in g_TeamArray:
			if team.name = content:
				return SERVER_TO_MEN + NAME_UNAVAIL + MSG_END

		#创建新的队伍
		newTeam  = TeamObj(content)
		g_TeamArray.append(newTeam)

		return SERVER_TO_MEN + NAME_AVAIL + MSG_END

	#队员ID列表
	elif subtype == TEAM_ID_MSG :
		#将队员加入ID
		num = int(content[1:2])


def parseDestMsg(msgContent):
	print("msg from MS")

	if len(msgContent) < 2 :
		return None

	mid = msgContent[0:1] #击中目标物的ID

	#找出ID对应的组

	for m in g_memArray:
		if mid == m.id:
			m.addScore(g_config['scoreUint']) #

	return None