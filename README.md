# DevOps Telegram Monitoring Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-Supported-blue)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Docker-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Project](https://img.shields.io/badge/Project-Learning%20DevOps-orange)

A production-style Telegram monitoring and alerting bot built with Python, Docker, and DevOps best practices.

</div>

---

## Overview

DevOps Telegram Monitoring Bot is a hands-on DevOps learning project that monitors system metrics and sends alerts through Telegram.

The project is designed to practice real-world DevOps concepts such as:

* System monitoring
* Alerting
* Logging
* Environment configuration
* Git and GitHub workflow
* Docker containerization
* Docker Compose
* Linux server deployment preparation

---

## Features

### Monitoring

* CPU usage
* RAM usage
* Disk usage
* System uptime
* Full system status

### Alerting

* Startup notification
* High CPU alert
* CPU recovery alert
* High RAM alert
* RAM recovery alert
* High disk alert
* Disk recovery alert

### Configuration

* Environment variables with `.env`
* Secure token management
* Configurable alert thresholds
* Docker and Docker Compose support

### Logging

* Startup logs
* Alert logs
* Recovery logs
* Operational logs

---

## Available Telegram Commands

| Command   | Description                 |
| --------- | --------------------------- |
| `/start`  | Start the bot               |
| `/help`   | Show help menu              |
| `/status` | Show complete system status |
| `/cpu`    | Show CPU usage              |
| `/ram`    | Show RAM usage              |
| `/disk`   | Show disk usage             |
| `/uptime` | Show system uptime          |
| `/id`     | Show Telegram chat ID       |

---

## Project Structure

```text
devops-telegram-bot/
├── bot/
│   ├── __init__.py
│   └── main.py
│
├── config/
│   └── config.py
│
├── logs/
│   └── bot.log
│
├── .dockerignore
├── .env
├── .gitattributes
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## Tech Stack

* Python 3.12
* python-telegram-bot
* psutil
* python-dotenv
* Docker
* Docker Compose
* Git
* GitHub

---

## Environment Variables

Create a local `.env` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
```

Important:

* Do not commit `.env`
* Keep secrets local
* Use `/id` in Telegram to get your chat ID

---

## Run Locally with Python

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python -m bot.main
```

---

## Run with Docker

Build the Docker image:

```powershell
docker build -t devops-telegram-bot:latest .
```

Run the bot in detached mode:

```powershell
docker run -d --name devops-telegram-bot --env-file .env devops-telegram-bot:latest
```

Check the running container:

```powershell
docker ps
```

Check logs:

```powershell
docker logs devops-telegram-bot
```

Stop and remove the container:

```powershell
docker stop devops-telegram-bot
docker rm devops-telegram-bot
```

---

## Run with Docker Compose

Start the bot:

```powershell
docker compose up -d --build
```

Check status:

```powershell
docker compose ps
```

Check logs:

```powershell
docker compose logs bot
```

Restart the bot:

```powershell
docker compose restart bot
```

Stop the bot:

```powershell
docker compose down
```

---

## Docker Monitoring Notes

When the bot runs inside Docker, system metrics are collected from the Linux/Docker environment, not directly from the Windows Task Manager.

For local Docker Desktop usage:

* `/cpu` shows CPU usage visible to the Docker/Linux environment
* `/ram` shows RAM visible to the Docker/Linux environment
* `/disk` checks the Linux root path `/`
* `/uptime` shows the uptime of the Linux environment behind Docker

When deployed to a Linux VPS, these metrics will represent the actual server environment.

---

## Current Status

Completed:

* Telegram bot setup
* Monitoring commands
* CPU, RAM, disk, and uptime checks
* Startup notification
* CPU, RAM, and disk alerts
* Recovery alerts
* Logging
* GitHub workflow
* Docker support
* Docker Compose support

Next steps:

* Prepare Linux deployment
* Deploy to VPS
* Add process/restart management
* Add CI/CD with GitHub Actions
* Add Prometheus
* Add Grafana

---

## Security

Sensitive information is stored in `.env` and excluded from version control.

Never commit:

```text
.env
BOT_TOKEN
CHAT_ID
```

---

## Author

**Milad Sarhadbani**

DevOps Learning Journey

Building practical monitoring and automation solutions using modern DevOps tools and workflows.

---

Star this repository if you like the project.
