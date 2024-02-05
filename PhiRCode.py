import os,platform
if platform.system()=='Windows':
    print('欢迎回到 Phigros！')
    print('注意：输入数据时不要在末尾添加反斜杠！')
    d=input('请输入新建谱面目录：')
    n=input('请输入导入曲绘目录：')
    m=input('请输入导入音乐目录：')
    index=0
    for varl in [d,n,m]:
        index+=1
        if varl[-1]=='\\':
            if index==1:
                d=d[:-2]
            elif index==2:
                n=n[:-2]
            elif index==3:
                m=m[:-2]
        if varl[-2]=='\\"':
            if index==1:
                d=d[:-3]+'"'
            elif index==2:
                n=n[:-3]+'"'
            elif index==3:
                m=m[:-3]+'"'
    if not os.path.exists(d):
        os.makedirs(d)
    if not os.path.exists(os.getenv('PROGRAMDATA')+'\\BME\\PyGros\\'):
        os.makedirs(os.getenv('PROGRAMDATA')+'\\BME\\PyGros\\')
    os.chdir(d)
    os.system('copy '+n+' '+d)
    os.system('copy '+m+' '+d)
    os.system('echo # >> info.txt')
    os.system('echo Name: '+input('请输入名称：')+' >> info.txt')
    os.system('echo Path: '+d.split('\\')[-1]+' >> info.txt')
    os.system('echo Song: '+m.split('\\')[-1]+' >> info.txt')
    os.system('echo Picture: '+n.split('\\')[-1]+' >> info.txt')
    os.system('echo Chart: pygrox.json >> info.txt')
    os.system('echo Level: '+input('请输入定级：')+' >> info.txt')
    os.system('echo Composer: '+input('请输入曲师：')+' >> info.txt')
    os.system('echo Charter: '+input('请输入谱师：')+' >> info.txt')
    if os.path.isfile(os.getenv('PROGRAMDATA')+'\\BME\\PyGros\\Dir.var'):
        os.remove(os.getenv('PROGRAMDATA')+'\\BME\\PyGros\\Dir.var')
    os.system('echo '+d+'\\pygrox.json" >> '+os.getenv('PROGRAMDATA')+'\\BME\\PyGros\\Dir.var') 
    input('启动 PhiECode 以继续编辑')
else:
    input('暂不支持此平台')