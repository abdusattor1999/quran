from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

home_keys = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
home_keys.insert(KeyboardButton("🧎 Namoz vaqti"))
home_keys.insert(KeyboardButton("📖 Qur'on tafsiri"))