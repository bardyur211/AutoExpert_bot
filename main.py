import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ContentType, Message
from aiogram.fsm.storage.memory import MemoryStorage
import keyboard
from Config import TOKEN


# Config logging
logging.basicConfig(level=logging.INFO)

# BOt token and dispatcher
BOT = Bot(token=TOKEN)
dp = Dispatcher()
storage = MemoryStorage()


@dp.message(F.content_type == ContentType.NEW_CHAT_MEMBERS)
async def new_member_handler(message: Message):
    new_member = message.new_chat_members[0]
    message_answer = f"""Привет, [{new_member.full_name}](tg://user?id={new_member.id})! Мы рады что ты с нами!
Перед тем как задавать вопросы, лучше ознакомься с правилами и основными разделами группы"""
    message_answer = message_answer.replace("!", "\\!")
    await message.answer(message_answer,
                         parse_mode='MarkdownV2',
                         reply_markup=keyboard.main_kb)


async def main():
    await dp.start_polling(BOT)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())