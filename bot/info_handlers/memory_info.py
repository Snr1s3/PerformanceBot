from .info_base import InfoBase

class MemoryInfo(InfoBase):
    def fetch(self):
        def formatter(info):
            arr = []
            for key, value in info.items():
                key_upper = key.upper()
                if key_upper == "RAM_TOTAL":
                    value = str(value) + " GB"
                elif key_upper == "RAM_AVAILABLE":
                    value = str(value) + " GB"
                elif key_upper == "RAM_PERCENT":
                    value = str(value) + " %"
                arr.append(f"{key_upper} : {value}")
            return arr
        return self.get_info("memory", formatter)