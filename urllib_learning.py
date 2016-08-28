#_*_coding:utf-8_*_
#author:Tiantian
import urllib.request
import urllib.parse
u = urllib.request.urlopen('http://www.96dyy.com/dianying/')
print(u.read())
'''
url = 'http://pythonprogramming.net'
values = {'s':'basic',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData) 
'''
