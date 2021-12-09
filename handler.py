from aiogram import types
from loader import dp


@dp.message_handler(commands=['start'])
async def do_start(message: types.Message):
    await message.answer("Assalomu alaykum Abdulaziz ishladi webhook!")
