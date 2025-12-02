from typing import Any, Dict, List
from .info_base import InfoBase


class CpuInfo(InfoBase):
    def fetch(self) -> List[str]:
        def formatter(info: Dict[str, Any]) -> List[str]:
            arr: List[str] = []
            for key, value in info.items():
                key_upper = key.upper()
                if key_upper == "CPU":
                    value = str(value) + "%"
                elif key_upper == "FREQUENCY":
                    value = str(value) + "MHz"
                if key_upper not in ("CPU_CORE", "FREQUENCY_CORE"):
                    arr.append(f"{key_upper}: {value}")
            return arr
        return self.get_info("cpu", formatter)
