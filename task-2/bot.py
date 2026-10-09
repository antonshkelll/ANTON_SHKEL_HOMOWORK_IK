# Шкель Антон ПрИнж25-1

import asyncio
import os
import random
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

LYRICS_FILE = Path(__file__).parent / "lyrics.txt"

dp = Dispatcher()


def load_lines():
    if not LYRICS_FILE.exists():
        return []
    text = LYRICS_FILE.read_text(encoding="utf-8")
    lines = (line.strip() for line in text.splitlines())
    return [line for line in lines if line and not line.startswith("#")]


LINES = load_lines()


@dp.message(CommandStart())
async def start(message: Message):
    name = message.from_user.first_name if message.from_user else "друг"
    await message.answer(
        f"Привет, {name}! 👋\n\n"
        "Я умею немного, но с душой:\n"
        "/start — показать это сообщение\n"
        "/swaga — случайная строчка из трека «ДИНАСТИЯ» — madk1d\n\n"
        "Сделал Шкель Антон, ПрИнж25-1"
    )


@dp.message(Command("swaga"))
async def swaga(message: Message):
    if not LINES:
        await message.answer("Строчки куда-то пропали 😔 Проверь файл lyrics.txt")
        return
    await message.answer(random.choice(LINES))


async def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise SystemExit("Не найден BOT_TOKEN.")
    bot = Bot(token)
    print("Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
