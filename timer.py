import time
from threading import Event

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.event = Event()

    def start(self):
        self.event.wait(self.duration)

    def stop(self):
        self.event.set()
