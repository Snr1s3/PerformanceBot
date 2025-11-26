from backend_socket.socket_con import SocketCon
from info_handlers.capture_info import CaptureInfo
from info_handlers.cpu_info import CpuInfo
from info_handlers.disk_info import DiskInfo
from info_handlers.docker_info import DockerInfo
from info_handlers.memory_info import MemoryInfo
from info_handlers.network_info import NetworkInfo
from info_handlers.sensors_info import SensorsInfo
from info_handlers.system_info import SystemInfo



class BaseInfo:
    MAX_LEN = 4096

    def __init__(self):
        self.sock = SocketCon()
        self.sock.connect()
    
    async def send_long_message(self, message, update, **kwargs):
        for i in range(0, len(message), self.MAX_LEN):
            await update.message.reply_text(message[i:i+self.MAX_LEN], **kwargs)

    def system(self):
        return SystemInfo(self.sock).fetch()
    def cpu(self):
        return CpuInfo(self.sock).fetch()
    def docker(self):
        return DockerInfo(self.sock).fetch()
    def memory(self):
        return MemoryInfo(self.sock).fetch()
    def sensors(self):
        return SensorsInfo(self.sock).fetch()
    def disk(self):
        return DiskInfo(self.sock).fetch()
    def network(self):
        return NetworkInfo(self.sock).fetch()
    def capture(self):
        return CaptureInfo(self.sock).fetch()