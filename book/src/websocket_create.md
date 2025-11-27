# Create WebSocket

This example shows how to create a simple WebSocket server using FastAPI.  
The server allows clients to connect to the `/ws` endpoint and receive a JSON message with CPU, memory, and Docker container information.  
You can use this as a starting point to implement more advanced real-time monitoring features.

---

## Example Code

```python
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import psutil
import docker
import json

app = FastAPI(title="Performance Dashboard API")

# Enable CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

docker_client = docker.from_env()

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    docker_containers = []
    for idx, container in enumerate(docker_client.containers.list(all=True)):
        try:
            container_data = {
                "id": container.id[:12] if container.id else "unknown",
                "name": container.name if container.name else "unknown",
                "status": container.status if container.status else "unknown",
                "image": container.image.tags[0] if container.image.tags else (container.image.id[:12] if container.image.id else "unknown"),
                "created": container.attrs.get('Created', '')[:19] if container.attrs.get('Created') else 'unknown'
            }
            docker_containers.append({f"container{idx}": container_data})
        except Exception as e:
            print(f"Error processing container: {e}")
            continue

    latest_data = {
        "cpu": {
            "cores_count": psutil.cpu_count(logical=False),
            "threads_count": psutil.cpu_count(),
            "cpu": round(psutil.cpu_percent(), 1),
            "frequency": round(psutil.cpu_freq().current, 1),
        },
        "memory": {
            "ram_total": round(psutil.virtual_memory().total / (1024**3), 2),
            "ram_available": round(psutil.virtual_memory().available / (1024**3), 2),
            "ram_percent": round(psutil.virtual_memory().percent, 1),
        },
        "docker": {
            "containers": docker_containers
        }
    }
    await websocket.send_text(json.dumps(latest_data))
    await websocket.close()

# Simple HTTP root endpoint
@app.get("/")
def read_root():
    return {"message": "Performance Dashboard API is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
```
## Output
```json
{
  "cpu": {
    "cores_count": 4,
    "threads_count": 8,
    "cpu": 4.5,
    "frequency": 2611.2
  },
  "memory": {
    "ram_total": 7.61,
    "ram_available": 4.94,
    "ram_percent": 35.1
  },
  "docker": {
    "containers": [
      {
        "container0": {
          "id": "970b24a9730e",
          "name": "bot2",
          "status": "exited",
          "image": "performance-bot:latest",
          "created": "2025-11-26T14:18:18"
        }
      },
      {
        "container1": {
          "id": "900d303cb952",
          "name": "bot",
          "status": "exited",
          "image": "snr1s3/performance-bot:latest",
          "created": "2025-11-26T10:53:37"
        }
      }
    ]
  }
}
```