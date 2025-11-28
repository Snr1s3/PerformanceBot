# PerformanceBot

PerformanceBot is a Telegram bot for monitoring system performance metrics in real time.   

[![Docs](https://img.shields.io/badge/Docs-snr1s3%2Fperformance--bot-blue?logo=docs)](https://snr1s3.github.io/PerformanceBot)           
[![Docker Hub](https://img.shields.io/badge/dockerhub-snr1s3%2Fperformance--bot-blue?logo=docker)](https://hub.docker.com/repository/docker/snr1s3/performance-bot/general)

## Features

- View system information (OS, kernel, uptime, users)
- Monitor CPU usage and per-core stats 
- Check memory usage
- Display disk usage and partitions
- Show network statistics and interfaces
- List Docker images and containers
- View hardware sensors (fans, temperatures, battery)
- All info available via Telegram commands

## Usage

1. **Start the bot:**  
   `/start` – Shows welcome and help

2. **Available commands:**  
   - `/system` – System info  
   - `/cpu` – CPU info  
   - `/memory` – Memory info  
   - `/disk` – Disk info  
   - `/network` – Network info  
   - `/docker` – Docker info  
   - `/sensors` – Sensors info  
   - `/all` – All info  
   - `/help` – Show help

## Setup

1. Clone the repository && Run the setup:
   ```bash
   git clone https://github.com/Snr1s3/PerformanceBot.git
   cd PerformanceDashboard
   bash setup.sh
   ```
2. Run the backend:
   ```bash
   bash backend/run_backend.sh
   ```
3. Configurate environment variables named BOT_TOKEN and WEB_SOCKET_URL
   ```bash
   # Add this lines in the ~/.bashrc
   BOT_TOKEN="REPLACE WITH YOUR TOKEN"
   WEB_SOCKET_URL="REPLACE WITH YOUR URL"
   ```
4. Run the bot:
   ```bash
   # Run the bot locally
   bash bot/run_bot.sh
   # Or run the bot as a Docker container (recommended for cloud hosting the bot and having the backend on a different server)
   sudo docker run --name bot -e WEB_SOCKET_URL=$WEB_SOCKET_URL -e BOT_TOKEN=$BOT_TOKEN performance-bot


