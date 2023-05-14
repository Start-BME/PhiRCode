from os import *
from os.path import *
from sys import *
def about():
    print('PhiRCode')
about()
system('copy PhiTCode.py >> '+getenv('TEMP'))
chdir(getenv('APPDATA'))
if not exists('BME'):
    mkdir('BME')
if not exists('BME\\PGS'):
    mkdir('BME\\PGS')
chdir('BME\\PGS')
system('copy '+getenv('TEMP')+'\\PhiTCode.py .')
while True:
    print('[F]ile [C]ontrol [A]bout')
    mbo=input('Opt. >>>')
    if mbo=='F' or mbo=='f':
        print('''[N]ew
[S]ave
[C]lose''')
        smo=input('Opt. >>>')
        if smo=='N' or smo=='n':
            print('''[I]nfo File
[S]core
[J]son''')
            r=input('Opt. >>>')
            if r=='I' or r=='i':
                system('echo # >> info.txt')
                for i in ['Name','Path','Song','Picture','Chart','Level','Composer','Charter']:
                    system('echo '+i+': '+input(i+':')+' >> info.txt')
            elif r=='S' or r=='s': 
                for i in ['Score','Music','Score Picture','Info']:
                    system('copy '+input(i+' File Path:')+' .')
                print('The operation is complete. You can save using File > Save.')
            elif r=='J' or r=='j':
                system('notepad PhiTCode.py')
            continue
        elif smo=='S' or smo=='s':
            system('copy . >> '+input('Please select a save location:'))
            print('Score be saved. You can close by clicking File > Close, or click the Close button in the upper right corner.')
            input()
            continue
        elif smo=='C' or smo=='c':
            print('If not saved, the changes will remain in %Temp%\\BME\\PGS\\Old.')
            input()
            mkdir('Old')
            system('copy . old')
            exit()
        else:
            input('Option Error.')
            continue
    elif mbo=='C' or mbo=='c':
        print('''[C]lear
[S]ettings''')
        smo=input('Opt. >>>')
        if smo=='C' or smo=='c':
            system('cls')
            continue
        elif smo=='S' or smo=='s':
            print('(Re)[I]nstall Module')
            ssm=input('Opt. >>>')
            if ssm=='I' or ssm=='i':
                print('Make sure the Python installation directory is added to the Path variable.')
                pp=input('PIP v. >')
                system('''python -m pip install os
python -m pip install sys''')
                continue
            else:
                input('Option Error.')
                continue
        else:
            input('Option Error.')
            continue
    elif mbo=='A' or mbo=='a':
        print('''[A]bout
[G]itHub Project
[L]icenses''')
        smo=input('Opt. >>>')
        if smo=='A' or smo=='a':
            about()
            continue
        elif smo=='G' or smo=='g':
            system('start https://github.com/users/Start-BME/projects/1')
            continue
        elif smo=='L' or smo=='l':
            print('[P]roject')
            ssm=input('Opt. >>>')
            if ssm=='P' or ssm=='p':
                system('notepad.exe '+argv[0].replace('PyGrosScore.py','LICENSE'))

        else:
            input('Option Error.')
            continue
    else:
        input('Option Error.')
        continue