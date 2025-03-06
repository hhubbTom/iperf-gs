import time

class Statistics:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.total_bytes = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def add_bytes(self, byte_count):
        self.total_bytes += byte_count

    def get_bandwidth(self):
        duration = self.end_time - self.start_time
        return self.total_bytes * 8 / duration / 1e6  # Mbps
