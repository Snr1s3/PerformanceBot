from .info_base import InfoBase

class SystemInfo(InfoBase):
    def fetch(self):
        def formatter(info):
            return [f"{k.upper()} : {v}" for k, v in info.items()]
        return self.get_info("system_info", formatter)