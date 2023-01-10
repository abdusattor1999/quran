from loader import dp 
from aiogram.types import Message, CallbackQuery
from keyboards.inline.inline_keys import sura_callback,sura_inline
import requests,json
from utils.other import nuqta

def tafsir_request(sura, oyat=None):
    if oyat:
        url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}/{oyat}.json"
    else:
        url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}.json"
    response = requests.get(url).json()
    return response


@dp.message_handler(text="📖 Qur'on tafsiri")
async def tafsir_bosildi(ms:Message):
    await ms.answer("Surani tanlang", reply_markup=sura_inline)


@dp.callback_query_handler(sura_callback.filter())
async def sura_tafir(call:CallbackQuery):
    malumot = call.get_current()
    sura = malumot["data"]
    sura = nuqta(sura)[1]
    jami = [f"Sura tartib raqami : {sura}\n\n"]
    jami_len = len(jami)
    savol = tafsir_request(sura)
    asosiy = savol['chapter']
    for i in asosiy:
        bir = f"{i['verse']}.{i['text']} "
        if len(bir) + jami_len >= 2048:
            await call.message.answer("  ".join(jami))
            jami = [bir]
            jami_len = 0
        else:
            jami.append(bir)
            jami_len += len(bir)
    if jami:
        await call.message.answer("  ".join(jami))
    await call.message.delete()


