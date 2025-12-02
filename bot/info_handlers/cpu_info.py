from .info_base import InfoBase


class CpuInfo(InfoBase):
    def fetch(self):

        def formatter(info):
            arr = []
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
