import zipfile
import time
from datetime import datetime
from colored import fg

print('\n')
print(fg('magenta')+f"""[[[[[[[[]]]]]]]]]]]]]]]]]]]]]
[]                         []""")
print(fg('yellow')+  """[]Zip File Password Cracker[]""")

print(fg('cyan')+    """[]        By VPS           []""")

print(fg('magenta')+ """[[[[[[[[[[[[[[[]]]]]]]]]]]]]]"""+fg('white'))
print('\n')

zip_file = input('Enter zip file name with location : ')
pwd_file = input('Enter password dictionary file name with location : ')

print('\n')

start_time=datetime.today()
start = time.time()

color1=fg('red')
color2=fg('white')

try:
    zip_file_loaded =zipfile.ZipFile(zip_file)
except:
    print(color1+'No such zip file.'+color2)    
    input('Press Enter key to exit : ')
    quit()
try:
    pwd_file_loaded = open(pwd_file,'r')
except:
    print(color1+'No such password file.'+color2)
    input('Press Enter key to exit : ')
    quit()    

count=0

for password in pwd_file_loaded:
        count+=1
        print(password.strip('\n')+'-checking')
        
        try:
            
            zip_file_loaded.extractall(pwd=password.strip('\n').encode())
            password_founded=password.strip('\n')
            print('\n')
            print(f'Zip file : {zip_file}')
            print(f'Password Dictionary file : {pwd_file}')
            print('\n')
            print(f'Started time : {start_time}')
            end_time = datetime.today()
            end=time.time()
            print(f'Ended time : {end_time}')
            print(f'Time spend (in seconds) : {end-start} seconds')
            print(f'Time spend (in minutes) : {(end-start)/60} minutes')
            print(f'Time spend (in hours) : {((end-start)/60)/60} hours')
            print('\n')
            print(f'No. of items checked = {count}')
            print('\n')
            color=fg('cyan')
            color2=fg('white')
            print('Password found = '+color+password_founded+color2)
            
            break
            
        except:
            pass
else:
    print('\n')
    print(f'Zip file : {zip_file}')
    print(f'Password Dictionary file : {pwd_file}')
    print('\n')    
    print(f'Started time : {start_time}')
    end_time = datetime.today()
    end=time.time()
    print(f'Ended time : {end_time}')
    print(f'Time spend (in seconds) : {end-start} seconds')
    print(f'Time spend (in minutes) : {(end-start)/60} minutes')
    print(f'Time spend (in hours) : {((end-start)/60)/60} hours')
    print('\n')
    print(f'No. of items checked = {count}')
    print('\n')
    color1=fg('red')
    color2=fg('white')
    print(color1+'Password not found.'+color2)

print('\n')
input('Press Enter key to exit :')    