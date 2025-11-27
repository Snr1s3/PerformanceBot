# Introduction

---

## 💡 Idea

**Performance Bot** was created when I needed a simple way to monitor my home server from outside my home, without using complicated commands.

At first, I considered building a web page, but I wanted to try something new. That’s when I came up with the idea of building a bot.

---

## 📋 Summary

To start my project, I needed to gather all the essential information from my server:

- `/system` – System info  
- `/cpu` – CPU info  
- `/memory` – Memory info  
- `/disk` – Disk info  
- `/network` – Network info  
- `/docker` – Docker info  
- `/sensors` – Sensors info  

After some research, I found two very useful Python libraries:  
- `psutil` for gathering system info  
- `docker`, the Docker SDK for getting Docker info (images and containers)

---

## ⚙️ Implementation

With those libraries in mind, I started a WebSocket server using the **FastAPI** framework and began serving it on my localhost at port 8000.

Once I had the WebSocket server working, I started researching how to create a Telegram bot. I discovered a Telegram bot called **TheBotFather**, which lets you create and customize bot profiles and provides you with a token to work with.

After the bot was ready, I worked on the `Dockerfile` to make deployment easier, whether in the cloud or if the bot and backend are running on different servers. While working on the Dockerfile, I found that **GitHub** can help you create an image and push that image to Docker Hub automatically when you push to the GitHub repo.

---

## 📚 Documentation

Finally, I found **mdBook**, which helps me deploy documentation for the repo using Markdown files, making everything much easier.