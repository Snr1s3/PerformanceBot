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
    def dockerinfo(self):
        content = self.receive()
        arr = []
        try:
            data = json.loads(content)
            docker_info = data.get("docker", {})
            images = docker_info.get("images", [])
            if images:
                arr.append("DOCKER IMAGES:")
                for img in images:
                    for _, value in img.items():
                        tags = ", ".join(value.get("tags", []))
                        arr.append(
                            f"  ID: {value.get('id', 'N/A')}\n"
                            f"  Tags: {tags}\n"
                            f"  Size: {value.get('size_mb', 'N/A')} MB\n"
                            f"  Created: {value.get('created', 'N/A')}\n"
                        )
            containers = docker_info.get("containers", [])
            if containers:
                arr.append("DOCKER CONTAINERS:")
                for cont in containers:
                    for _, value in cont.items():
                        arr.append(
                            f"  ID: {value.get('id', 'N/A')}\n"
                            f"  Name: {value.get('name', 'N/A')}\n"
                            f"  Status: {value.get('status', 'N/A')}\n"
                            f"  Image: {value.get('image', 'N/A')}\n"
                            f"  Created: {value.get('created', 'N/A')}\n"
                        )
        except Exception as e:
            print("Error parsing JSON:", e)
            print("Raw content:", content)
        return arr
    def networkinfo(self):
        content = self.receive()
        arr = []
        try:
            data = json.loads(content)
            network_info = data.get("network", {})
            io_counters = network_info.get("io_counters", {})
            interfaces = network_info.get("interfaces", {})

            # IO COUNTERS
            if io_counters:
                arr.append("IO COUNTERS:")
                total = io_counters.get("total", {})
                if total:
                    arr.append("  TOTAL:")
                    for k, v in total.items():
                        arr.append(f"    {k}: {v}")
                per_interface = io_counters.get("per_interface", {})
                if per_interface:
                    arr.append("  PER INTERFACE:")
                    for iface, stats in per_interface.items():
                        arr.append(f"    {iface}:")
                        for k, v in stats.items():
                            arr.append(f"      {k}: {v}")

            # INTERFACES
            if interfaces:
                arr.append("INTERFACES:")
                for iface, info in interfaces.items():
                    arr.append(f"  {iface}:")
                    stats = info.get("stats", {})
                    if stats:
                        arr.append("    STATS:")
                        for k, v in stats.items():
                            arr.append(f"      {k}: {v}")
                    addresses = info.get("addresses", [])
                    if addresses:
                        arr.append("    ADDRESSES:")
                        for addr in addresses:
                            addr_str = ", ".join(f"{k}: {v}" for k, v in addr.items())
                            arr.append(f"      {addr_str}")

        except Exception as e:
            print("Error parsing JSON:", e)
            print("Raw content:", content)
        return arr
    def sensorsinfo(self):
        content = self.receive()
        arr = []
        try:
            data = json.loads(content)
            sensors = data.get("sensors", {})
            for key, value in sensors.items():
                key_upper = key.upper()
                if isinstance(value, dict) and value:  # non-empty dict
                    arr.append(f"{key_upper}:")
                    for subkey, subval in value.items():
                        arr.append(f"  {subkey}: {subval}")
                elif isinstance(value, dict) and not value:  # empty dict
                    arr.append(f"{key_upper}: none")
                else:
                    arr.append(f"{key_upper}: {value}")
        except Exception as e:
            print("Error parsing JSON:", e)
            print("Raw content:", content)
        return arr

def test_connect_and_receive():
    sock = SocketCon()
    sock.connect("ws://localhost:8000/ws")
    response = sock.receive()
    print("Received:", response)
    """
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
        print("\n\n\n\n")
        for a in sock.dockerinfo():
            print(a)
    """
    print("\n\n\n\n")
    for a in sock.networkinfo():
        print(a)
    print("\n\n\n\n")
    for a in sock.sensorsinfo():
        print(a)
if __name__ == "__main__":
    test_connect_and_receive()

