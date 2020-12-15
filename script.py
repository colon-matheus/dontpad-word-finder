import requests

BASE_URL = 'http://dontpad.com'


r = requests.get(BASE_URL)

print(r.text)