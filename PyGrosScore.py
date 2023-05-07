from os import *
from os.path import *
from sys import *
def about():
    print('PhiRCode')
about()
system('copy template.py >> '+getenv('TEMP'))
chdir(getenv('TEMP'))
while True:
    if isfile('BME'):
        remove('BME')
    if isfile('BME\\PGS'):
        remove('BME\\PGS')
    if not exists('BME'):
        mkdir('BME')
    if not exists('BME\\PGS'):
        mkdir('BME\\PGS')
    chdir('BME\\PGS')
    system('copy ..\\..\\template.py .')
    print('[F]ile [C]ontrol [A]bout')
    mbo=input('Opt. >>>')
    if mbo=='F' or mbo=='f':
        print('''[N]ew
        [S]ave
        Save .[Z]ip
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
                system('notepad template.py')
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
        elif smo=='Z' or smo=='z':
            system(argv[0]+'\\7-zip\\7z32.exe a -t7z '+input('Zip save file:')+' .\*')
            input('Zipped folder to be Saved.')
            continue
        else:
            input('Option Error.')
            continue
    elif mbo=='C' or mbo=='c':
        print('[C]lear')
        print('[S]ettings')
        smo=input('Opt. >>>')
        if smo=='C' or smo=='c':
            system('cls')
            continue
        elif smo=='S' or smo=='s':
            print('Settings')
            print('========')
            print('[Z]ip setting:')
            ssm=input('Opt. >>>')
            if ssm=='Z' or ssm=='z':
                print('Uninstall 7-zip x86_[3]2 module')
                sss=input('Opt. >>>')
                def rec7z():
                    print('Are you sure you want to uninstall? It will not be recoverable and will need to be re-downloaded from GitHub.')
                    input('If canceled, close the window, otherwise press enter.')
                    chdir(argv[0].replace('PyGrosScore.py','7-zip'))
                if sss=='3':
                    rec7z()
                    remove('7z32.exe')
                else:
                    input('Option Error.')
                    continue
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
            print('''[P]roject
            [7]-zip''')
            ssm=input('Opt. >>>')
            if ssm=='P' or ssm=='p':
                system('notepad.exe '+argv[0].replace('PyGrosScore.py','LICENSE'))
            elif ssm=='7':
                system(argv[0].replace('PyGrosScore.py','7-zip\\Licenses'))
        else:
            input('Option Error.')
            continue
    else:
        input('Option Error.')
        continue