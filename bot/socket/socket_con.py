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
            self.ws.connect(url)

    def send(self, message):
        if self.ws:
            self.ws.send(message)

    def receive(self):
        if self.ws:
            return self.ws.recv()
        
    def systeminfo(self):
        content = self.receive()
        arr = []
        try:
            data = json.loads(content)
            system_info = data.get("system_info", {})
            for key, value in system_info.items():
                arr.append(f"{key.upper()} : {value}")
        except Exception as e:
            print("Error parsing JSON:", e)
            print("Raw content:", content)
        return arr
    
    def cpuinfo(self):
        content = self.receive()
        arr = []
        try:
            data = json.loads(content)
            system_info = data.get("cpu", {})
            for key, value in system_info.items():
                key_upper = key.upper()
                if key_upper == "CPU":
                    value = str(value) + " %"
                elif key_upper == "FREQUENCY":
                    value = str(value) + " GHz"
                if key_upper not in ("CPU_CORE", "FREQUENCY_CORE"):
                    arr.append(f"{key_upper} : {value}")
        except Exception as e:
            print("Error parsing JSON:", e)
            print("Raw content:", content)
        return arr
    def memoryinfo(self):
        content = self.receive()
        arr = []
        try:
            data = json.loads(content)
            system_info = data.get("memory", {})
            for key, value in system_info.items():
                key_upper = key.upper()
                if key_upper == "RAM_TOTAL":
                    value = str(value) + " GB"
                elif key_upper == "RAM_AVAILABLE":
                    value = str(value) + " GB"
                elif key_upper == "RAM_PERCENT":
                    value = str(value) + " %"
                arr.append(f"{key_upper} : {value}")
        except Exception as e:
            print("Error parsing JSON:", e)
            print("Raw content:", content)
        return arr
    def diskinfo(self):
        content = self.receive()
        arr = []
        try:
            data = json.loads(content)
            system_info = data.get("disks", {})
            for key, value in system_info.items():
                key_upper = key.upper()
                if key_upper == "DISK" and isinstance(value, list):
                    for disk in value:
                        disk_str = "\n  ".join(f"{k.upper()}: {v}" for k, v in disk.items())
                        arr.append(f"{disk_str}\n")
                else:
                    arr.append(f"{key_upper} : {value}")
        except Exception as e:
            print("Error parsing JSON:", e)
            print("Raw content:", content)
        return arr

def test_connect_and_receive():
    sock = SocketCon()
    sock.connect("ws://localhost:8000/ws")
    response = sock.receive()
    print("Received:", response)
    print("\n\n\n\n")
    for a in sock.systeminfo():
        print(a)
    print("\n\n\n\n")
    for a in sock.cpuinfo():
        print(a)
    print("\n\n\n\n")
    for a in sock.memoryinfo():
        print(a)
        
    print("\n\n\n\n")
    for a in sock.diskinfo():
        print(a)

if __name__ == "__main__":
    test_connect_and_receive()

