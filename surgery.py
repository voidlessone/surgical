import socket
ip = "www.google.com"
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

s.connect((ip, port))
msg = "hello"
s.send(msg.encode('utf-8'))
r = s.recv(1024)
print(r)
