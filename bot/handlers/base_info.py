from bot.socket.socket_con import SocketCon


class BaseInfo:
    def __init__(self):
        self.sock = SocketCon()
        self.sock.connect()

    def system(self):
        return self.sock.systeminfo()
    def cpu(self):
        return self.sock.cpuinfo()
    def docker(self):
        return self.sock.dockerinfo()
    def memory(self):
        return self.sock.memoryinfo()
    def sensors(self):
        return self.sock.sensorsinfo()
    def disk(self):
        return self.sock.diskinfo()
    def network(self):
        return self.sock.networkinfo()