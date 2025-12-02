from .info_base import InfoBase


class SystemInfo(InfoBase):
    def fetch(self):
        def formatter(info):
            arr = []
            for k, v in info.items():
                key_upper = k.upper()
                if key_upper == "USERS" and isinstance(v, list):
                    for user in v:
                        user_str = "\n  ".join(
                            f"{k.upper()}: {v}" for k, v in user.items())
                        arr.append(f"{user_str}")
                else:
                    arr.append(f"{key_upper}: {v}")
            return arr
        return self.get_info("system_info", formatter)
