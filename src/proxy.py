import socket 

ip_proxy = '192.168.1.3' 
port_proxy = 3128
ip_client = '192.168.1.3'
port_client = 3129
ip_server = '192.168.1.3'

addr_proxy = (ip_proxy, port_proxy) 
proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
proxy_socket.bind(addr_proxy) 
proxy_socket.listen(1)

while True:
    print('aguardando conexao...')
    con, client = proxy_socket.accept()
    print('concectado com '+client[0])
    while True:
        msg = con.recv(1024).decode('utf-8')
        if not msg: break
        print(client, msg)       
    print('finalizando conexao do cliente '+client[0])
    con.close()