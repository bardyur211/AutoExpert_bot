import asyncio
import logging
import sys
import pathlib
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (ContentType, Message, CallbackQuery, KeyboardButton,
                           InlineKeyboardButton, ReplyKeyboardMarkup)
import keyboard
from Config import TOKEN


# Config logging
logging.basicConfig(level=logging.INFO)

# BOt token and dispatcher
BOT = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.content_type == ContentType.NEW_CHAT_MEMBERS)
async def new_member_handler(message: Message):
    new_member = message.new_chat_members[0]
    await message.answer(f"""Привет, {new_member.full_name}! Мы рады что ты с нами!
    Перед тем как задавать вопросы, лучше ознакомься с правилами и основными разделами группы""",
                         reply_markup=keyboard.main_kb)


async def main():
    await dp.start_polling(BOT)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())