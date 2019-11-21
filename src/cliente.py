import socket 
ip = raw_input('digite o ip de conexao: ') 
port = 7000 
addr = ((ip,port)) 
msg = 'CONECTADO'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
client_socket.connect(addr)
client_socket.sendto(msg, (ip, port))  
client_socket.close()