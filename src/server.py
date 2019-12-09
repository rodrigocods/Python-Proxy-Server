# -*- coding: utf-8 -*-
import socket 

ip_proxy = '10.1.2.184' 
port_proxy = 65001
ip_client = '10.1.2.184'
port_client = 65002
ip_server = '10.1.2.184'
port_server = 65003

addr_proxy = (ip_proxy, port_proxy) 
addr_client = (ip_client, port_client)
addr_server = (ip_server, port_server)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind(addr_server) 
server_socket.listen(5)

print('aguardando conexao...')
con, proxy = server_socket.accept()
print('concectado com '+proxy[0])
msg = con.recv(1024).decode('utf-8')
if not msg: server_socket.close()   
print(proxy, msg)
print('finalizando conexao do cliente '+proxy[0])
server_socket.close()

server2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server2_socket.connect(addr_client)
resposta = "mensagem '%s' recebida pelo servidor"% msg
server2_socket.send(bytes(resposta,'utf-8'))
server2_socket.close()