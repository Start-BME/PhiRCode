from os import system,chdir,makedirs,mkdir,getenv,getcwd,rmdir
from os import remove as delete
from os.path import exists,isfile
import sys as s
def about():
    print('PyGros Product')
    print('This project uses the MIT License.')
    print('This project is made by Start-BME.')
about()
chdir(getenv('TEMP'))
while True:
    if isfile('BME'):
        delete('BME')
    if isfile('BME\\PGS'):
        delete('BME\\PGS')
    if not exists('BME'):
        mkdir('BME')
    if not exists('BME\\PGS'):
        mkdir('BME\\PGS')
    chdir('BME\\PGS')
    print('[F]ile [C]ontrol [A]bout')
    mbo=input('Options:')
    if mbo=='F' or mbo=='f':
        print('[N]ew Score')
        print('[S]ave')
        print('Save .[Z]ip')
        print('[C]lose')
        smo=input('Options:')
        if smo=='N' or smo=='n':
            system('copy '+input('Score File Path:')+' .')
            system('copy '+input('Music File Path:')+' .')
            system('copy '+input('Score Picture File Path:')+' .')
            print('To write info from scratch, enter [Wr].')
            print('To import an info file, enter the path.')
            ssm=input('Info file options:')
            if ssm=='Wr' or ssm=='wR' or ssm=='WR' or ssm=='wr':
                system('echo # >> info.txt')
                system('echo Name: '+input('Name:')+' >> info.txt')
                system('echo Path: '+input('Path:')+' >> info.txt')
                system('echo Song: '+input('Song:')+' >> info.txt')
                system('echo Picture: '+input('Picture:')+' >> info.txt')
                system('echo Chart: '+input('Chart:')+' >> info.txt')
                system('echo Level: '+input('Level:')+' >> info.txt')
                system('echo Composer: '+input('Composer:')+' >> info.txt')
                system('echo Charter: '+input('Charter:')+' >> info.txt')
            else:
                system('copy '+ssm+' .')
            print('The operation is complete. You can save using File > Save.')
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
            print('[3]2-bit Zip')
            print('[6]4-bit Zip')
            ssm=input('Options:')
            if ssm=='6':
                system(s.argv[0]+'\\7-zip\\7z.exe a -t7z '+input('Zip save file:')+' .\*')
                input('Zipped folder to be Saved.')
                continue
            elif ssm=='3':
                system(s.argv[0]+'\\7-zip\\7z32.exe a -t7z '+input('Zip save file:')+' .\*')
                input('Zipped folder to be Saved.')
                continue
            else:
                input('Option Error.')
                continue
        else:
            input('Option Error.')
            continue
    elif mbo=='C' or mbo=='c':
        print('[C]lear')
        print('[S]ettings')
        smo=input('Options:')
        if smo=='C' or smo=='c':
            system('cls')
            continue
        elif smo=='S' or smo=='s':
            print('Settings')
            print('========')
            print('[Z]ip setting:')
            ssm=input('Options:')
            if ssm=='Z' or ssm=='z':
                print('Uninstall 7-Zip x[6]4 module')
                print('Uninstall 7-zip x86_[3]2 module')
                sss=input('Options:')
                def rec7z():
                    print('Are you sure you want to uninstall? It will not be recoverable and will need to be re-downloaded from GitHub.')
                    input('If canceled, close the window, otherwise press enter.')
                    chdir(s.argv[0].replace('PyGrosScore.py','7-zip'))
                if sss=='6':
                    rec7z()
                    delete('7z.exe')
                elif sss=='3':
                    rec7z()
                    delete('7z32.exe')
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
        print('[A]bout')
        print('[G]itHub Project')
        smo=input('Options:')
        if smo=='A' or smo=='a':
            about()
            continue
        elif smo=='G' or smo=='g':
            system('start https://github.com/users/Start-BME/projects/1')
            continue
        else:
            input('Option Error.')
            continue
    else:
        input('Option Error.')
        continue
