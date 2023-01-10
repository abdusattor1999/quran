import requests, json

def namoz(location):
    nomlar = {
        "Fajr":"Bomdod",
        "Sunrise":"Quyosh",
        "Dhuhr":"Peshin",
        "Asr":"Asr",
        "Maghrib":"Shom",
        "Isha'a":"Xufton"
    }
    url = f"https://dailyprayer.abdulrcs.repl.co/api/{location}"
    response = requests.get(url)
    data = response.json()
    text = f"🕌 Namoz vaqtlari :\n🏙 Joylashuv : {location}\n\n"
    for prayer in data["today"]:
        text += f"▫️ {nomlar.get(prayer)} : {data['today'][prayer]}\n"
    text += "\n‼️ Eslatma \nAsr vaqti Hanafiy mazhabiga ko'ra \n'30 ~ 60' daqiqa kechroq bo'ladi"
    return text



def jsonExtract(obj, key):
    arr = []
    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

def nuqta(gap):
    a,b = gap.split(":")
    return [a,b]


# Quron oyat tafsiri api
def quron(sura , oyat=None):
    if oyat:
        url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}/{oyat}.json"
        respons = requests.get(url)
        r = respons.json()
        return r
    else:
        url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}.json"
        respons = requests.get(url)
        javob =[]
        suraa = respons.json()
        for i in respons.json():
            javob.append(jsonExtract(suraa, "text"))
        return javob
