# DevOps Telegram Monitoring Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-Supported-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI-blue)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Docker-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Project](https://img.shields.io/badge/Project-Learning%20DevOps-orange)
[![CI](https://github.com/milad5108/devops-telegram-bot/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/milad5108/devops-telegram-bot/actions/workflows/ci.yml)

A production-style Telegram monitoring and alerting bot built with Python, Docker, Docker Compose, and DevOps best practices.

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
* GitHub Actions CI
* Linux deployment preparation

This project is built as a portfolio-ready DevOps project to demonstrate practical monitoring, automation, containerization, and CI workflow skills.

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
* `.env.example` template for safe configuration sharing

### Logging

* Startup logs
* Alert logs
* Recovery logs
* Operational logs

### DevOps Workflow

* Git and GitHub version control
* Docker image build
* Docker Compose orchestration
* GitHub Actions CI workflow
* Automated Python compile check
* Automated Docker build check

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
├── .github/
│   └── workflows/
│       └── ci.yml
│
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
├── .env.example
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
* GitHub Actions

---

## Environment Variables

Create a local `.env` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
```

You can use `.env.example` as a template:

```env
BOT_TOKEN=your_telegram_bot_token_here
CHAT_ID=your_telegram_chat_id_here
```

Important:

* Do not commit `.env`
* Keep secrets local
* Use `/id` in Telegram to get your chat ID
* Only commit `.env.example`, not the real `.env` file

---

## Run Locally with Python

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the bot:

```powershell
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

Follow logs:

```powershell
docker compose logs -f bot
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

## GitHub Actions CI

This project includes a GitHub Actions workflow that runs automatically on push and pull request events.

The CI workflow performs:

* Repository checkout
* Python 3.12 setup
* Dependency installation from `requirements.txt`
* Python compile check for the `bot` package
* Docker image build check

Workflow file:

```text
.github/workflows/ci.yml
```

This helps confirm that the project can be installed, checked, and containerized successfully in a clean GitHub Actions environment.

---

## Docker Monitoring Notes

When the bot runs inside Docker, system metrics are collected from the Linux/Docker environment, not directly from the Windows Task Manager.

For local Docker Desktop usage:

* `/cpu` shows CPU usage visible to the Docker/Linux environment
* `/ram` shows RAM visible to the Docker/Linux environment
* `/disk` checks the Linux root path `/`
* `/uptime` shows the uptime of the Linux environment behind Docker

When deployed to a Linux server, these metrics will represent the actual server environment.

---

## Current Status

Completed:

* Telegram bot setup
* Monitoring commands
* CPU, RAM, disk, and uptime checks
* Full status command
* Startup notification
* CPU, RAM, and disk alerts
* Recovery alerts
* Logging
* GitHub workflow
* Docker support
* Docker Compose support
* GitHub Actions CI
* CI badge in README
* Environment example file
* Project summary documentation

Next steps:

* Improve portfolio documentation
* Add optional deployment guide
* Add Prometheus metrics endpoint
* Add Grafana dashboard documentation

---

## Security

Sensitive information is stored in `.env` and excluded from version control.

Never commit:

```text
.env
BOT_TOKEN
CHAT_ID
```

Safe to commit:

```text
.env.example
```

---

## Portfolio Highlights

This project demonstrates:

* Building a real Telegram monitoring bot
* Reading system metrics with Python
* Sending automated alerts
* Using environment variables securely
* Containerizing a Python application with Docker
* Running the project with Docker Compose
* Managing code with Git and GitHub
* Creating a CI workflow with GitHub Actions
* Preparing a project for professional GitHub portfolio presentation

---

## Author

**Milad Sarhadbani**

DevOps Learning Journey

Building practical monitoring and automation solutions using modern DevOps tools and workflows.

---

Star this repository if you like the project.
