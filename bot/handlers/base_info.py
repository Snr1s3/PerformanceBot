from bot.socket.socket_con import SocketCon
from bot.info_handlers.cpu_info import CpuInfo
from bot.info_handlers.disk_info import DiskInfo
from bot.info_handlers.docker_info import DockerInfo
from bot.info_handlers.memory_info import MemoryInfo
from bot.info_handlers.network_info import NetworkInfo
from bot.info_handlers.sensors_info import SensorsInfo
from bot.info_handlers.system_info import SystemInfo



class BaseInfo:
    def __init__(self):
        self.sock = SocketCon()
        self.sock.connect()

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