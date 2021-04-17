
import requests
ssl = 'authenticate.cert'
resp = requests.get('http://httpbin.org/ip', verify = 'path to that certificate')
print(resp)