from os import system,chdir,makedirs,mkdir,getenv
def about():
    print('PyGros Score Version 1.0')
    print('This project uses the MIT License and will be published on GitHub.')
    print('This project is made by Start-BME.')
about()
chdir(getenv('TEMP'))
makedirs('BME\\PGS')
chdir('BME\\PGS')
print('[F]ile [C]ontrol [A]bout')
while True:
    mbo=input('Options:')
    print('=====================')
    if mbo=='F' or mbo=='f':
        print('[N]ew Score')
        print('[S]ave')
        print('[C]lose')
        smo=input('Options:')
        if smo=='N' or ssm=='n':
            system('copy '+input('Score File Path:')+' .')
            system('copy '+input('Music File Path:')+' .')
            system('copy '+input('Score Picture File Path:')+' .')
            print('To write info from scratch, enter [Wr].')
            print('To import an info file, enter the path.')
            ssm=input('Info file options:')
            if ssm=='Wr' or ssm=='wR' or ssm=='WR' or ssm=='wr':
                system('echo # >> info.txt')
                system('echo Name: '+input('Name')+' >> info.txt')
                system('echo Path: '+input('Path')+' >> info.txt')
                system('echo Song: '+input('Song')+' >> info.txt')
                system('echo Picture: '+input('Picture')+' >> info.txt')
                system('echo Chart: '+input('Chart')+' >> info.txt')
                system('echo Level: '+input('Level')+' >> info.txt')
                system('echo Composer: '+input('Composer')+' >> info.txt')
                system('echo Charter: '+input('Charter')+' >> info.txt')
            else:
                system('copy '+ssm+' .')
            print('The operation is complete. You can save using File > Save.')
            continue
        elif smo=='S' or smo=='s':
            system('copy . >> '+input('Please select a save location:'))
            print('Score be saved. You can close by clicking File>Close, or click the Close button in the upper right corner.')
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
        print('[C]lear')
        smo=input('Options:')
        if smo=='C' or smo=='c':
            system('cls')
        else:
            input('Option Error.')
            continue
    elif mbo=='A' or mbo=='a':
        print('[A]bout')
        print('[G]itHub Project')
        smo=input('Options:')
        if smo=='A' or smo=='a':
            about()
        elif smo=='G' or smo=='g':
            system('start https://github.com/users/Start-BME/projects/1')
        else:
            input('Option Error.')
            continue
    else:
        input('Option Error.')
        continue
