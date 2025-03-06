from network import create_tcp_client_socket, create_udp_client_socket
from data_generator import generate_data
from timer import Timer
from statistics import Statistics

def run_client(host, port, duration, use_udp):
    if use_udp:
        client_socket = create_udp_client_socket()
        handle_udp_connection(client_socket, host, port, duration)
    else:
        client_socket = create_tcp_client_socket(host, port)
        handle_tcp_connection(client_socket, duration)

def handle_tcp_connection(client_socket, duration):
    data = generate_data(1024)
    stats = Statistics()
    timer = Timer(duration)
    stats.start()
    timer.start()
    while not timer.event.is_set():
        client_socket.sendall(data)
        stats.add_bytes(len(data))
    stats.stop()
    client_socket.close()
    print(f"Bandwidth: {stats.get_bandwidth()} Mbps")

def handle_udp_connection(client_socket, host, port, duration):
    data = generate_data(1024)
    stats = Statistics()
    timer = Timer(duration)
    stats.start()
    timer.start()
    while not timer.event.is_set():
        client_socket.sendto(data, (host, port))
        stats.add_bytes(len(data))
    stats.stop()
    client_socket.close()
    print(f"Bandwidth: {stats.get_bandwidth()} Mbps")
