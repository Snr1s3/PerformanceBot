import os
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
        self.connected = False

    def connect(self, url=os.getenv("WEB_SOCKET_URL", "")):
        if self.ws is None:
            self.ws = websocket.WebSocket()
            try:
                self.ws.connect(url)
                self.connected = True
            except Exception as e:
                print(f"Could not connect to {url}: {e}")
                self.ws = None
                self.connected = False

    def receive(self):
        if self.ws and self.connected:
            try:
                return self.ws.recv()
            except Exception as e:
                print(f"WebSocket receive error: {e}")
                self.ws = None
                self.connected = False
        print("Falling back to jsons/TEST.json")
        try:
            with open("jsons/TEST.json", "r") as f:
                return json.dumps(json.load(f))
        except Exception as e:
            print(f"Error reading jsons/TEST.json: {e}")
            return '{}'
