# 🚀 DevOps Telegram Monitoring Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/Project-Learning%20DevOps-orange)

A Production-Style Telegram Monitoring & Alerting System

Built with Python, Telegram Bot API and DevOps Best Practices

</div>

---

## 📖 Overview

DevOps Telegram Monitoring Bot is a monitoring and alerting solution that collects system metrics and sends real-time notifications through Telegram.

The project was built as a hands-on DevOps learning journey covering:

* Infrastructure Monitoring
* Alerting Systems
* Logging
* Environment Configuration
* Git & GitHub Workflow
* Docker Containerization (Upcoming)
* VPS Deployment (Upcoming)

---

## ✨ Features

### 📊 Monitoring

* CPU Monitoring
* RAM Monitoring
* Disk Monitoring
* System Uptime
* Full System Status

### 🚨 Alerting

* High CPU Alerts
* CPU Recovery Alerts
* High RAM Alerts
* RAM Recovery Alerts
* High Disk Alerts
* Disk Recovery Alerts
* Startup Notifications

### ⚙️ Configuration

* Environment Variables Support
* Custom Alert Thresholds
* Secure Token Management

### 📝 Logging

* Startup Logs
* Alert Logs
* Recovery Logs
* Operational Logs

---

## 🤖 Available Commands

| Command | Description            |
| ------- | ---------------------- |
| /start  | Start the bot          |
| /help   | Show help menu         |
| /status | Complete system status |
| /cpu    | CPU usage              |
| /ram    | RAM usage              |
| /disk   | Disk usage             |
| /uptime | System uptime          |
| /id     | Telegram Chat ID       |

---

## 📂 Project Structure

```text
devops-telegram-bot/
│
├── bot/
│   └── main.py
│
├── config/
├── logs/
│   └── bot.log
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

* Python 3.12
* python-telegram-bot
* psutil
* dotenv
* Git
* GitHub

---

## 📈 Roadmap

### Current Version

* [x] Monitoring System
* [x] Alerting System
* [x] Logging System
* [x] GitHub Integration

### Next Steps

* [ ] Docker Support
* [ ] Docker Compose
* [ ] Linux Service Monitoring
* [ ] Container Monitoring
* [ ] VPS Deployment
* [ ] Production Environment

---

## 🔐 Security

Sensitive information is stored using environment variables and excluded from version control.

```env
BOT_TOKEN=***
CHAT_ID=***
```

---

## 👨‍💻 Author

**Milad Sarhadbani**

DevOps Learning Journey

Building practical monitoring and automation solutions using modern DevOps tools and workflows.

---

⭐ Star this repository if you like the project.
