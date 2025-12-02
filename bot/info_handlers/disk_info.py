from typing import Any, Dict, List
from .info_base import InfoBase


class DiskInfo(InfoBase):
    def fetch(self):
        def formatter(info):
            arr = []
            disks = info.get("disk", [])
            for disk in disks:
                for key, value in disk.items():
                    key_upper = key.upper()
                    if key_upper in ("TOTAL_GB", "USED_GB", "FREE_GB"):
                        value = f"{value}GB"
                    if key_upper == "PERCENT":
                        value = f"{value}%\n"
                    arr.append(f"  {key_upper}: {value}")
            return arr
        return self.get_info("disks", formatter)