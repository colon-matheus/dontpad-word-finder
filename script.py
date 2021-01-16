import requests
import re

desiredWord = 'senha'

i = 0
while i < 10:
    r = requests.get(f'http://dontpad.com/{i}')
    if r.status_code:
        find = re.search(desiredWord, r.text)
        if find:
            print(f'http://dontpad.com/{i}')  
    i += 1
print('Done')    
