# -*- coding: utf-8 -*-
import socket 
from datetime import datetime
now = datetime.now()
hora_atual = "%s:%s:%s"%(now.hour,now.minute,now.second)
data_atual = "%s/%s/%s"%(now.day,now.month,now.year)

log = open('log.txt', 'a')

ip_proxy = '192.168.1.3' 
port_proxy = 3131
ip_client = '192.168.1.3'
port_client = 3132
port_server = 3133
ip_bloq = ["192.168.1.4","192.168.1.6","192.168.1.2"]

addr_proxy = (ip_proxy, port_proxy) 
addr_client = (ip_client, port_client)

proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
proxy_socket.bind(addr_proxy) 
proxy_socket.listen(5)

print('aguardando conexao...')
con, client = proxy_socket.accept()


print('concectado com '+client[0])
msg, ip_server = con.recv(1024).decode('utf-8').split('/')
if not msg: proxy_socket.close()
print(client, msg)       
print('finalizando conexao do cliente '+client[0])
proxy_socket.close()

addr_server = (ip_server, port_server)
text = "%s|%s|%s|%s|%s\n"%(client,ip_server,data_atual,hora_atual,msg)
log.write(text)
log.close()
aux = 0
aux2 = 0
while(aux<2):
    aux+=1
    proxy2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    i = 0
    for i in range(len(ip_bloq)):
        if ip_server == ip_bloq[i]:
            print("FOI SOLICITADO UM ENDEREÇO QUE ESTÁ BLOQUEADO!")
            aux2 = 1
            break
    if aux2 == 1:
        break
    proxy2_socket.connect(addr_server)
    proxy2_socket.send(bytes(msg,'utf-8'))
    proxy2_socket.close()