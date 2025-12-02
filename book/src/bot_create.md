# Create Bot

This guide will help you set up and run the Telegram bot for the Performance Dashboard project.

---

## Step 1: Create Your Bot with BotFather

1. Open Telegram and search for [@BotFather](https://t.me/BotFather).
2. Start a chat and send `/newbot`.
3. Follow the instructions to set your bot’s name and username.
4. Copy the token provided by BotFather — you’ll need it for the next step.

---
## Step 2: Set Up the Project

Try to connect to the bot creating bot.py

```python
    from telegram.ext import ApplicationBuilder
    from config import BOT_TOKEN
    from handlers import setup_handlers


    def main() -> None:
        app = ApplicationBuilder().token(BOT_TOKEN).build()
        setup_handlers(app)
        app.run_polling()

    if __name__ == "__main__":
        main()
```


## Step 3: Add Command Handlers

Example for a `/cpu` command handler:

```python
    from telegram.ext import CommandHandler, ContextTypes
    
    # ... previous setup ...
    def setup_handlers(app):
        app.add_handler(CommandHandler("cpu", cpu_Handler))

    async def cpu_Handler(update, context: ContextTypes.DEFAULT_TYPE):
        content = CpuInfo(SocketCon()).fetch()
        msg = "<b>CPU INFO:</b>\n" + "\n".join(content)
        await update.message.reply_text(msg, parse_mode="HTML")
```
## Step 4: Create the CPU Handler
Create cpuInfo.py and infoBase.py:
```python
    # cpuInfo.py
    from telegram import Update
    from telegram.ext import ContextTypes
    from .info_base import InfoBase 

    class CpuInfo(InfoBase):
        def fetch(self):
            def formatter(info):
                arr = []
                for key, value in info.items():
                    key_upper = key.upper()
                    if key_upper == "CPU":
                        value = str(value) + " %"
                    elif key_upper == "FREQUENCY":
                        value = str(value) + " GHz"
                    if key_upper not in ("CPU_CORE", "FREQUENCY_CORE"):
                        arr.append(f"{key_upper} : {value}")
                return arr
            return self.get_info("cpu", formatter)
```
```python
    # infoBase.py
    import json

    class InfoBase:
        def __init__(self, socket_con):
            self.socket_con = socket_con

        def get_info(self, section: str, formatter: callable) -> list:
            content = self.socket_con.receive()
            arr = []
            try:
                data = json.loads(content)
                if section:
                    info = data.get(section, {})
                    arr = formatter(info)
                else:
                    return data
            except Exception as e:
                print("Error parsing JSON:", e)
                print("Raw content:", content)
            return arr
```

Step 5: Connect to the Backend via WebSocket
Create socket_con.py:
```python
import os
import websocket
import json

class SocketCon:
    _instance = None
    _ws = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SocketCon, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.ws = None
        self.connected = False

    def connect(self, url=os.getenv("WEB_SOCKET_URL", "")):
        if self.ws is None:
            self.ws = websocket.WebSocket()
            try:
                self.ws.connect(url)
                self.connected = True
            except Exception as e:
                print(f"Could not connect to {url}: {e}")
                self.ws = None
                self.connected = False

    def receive(self):
        if self.ws and self.connected:
            try:
                return self.ws.recv()
            except Exception as e:
                print(f"WebSocket receive error: {e}")
                self.ws = None
                self.connected = False
        print("Falling back to jsons/TEST.json")
        try:
            with open("jsons/TEST.json", "r") as f:
                return json.dumps(json.load(f))
        except Exception as e:
            print(f"Error reading jsons/TEST.json: {e}")
            return '{}'
```    
## How to Run the Bot
Follow these steps to start the Telegram bot:
```bash
    # Install dependencies
    pip install -r requirements.txt

    # Change directory to the backend
    cd bot
    
    # Run the backend 
    python bot.py
```
---
## Bot Output
When you send /cpu to the bot, you might see:
```json
User                    BOT
--------> /cpu              
                   <-------
        CPU INFO:
        CORES_COUNT: 4
        THREAD_COUNT: 8
        CPU: 4.5%
        FREQUENCY: 2611.2 MHz