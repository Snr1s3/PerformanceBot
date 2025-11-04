import datetime
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import psutil
import asyncio
import json
import docker

app = FastAPI(title="Performance Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Performance Dashboard API Running"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # Accept the connection
    
    try:
        while True:
            # Send simple message every 2 seconds
            message = {
                "cpu": psutil.cpu_percent(interval=1),
                "cpucore": psutil.cpu_percent(interval=1, percpu=True),
                "cores": psutil.cpu_count(logical=False),
                "threads": psutil.cpu_count(),
                "frequency":psutil.cpu_freq(),
                "frequencycore":psutil.cpu_freq(percpu=True),
                "ram":psutil.virtual_memory(),
                "disk":psutil.disk_partitions(all=False),
                # ADD disk usage?
                "nic":psutil.net_if_addrs(),
                "netcons":psutil.net_connections(kind='inet'),
                "boottime":datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
            }
            await websocket.send_text(json.dumps(message))
            await asyncio.sleep(2)
            
    except Exception as e:
        print(f"Connection closed: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)