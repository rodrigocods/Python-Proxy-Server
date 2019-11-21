import socket 
host = '' 
port = 7000 
addr = (host, port) 
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serv_socket.bind(addr) 
serv_socket.listen(5)

while True:
    print('aguardando conexao')
    con, cliente = serv_socket.accept()
    print(cliente) 
    print('conectado')
serv_socket.close() 