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

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

client_socket.connect(addr_proxy)
print("Digite a mensagem seguindo a sintaxe 'mensagem/Ip qual deseja mandar'\n")
msg = input()
client_socket.send(bytes(msg,'utf-8'))
client_socket.close()

client2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client2_socket.bind(addr_client) 
client2_socket.listen(5)
print('aguardando resposta do server...')
con, server = client2_socket.accept()
resposta = con.recv(1024).decode('utf-8')
print(resposta)
client2_socket.close()
