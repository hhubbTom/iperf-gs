from network import create_tcp_server_socket, create_udp_server_socket
from statistics import Statistics

def run_server(port, use_udp):
    if use_udp:
        server_socket = create_udp_server_socket(port)
        handle_udp_connection(server_socket)
    else:
        server_socket = create_tcp_server_socket(port)
        handle_tcp_connection(server_socket)

def handle_tcp_connection(server_socket):
    conn, addr = server_socket.accept()
    stats = Statistics()
    stats.start()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        stats.add_bytes(len(data))
    stats.stop()
    conn.close()
    print(f"Bandwidth: {stats.get_bandwidth()} Mbps")

def handle_udp_connection(server_socket):
    stats = Statistics()
    stats.start()
    while True:
        data, addr = server_socket.recvfrom(1024)
        if not data:
            break
        stats.add_bytes(len(data))
    stats.stop()
    print(f"Bandwidth: {stats.get_bandwidth()} Mbps")
