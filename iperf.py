import argparse
from server import run_server
from client import run_client

def parse_arguments():
    parser = argparse.ArgumentParser(description='Simple iperf tool')
    parser.add_argument('mode', choices=['server', 'client'], help='Run as server or client')
    parser.add_argument('--host', type=str, default='localhost', help='Server hostname (for client mode)')
    parser.add_argument('--port', type=int, default=5201, help='Port number')
    parser.add_argument('--time', type=int, default=10, help='Duration of the test in seconds')
    parser.add_argument('--udp', action='store_true', help='Use UDP instead of TCP')
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.mode == 'server':
        run_server(args.port, args.udp)
    else:
        run_client(args.host, args.port, args.time, args.udp)

if __name__ == '__main__':
    main()
