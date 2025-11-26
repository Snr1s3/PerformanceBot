from datetime import datetime
import json
import os
from .info_base import InfoBase

class CaptureInfo(InfoBase):
    def fetch(self):
        def formatter(info):
            return None
        os.makedirs("jsons", exist_ok=True) 
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"jsons/data_{timestamp}.json"
        with open(filename, 'w') as f:
            json.dump(self.get_info(None, formatter), f, indent=2)
        return filename