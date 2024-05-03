from datetime import datetime, timedelta
import aiogram 
from aiogram.types import KeyboardButton, InlineKeyboardButton, BotCommand
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from apscheduler.schedulers.background import BackgroundScheduler

import __token__
from DB.db import add_data

bot = aiogram.Bot(__token__.TOKEN)
dp = aiogram.Dispatcher()
sched = BackgroundScheduler()

def round_to_hour(dt: datetime):
    return (dt.replace(second=0, microsecond=0, minute=0, hour=dt.hour) + timedelta(hours=1))

sched.add_job(add_data, 'interval', hours=1, start_date=round_to_hour(datetime.now()))
# sched.add_job(add_data, 'interval', minutes=1)