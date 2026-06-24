import os
import datetime
import psutil


from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


# خواندن فایل .env
load_dotenv()

# گرفتن Token از Environment Variable
TOKEN = os.getenv("BOT_TOKEN")


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


def main():
    """
    راه‌اندازی ربات
    """

    # بررسی وجود Token
    if not TOKEN:
        raise ValueError("BOT_TOKEN not found in .env file")

    # ساخت Application تلگرام
    app = Application.builder().token(TOKEN).build()

    # ثبت دستورات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("cpu", cpu_command))
    app.add_handler(CommandHandler("ram", ram_command))
    app.add_handler(CommandHandler("disk", disk_command))
    app.add_handler(CommandHandler("uptime", uptime_command))

    print("DevOps Telegram Bot is running...")

    # شروع دریافت پیام‌ها
    app.run_polling()


if __name__ == "__main__":
    main()