import os
import datetime
import asyncio
import psutil
import logging


from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


# خواندن فایل .env
load_dotenv()
logging.basicConfig(
    filename="logs/bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# گرفتن Token از Environment Variable
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

CPU_ALERT_THRESHOLD = int(os.getenv("CPU_ALERT_THRESHOLD"))
CPU_RECOVERY_THRESHOLD = int(os.getenv("CPU_RECOVERY_THRESHOLD"))

RAM_ALERT_THRESHOLD = int(os.getenv("RAM_ALERT_THRESHOLD"))
RAM_RECOVERY_THRESHOLD = int(os.getenv("RAM_RECOVERY_THRESHOLD"))

DISK_ALERT_THRESHOLD = int(os.getenv("DISK_ALERT_THRESHOLD"))
DISK_RECOVERY_THRESHOLD = int(os.getenv("DISK_RECOVERY_THRESHOLD"))

cpu_alert_sent = False
ram_alert_sent = False
disk_alert_sent = False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handler دستور /start
    """
    await update.message.reply_text(
        "سلام 👋\n\n"
        "من DevOps Telegram Bot هستم.\n"
        "برای مانیتورینگ و مدیریت سرور ساخته شده‌ام 🚀"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handler دستور /help
    """
    help_text = """
📚 DevOps Telegram Bot Commands

/start - شروع ربات
/help - نمایش راهنما

🔧 Monitoring Commands
/status - وضعیت کامل سرور
/cpu - میزان مصرف CPU
/ram - میزان مصرف RAM
/disk - وضعیت فضای Disk
/uptime - مدت زمان روشن بودن سرور
"""

    await update.message.reply_text(help_text)


async def cpu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handler دستور /cpu
    """
    cpu_usage = psutil.cpu_percent(interval=1)

    message = (
        "🖥 CPU Status\n\n"
        f"Current CPU Usage: {cpu_usage}%"
    )

    await update.message.reply_text(message)


async def ram_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handler دستور /ram
    """
    memory = psutil.virtual_memory()

    total_gb = memory.total / (1024 ** 3)
    used_gb = memory.used / (1024 ** 3)
    percent = memory.percent

    message = (
        "🧠 RAM Status\n\n"
        f"Usage: {percent}%\n"
        f"Used: {used_gb:.2f} GB\n"
        f"Total: {total_gb:.2f} GB"
    )

    await update.message.reply_text(message)

async def disk_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handler دستور /disk
    """

    # خواندن اطلاعات درایو C در ویندوز
    disk = psutil.disk_usage("C:\\")

    total_gb = disk.total / (1024 ** 3)
    used_gb = disk.used / (1024 ** 3)
    free_gb = disk.free / (1024 ** 3)
    percent = disk.percent

    message = (
        "💾 Disk Status\n\n"
        f"Usage: {percent}%\n"
        f"Used: {used_gb:.2f} GB\n"
        f"Free: {free_gb:.2f} GB\n"
        f"Total: {total_gb:.2f} GB"
    )

    await update.message.reply_text(message)

async def uptime_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handler دستور /uptime
    """

    boot_time = psutil.boot_time()

    boot_datetime = datetime.datetime.fromtimestamp(boot_time)

    uptime = datetime.datetime.now() - boot_datetime

    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    message = (
        "⏳ System Uptime\n\n"
        f"Days: {days}\n"
        f"Hours: {hours}\n"
        f"Minutes: {minutes}\n"
        f"Seconds: {seconds}"
    )

    await update.message.reply_text(message)

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handler دستور /status
    """

    # CPU
    cpu = psutil.cpu_percent(interval=1)

    # RAM
    memory = psutil.virtual_memory()

    # Disk (Windows)
    disk = psutil.disk_usage("C:\\")

    # Uptime
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time

    days = uptime.days
    hours = uptime.seconds // 3600
    minutes = (uptime.seconds % 3600) // 60

    message = (
        "🤖 DevOps Server Status\n\n"
        "🖥 CPU\n"
        f"Usage: {cpu}%\n\n"

        "🧠 RAM\n"
        f"Usage: {memory.percent}%\n"
        f"Used: {memory.used / (1024 ** 3):.2f} GB / "
        f"{memory.total / (1024 ** 3):.2f} GB\n\n"

        "💾 Disk\n"
        f"Usage: {disk.percent}%\n"
        f"Free: {disk.free / (1024 ** 3):.2f} GB\n\n"

        "⏳ Uptime\n"
        f"{days} Days {hours} Hours {minutes} Minutes"
    )

    await update.message.reply_text(message)

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handler دستور /id
    """

    chat_id = update.effective_chat.id

    message = (
        "🆔 Telegram Chat ID\n\n"
        f"Your Chat ID: {chat_id}"
    )

    await update.message.reply_text(message)

async def send_test_alert(app):
    """
    ارسال پیام تست Alert
    """

    message = (
        "🚨 TEST ALERT\n\n"
        "DevOps Monitoring Bot is online ✅"
    )

    await app.bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )

    logger.info("Bot started successfully")


