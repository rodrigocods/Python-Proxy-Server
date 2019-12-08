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

proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
proxy_socket.bind(addr_proxy) 
proxy_socket.listen(5)

while True:
    print('aguardando conexao...')
    con, client = proxy_socket.accept()
    print('concectado com '+client[0])
    msg = con.recv(1024).decode('utf-8')
    if not msg: proxy_socket.close()
    print(client, msg)       
    print('finalizando conexao do cliente '+client[0])
    proxy_socket.close()

    proxy2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    proxy2_socket.connect(addr_server)
    proxy2_socket.send(bytes(msg,'utf-8'))
    proxy2_socket.close()