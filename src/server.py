import socket 
host = '' 
port = 7000 
addr = (host, port) 
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
serv_socket.bind(addr) 

while True:
    print('aguardando conexao...')
    msg, cliente = serv_socket.recvfrom(1024)
    print(cliente) 
    print(msg)
serv_socket.close() 