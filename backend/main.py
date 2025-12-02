import datetime
import platform
import time
from typing import Dict, Set
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import psutil
import asyncio
import json
import docker
from logger import logger

docker_client = docker.from_env()
connected_clients: Set[WebSocket] = set()
latest_data: Dict = {}
data_lock = asyncio.Lock()


async def system_monitor():
    global latest_data, connected_clients
    logger.info("System monitor started...")
    while True:
        try:
            disks_json = []
            for disk in psutil.disk_partitions(all=False):
                try:
                    usage = psutil.disk_usage(disk.mountpoint)
                    disk_info = {
                        "device": disk.device,
                        "mountpoint": disk.mountpoint,
                        "fstype": disk.fstype,
                        "total_gb": round(usage.total / (1024**3), 2),
                        "used_gb": round(usage.used / (1024**3), 2),
                        "free_gb": round(usage.free / (1024**3), 2),
                        "percent": round(
                            (usage.used / usage.total) * 100, 1
                        )
                    }
                    disks_json.append(disk_info)
                except PermissionError:
                    continue
            users_json = []
            for user in psutil.users():
                users_info = {
                    "name": user.name,
                    "terminal": user.terminal if user.terminal else "None",
                    "host": user.host if user.host else "localhost",
                    "started": datetime.datetime.fromtimestamp(
                        user.started
                    ).strftime("%Y-%m-%d %H:%M:%S"),
                    "pid": user.pid if user.pid else "None"
                }
                users_json.append(users_info)
            fans_json = {}
            try:
                fans_data = psutil.sensors_fans()
                if fans_data:
                    for device_name, fans in fans_data.items():
                        fans_json[device_name] = []
                        for fan in fans:
                            fan_info = {
                                "label": fan.label if fan.label else "unknown",
                                "current_rpm": int(fan.current)
                                if fan.current else 0
                            }
                            fans_json[device_name].append(fan_info)
            except (AttributeError, OSError):
                fans_json = {"info": "No fan data available"}
            temperatures_json = {}
            try:
                temp_data = psutil.sensors_temperatures()
                if temp_data:
                    for device_name, temps in temp_data.items():
                        temperatures_json[device_name] = []
                        for temp in temps:
                            label = None
                            if temp.label:
                                label = temp.label
                            else:
                                label = "unknown"
                            temp_info = {
                                "label": label,
                                "current": round(temp.current, 1),
                                "high": round(temp.high, 1)
                                if temp.high else None,
                                "critical": round(temp.critical, 1)
                                if temp.critical else None
                            }
                            temperatures_json[device_name].append(temp_info)
            except (AttributeError, OSError):
                temperatures_json = {
                    "info": "No temperature data available"
                }
            battery_json = {}
            try:
                battery = psutil.sensors_battery()
                if battery:
                    battery_json = {
                        "percent": round(battery.percent, 1),
                        "secsleft": (
                            battery.secsleft
                            if battery.secsleft != -1
                            else "unlimited"
                        ),
                        "power_plugged": battery.power_plugged
                    }
                else:
                    battery_json = {"info": "No battery detected"}
            except (AttributeError, OSError):
                battery_json = {"info": "Battery data not available"}
            net_io_json = {}
            try:
                net_io_total = psutil.net_io_counters()
                net_io_json["total"] = {
                    "bytes_sent": net_io_total.bytes_sent,
                    "bytes_recv": net_io_total.bytes_recv,
                    "packets_sent": net_io_total.packets_sent,
                    "packets_recv": net_io_total.packets_recv,
                    "errin": net_io_total.errin,
                    "errout": net_io_total.errout,
                    "dropin": net_io_total.dropin,
                    "dropout": net_io_total.dropout
                }

                net_io_per_interface = psutil.net_io_counters(pernic=True)
                net_io_json["per_interface"] = {}
                for interface_name, stats in net_io_per_interface.items():
                    net_io_json["per_interface"][interface_name] = {
                        "bytes_sent": stats.bytes_sent,
                        "bytes_recv": stats.bytes_recv,
                        "packets_sent": stats.packets_sent,
                        "packets_recv": stats.packets_recv,
                        "errin": stats.errin,
                        "errout": stats.errout,
                        "dropin": stats.dropin,
                        "dropout": stats.dropout
                    }
            except (AttributeError, OSError):
                net_io_json = {"info": "Network I/O data not available"}
            net_if_stats_json = {}
            try:
                net_if_stats = psutil.net_if_stats()
                for interface_name, stats in net_if_stats.items():
                    net_if_stats_json[interface_name] = {
                        "isup": stats.isup,
                        "duplex": (
                            stats.duplex.name
                            if hasattr(stats.duplex, 'name')
                            else str(stats.duplex)
                        ),
                        "speed": stats.speed,
                        "mtu": stats.mtu,
                        "flags": stats.flags
                    }
            except (AttributeError, OSError):
                net_if_stats_json = {
                    "info": "Network interface stats not available"
                }
            nic_addrs_json = {}
            try:
                for interface_name, addresses in psutil.net_if_addrs().items():
                    nic_addrs_json[interface_name] = []
                    for addr in addresses:
                        addr_info = {
                            "family": (
                                addr.family.name
                                if hasattr(addr.family, 'name')
                                else str(addr.family)
                            ),
                            "address": addr.address,
                            "netmask": addr.netmask,
                            "broadcast": addr.broadcast
                        }
                        nic_addrs_json[interface_name].append(addr_info)
            except (AttributeError, OSError):
                nic_addrs_json = {
                    "info": "Network interface addresses not available"
                }
            merged_interfaces = {}
            all_interfaces = set()
            if (
                isinstance(net_if_stats_json, dict)
                and "info" not in net_if_stats_json
            ):
                all_interfaces.update(net_if_stats_json.keys())
            if (
                isinstance(nic_addrs_json, dict)
                and "info" not in nic_addrs_json
            ):
                all_interfaces.update(nic_addrs_json.keys())
            for interface_name in all_interfaces:
                merged_interfaces[interface_name] = {}

                if interface_name in net_if_stats_json:
                    merged_interfaces[interface_name]["stats"] = (
                        net_if_stats_json[interface_name]
                    )
                else:
                    merged_interfaces[interface_name]["stats"] = {
                        "info": "Stats not available"
                    }

                if interface_name in nic_addrs_json:
                    merged_interfaces[interface_name]["addresses"] = (
                        nic_addrs_json[interface_name]
                    )
                else:
                    merged_interfaces[interface_name]["addresses"] = [
                        {"info": "Addresses not available"}
                    ]

            docker_images = []
            i = 0
            for img in docker_client.images.list():
                try:
                    img_data = {
                        "id": img.id[:19] if img.id else "unknown",
                        "tags": img.tags if img.tags else ["<none>"],
                        "size_mb": round(
                            img.attrs.get('Size', 0) / (1024 * 1024), 2
                        ),
                        "created": (
                            img.attrs.get('Created', '')[:19]
                            if img.attrs.get('Created')
                            else 'unknown'
                        )
                    }
                    image_info = {
                        f"image{i}": img_data
                    }
                    docker_images.append(image_info)
                    i += 1

                except Exception as e:
                    logger.error(f"Error processing image: {e}")
                    continue
            docker_containers = []
            j = 0
            for container in docker_client.containers.list(all=True):
                try:
                    container_data = {
                        "id": (
                            container.id[:12]
                            if container.id else "unknown"
                        ),
                        "name": (
                            container.name
                            if container.name else "unknown"
                        ),
                        "status": (
                            container.status
                            if container.status else "unknown"
                        ),
                        "image": (
                            container.image.tags[0]
                            if container.image.tags
                            else (
                                container.image.id[:12]
                                if container.image.id
                                else "unknown"
                            )
                        ),
                        "created": (
                            container.attrs.get('Created', '')[:19]
                            if container.attrs.get('Created')
                            else 'unknown'
                        )
                    }

                    container_info = {
                        f"container{j}": container_data
                    }
                    docker_containers.append(container_info)
                    j += 1

                except Exception as e:
                    logger.error(f"Error processing container: {e}")
                    continue

            async with data_lock:
                latest_data = {
                    "timestamp": datetime.datetime.now().isoformat(),
                    "system_info": {
                        "platform": platform.system(),
                        "node": platform.node(),
                        "release": platform.release(),
                        "version": platform.version(),
                        "machine": platform.machine(),
                        "boottime": datetime.datetime.fromtimestamp(
                            psutil.boot_time()
                        ).strftime("%Y-%m-%d %H:%M:%S"),
                        "uptime_seconds": int(
                            time.time() - psutil.boot_time()
                        ),
                        "users_count": len(users_json),
                        "users": users_json,
                    },
                    "cpu": {
                        "cores_count": psutil.cpu_count(logical=False),
                        "threads_count": psutil.cpu_count(),
                        "cpu": round(psutil.cpu_percent(), 1),
                        "frequency": round(psutil.cpu_freq().current, 1),
                    },
                    "memory": {
                        "ram_total": round(
                            psutil.virtual_memory().total / (1024**3), 2
                        ),
                        "ram_available": round(
                            psutil.virtual_memory().available / (1024**3), 2
                        ),
                        "ram_percent": round(
                            psutil.virtual_memory().percent, 1
                        ),
                    },
                    "disks": {
                        "disk": disks_json,
                    },
                    "network": {
                        "io_counters": net_io_json,
                        "interfaces": merged_interfaces,
                    },
                    "sensors": {
                        "battery": battery_json,
                        "fans": fans_json,
                        "temperatures": temperatures_json,
                    },
                    "docker": {
                        "images": docker_images,
                        "containers": docker_containers
                    }
                }
            disconnected_clients = set()
            for client in connected_clients.copy():
                try:
                    await client.send_text(json.dumps(latest_data))
                except Exception as e:
                    logger.error(f"Failed to send to client: {e}")
                    disconnected_clients.add(client)
            connected_clients -= disconnected_clients
            logger.info(f"Data sent to {len(connected_clients)} clients")
        except Exception as e:
            logger.error(f"System monitor error: {e}")
        await asyncio.sleep(2)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting background system monitor...")
    monitor_task = asyncio.create_task(system_monitor())
    yield
    logger.info("Shutting down system monitor...")
    monitor_task.cancel()
    try:
        await monitor_task
    except asyncio.CancelledError:
        logger.error("System monitor stopped")

app = FastAPI(
    title="Performance Dashboard API",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.info(f"Client connected: {id(websocket)}")

    connected_clients.add(websocket)

    async with data_lock:
        if latest_data:
            try:
                await websocket.send_text(
                    json.dumps(latest_data)
                )
                logger.info(f"Initial data sent to client: {id(websocket)}")
            except Exception as e:
                logger.error(f"Failed to send initial data: {e}")
    try:
        while True:
            await asyncio.sleep(1)
    except Exception as e:
        logger.error(f"Client {id(websocket)} disconnected: {e}")
    finally:
        connected_clients.discard(websocket)
        logger.info(f"Client {id(websocket)} removed")


@app.get("/")
def read_root():
    return {
        "message": "Performance Dashboard API is running."
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, host="0.0.0.0", port=8000, reload=True
    )
