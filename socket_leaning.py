#_*_coding:utf-8_*_
#author:Tiantian
import socket ,sys

try:
# create a AF_INET ,socket stream(TCP)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
#    print("Failed to create socket. Error code: " + str(Msg[0]) + ",Error message : " + Msg[1])
    sys.exit()
print("socket created")
ad = input("请输入网站地址：")
host = ad
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    #print("hostname could not be resolved. exiting")
    sys.exit()
print("ip address of " + host + " is " + remote_ip)
'''
# using ipv4 protecol and socket stream
    s.connect(("www.python.org",80))
    print("crate a socket")
'''
'''
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 80))
serversocket.listen(5)
while True:
    (clientsocket, address) = serversocket.accept()
    ct = client_thread(clientsocket)
    ct.run()
'''
# create a socket_server

