import socket

def create_tcp_server_socket(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    return server_socket

def create_udp_server_socket(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', port))
    return server_socket

def create_tcp_client_socket(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket

def create_udp_client_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return client_socket
