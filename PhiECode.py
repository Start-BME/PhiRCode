import os
score_ver=3
score_offset=score_notenum=0
def scho(systr:str):
    os.system('echo '+systr+' >> '+open(os.getenv('PROGRAMDATA')+'\\BME\\PyGros\\Dir.var',encoding='utf-8').readline().strip())
def see():
    text=[
    '{',
    '    "formatVersion": '+score_ver+',',
    '    "offset": '+score_offset+',',
    '    "numOfNotes": '+score_notenum+',',
    '    "judgeLineList": [',
            #Line ---
    '    ]',
    '}']
    return text
while True:
    os.system('cls')
    print('文件(F) 编辑(E) 查看(V) 工具(T)')
    s=input('选择(输入大写字母)：')
    if s=='F':
        print('保存(S)')
        ss=input('选择(输入大写字母)：')
        if ss=='S':
            os.remove(open(os.getenv('PROGRAMDATA')+'\\BME\\PyGros\\Dir.var',encoding='utf-8').readline().strip())
            for txt in see():
                scho(txt)
    elif s=='E':
        print('数据调整(D)')
        ss=input('选择(输入大写字母)：')
        if ss=='D':
            score_offset=float(input('延迟(s)：'))
            score_notenum=int(input('物量：'))
    elif s=='V':
        print('预览(L) 颜色(C)')
        ss=input('选择(输入大写字母)：')
        if ss=='L':
            for txt in see():
                print(txt)
        elif ss=='C':
            color=input('颜色：(输入Windows color 16进制色号)')
            os.system('color '+color)
    elif s=='T':
        print('切换至旧版(O)')
        ss=input('选择(输入大写字母)：')
        if ss=='O':
            os.system('copy PhiTCode.py '+os.getenv('PROGRAMDATA')+'\\BME\\PyGros\\')
            os.system('copy pygros.py '+os.getenv('PROGRAMDATA')+'\\BME\\PyGros\\')
            os.system('NOTEPAD.EXE '+os.getenv('PROGRAMDATA')+'\\BME\\PyGros\\PhiTCode.py')
