from .info_base import InfoBase
from typing import Any, Dict, List


class SystemInfo(InfoBase):
    def fetch(self) -> List[str]:
        def formatter(info: Dict[str, Any]) -> List[str]:
            arr: List[str] = []
            for k, v in info.items():
                key_upper = k.upper()
                if key_upper == "USERS" and isinstance(v, list):
                    for user in v:
                        user_str = "\n  ".join(
                            f"{k.upper()}: {v}" for k, v in user.items()
                        )
                        arr.append(f"{user_str}")
                else:
                    arr.append(f"{key_upper}: {v}")
            return arr
        return self.get_info("system_info", formatter)
