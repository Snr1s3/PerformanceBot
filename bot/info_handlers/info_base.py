import json
from typing import Any, Callable, List, Optional, Dict, Union
from logger import logger

class InfoBase:
    def __init__(self, socket_con: Any) -> None:
        self.socket_con = socket_con

    def get_info(
        self,
        section: Optional[str],
        formatter: Optional[Callable[[Any], List[str]]]
    ) -> Union[List[str], Dict[str, Any]]:
        content = self.socket_con.receive()
        arr: List[str] = []
        try:
            data = json.loads(content)
            if section:
                info = data.get(section, {})
                arr = formatter(info) if formatter else []
            else:
                return data
        except Exception as e:
            logger.error("Error parsing JSON:", e)
            logger.error("Raw content:", content)
        return arr