async def cpu_alert_monitor(app):
    global cpu_alert_sent

    while True:

        cpu_usage = psutil.cpu_percent(interval=1)

        # ارسال هشدار
        if cpu_usage > CPU_ALERT_THRESHOLD and not cpu_alert_sent:

            message = (
                "🚨 HIGH CPU ALERT\n\n"
                f"CPU Usage: {cpu_usage}%\n\n"
                "Server is under high load!"
            )

            await app.bot.send_message(
                chat_id=CHAT_ID,
                text=message
            )

            cpu_alert_sent = True
            logger.warning(f"High CPU Alert - Usage: {cpu_usage}%")

        # ارسال پیام Recovery
        elif cpu_usage < CPU_RECOVERY_THRESHOLD and cpu_alert_sent:

            message = (
                "✅ CPU RECOVERED\n\n"
                f"Current CPU Usage: {cpu_usage}%"
            )

            await app.bot.send_message(
                chat_id=CHAT_ID,
                text=message
            )

            cpu_alert_sent = False
            logger.info(f"CPU Recovered - Usage: {cpu_usage}%")

        await asyncio.sleep(10)

async def ram_alert_monitor(app):
    global ram_alert_sent

    while True:

        memory = psutil.virtual_memory()
        ram_usage = memory.percent

        # Alert
        if ram_usage > RAM_ALERT_THRESHOLD and not ram_alert_sent:

            message = (
                "🚨 HIGH RAM ALERT\n\n"
                f"RAM Usage: {ram_usage}%\n\n"
                "Memory usage is critically high!"
            )

            await app.bot.send_message(
                chat_id=CHAT_ID,
                text=message
            )

            ram_alert_sent = True
            logger.warning(f"High RAM Alert - Usage: {ram_usage}%")

        # Recovery
        elif ram_usage < RAM_RECOVERY_THRESHOLD and ram_alert_sent:

            message = (
                "✅ RAM RECOVERED\n\n"
                f"Current RAM Usage: {ram_usage}%"
            )

            await app.bot.send_message(
                chat_id=CHAT_ID,
                text=message
            )

            ram_alert_sent = False
            logger.info(f"RAM Recovered - Usage: {ram_usage}%")

        await asyncio.sleep(10)

async def disk_alert_monitor(app):
    global disk_alert_sent

    while True:

        disk = psutil.disk_usage("C:\\")
        disk_usage = disk.percent

        # Alert
        if disk_usage > DISK_ALERT_THRESHOLD and not disk_alert_sent:

            message = (
                "🚨 HIGH DISK ALERT\n\n"
                f"Disk Usage: {disk_usage}%\n\n"
                "Disk space is running low!"
            )

            await app.bot.send_message(
                chat_id=CHAT_ID,
                text=message
            )

            disk_alert_sent = True
            logger.warning(f"High Disk Alert - Usage: {disk_usage}%")

        # Recovery
        elif disk_usage < DISK_RECOVERY_THRESHOLD and disk_alert_sent:

            message = (
                "✅ DISK RECOVERED\n\n"
                f"Current Disk Usage: {disk_usage}%"
            )

            await app.bot.send_message(
                chat_id=CHAT_ID,
                text=message
            )

            disk_alert_sent = False
            logger.info(f"Disk Recovered - Usage: {disk_usage}%")

        await asyncio.sleep(10)

async def startup(app):
    """
    اجرا هنگام بالا آمدن ربات
    """

    await send_test_alert(app)

    app.create_task(
        cpu_alert_monitor(app)
    )

    app.create_task(
        ram_alert_monitor(app)
    )

    app.create_task(
     disk_alert_monitor(app)
    )


def main():
    """
    راه‌اندازی ربات
    """

    # بررسی وجود Token
    if not TOKEN:
        raise ValueError("BOT_TOKEN not found in .env file")

    # ساخت Application تلگرام
    app = (
    Application.builder()
    .token(TOKEN)
    .post_init(startup)
    .build()
)

    # ثبت دستورات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("cpu", cpu_command))
    app.add_handler(CommandHandler("ram", ram_command))
    app.add_handler(CommandHandler("disk", disk_command))
    app.add_handler(CommandHandler("uptime", uptime_command))
    app.add_handler(CommandHandler("status", status_command))
    app.add_handler(CommandHandler("id", id_command))

    print("DevOps Telegram Bot is running...")

    # شروع دریافت پیام‌ها
    app.run_polling()


if __name__ == "__main__":
    main()