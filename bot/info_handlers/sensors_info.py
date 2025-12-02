from .info_base import InfoBase


class SensorsInfo(InfoBase):
    def fetch(self):
        def formatter(info):
            arr = []
            for key, value in info.items():
                key_upper = key.upper()
                if isinstance(value, dict):
                    if not value:
                        arr.append(f"{key_upper}: none")
                    else:
                        arr.append(f"{key_upper}:")
                        if key_upper == "BATTERY":
                            for subkey, subval in value.items():
                                arr.append(
                                    f"  {self.add_unit(subkey, subval)}"
                                )
                        else:
                            self.subvalues(arr, value)
                else:
                    arr.append(f"{key_upper}: {value}")
            return arr
        return self.get_info("sensors", formatter)

    def add_unit(self, k, v):
        if "temp" in k.lower() or k.lower() in {
            "current", "high", "critical"
        }:
            return f"{k}: {v}°C"
        if "fan" in k.lower() or k.lower() == "current_rpm":
            return f"{k}: {v} RPM"
        if "percent" in k.lower() or k.lower() == "percent":
            return f"{k}: {int(v)}%"
        return f"{k}: {v}"

    def subvalues(self, arr, value):
        for subkey, subval in value.items():
            arr.append(f"  {subkey}:")
            if isinstance(subval, list):
                for item in subval:
                    if isinstance(item, dict):
                        item_str = '\n    '.join(
                            self.add_unit(k, v)
                            for k, v in item.items()
                        )
                        arr.append(f"    {item_str}")
                    else:
                        arr.append(f"    {item}")
            else:
                arr.append(f"    {subval}")
