from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram_inline_paginations.paginator import Paginator
from aiogram.utils.callback_data import CallbackData

sura_names = {
    "1.Al-Fatihah":"1","2.Al-Baqarah":"2","3.Aali 'Imran":"3","4.An-Nisa":"4","5.Al-Ma'idah":"5",
    "6.Al-An'am":"6","7.Al-A'raf":"7","8.Al-Anfal":"8","9.At-Tawbah":"9","10.Yunus":"10","11.Hud":"11",
    "12.Yusuf":"12","13.Ar-Ra'd":"13","14.Ibrahim":"14","15.Al-Hijr":"15","16.An-Nahl":"16","17.Al-Isra":"17",
    "18.Al-Kahf":"18","19.Maryam":"19","20.Ta-Ha":"20","21.Al-Anbiya":"21","22.Al-Hajj":"22","23.Al-Mu'minun":"23",
    "24.An-Nur":"24","25.Al-Furqan":"25","26.Ash-Shu'ara":"26","27.An-Naml":"27","28.Al-Qasas":"28","29.Al-Ankabut":"29",
    "30.Ar-Rum":"30","31.Luqmaan":"31","32.As-Sajdah":"32","33.Al-Ahzaab":"33","34.Saba":"34","35.Faatir":"35","36.Ya-Sin":"36",
    "37.As-Saaffaat":"37","38.Saad":"38","39.Az-Zumar":"39","40.Ghafir":"40","41.Fussilat":"41","42.Ash-Shura":"42","43.Az-Zukhruf":"43",
    "44.Ad-Dukhaan":"44","45.Al-Jaathiyah":"45","46.Al-Ahqaaf":"46","47.Muhammad":"47","48.Al-Fath":"48","49.Al-Hujuraat":"49","50.Qaaf":"50",
    "51.Adh-Dhaariyaat":"51","52.At-Toor":"52","53.An-Najm":"53","54.Al-Qamar":"54","55.Ar-Rahman":"55","56.Al-Waqi'ah":"56","57.Al-Hadeed":"57",
    "58.Al-Mujadila":"58","59.Al-Hashr":"59","60.Al-Mumtahanah":"60","61.As-Saff":"61","62.Al-Jumu'ah":"62","63.Al-Munafiqoon":"63","64.At-Taghabun":"64",
    "65.At-Talaq":"65","66.At-Tahreem":"66","67.Al-Mulk":"67","68.Al-Qalam":"68","69.Al-Haaqqa":"69","70.Al-Ma'aarij":"70","71.Nuh":"71",
    "72.Al-Jinn":"72","73.Al-Muzzammil":"73","74.Al-Muddaththir":"74","75.Al-Qiyamah":"75","76.Al-Insaan":"76","77.Al-Mursalaat":"77","78.An-Naba'":"78",
    "79.An-Naazi'aat":"79","80.Abasa":"80","81.At-Takweer":"81","82.Al-Infitar":"82","83.Al-Mutaffifeen":"83","84.Al-Inshiqaaq":"84","85.Al-Burooj":"85",
    "86.At-Taariq":"86","87.Al-A'la":"87","88.Al-Ghaashiyah":"88","89.Al-Fajr":"89","90.Al-Balad":"90","91.Ash-Shams":"91","92.Al-Layl":"92","93.Ad-Dhuha":"93",
    "94.Ash-Sharh":"94","95.At-Tin":"95","96.Al-Alaq":"96","97.Al-Qadr":"97","98.Al-Bayyinah":"98","99.Az-Zalzalah":"99","100.Al-'Aadiyat":"100","101.Al-Qaari'ah":"101",
    "102.At-Takaathur":"102","103.Al-'Asr":"103","104.Al-Humazah":"104","105.Al-Fil":"105","106.Quraish":"106","107.Al-Maa'oon":"107","108.Al-Kavsar":"108",
    "109.Al-Kaafirun":"109","110.An-Nasr":"110","111.Al-Masad":"111","112.Al-Ixlos":"112","113.Al-Falaq":"113","114.An-Naas":"114"

}

sura_callback = CallbackData("suralar","name")

sura_inline = InlineKeyboardMarkup(row_width=2)
for tx, cd in sura_names.items():
    sura_inline.insert(InlineKeyboardButton(text=tx, callback_data=sura_callback.new(name=cd)))
# paginator = Paginator(data=sura_inline, size=62)



##########################################################################################################
joy_callback = CallbackData("joy","nomi")

viloyat_list = ["Toshkent","Farg'ona","Namangan","Andijon","Samarqand","Buxoro","Navoiy","Qarshi","Nukus"]
joylar = InlineKeyboardMarkup(row_width=2)
for joy in viloyat_list:
    joylar.insert(InlineKeyboardButton(text=joy, callback_data=joy_callback.new(nomi=joy)))

quron_choice = InlineKeyboardMarkup(row_width=2)
quron_choice.insert(InlineKeyboardButton(text="Suraning to'liq manosi",callback_data="sura"))
quron_choice.insert(InlineKeyboardButton(text="Belgilangan oyat manosi",callback_data="oyat"))
