import asyncio

from aiogram import types
from aiogram.filters import CommandStart
from aiogram.types.input_file import FSInputFile

import __init__ 
from DB.xlsx_worker import write_to_excel, file_path
from DB.db import get_data_by_date

bot = __init__.bot
dp = __init__.dp
sched = __init__.sched

@dp.message(CommandStart())
async def send_welcome(mess: types.Message):
    write_to_excel(get_data_by_date())
    document = FSInputFile(file_path)
    await bot.send_document(mess.from_user.id, document)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    sched.start()
    asyncio.run(main())