from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp 
from keyboards.inline.inline_keys import joylar, sura_inline, quron_choice,joy_callback
from keyboards.default.main_keys import home_keys   
from utils.other import namoz, nuqta


@dp.message_handler(text="🧎 Namoz vaqti")
async def namoz_vaqtlari(ms:Message):
    await ms.answer("Bugunlik namoz vaqtlarini bilish uchun o'zingizni yoki o'zingizga yaqin viloyatni tanlang :", reply_markup=joylar)

@dp.callback_query_handler(joy_callback.filter())
async def location_selected(call:CallbackQuery, state:FSMContext):
    call_data = call.get_current()
    data = call_data['data']
    data = nuqta(data)[1]
    print(data)
    javob = namoz(data)
    await call.message.answer(text=javob, reply_markup=home_keys)
    await state.finish()
    await call.message.delete()




