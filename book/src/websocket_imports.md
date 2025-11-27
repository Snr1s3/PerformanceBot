# 📦WebSocket Imports

This section documents all the imports used in `backend/main.py` and their purposes.

---

## Standard Library Imports

- **datetime**  
  For handling dates and times, such as timestamps and formatting.

- **platform**  
  To retrieve information about the underlying platform (OS, node, release, etc.).

- **time**  
  For time-related functions, such as calculating uptime.

- **typing (Dict, Set)**  
  For type hinting dictionaries and sets.

- **contextlib (asynccontextmanager)**  
  To manage the application lifespan with asynchronous context managers.

- **asyncio**  
  For asynchronous programming, including tasks, locks, and sleep.

- **json**  
  For encoding and decoding JSON data.

---

## Third-Party Imports

- **fastapi**  
  - `FastAPI`: The main FastAPI application class.
  - `WebSocket`: For handling WebSocket connections.

- **fastapi.middleware.cors (CORSMiddleware)**  
  To enable Cross-Origin Resource Sharing (CORS) for the API.

- **psutil**  
  For retrieving system information such as CPU, memory, disk, sensors, and network stats.

- **docker**  
  For interacting with Docker, including listing images and containers.

---

## Summary Table

| Module         | Purpose                                              |
|----------------|------------------------------------------------------|
| datetime       | Date and time handling                               |
| platform       | System/platform information                          |
| time           | Time calculations                                    |
| typing         | Type hints for Dict and Set                          |
| contextlib     | Async context management                             |
| fastapi        | API and WebSocket framework                          |
| fastapi.middleware.cors | CORS middleware for FastAPI                 |
| psutil         | System resource monitoring                           |
| asyncio        | Async programming primitives                         |
| json           | JSON serialization/deserialization                   |
| docker         | Docker API interaction                               |

---