
import requests
resp = requests.get('http://httpbin.org/ip')
print("*"*50)
print("IP address of Jenkins host is ------------------{}-----------------".format(resp.text))
print("*"*50)
