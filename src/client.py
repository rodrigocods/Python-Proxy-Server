import socket 

ip_proxy = '192.168.1.3' 
port_proxy = 3128
ip_client = '192.168.1.3'
port_client = 3129
ip_server = '192.168.1.3'

addr_proxy = (ip_proxy, port_proxy) 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr_proxy)

print("Para sair digite e mande'sair'\n")
msg = input()
while msg != 'sair':
    client_socket.send(bytes(msg,'utf-8'))
    msg = input()
client_socket.close()
