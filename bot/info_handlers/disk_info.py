from .info_base import InfoBase

class DiskInfo(InfoBase):
    def fetch(self):
        def formatter(info):
            arr = []
            for key, value in info.items():
                key_upper = key.upper()
                if key_upper == "DISK" and isinstance(value, list):
                    for disk in value:
                        disk_str = "\n  ".join(f"{k.upper()}: {v}" for k, v in disk.items())
                        arr.append(f"{disk_str}\n")
                else:
                    arr.append(f"{key_upper} : {value}")
            return arr
        return self.get_info("disk", formatter)