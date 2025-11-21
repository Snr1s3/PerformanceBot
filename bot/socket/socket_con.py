import websocket
import json

class SocketCon:
    _instance = None
    _ws = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SocketCon, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.ws = None

    def connect(self, url="ws://localhost:8000/ws"):
        if self.ws is None:
            self.ws = websocket.WebSocket()
            try:
                self.ws.connect(url)
            except ConnectionRefusedError as e:
                print(f"Could not connect to {url}: {e}")
                self.ws = None

    def receive(self):
        if self.ws:
            return self.ws.recv()