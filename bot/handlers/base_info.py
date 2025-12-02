from backend_socket.socket_con import SocketCon
from info_handlers.capture_info import CaptureInfo
from info_handlers.cpu_info import CpuInfo
from info_handlers.disk_info import DiskInfo
from info_handlers.docker_info import DockerInfo
from info_handlers.memory_info import MemoryInfo
from info_handlers.network_info import NetworkInfo
from info_handlers.sensors_info import SensorsInfo
from info_handlers.system_info import SystemInfo
import html


class BaseInfo:
    MAX_LEN = 4096

    def __init__(self):
        self.sock = SocketCon()
        self.sock.connect()

    async def send_long_message(self, message, update, **kwargs):
        for i in range(0, len(message), self.MAX_LEN):
            await update.message.reply_text(message[i:i+self.MAX_LEN], **kwargs)

    def system(self):
        return "<b>SYSTEM INFO:</b>\n" + "\n".join(SystemInfo(self.sock).fetch())

    def cpu(self):
        return "<b>CPU INFO:</b>\n" + "\n".join(CpuInfo(self.sock).fetch())

    def docker(self):
        safe_content = [html.escape(line)
                        for line in DockerInfo(self.sock).fetch()]
        return "<b>DOCKER INFO:</b>\n" + "\n".join(safe_content)

    def memory(self):
        return "<b>MEMORY INFO:</b>\n" + "\n".join(MemoryInfo(self.sock).fetch())

    def sensors(self):
        return "<b>Sensors INFO:</b>\n" + "\n".join(SensorsInfo(self.sock).fetch())

    def disk(self):
        return "<b>DISK INFO:</b>\n" + "\n".join(DiskInfo(self.sock).fetch())

    def network(self):
        return "<b>NETWORK INFO:</b>\n" + "\n".join(NetworkInfo(self.sock).fetch())

    def capture(self):
        return CaptureInfo(self.sock).fetch()
