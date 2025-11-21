from .info_base import InfoBase

class NetworkInfo(InfoBase):
    def fetch(self):
        def formatter(info):
            arr = []
            io_counters = info.get("io_counters", {})
            interfaces = info.get("interfaces", {})
            if io_counters:
                arr.append("IO COUNTERS:")
                total = io_counters.get("total", {})
                if total:
                    arr.append("  TOTAL:")
                    for k, v in total.items():
                        arr.append(f"    {k}: {v}")
                per_interface = io_counters.get("per_interface", {})
                if per_interface:
                    arr.append("  PER INTERFACE:")
                    for iface, stats in per_interface.items():
                        arr.append(f"    {iface}:")
                        for k, v in stats.items():
                            arr.append(f"      {k}: {v}")
            if interfaces:
                arr.append("INTERFACES:")
                for iface, info in interfaces.items():
                    arr.append(f"  {iface}:")
                    stats = info.get("stats", {})
                    if stats:
                        arr.append("    STATS:")
                        for k, v in stats.items():
                            arr.append(f"      {k}: {v}")
                    addresses = info.get("addresses", [])
                    if addresses:
                        arr.append("    ADDRESSES:")
                        for addr in addresses:
                            addr_str = ", ".join(f"{k}: {v}" for k, v in addr.items())
                            arr.append(f"      {addr_str}")
            return arr
        return self.get_info("network", formatter)