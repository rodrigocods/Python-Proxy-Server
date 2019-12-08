import socket 

ip_proxy = '192.168.1.3' 
port_proxy = 3128
ip_client = '192.168.1.3'
port_client = 3129
ip_server = '192.168.1.3'
port_server = 3130

addr_proxy = (ip_proxy, port_proxy) 
addr_client = (ip_client, port_client)
addr_server = (ip_server, port_server)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind(addr_server) 
server_socket.listen(5)

while True:
    print('aguardando conexao...')
    con, proxy = server_socket.accept()
    print('concectado com '+proxy[0])
    msg = con.recv(1024).decode('utf-8')
    if not msg: server_socket.close()   
    print('finalizando conexao do cliente '+proxy[0])
    server_socket.close()

    server2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server2_socket.connect(addr_client)
    server2_socket.send(bytes(msg,'utf-8'))
    server2_socket.close()