from typing import Any, Dict, List
from .info_base import InfoBase


class DiskInfo(InfoBase):
    def fetch(self) -> List[str]:
        def formatter(info: Dict[str, Any]) -> List[str]:
            arr: List[str] = []
            disks = info.get("disk", [])
            for disk in disks:
                arr.append("  DEVICE: " + str(disk.get("device", "")))
                arr.append("  MOUNTPOINT: " + str(disk.get("mountpoint", "")))
                arr.append("  FSTYPE: " + str(disk.get("fstype", "")))
                arr.append("  TOTAL_GB: " + str(disk.get("total_gb", "")) + "GB")
                arr.append("  USED_GB: " + str(disk.get("used_gb", "")) + "GB")
                arr.append("  FREE_GB: " + str(disk.get("free_gb", "")) + "GB")
                arr.append("  PERCENT: " + str(disk.get("percent", "")) + "%\n")
            return arr
        return self.get_info("disks", formatter)
