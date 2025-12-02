from typing import Any, Dict, List
from .info_base import InfoBase


class DockerInfo(InfoBase):
    def fetch(self) -> List[str]:
        def formatter(info: Dict[str, Any]) -> List[str]:
            arr: List[str] = []
            images = info.get("images", [])
            if images:
                arr.append("DOCKER IMAGES:")
                for img in images:
                    for _, value in img.items():
                        tags = ", ".join(value.get("tags", []))
                        arr.append(
                            f"  ID: {value.get('id', 'N/A')}\n"
                            f"  Tags: {tags}\n"
                            f"  Size: {value.get('size_mb', 'N/A')} MB\n"
                            f"  Created: {value.get('created', 'N/A')}\n"
                        )
            containers = info.get("containers", [])
            if containers:
                arr.append("DOCKER CONTAINERS:")
                for cont in containers:
                    for _, value in cont.items():
                        arr.append(
                            f"  ID: {value.get('id', 'N/A')}\n"
                            f"  Name: {value.get('name', 'N/A')}\n"
                            f"  Status: {value.get('status', 'N/A')}\n"
                            f"  Image: {value.get('image', 'N/A')}\n"
                            f"  Created: {value.get('created', 'N/A')}\n"
                        )
            return arr
        return self.get_info("docker", formatter)
