import json
import os
import pytest
from main import tests as bot_tests
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
        # Replace the expected string below with the actual expected output for sensors
        assert sensors == "<b>SENSORS INFO:</b>\nBATTERY_PERCENT: 100.0%\nPOWER_PLUGGED: True"
"""
    def test_capture(self):
        base_info = BaseInfo()
        capture = base_info.capture()
        # Replace the expected string below with the actual expected output for capture
        assert capture == "<b>CAPTURE INFO:</b>\n..."

    def test_network(self):
        base_info = BaseInfo()
        network = base_info.network()
        # Replace the expected string below with the actual expected output for network
        assert network == "<b>NETWORK INFO:</b>\n..."
"""