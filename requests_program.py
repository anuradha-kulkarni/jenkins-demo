
import requests
ssl = 'authenticate.cert'
resp = requests.get('http://httpbin.org/ip')
print("IP address of Jenkins host is ------------------{}-----------------".format(resp.text))
