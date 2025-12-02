import json
from handlers.base_info import BaseInfo


class TestBot:

    def test_system(self):
        base_info = BaseInfo()
        system = base_info.system()
        assert system == "<b>SYSTEM INFO:</b>\nPLATFORM: Linux\nNODE: DESKTOP-MV73RIF\nRELEASE: 6.6.87.2-microsoft-standard-WSL2\nVERSION: #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025\nMACHINE: x86_64\nBOOTTIME: 2025-11-26 10:02:57\nUPTIME_SECONDS: 19706\nUSERS_COUNT: 1\nNAME: alice\n  TERMINAL: pts/0\n  HOST: localhost\n  STARTED: 1700000000.0\n  PID: 1234"

    def test_cpu(self):
        base_info = BaseInfo()
        cpu = base_info.cpu()
        assert cpu == "<b>CPU INFO:</b>\nCORES_COUNT: 4\nTHREADS_COUNT: 8\nCPU: 4.5%\nFREQUENCY: 2611.2MHz"

    def test_disk(self):
        base_info = BaseInfo()
        disk = base_info.disk()
        assert disk == "<b>DISK INFO:</b>\n  DEVICE: /dev/sdd\n  MOUNTPOINT: /\n  FSTYPE: ext4\n  TOTAL_GB: 1006.85GB\n  USED_GB: 10.16GB\n  FREE_GB: 945.48GB\n  PERCENT: 1.0%\n"

    def test_memory(self):
        base_info = BaseInfo()
        memory = base_info.memory()
        print(memory)
        assert memory == "<b>MEMORY INFO:</b>\nRAM_TOTAL: 7.61GB\nRAM_AVAILABLE: 4.94GB\nRAM_PERCENT: 35.1%"

    def test_docker(self):
        base_info = BaseInfo()
        docker = base_info.docker()
        assert docker == "<b>DOCKER INFO:</b>\nDOCKER IMAGES:\n  ID: sha256:7c2c6ee6dd0d\n  Tags: performance-bot:latest\n  Size: 144.64 MB\n  Created: 2025-11-26T14:18:15\n\nDOCKER CONTAINERS:\n  ID: 970b24a9730e\n  Name: bot2\n  Status: exited\n  Image: performance-bot:latest\n  Created: 2025-11-26T14:18:18\n"

    def test_sensors(self):
        base_info = BaseInfo()
        sensors = base_info.sensors()
        assert sensors == "<b>Sensors INFO:</b>\nBATTERY:\n  percent: 100%\n  secsleft: -2\n  power_plugged: True\nFANS:\n  fan1:\n    label: CPU Fan\n    current_rpm: 2200 RPM\nTEMPERATURES:\n  coretemp:\n    label: Core 0\n    current: 45.0°C\n    high: 100.0°C\n    critical: 105.0°C\n  acpitz:\n    label: TZ0\n    current: 27.8°C\n    high: 128.0°C\n    critical: 128.0°C"

    def test_capture(self):
        base_info = BaseInfo()
        capture = base_info.capture()
        with open(capture) as f1, open('jsons/TEST.json') as f2:
            obj1 = json.load(f1)
            obj2 = json.load(f2)
        assert obj1 == obj2

    def test_network(self):
        base_info = BaseInfo()
        network = base_info.network()
        assert network == "<b>NETWORK INFO:</b>\nIO COUNTERS:\n  TOTAL:\n    bytes_sent: 597009252\n    bytes_recv: 588188535\n    packets_sent: 421337\n    packets_recv: 457500\n    errin: 0\n    errout: 0\n    dropin: 0\n    dropout: 0\n  PER INTERFACE:\n    eth0:\n      bytes_sent: 43977648\n      bytes_recv: 59787387\n      packets_sent: 45817\n      packets_recv: 83730\n      errin: 0\n      errout: 0\n      dropin: 0\n      dropout: 0\nINTERFACES:\n  eth0:\n    STATS:\n      isup: True\n      duplex: NIC_DUPLEX_FULL\n      speed: 10000\n      mtu: 1500\n      flags: up,broadcast,running,multicast\n    ADDRESSES:\n      family: AF_INET\n       address: 172.21.88.59\n       netmask: 255.255.240.0\n       broadcast: 172.21.95.255\n      family: AF_INET6\n       address: fe80::215:5dff:fe48:e385%eth0\n       netmask: ffff:ffff:ffff:ffff::\n       broadcast: None\n      family: AF_PACKET\n       address: 00:15:5d:48:e3:85\n       netmask: None\n       broadcast: ff:ff:ff:ff:ff:ff"
