import requests


a = requests.get('http://54.144.14.170:11817')
print(a.status_code)