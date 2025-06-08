import asyncio
import os
import time
import random
import sqlite3
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# --- KONFIGURACJA ---
API_TOKEN = os.getenv("BOT_TOKEN", "PUT_YOUR_TOKEN_HERE")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# --- STANY FSM ---
class AcceptState(StatesGroup):
    waiting_for_math = State()
class OpinionState(StatesGroup):
    waiting_for_text = State()
    waiting_for_photo = State()
    waiting_for_rating = State()
    waiting_for_confirm = State()
class MarketplaceState(StatesGroup):
    choosing_type = State()
    entering_title = State()
    entering_description = State()
    entering_price = State()
    entering_location = State()
    choosing_transaction = State()
    uploading_photos = State()
    choosing_safe_deal = State()
    confirming = State()

# --- MENU ---
MENU_BUTTONS = [
    ["🔥 𝙉𝙄𝙂𝙃𝙏_𝙇𝙄𝙎𝙏 🔥"],
    ["🔍 𝙎𝙕𝙐𝙆𝘼𝙅 🔍"],
    ["🛍️ 𝙈𝘼𝙍𝙆𝙀𝙏𝙋𝙇𝘼𝘾𝙀 🛍️"],
]
def get_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for row in MENU_BUTTONS:
        kb.add(*row)
    return kb

# --- ANTYSPAM ---
MATH_QUESTIONS = [
    ("2x2 = ?", "4"),
    ("8-4 = ?", "4"),
    ("7:1 = ?", "7"),
    ("6+3 = ?", "9"),
    ("10-9 = ?", "1"),
]

async def delete_prev(msg):
    try:
        await msg.delete()
    except:
        pass

# ...dalsza logika bota (menu, sklepy, opinie, marketplace, obsługa stanów)...

# --- URUCHOMIENIE BOTA ---
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
