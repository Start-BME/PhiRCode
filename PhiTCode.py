#初始化
import os
def scho(systr:str):
    os.system('echo '+systr+' >> '+open(os.getenv('PROGRAMDATA')+'\\BME\\PyGros\\Dir.var',encoding='utf-8').readline().strip())
os.system('pause')
scho('{')
scho('    "formatVersion": 3,')
def end(): #结束语句，必须要添加在末尾
    scho('    ]')
    scho('}')
def offset(sec:float): #歌曲延迟，必须要添加在开头
    scho('    "offset": '+sec+',')
def notesnum(note:int): #物量，必须添加在offset之后
    scho('    "numOfNotes": '+note)
def noteline(): #开始编写判定线和Note事件
    scho('    "judgeLineList": [')
#请在以下区域编辑自制谱
