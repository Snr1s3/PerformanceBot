from .info_base import InfoBase

class SensorsInfo(InfoBase):
    def fetch(self):
        def formatter(info):
            arr = []
            for key, value in info.items():
                key_upper = key.upper()
                if isinstance(value, dict) and value:
                    arr.append(f"{key_upper}:")
                    for subkey, subval in value.items():
                        arr.append(f"  {subkey}: {subval}")
                elif isinstance(value, dict) and not value:
                    arr.append(f"{key_upper}: none")
                else:
                    arr.append(f"{key_upper}: {value}")
            return arr
        return self.get_info("sensors", formatter)