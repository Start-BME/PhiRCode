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
def notescount(note:int): #物量，必须添加在offset之后
    scho('    "numOfNotes": '+note)
def noteline(): #开始编写判定线和Note事件，必须添加在notescount之后
    scho('    "judgeLineList": [')
def line_start(): #开始编写一条判定线
    scho('        {')
def line_end(): #结束编写一条判定线
    scho('        }')
def line_notescount(note:int): #对于此判定线的物量
    scho('            "numOfNotes": '+note)
def line_noteabove(note:int): #对于此判定线的正面判定note物量
    scho('            "numOfNotesAbove": '+note)
def line_notebelow(note:int): #对于此判定线的反面判定note物量
    scho('            "numOfNotesBelow": '+note)
def line_bpm(bpm:float): #此判定线的bpm
    scho('            "bpm": '+bpm)
#请在以下区域编辑自制谱
