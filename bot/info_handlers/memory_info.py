from typing import Any, Dict, List
from .info_base import InfoBase


class MemoryInfo(InfoBase):
    def fetch(self) -> List[str]:
        def formatter(info: Dict[str, Any]) -> List[str]:
            arr: List[str] = []
            for key, value in info.items():
                key_upper = key.upper()
                if key_upper == "RAM_TOTAL":
                    value = str(value) + "GB"
                elif key_upper == "RAM_AVAILABLE":
                    value = str(value) + "GB"
                elif key_upper == "RAM_PERCENT":
                    value = str(value) + "%"
                arr.append(f"{key_upper}: {value}")
            return arr
        return self.get_info("memory", formatter)
