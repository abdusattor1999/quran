from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_keys import home_keys
from loader import dp
from aiogram.dispatcher import FSMContext

@dp.message_handler(state="*")
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state:FSMContext):
    if state:
        await state.finish()
    await message.reply(f"Assalomu aleykum <b>{message.from_user.first_name.title()}</b>\nBu bot Qur'on oyatlari tafsiri \nva namoz vaqtlari haqida ma'lumot \nolish uchun yasaldi.", reply_markup=home_keys)
