# Telegram bot: Game Account Sale Bot (using aiogram 3.x)
# Requirements: aiogram>=3.4.1, Python 3.8+
# IMPORTLAR
import asyncio
import logging
from datetime import datetime
from typing import Dict, Any
import os
# IMPORTLAR 2
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import (Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove,InputMediaPhoto, ContentType)
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

# # BOT DANNIYLARI
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
PAYMENT_CARD = os.getenv("PAYMENT_CARD")
PAYMENT_HOLDER = os.getenv("PAYMENT_HOLDER")
PAYMENT_AMOUNT = os.getenv("PAYMENT_AMOUNT")
PAYMENTS_NUMBER = os.getenv("PAYMENTS_NUMBER")
CLASH_OF_CLANS_ID = os.getenv("CLASH_OF_CLANS_ID")
BRAWL_STARS_ID = os.getenv("BRAWL_STARS_ID")
PUBG_MOBILE_ID = os.getenv("PUBG_MOBILE_ID")
EFOOTBALL_ID = os.getenv("EFOOTBALL_ID")
# ✅ ASOSIY OBYEKTLAR NAVIGATSIYA
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()
pending_posts: Dict[int, Dict[str, Any]] = {}
logging.basicConfig(level=logging.INFO)
# BOT ORQAGA TUGMASI UCHUN
@router.message(F.text == "🔙 ORQAGA")
async def go_back(message: Message, state: FSMContext):
    current_state = await state.get_state()
    # -------- CLASH OF CLANS --------
    if current_state == "ClashOfClansForm:ratusha":
        await message.answer("QAYSI O‘YIN BO‘YICHA E'LON BERMOQCHISIZ ❓\n\n ⌨️ QUYIDAGI MENYUDAN BO‘LIMNI TANLANG VA BOSHLAYMIZ! 👇", reply_markup=get_game_menu())
        await state.set_state(GameSelection.waiting_for_game)
    elif current_state == "ClashOfClansForm:kubik":
        await message.answer(
"🏠 RATUSHA DARAJASINI KIRITING\n\n"
"❗️TO‘G‘RI YOZING. E'LONINGIZ SHUNGA BOG‘LIQ.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏡 6-TH\n"
"— 🏡 9-TH\n"
"— 🏡 12-TH\n"
"— 🏡 15-TH\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_clash_ratusha_menu())
        await state.set_state(ClashOfClansForm.ratusha)
    elif current_state == "ClashOfClansForm:skin":
        await message.answer(
"🏆 KUBIK DARAJASINI KIRITING\n\n"
"❗️ILTIMOS, ANIQ SON KIRITILSIN. BU BILAN AKAUNTINGIZ QIYMATI BAHOLANADI.\n\n\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏅 MASTER\n"
"— 🏆 CHAEMPION\n"
"— 👑 LAGEND\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_clash_kubik_menu())
        await state.set_state(ClashOfClansForm.kubik)
    elif current_state == "ClashOfClansForm:gold_pass":
        await message.answer(
"🦹 SKINLAR SONINI KIRITING\n\n"
"❗️E'LONINGIZ TO‘LIQ CHIQISHI UCHUN SKINLAR SONINI ANIQ KIRITING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🎭 LUCHNITSA 5 TA SKIN\n"
"— 🎭 XRANITEL 3 TA SKIN\n"
"— 🎭 KAROL 1 TA SKIN\n\n"
"✅ ILOJI BORICHA TO‘LIQ YOZING: 'GEROY NOMI + . TA SKIN' KO‘RINISHIDA!", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.skin)
    elif current_state == "ClashOfClansForm:obmen":
        await message.answer(
"🎫 GOLD PASS SONINI KIRITING\n\n"
"❗️GOLD PASS — AKAUNT QIYMATIGA KATTA TA'SIR QILADI, SHUNING UCHUN UNI TO‘G‘RI KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏅 YOQ GOLD PASS\n"
"— 🏅 1 TA GOLD PASS\n"
"— 🏅 6 TA GOLD PASS\n\n"
"✅ ILOJI BORICHA TO‘LIQ YOZING: 'SON + TA GOLD PASS' KO‘RINISHIDA!", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.gold_pass)
    elif current_state == "ClashOfClansForm:qoshimcha":
        await message.answer(
"♻️ OBMEN BORMI?\n\n"
"❗️AGAR OBMEN (ALMASHTIRUV) MUMKIN BO‘LSA, QUYIDAGI SHAKLLARDAN BIRINI YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— ✅ HA, OBMEN BOR\n"
"— ❌ YO‘Q, FAQAT SOTILADI\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_yes_no_menu())
        await state.set_state(ClashOfClansForm.obmen)
    elif current_state == "ClashOfClansForm:ulang":
        await message.answer(
"🔖 QO‘SHIMCHA MA'LUMOT KIRITASIZMI?\n\n"
"❗️AGAR E'LONINGIZGA QO‘SHIMCHA TUSHUNTIRISH YOKI MUHIM MA'LUMOT QO‘SHMOQCHI BO‘LSANGIZ — BU YERGA YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📝 AKKAUNTDA QO‘SHIMCHA QAHRAMONLAR BOR\n"
"— 📝 OBMEN FAQAT MAXSUS SHAXSLARGA\n"
"— 📝 SOTILGANIDAN KEYIN QAYTARIB OLINMAYDI\n\n"
"✅ AGAR YO‘Q BO‘LSA, 'YO‘Q' DEB YUBORING!", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.qoshimcha)
    elif current_state == "ClashOfClansForm:narx":
        await message.answer(
"📧 ULANGAN SERVISNI KIRITING\n\n"
"❗️BU BO‘LIMDA QANDAY SERVISLAR ULANGANINI KO‘RSATISHINGIZ ZARUR.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📱 SUPERCELL ID\n"
"— 🎮 GOOGLE PLAY\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_account_type_menu())
        await state.set_state(ClashOfClansForm.ulang)
    elif current_state == "ClashOfClansForm:tolov":
        await message.answer(
"💸 NARXINI KIRITING\n\n"
"❗️ILTIMOS, AKAUNT UCHUN QO‘YMOQCHI BO‘LGAN NARXNI TO‘LIQ YOZING.\n"
"SO‘MDA MIQDOR KO‘RSATILISHI SHART!\n\n"
"🔰 MISOL UCHUN:\n"
"— 💰 30 000 SO‘M\n"
"— 💰 75 000 SO‘M\n"
"— 💰 150 000 SO‘M\n\n"
"✅ AGAR BEPUL BO‘LSA, 'TEKIN' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.narx)
    elif current_state == "ClashOfClansForm:manzil":
        await message.answer(
"💳 TO‘LOV TURINI KIRITING\n\n"
"❗️ILTIMOS, QABUL QILADIGAN TO‘LOV USULINI ANIQ KO‘RSATING. (BIR NECHTASINI HAM YAZSA BO‘LADI)\n\n"
"🔰 MISOL UCHUN:\n"
"— 💳 KARTA\n"
"— 💵 NAQD\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_payment_menu())
        await state.set_state(ClashOfClansForm.tolov)
    elif current_state == "ClashOfClansForm:telegram":
        await message.answer(
"🏠 MANZILINGIZNI KIRITING\n\n"
"❗️MANZIL — TO‘LOV YOKI UCHRASHUV UCHUN MUHIM BO‘LISHI MUMKIN. ILTIMOS, ANIQ YOKI UMUMIY MANZIL YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏘️ TOSHKENT SHAHRIDA\n"
"— 📍 ANDIJON VILOYATI, ASAKA\n"
"— 🗺️ FAQAT ONLINE SAVDO\n\n"
"✅ AGAR HOZIRCHA AHAMIYATLI BO‘LMASA, 'YO‘Q' DEB YOZISHINGIZ MUMKIN!", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.manzil)
    elif current_state == "ClashOfClansForm:nomer":
        await message.answer(
"📩 TELEGRAM USERNAMEYINGIZNI KIRITING\n\n"
"❗️AGAR SOTUVCHI YOKI ADMIN SIZ BILAN BOG‘LANISHI KERAK BO‘LSA, USERNAME ORQALI ALOQA QILADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— @USERNAME\n"
"— @SAYYAXuz\n"
"— YO'Q\n\n"
"✅ AGAR USERNAME YO‘Q BO‘LSA 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.telegram)
    elif current_state == "ClashOfClansForm:screenshots":
        await message.answer(
"📞 TELEFON RAQAMINGIZNI KIRITING\n\n"
"❗️AGAR USERNAME BO‘LMASA YOKI TELEFON ORQALI BOG‘LANISHNI HOHLASANGIZ, RAQAMINGIZNI TO‘LIQ KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— +998 90 XXX XX XX\n"
"— +998 99 XXX XX XX\n\n"
"✅ ILTIMOS, XALQARO FORMATDA YOZING: '+998' BILAN BOSHLANSIN!", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.nomer)
    elif current_state == "ClashOfClansForm:payment_screenshot":
        await message.answer("📸 ILTIMOS, AKKAUNTINGIZNI RASMINI YUBORING (MAX 10 TA).\n"
        "HAMMASINI 1 TADA YUBORING MSOL 10 TASINI 1 TA QILIB. \n TUGAGACH '✅ RASMNI YUBORISH ' TUGMASINI BOSING.", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.screenshots)
    # -------- BRAWL STARS --------
    elif current_state == "BrawlStarsForm:kubik":
        await message.answer("QAYSI O‘YIN BO‘YICHA E'LON BERMOQCHISIZ ❓\n\n ⌨️ QUYIDAGI MENYUDAN BO‘LIMNI TANLANG VA BOSHLAYMIZ! 👇", reply_markup=get_game_menu())
        await state.set_state(GameSelection.waiting_for_game)
    elif current_state == "BrawlStarsForm:brawler":
        await message.answer(
"🏆 KUBIKLAR SONINI KIRITING\n\n"
"❗️ILTIMOS, ANIQ SON KIRITILSIN. BU BILAN AKAUNTINGIZ QIYMATI BAHOLANADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🎲 3500 KUBIK\n"
"— 🎲 8000 KUBIK\n"
"— 🎲 12500 KUBIK\n\n"
"✅ FAQAT SON EMAS, 'KUBIK' SO‘ZINI HAM QO‘SHISHNI UNUTMANG!", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.kubik)
    elif current_state == "BrawlStarsForm:legendarni":
        await message.answer(
"🥷 BRAWLERLAR SONINI KIRITING\n\n"
"❗️AKKAUNTDA NECHTA BRAWLER BORLIGINI KO‘RSATING. ILTIMOS, ANIQ SON KIRITING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 54 TA BRAWLER\n"
"— 62 TA BRAWLER\n"
"— 38 TA BRAWLER\n\n"
"✅ ILTIMOS, FAQAT SONINI VA 'TA' YOZING (MASALAN: 62 TA)", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.brawler)
    elif current_state == "BrawlStarsForm:skin":
        await message.answer(
"🏆 LEGENDAR BRAWLERLAR SONINI KIRITING\n\n"
"❗️AKKAUNTDA NECHTA LEGENDARNY BRAWLER BORLIGINI KIRITING. ILTIMOS, FAQAT SON YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 1 TA LEGENDAR\n"
"— 3 TA LEGENDAR\n"
"— 5 TA LEGENDAR\n\n"
"✅ AGAR LEGENDARNY BRAWLER BO‘LMASA, '0' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.legendarni)
    elif current_state == "BrawlStarsForm:brawl_pass":
        await message.answer(
"🦹 SKINLARNI KIRITING\n\n"
"❗️AKKAUNTDA MAVJUD SKINLARNI SANAB YOZING YOKI UMUMIY SONINI KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— GOLD MECHA BO, PHOENIX CROW, HEROINE BIBI\n"
"— 17 TA SKIN\n"
"— KO‘PCHILIGI RARE VA EPIC SKINLAR\n\n"
"✅ AGAR HECH QANDAY SKIN BO‘LMASA, 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.skin)
    elif current_state == "BrawlStarsForm:obmen":
        await message.answer(
"🎫 BRAWL PASS MA'LUMOTINI KIRITING\n\n"
"❗️AKKAUNTINGIZDA BRAWL PASS BORMI YOKI YO‘QLIGINI KO‘RSATING. ILTIMOS, ANIQ YOKI SODDA JAVOB YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— BOR\n"
"— YO‘Q\n"
"— OLDIN BOR EDI\n"
"— 5 MAROTABA OLGANMAN\n\n"
"✅ AGAR HECH QACHON OLMAGAN BO‘LSANGIZ, 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.brawl_pass)
    elif current_state == "BrawlStarsForm:qoshimcha":
        await message.answer(
"♻️ OBMEN BORMI?\n\n"
"❗️AGAR OBMEN (ALMASHTIRUV) MUMKIN BO‘LSA, QUYIDAGI SHAKLLARDAN BIRINI YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— ✅ HA, OBMEN BOR\n"
"— ❌ YO‘Q, FAQAT SOTILADI\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_yes_no_menu())
        await state.set_state(BrawlStarsForm.obmen)
    elif current_state == "BrawlStarsForm:ulang":
        await message.answer(
"🔖 QO‘SHIMCHA MA'LUMOT KIRITASIZMI?\n\n"
"❗️AGAR E'LONINGIZGA QO‘SHIMCHA TUSHUNTIRISH YOKI MUHIM MA'LUMOT QO‘SHMOQCHI BO‘LSANGIZ — BU YERGA YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📝 AKKAUNTDA QO‘SHIMCHA QAHRAMONLAR BOR\n"
"— 📝 OBMEN FAQAT MAXSUS SHAXSLARGA\n"
"— 📝 SOTILGANIDAN KEYIN QAYTARIB OLINMAYDI\n\n"
"✅ AGAR YO‘Q BO‘LSA, 'YO‘Q' DEB YUBORING!", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.qoshimcha)
    elif current_state == "BrawlStarsForm:narx":
        await message.answer(
"📧 ULANGAN SERVISNI KIRITING\n\n"
"❗️BU BO‘LIMDA QANDAY SERVISLAR ULANGANINI KO‘RSATISHINGIZ ZARUR.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📱 SUPERCELL ID\n"
"— 🎮 GOOGLE PLAY\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_account_type_menu())
        await state.set_state(BrawlStarsForm.ulang)
    elif current_state == "BrawlStarsForm:tolov":
        await message.answer(
"💸 NARXINI KIRITING\n\n"
"❗️ILTIMOS, AKAUNT UCHUN QO‘YMOQCHI BO‘LGAN NARXNI TO‘LIQ YOZING.\n"
"SO‘MDA MIQDOR KO‘RSATILISHI SHART!\n\n"
"🔰 MISOL UCHUN:\n"
"— 💰 30 000 SO‘M\n"
"— 💰 75 000 SO‘M\n"
"— 💰 150 000 SO‘M\n\n"
"✅ AGAR BEPUL BO‘LSA, 'TEKIN' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.narx)
    elif current_state == "BrawlStarsForm:manzil":
        await message.answer(
"💳 TO‘LOV TURINI KIRITING\n\n"
"❗️ILTIMOS, QABUL QILADIGAN TO‘LOV USULINI ANIQ KO‘RSATING. (BIR NECHTASINI HAM YAZSA BO‘LADI)\n\n"
"🔰 MISOL UCHUN:\n"
"— 💳 KARTA\n"
"— 💵 NAQD\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_payment_menu())
        await state.set_state(BrawlStarsForm.tolov)
    elif current_state == "BrawlStarsForm:telegram":
        await message.answer(
"🏠 MANZILINGIZNI KIRITING\n\n"
"❗️MANZIL — TO‘LOV YOKI UCHRASHUV UCHUN MUHIM BO‘LISHI MUMKIN. ILTIMOS, ANIQ YOKI UMUMIY MANZIL YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏘️ TOSHKENT SHAHRIDA\n"
"— 📍 ANDIJON VILOYATI, ASAKA\n"
"— 🗺️ FAQAT ONLINE SAVDO\n\n"
"✅ AGAR HOZIRCHA AHAMIYATLI BO‘LMASA, 'YO‘Q' DEB YOZISHINGIZ MUMKIN!", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.manzil)
    elif current_state == "BrawlStarsForm:nomer":
        await message.answer(
"📩 TELEGRAM USERNAMEYINGIZNI KIRITING\n\n"
"❗️AGAR SOTUVCHI YOKI ADMIN SIZ BILAN BOG‘LANISHI KERAK BO‘LSA, USERNAME ORQALI ALOQA QILADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— @USERNAME\n"
"— @SAYYAXuz\n"
"— YO'Q\n\n"
"✅ AGAR USERNAME YO‘Q BO‘LSA 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.telegram)
    elif current_state == "BrawlStarsForm:screenshots":
        await message.answer(
"📞 TELEFON RAQAMINGIZNI KIRITING\n\n"
"❗️AGAR USERNAME BO‘LMASA YOKI TELEFON ORQALI BOG‘LANISHNI HOHLASANGIZ, RAQAMINGIZNI TO‘LIQ KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— +998 90 XXX XX XX\n"
"— +998 99 XXX XX XX\n\n"
"✅ ILTIMOS, XALQARO FORMATDA YOZING: '+998' BILAN BOSHLANSIN!", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.nomer)
    elif current_state == "BrawlStarsForm:payment_screenshot":
        await message.answer("📸 ILTIMOS, AKKAUNTINGIZNI RASMINI YUBORING (MAX 10 TA).\n"
        "HAMMASINI 1 TADA YUBORING MSOL 10 TASINI 1 TA QILIB. \n TUGAGACH '✅ RASMNI YUBORISH ' TUGMASINI BOSING.", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.screenshots)
    # -------- PUBG MOBILE --------
    elif current_state == "PubgMobileForm:lvl":
        await message.answer("QAYSI O‘YIN BO‘YICHA E'LON BERMOQCHISIZ ❓\n\n ⌨️ QUYIDAGI MENYUDAN BO‘LIMNI TANLANG VA BOSHLAYMIZ! 👇", reply_markup=get_game_menu())
        await state.set_state(GameSelection.waiting_for_game)
    elif current_state == "PubgMobileForm:prokachka":
        await message.answer(
"〽️ LVL DARAJASINI KIRITING\n\n"
"❗️ILTIMOS, ANIQ SON KIRITILSIN. BU BILAN AKAUNTINGIZ QIYMATI BAHOLANADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🎖️ 80-LVL\n"
"— 🎖️ 85-LVL\n"
"— 🎖️ 30-LVL\n\n"
"✅ FAQAT SON EMAS, 'LVL' SO‘ZINI HAM QO‘SHISHNI UNUTMANG!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.lvl)
    elif current_state == "PubgMobileForm:kilchat":
        await message.answer(
"🔫 PROKACHKALARNI KIRITING\n\n"
"❗️PUBG AKKAUNTINGIZDA QANCHA PROKACHKA (YA’NI KO‘TARILGAN SKINLAR, LEVELLI QUROLLAR, UC-ORQALI OCHILGAN NARSA) BORLIGINI KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— M416 MAX\n"
"— DP28 4-DARAJA\n"
"— 3 TA PROKACHKA BOR\n"
"— YO‘Q\n\n"
"✅ AGAR HECH QANDAY PROKACHKA BO‘LMASA, 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.prokachka)
    elif current_state == "PubgMobileForm:xsuit":
        await message.answer(
"🪄 KILCHAT BO‘LGANLAR SONINI KIRITING\n\n"
"❗️AKKAUNTINGIZDA NECHTA BRAWLER TO‘LIQ KILCHAT (YA’NI MAKSIMAL DARAJADA OCHILGAN) EKANINI KO‘RSATING. ILTIMOS, SONDA YOZING YOKI QISQACHA TUSHUNTIRING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 7 TA KILCHAT\n"
"— HAMMASI KILCHAT QILINGAN\n"
"— YO'Q\n\n"
"✅ AGAR HECH QANDAY KILCHAT BO‘LMASA, '0' DEB YOZING YOKI 'YO‘Q' DEB BELGILANG!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.kilchat)
    elif current_state == "PubgMobileForm:ultimate":
        await message.answer(
"🦹 X-SUITLAR SONINI KIRITING\n\n"
"❗️PUBG AKKAUNTINGIZDA NECHTA X-SUIT (YA’NI MAXSUS EFFEKTLI KOSTYUMLAR) BORLIGINI KO‘RSATING. ILTIMOS, FAQAT SON YOZING YOKI NOMLARINI SANAB CHIQING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 2 TA X-SUIT\n"
"— PHARAOH VA MECHA X-SUIT\n"
"— YO'Q\n\n"
"✅ AGAR HECH QANDAY X-SUIT BO‘LMASA, '0' YOKI 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.xsuit)
    elif current_state == "PubgMobileForm:mifik":
        await message.answer(
"🧛 ULTIMATELAR SONINI KIRITING\n\n"
"❗️AKKAUNTINGIZDA NECHTA ULTIMATE KO‘RINISH (YA’NI ENG QIMMAT VA EFFEKTI BOR KOSTYUMLAR) BORLIGINI YOZING. ILTIMOS, SONDA YOKI NOMLARDA KIRITING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 1 TA ULTIMATE\n"
"— 3 TA BOR: BLOOD RAVEN, INFERNO RIDER, SILVER TITAN\n"
"— YO‘Q\n\n"
"✅ AGAR HECH QANDAY ULTIMATE BO‘LMASA, '0' YOKI 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.ultimate)
    elif current_state == "PubgMobileForm:sportcar":
        await message.answer(
"🥷 MIFIKLAR SONINI KIRITING\n\n"
"❗️PUBG AKKAUNTINGIZDA NECHTA MIFIK KO‘RINISH (YA’NI QIZIL RAMKALI KOSTYUMLAR, QIMMAT SKINLAR) BORLIGINI KO‘RSATING. ILTIMOS, SONDA YOKI NOMLARDA YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 7 TA MIFIK\n"
"— 3 TA: BLOOD RAVEN, CYCLOPS, FLAME LORD\n"
"— YO‘Q\n\n"
"✅ AGAR MIFIK YO‘Q BO‘LSA, '0' YOKI 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.mifik)
    elif current_state == "PubgMobileForm:royal_pass":
        await message.answer(
"🏎 SPORTCARLAR SONINI KIRITING\n\n"
"❗️PUBG AKKAUNTINGIZDA NECHTA SPORTCAR (YA’NI TESLA, KOENIGSEGG, BUGATTI, LAMBORGHINI KABI MAXSUS MASHINALAR) BORLIGINI YOZING. ILTIMOS, SONDA YOKI NOMLARDA KIRITING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 2 TA SPORTCAR\n"
"— TESLA MODEL Y VA KOENIGSEGG BOR\n"
"— YO‘Q\n\n"
"✅ AGAR SPORTCAR BO‘LMASA, '0' YOKI 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.sportcar)
    elif current_state == "PubgMobileForm:obmen":
        await message.answer(
"⚜️ ROYAL PASSLAR SONINI KIRITING\n\n"
"❗️PUBG AKKAUNTINGIZDA NECHTA ROYAL PASS OLGANLIGINGIZNI KO‘RSATING. ILTIMOS, SONDA YOKI QISQACHA TUSHUNTIRIB YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 5 TA ROYAL PASS\n"
"— 10-MAVSUMDAN 25-GACHA BOR\n"
"— YO'Q\n\n"
"✅ AGAR HECH QACHON ROYAL PASS OLMAGAN BO‘LSANGIZ, '0' YOKI 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.royal_pass)
    elif current_state == "PubgMobileForm:qoshimcha":
        await message.answer(
"♻️ OBMEN BORMI?\n\n"
"❗️AGAR OBMEN (ALMASHTIRUV) MUMKIN BO‘LSA, QUYIDAGI SHAKLLARDAN BIRINI YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— ✅ HA, OBMEN BOR\n"
"— ❌ YO‘Q, FAQAT SOTILADI\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_yes_no_menu())
        await state.set_state(PubgMobileForm.obmen)
    elif current_state == "PubgMobileForm:ulang":
       await message.answer(
"🔖 QO‘SHIMCHA MA'LUMOT KIRITASIZMI?\n\n"
"❗️AGAR E'LONINGIZGA QO‘SHIMCHA TUSHUNTIRISH YOKI MUHIM MA'LUMOT QO‘SHMOQCHI BO‘LSANGIZ — BU YERGA YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📝 AKKAUNTDA QO‘SHIMCHA QAHRAMONLAR BOR\n"
"— 📝 OBMEN FAQAT MAXSUS SHAXSLARGA\n"
"— 📝 SOTILGANIDAN KEYIN QAYTARIB OLINMAYDI\n\n"
"✅ AGAR YO‘Q BO‘LSA, 'YO‘Q' DEB YUBORING!", reply_markup=get_back_menu())
       await state.set_state(PubgMobileForm.qoshimcha)
    elif current_state == "PubgMobileForm:narx":
        await message.answer(
"📧 ULANGAN SERVISNI KIRITING\n\n"
"❗️BU BO‘LIMDA QANDAY SERVISLAR ULANGANINI KO‘RSATISHINGIZ ZARUR.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📱 POCHTA\n"
"— 🎮 GOOGLE PLAY\n"
"— YO'Q\n\n"
"✅ AGAR HECH QANDAY ULANGAN SERVER BO‘LMASA, '0' YOKI 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.ulang)
    elif current_state == "PubgMobileForm:tolov":
        await message.answer(
"💸 NARXINI KIRITING\n\n"
"❗️ILTIMOS, AKAUNT UCHUN QO‘YMOQCHI BO‘LGAN NARXNI TO‘LIQ YOZING.\n"
"SO‘MDA MIQDOR KO‘RSATILISHI SHART!\n\n"
"🔰 MISOL UCHUN:\n"
"— 💰 30 000 SO‘M\n"
"— 💰 75 000 SO‘M\n"
"— 💰 150 000 SO‘M\n\n"
"✅ AGAR BEPUL BO‘LSA, 'TEKIN' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.narx)
    elif current_state == "PubgMobileForm:manzil":
        await message.answer(
"💳 TO‘LOV TURINI KIRITING\n\n"
"❗️ILTIMOS, QABUL QILADIGAN TO‘LOV USULINI ANIQ KO‘RSATING. (BIR NECHTASINI HAM YAZSA BO‘LADI)\n\n"
"🔰 MISOL UCHUN:\n"
"— 💳 KARTA\n"
"— 💵 NAQD\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_payment_menu())
        await state.set_state(PubgMobileForm.tolov)
    elif current_state == "PubgMobileForm:telegram":
        await message.answer("🏠 MANZILINGIZNI KIRITING\n\n"
"❗️MANZIL — TO‘LOV YOKI UCHRASHUV UCHUN MUHIM BO‘LISHI MUMKIN. ILTIMOS, ANIQ YOKI UMUMIY MANZIL YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏘️ TOSHKENT SHAHRIDA\n"
"— 📍 ANDIJON VILOYATI, ASAKA\n"
"— 🗺️ FAQAT ONLINE SAVDO\n\n"
"✅ AGAR HOZIRCHA AHAMIYATLI BO‘LMASA, 'YO‘Q' DEB YOZISHINGIZ MUMKIN!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.manzil)
    elif current_state == "PubgMobileForm:nomer":
        await message.answer(
"📩 TELEGRAM USERNAMEYINGIZNI KIRITING\n\n"
"❗️AGAR SOTUVCHI YOKI ADMIN SIZ BILAN BOG‘LANISHI KERAK BO‘LSA, USERNAME ORQALI ALOQA QILADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— @USERNAME\n"
"— @SAYYAXuz\n"
"— YO'Q\n\n"
"✅ AGAR USERNAME YO‘Q BO‘LSA 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.telegram)
    elif current_state == "PubgMobileForm:screenshots":
        await message.answer(
"📞 TELEFON RAQAMINGIZNI KIRITING\n\n"
"❗️AGAR USERNAME BO‘LMASA YOKI TELEFON ORQALI BOG‘LANISHNI HOHLASANGIZ, RAQAMINGIZNI TO‘LIQ KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— +998 90 XXX XX XX\n"
"— +998 99 XXX XX XX\n\n"
"✅ ILTIMOS, XALQARO FORMATDA YOZING: '+998' BILAN BOSHLANSIN!", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.nomer)
    elif current_state == "PubgMobileForm:payment_screenshot":
        await message.answer( "📸 ILTIMOS, AKKAUNTINGIZNI RASMINI YUBORING (MAX 10 TA).\n"
        "HAMMASINI 1 TADA YUBORING MSOL 10 TASINI 1 TA QILIB. \n TUGAGACH '✅ RASMNI YUBORISH ' TUGMASINI BOSING.", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.screenshots)
    # -------- EFOOTBALL --------
    elif current_state == "EfootballForm:sila":
        await message.answer("QAYSI O‘YIN BO‘YICHA E'LON BERMOQCHISIZ ❓\n\n ⌨️ QUYIDAGI MENYUDAN BO‘LIMNI TANLANG VA BOSHLAYMIZ! 👇", reply_markup=get_game_menu())
        await state.set_state(GameSelection.waiting_for_game)
    elif current_state == "EfootballForm:epic":
        await message.answer(
"⚡️ SILANI KIRITING\n\n"
"❗️ILTIMOS, ANIQ SON KIRITILSIN. BU BILAN AKAUNTINGIZ QIYMATI BAHOLANADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— ⚔️ 1500 SILA\n"
"— ⚔️ 3200 SILA\n"
"— ⚔️ 4500 SILA\n\n"
"✅ FAQAT SON EMAS, 'SILA' SO‘ZINI HAM QO‘SHISHNI UNUTMANG!", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.sila)
    elif current_state == "EfootballForm:coin":
        await message.answer(
"🦸‍♂️ EPICLAR SONINI KIRITING\n\n"
"❗️EFOOTBALL AKKAUNTINGIZDA NECHTA EPIC O‘YINCHI BORLIGINI KO‘RSATING. ILTIMOS, FAQAT SON YOKI NOMLARDA KIRITING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 4 TA EPIC\n"
"— EPIC: MESSI, BECKHAM, BATISTUTA, ZANETTI\n"
"— EPIC YO‘Q\n\n"
"✅ AGAR HECH QANDAY EPIC BO‘LMASA, '0' YOKI 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.epic)
    elif current_state == "EfootballForm:obmen":
        await message.answer(
"💰 COIN MIQDORINI KIRITING\n\n"
"❗️EFOOTBALL AKKAUNTINGIZDA HOZIRDA NECHTA COIN BORLIGINI YOZING. ILTIMOS, FAQAT SON KIRITING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 500 COIN\n"
"— 1250 TA\n"
"— 0 COIN\n\n"
"✅ AGAR COIN BO‘LMASA, '0' YOKI 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.coin)
    elif current_state == "EfootballForm:qoshimcha":
        await message.answer(
"♻️ OBMEN BORMI?\n\n"
"❗️AGAR OBMEN (ALMASHTIRUV) MUMKIN BO‘LSA, QUYIDAGI SHAKLLARDAN BIRINI YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— ✅ HA, OBMEN BOR\n"
"— ❌ YO‘Q, FAQAT SOTILADI\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_yes_no_menu())
        await state.set_state(EfootballForm.obmen)
    elif current_state == "EfootballForm:ulang":
        await message.answer(
"🔖 QO‘SHIMCHA MA'LUMOT KIRITASIZMI?\n\n"
"❗️AGAR E'LONINGIZGA QO‘SHIMCHA TUSHUNTIRISH YOKI MUHIM MA'LUMOT QO‘SHMOQCHI BO‘LSANGIZ — BU YERGA YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📝 AKKAUNTDA QO‘SHIMCHA QAHRAMONLAR BOR\n"
"— 📝 OBMEN FAQAT MAXSUS SHAXSLARGA\n"
"— 📝 SOTILGANIDAN KEYIN QAYTARIB OLINMAYDI\n\n"
"✅ AGAR YO‘Q BO‘LSA, 'YO‘Q' DEB YUBORING!", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.qoshimcha)
    elif current_state == "EfootballForm:narx":
        await message.answer(
"📧 ULANGAN SERVISNI KIRITING\n\n"
"❗️BU BO‘LIMDA QANDAY SERVISLAR ULANGANINI KO‘RSATISHINGIZ ZARUR.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📱 KONAMI ID\n"
"— 🎮 GOOGLE PLAY\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_account_type_menu2())
        await state.set_state(EfootballForm.ulang)
    elif current_state == "EfootballForm:tolov":
        await message.answer(
"💸 NARXINI KIRITING\n\n"
"❗️ILTIMOS, AKAUNT UCHUN QO‘YMOQCHI BO‘LGAN NARXNI TO‘LIQ YOZING.\n"
"SO‘MDA MIQDOR KO‘RSATILISHI SHART!\n\n"
"🔰 MISOL UCHUN:\n"
"— 💰 30 000 SO‘M\n"
"— 💰 75 000 SO‘M\n"
"— 💰 150 000 SO‘M\n\n"
"✅ AGAR BEPUL BO‘LSA, 'TEKIN' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.narx)
    elif current_state == "EfootballForm:manzil":
        await message.answer(
"💳 TO‘LOV TURINI KIRITING\n\n"
"❗️ILTIMOS, QABUL QILADIGAN TO‘LOV USULINI ANIQ KO‘RSATING. (BIR NECHTASINI HAM YAZSA BO‘LADI)\n\n"
"🔰 MISOL UCHUN:\n"
"— 💳 KARTA\n"
"— 💵 NAQD\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_payment_menu())
        await state.set_state(EfootballForm.tolov)
    elif current_state == "EfootballForm:telegram":
        await message.answer(
"🏠 MANZILINGIZNI KIRITING\n\n"
"❗️MANZIL — TO‘LOV YOKI UCHRASHUV UCHUN MUHIM BO‘LISHI MUMKIN. ILTIMOS, ANIQ YOKI UMUMIY MANZIL YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏘️ TOSHKENT SHAHRIDA\n"
"— 📍 ANDIJON VILOYATI, ASAKA\n"
"— 🗺️ FAQAT ONLINE SAVDO\n\n"
"✅ AGAR HOZIRCHA AHAMIYATLI BO‘LMASA, 'YO‘Q' DEB YOZISHINGIZ MUMKIN!", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.manzil)
    elif current_state == "EfootballForm:nomer":
        await message.answer(
"📩 TELEGRAM USERNAMEYINGIZNI KIRITING\n\n"
"❗️AGAR SOTUVCHI YOKI ADMIN SIZ BILAN BOG‘LANISHI KERAK BO‘LSA, USERNAME ORQALI ALOQA QILADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— @USERNAME\n"
"— @SAYYAXuz\n"
"— YO'Q\n\n"
"✅ AGAR USERNAME YO‘Q BO‘LSA 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.telegram)
    elif current_state == "EfootballForm:screenshots":
        await message.answer(
"📞 TELEFON RAQAMINGIZNI KIRITING\n\n"
"❗️AGAR USERNAME BO‘LMASA YOKI TELEFON ORQALI BOG‘LANISHNI HOHLASANGIZ, RAQAMINGIZNI TO‘LIQ KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— +998 90 XXX XX XX\n"
"— +998 99 XXX XX XX\n\n"
"✅ ILTIMOS, XALQARO FORMATDA YOZING: '+998' BILAN BOSHLANSIN!", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.nomer)
    elif current_state == "EfootballForm:payment_screenshot":
        await message.answer(
        "📸 ILTIMOS, AKKAUNTINGIZNI RASMINI YUBORING (MAX 10 TA).\n"
        "HAMMASINI 1 TADA YUBORING MSOL 10 TASINI 1 TA QILIB. \n TUGAGACH '✅ RASMNI YUBORISH ' TUGMASINI BOSING.", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.screenshots)
# BUTTONLAR SOZLAMMALRI
def append_common_buttons(keyboard: list[list[KeyboardButton]]) -> list[list[KeyboardButton]]:
    keyboard.append([
        KeyboardButton(text="🔙 ORQAGA"),
        KeyboardButton(text="🚩 BOSH SAHIFAGA")
    ])
    return keyboard
def get_back_menu():
    keyboard = [
        [KeyboardButton(text="🔙 ORQAGA"), KeyboardButton(text="🚩 BOSH SAHIFAGA")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
def get_game_menu():
    keyboard = [
        [KeyboardButton(text="⚔️ CLASH OF CLANS"), KeyboardButton(text="💫 BRAWL STARS")],
        [KeyboardButton(text="🔫 PUBG MOBILE"), KeyboardButton(text="⚽ EFOOTBALL")]
    ]
    return ReplyKeyboardMarkup(keyboard=append_common_buttons(keyboard), resize_keyboard=True)
def get_yes_no_menu():
    keyboard = [
        [KeyboardButton(text="✅ HA"), KeyboardButton(text="❌ YO'Q")]
    ]
    return ReplyKeyboardMarkup(keyboard=append_common_buttons(keyboard), resize_keyboard=True)
def get_account_type_menu():
    keyboard = [
        [KeyboardButton(text="📱 SUPERCELL ID"), KeyboardButton(text="🎮 GOOGLE PLAY")]
    ]
    return ReplyKeyboardMarkup(keyboard=append_common_buttons(keyboard), resize_keyboard=True)
def get_account_type_menu2():
    keyboard = [
        [KeyboardButton(text="📱 KONAMI ID"), KeyboardButton(text="🎮 GOOGLE PLAY")]
    ]
    return ReplyKeyboardMarkup(keyboard=append_common_buttons(keyboard), resize_keyboard=True)
def get_clash_ratusha_menu():
    th_levels = [f"🏡 {i}-TH" for i in range(6, 18)]
    keyboard = [ 
        [KeyboardButton(text=th_levels[i]), KeyboardButton(text=th_levels[i + 1])]
        for i in range(0, len(th_levels) - 1, 2)
    ]
    return ReplyKeyboardMarkup(keyboard=append_common_buttons(keyboard), resize_keyboard=True)
def get_clash_kubik_menu():
    labels = ["🥉BRONZA", "🥈SILVER", "🥇GOLD", "💎CRAYSTAL", "🏅MASTER", "🏆CHAEMPION", "🪙TITAN", "👑LAGEND"]
    keyboard = [[KeyboardButton(text=label)] for label in labels]
    return ReplyKeyboardMarkup(keyboard=append_common_buttons(keyboard), resize_keyboard=True)
def get_payment_menu():
    keyboard = [
        [KeyboardButton(text="💳 KARTA"), KeyboardButton(text="💵 NAXT")]
    ]
    return ReplyKeyboardMarkup(keyboard=append_common_buttons(keyboard), resize_keyboard=True)
def get_finish_photos_menu():
    keyboard = [
        [KeyboardButton(text="✅ RASMNI YUBORISH")]
    ]
    return ReplyKeyboardMarkup(keyboard=append_common_buttons(keyboard), resize_keyboard=True)
# STATE
class GameSelection(StatesGroup):
    waiting_for_game = State()
# FORMLAR
class ClashOfClansForm(StatesGroup):
    ratusha = State()
    kubik = State()
    skin = State()
    gold_pass = State()
    obmen = State()
    qoshimcha = State()
    ulang = State()
    narx = State()
    tolov = State()
    manzil = State()
    telegram = State()
    nomer = State()
    screenshots = State()
    payment_screenshot = State()
class BrawlStarsForm(StatesGroup):
    kubik = State()
    brawler = State()
    legendarni = State()
    skin = State()
    brawl_pass = State()
    obmen = State()
    qoshimcha = State()
    ulang = State()
    narx = State()
    tolov = State()
    manzil = State()
    telegram = State()
    nomer = State()
    screenshots = State()
    payment_screenshot = State()
class PubgMobileForm(StatesGroup):
     lvl = State()
     prokachka = State()
     kilchat = State()
     xsuit = State()
     ultimate = State()
     mifik = State()
     sportcar = State()
     royal_pass = State()
     qoshimcha = State()
     obmen = State()
     ulang = State()
     narx = State()
     tolov = State()
     manzil = State()
     telegram = State()
     nomer = State()
     screenshots = State()
     payment_screenshot = State()
class EfootballForm(StatesGroup):
    sila = State()
    epic = State()
    coin = State()
    obmen = State()
    qoshimcha = State()
    ulang = State()
    narx = State()
    tolov = State()
    manzil = State()
    telegram = State()
    nomer = State()
    screenshots = State()
    payment_screenshot = State()
# BOSHLANGICH BUTTONLAR VA KOMANDALAR
# /start komandasi — foydalanuvchini bosh sahifaga yuboradi
@router.message(Command("start"))
async def start_cmd(message: Message, state: FSMContext):
    await state.clear()
    first_name = message.from_user.first_name
    text =(
        f"""
✨ <b>ASSALOMU ALAYKUM</b>, <a href='tg://user?id={message.from_user.id}'>{first_name.upper()}</a>! 👋

🥳 <b>O‘YIN E'LON BERISH UCHUN KELDINGIZMI?</b> UNDA TO‘G‘RI JOYDASIZ!

📢 BU YERDA E'LONINGIZNI TEZ, OSON VA MINGLAB O‘YINCHILARGA YETKAZISHINGIZ MUMKIN!

❗ MUHIM ESLATMA BIZDA ELON PULLIK ❗ 

⌨️ <b>QUYIDAGI MENYUDAN BO‘LIMNI TANLANG VA BOSHLAYMIZ! 👇</b>
"""
 
    )
    await message.answer(
    text,
    reply_markup=get_game_menu(),
    parse_mode="HTML"
    )
    # 👇 MUHIM: state ni o‘rnatamiz
    await state.set_state(GameSelection.waiting_for_game)
# 🚩 BOSH SAHIFAGA — har qayerdan bosilsa ham asosiy menyuga qaytaradi
@router.message(F.text == "🚩 BOSH SAHIFAGA")
async def go_home(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("🚩 BOSH SAHIFAGA QAYTTINGIZ", reply_markup=get_game_menu())
    await state.set_state(GameSelection.waiting_for_game)


# 🔙 ORQAGA — agar foydalanuvchi hali o‘yin tanlamagan bo‘lsa, asosiy menyuga qaytadi
@router.message(F.text == "🔙 ORQAGA")
async def go_back(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == GameSelection.waiting_for_game:
        await state.clear()
        await message.answer("🚩 BOSH SAHIFAGA QAYTTINGIZ", reply_markup=get_game_menu())
        await state.set_state(GameSelection.waiting_for_game)
    # boshqa joylarda ishlatmoqchi bo‘lsang, boshqa `if`-larni qo‘shing
# O‘yin tanlash — bu tugmalardan birini tanlagan foydalanuvchiga mos formani boshlaydi
@router.message(StateFilter(GameSelection.waiting_for_game))
async def game_chosen(message: Message, state: FSMContext):

    game = message.text
    if game == "⚔️ CLASH OF CLANS":
        await message.answer(
"🏠 RATUSHA DARAJASINI KIRITING\n\n"
"❗️TO‘G‘RI YOZING. E'LONINGIZ SHUNGA BOG‘LIQ.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏡 6-TH\n"
"— 🏡 9-TH\n"
"— 🏡 12-TH\n"
"— 🏡 15-TH\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_clash_ratusha_menu())
        await state.set_state("ClashOfClansForm:ratusha")

    elif game == "💫 BRAWL STARS":
        await message.answer(
"🏆 KUBIKLAR SONINI KIRITING\n\n"
"❗️ILTIMOS, ANIQ SON KIRITILSIN. BU BILAN AKAUNTINGIZ QIYMATI BAHOLANADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🎲 3500 KUBIK\n"
"— 🎲 8000 KUBIK\n"
"— 🎲 12500 KUBIK\n\n"
"✅ FAQAT SON EMAS, 'KUBIK' SO‘ZINI HAM QO‘SHISHNI UNUTMANG!", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.kubik)

    elif game == "🔫 PUBG MOBILE":
        await message.answer(
"〽️ LVL DARAJASINI KIRITING\n\n"
"❗️ILTIMOS, ANIQ SON KIRITILSIN. BU BILAN AKAUNTINGIZ QIYMATI BAHOLANADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🎖️ 80-LVL\n"
"— 🎖️ 85-LVL\n"
"— 🎖️ 30-LVL\n\n"
"✅ FAQAT SON EMAS, 'LVL' SO‘ZINI HAM QO‘SHISHNI UNUTMANG!"
, reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.lvl)

    elif game == "⚽ EFOOTBALL":
        await message.answer(
"⚡️ SILANI KIRITING\n\n"
"❗️ILTIMOS, ANIQ SON KIRITILSIN. BU BILAN AKAUNTINGIZ QIYMATI BAHOLANADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— ⚔️ 1500 SILA\n"
"— ⚔️ 3200 SILA\n"
"— ⚔️ 4500 SILA\n\n"
"✅ FAQAT SON EMAS, 'SILA' SO‘ZINI HAM QO‘SHISHNI UNUTMANG!"
, reply_markup=get_back_menu())
        await state.set_state(EfootballForm.sila)

    else:
        await message.answer("❌ NOTOGRI OYIN TANLANDI", reply_markup=get_game_menu())

    # --- CLASH OF CLANS ---
    if current_state == ClashOfClansForm.ratusha:
        await message.answer("QAYSI O'YIN BO'YICHA E'LON BERMOQCHISIZ ❓", reply_markup=get_game_menu())
        await state.set_state(GameSelection.waiting_for_game)
    elif current_state == ClashOfClansForm.kubik:
        await message.answer("🏠 RATUSHA DARAJASINI KIRITING ✍️:", reply_markup=get_clash_ratusha_menu())
        await state.set_state(ClashOfClansForm.ratusha)
    elif current_state == ClashOfClansForm.skin:
        await message.answer("🏆 KUBIK DARAJASINI KIRITING:", reply_markup=get_clash_kubik_menu())
        await state.set_state(ClashOfClansForm.kubik)
    elif current_state == ClashOfClansForm.gold_pass:
        await message.answer("🦹 SKINLAR SONINI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.skin)
    elif current_state == ClashOfClansForm.obmen:
        await message.answer("🎫 GOLD PASS OLINGANMI:", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.gold_pass)
    elif current_state == ClashOfClansForm.qoshimcha:
        await message.answer("♻️ OBMEN BORMI:", reply_markup=get_yes_no_menu())
        await state.set_state(ClashOfClansForm.obmen)
    elif current_state == ClashOfClansForm.ulang:
        await message.answer("🔖 QO'SHIMCHA MA'LUMOT KIRITASIZMI (IXTIYORIY):", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.qoshimcha)
    elif current_state == ClashOfClansForm.narx:
        await message.answer("📧 ULANGAN SERVIS:", reply_markup=get_account_type_menu())
        await state.set_state(ClashOfClansForm.ulang)
    elif current_state == ClashOfClansForm.tolov:
        await message.answer("💸 NARXINI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.narx)
    elif current_state == ClashOfClansForm.manzil:
        await message.answer("💳 TOLOV TURINI KIRITING:", reply_markup=get_payment_menu())
        await state.set_state(ClashOfClansForm.tolov)
    elif current_state == ClashOfClansForm.telegram:
        await message.answer("🏠 MANZILINGIZNI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.manzil)
    elif current_state == ClashOfClansForm.nomer:
        await message.answer("📩 TELEGRAM USERNAMEYINGIZNI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.telegram)
    elif current_state == ClashOfClansForm.screenshots:
        await message.answer("📞 TELEFON RAQAMINGIZNI KIRITING (IXTIYORIY):", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.nomer)
    elif current_state == ClashOfClansForm.payment_screenshot:
        await message.answer("🖼 AKKAUNT RASMLARINI YUBORING:", reply_markup=get_back_menu())
        await state.set_state(ClashOfClansForm.screenshots)
    else:
        await state.clear()
        await message.answer("🚩 BOSH SAHIFAGAga QAYTTINGIZ", reply_markup=get_game_menu())
 # --- BRAWL STARS ---
    if current_state == BrawlStarsForm.kubik:
        await message.answer("🏆 KUBIKLAR SONINI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.brawler)
    elif current_state == BrawlStarsForm.brawler:
        await message.answer("🥷 BRAWLERLAR SONINI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.legendarni)
    elif current_state == BrawlStarsForm.legendarni:
        await message.answer("🏆 LEGENDAR BRAWLER NESHTA:", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.skin)
    elif current_state == BrawlStarsForm.skin:
        await message.answer("🦹 SKINLAR SONIN KIRITING:", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.brawl_pass)
    elif current_state == BrawlStarsForm.brawl_pass:
        await message.answer("🎫 BRAWL PASS OLINGANMI", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.obmen)
    elif current_state == BrawlStarsForm.obmen:
        await message.answer("♻️ OBMEN BORMI:", reply_markup=get_yes_no_menu())
        await state.set_state(BrawlStarsForm.qoshimcha)
    elif current_state == BrawlStarsForm.qoshimcha:
        await message.answer("🔖 QO‘SHIMCHA MA'LUMOT KIRITASIZMI (IXTIYORIY):", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.ulang)
    elif current_state == BrawlStarsForm.ulang:
        await message.answer("📧 ULANGAN SERVIS:", reply_markup=get_account_type_menu())
        await state.set_state(BrawlStarsForm.narx)
    elif current_state == BrawlStarsForm.narx:
        await message.answer("💸 NARXNI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.tolov)
    elif current_state == BrawlStarsForm.tolov:
        await message.answer("💳 TO‘LOV TURINI KIRITING:", reply_markup=get_payment_menu())
        await state.set_state(BrawlStarsForm.manzil)
    elif current_state == BrawlStarsForm.manzil:
        await message.answer("📩 TELEGRAM USERNAME:", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.telegram)
    elif current_state == BrawlStarsForm.telegram:
        await message.answer("📞 TELEFON RAQAMINGIZ (IXTIYORIY):", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.nomer)
    elif current_state == BrawlStarsForm.nomer:
        await message.answer("🖼 AKKAUNT RASMLARINI YUBORING:", reply_markup=get_back_menu())
        await state.set_state(BrawlStarsForm.screenshots)
    # --- PUBG MOBILE ---
    elif current_state == PubgMobileForm.lvl:
        await message.answer("〽️ LVL NI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.prokachka)
    elif current_state == PubgMobileForm.prokachka:
        await message.answer("🔫 PROKACHKA NI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.kilchat)
    elif current_state == PubgMobileForm.kilchat:
        await message.answer("🪄 KILCHATLARNI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.xsuit)
    elif current_state == PubgMobileForm.xsuit:
        await message.answer("🦹 X-SUIT BORMI:", reply_markup=get_yes_no_menu())
        await state.set_state(PubgMobileForm.ultimate)
    elif current_state == PubgMobileForm.ultimate:
        await message.answer("🧛 ULTIMATE BORMI:", reply_markup=get_yes_no_menu())
        await state.set_state(PubgMobileForm.mifik)
    elif current_state == PubgMobileForm.mifik:
        await message.answer("🥷 MIFIK BORMI:", reply_markup=get_yes_no_menu())
        await state.set_state(PubgMobileForm.sportcar)
    elif current_state == PubgMobileForm.sportcar:
        await message.answer("⚜️ ROYAL PASS OLINGANMI:", reply_markup=get_yes_no_menu())
        await state.set_state(PubgMobileForm.royal_pass)
    elif current_state == PubgMobileForm.royal_pass:
        await message.answer("🔖 QO‘SHIMCHA MA’LUMOT:", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.qoshimcha)
    elif current_state == PubgMobileForm.qoshimcha:
        await message.answer("♻️ OBMEN BORMI:", reply_markup=get_yes_no_menu())
        await state.set_state(PubgMobileForm.obmen)
    elif current_state == PubgMobileForm.obmen:
        await message.answer("📧 ULANGAN SERVIS:", reply_markup=get_account_type_menu())
        await state.set_state(PubgMobileForm.ulang)
    elif current_state == PubgMobileForm.ulang:
        await message.answer("💸 NARXINI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.narx)
    elif current_state == PubgMobileForm.narx:
        await message.answer("💳 TO‘LOV USULI:", reply_markup=get_payment_menu())
        await state.set_state(PubgMobileForm.tolov)
    elif current_state == PubgMobileForm.tolov:
        await message.answer("🏠 MANZILINGIZ:", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.manzil)
    elif current_state == PubgMobileForm.manzil:
        await message.answer("📩 TELEGRAM USERNAME:", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.telegram)
    elif current_state == PubgMobileForm.telegram:
        await message.answer("📞 TELEFON RAQAMINGIZ:", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.nomer)
    elif current_state == PubgMobileForm.nomer:
        await message.answer("🖼 AKKAUNT RASMLARINI YUBORING:", reply_markup=get_back_menu())
        await state.set_state(PubgMobileForm.screenshots)
    # --- EFOOTBALL ---
    elif current_state == EfootballForm.sila:
        await message.answer("⚡️ SILA NI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.epic)
    elif current_state == EfootballForm.epic:
        await message.answer("🦸‍♂️ EPIC BORMI:", reply_markup=get_yes_no_menu())
        await state.set_state(EfootballForm.coin)
    elif current_state == EfootballForm.coin:
        await message.answer("💰 COIN MIQDORINI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.qoshimcha)
    elif current_state == EfootballForm.qoshimcha:
        await message.answer("🔖 QO‘SHIMCHA MA’LUMOT:", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.obmen)
    elif current_state == EfootballForm.obmen:
        await message.answer("♻️ OBMEN BORMI:", reply_markup=get_yes_no_menu())
        await state.set_state(EfootballForm.ulang)
    elif current_state == EfootballForm.ulang:
        await message.answer("📧 ULANGAN SERVIS:", reply_markup=get_account_type_menu())
        await state.set_state(EfootballForm.narx)
    elif current_state == EfootballForm.narx:
        await message.answer("💸 NARXINI KIRITING:", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.tolov)
    elif current_state == EfootballForm.tolov:
        await message.answer("💳 TO‘LOV USULI:", reply_markup=get_payment_menu())
        await state.set_state(EfootballForm.manzil)
    elif current_state == EfootballForm.manzil:
        await message.answer("📩 TELEGRAM USERNAME:", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.telegram)
    elif current_state == EfootballForm.telegram:
        await message.answer("📞 TELEFON RAQAMINGIZ:", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.nomer)
    elif current_state == EfootballForm.nomer:
        await message.answer("🖼 AKKAUNT RASMLARINI YUBORING:", reply_markup=get_back_menu())
        await state.set_state(EfootballForm.screenshots)
# ROUTERLAR
# CLASH OF CLANS
@router.message(StateFilter(ClashOfClansForm.ratusha))
async def form_ratusha(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
        return
    valid_ratusha = ["🏡 6-TH", "🏡 7-TH", "🏡 8-TH", "🏡 9-TH", "🏡 10-TH",
                    "🏡 11-TH", "🏡 12-TH", "🏡 13-TH", "🏡 14-TH", 
                    "🏡 15-TH", "🏡 16-TH", "🏡 17-TH"]
    if message.text not in valid_ratusha:
        await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_clash_ratusha_menu())
        return
    await state.update_data(ratusha=message.text)
    await message.answer(
"🏆 KUBIK DARAJASINI KIRITING\n\n"
"❗️ILTIMOS, ANIQ SON KIRITILSIN. BU BILAN AKAUNTINGIZ QIYMATI BAHOLANADI.\n\n\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏅 MASTER\n"
"— 🏆 CHAEMPION\n"
"— 👑 LAGEND\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇"
, 
        reply_markup=get_clash_kubik_menu()
    )
    await state.set_state(ClashOfClansForm.kubik)
@router.message(StateFilter(ClashOfClansForm.kubik))
async def form_kubik(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
       return
    valid_kubik = ["🥉BRONZA", "🥈SILVER", "🥇GOLD", "💎CRAYSTAL", "🏅MASTER", "🏆CHAEMPION", "🪙TITAN", "👑LAGEND"]
    if message.text not in valid_kubik:
        await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_clash_kubik_menu())
        return
    await state.update_data(kubik=message.text)
    await message.answer(
"🦹 SKINLAR SONINI KIRITING\n\n"
"❗️E'LONINGIZ TO‘LIQ CHIQISHI UCHUN SKINLAR SONINI ANIQ KIRITING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🎭 LUCHNITSA 5 TA SKIN\n"
"— 🎭 XRANITEL 3 TA SKIN\n"
"— 🎭 KAROL 1 TA SKIN\n\n"
"✅ ILOJI BORICHA TO‘LIQ YOZING: 'GEROY NOMI + . TA SKIN' KO‘RINISHIDA!"
, 
        reply_markup=get_back_menu()
    )
    await state.set_state(ClashOfClansForm.skin)
@router.message(StateFilter(ClashOfClansForm.skin))
async def form_skin(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(skin=message.text)
   await message.answer(
"🎫 GOLD PASS SONINI KIRITING\n\n"
"❗️GOLD PASS — AKAUNT QIYMATIGA KATTA TA'SIR QILADI, SHUNING UCHUN UNI TO‘G‘RI KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏅 YOQ GOLD PASS\n"
"— 🏅 1 TA GOLD PASS\n"
"— 🏅 6 TA GOLD PASS\n\n"
"✅ ILOJI BORICHA TO‘LIQ YOZING: 'SON + TA GOLD PASS' KO‘RINISHIDA!",reply_markup=get_back_menu())
   await state.set_state(ClashOfClansForm.gold_pass)
@router.message(StateFilter(ClashOfClansForm.gold_pass))
async def form_gold_pass(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
      return
    await state.update_data(gold_pass=message.text)
    await message.answer(
"♻️ OBMEN BORMI?\n\n"
"❗️AGAR OBMEN (ALMASHTIRUV) MUMKIN BO‘LSA, QUYIDAGI SHAKLLARDAN BIRINI YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— ✅ HA, OBMEN BOR\n"
"— ❌ YO‘Q, FAQAT SOTILADI\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇"
,reply_markup=get_yes_no_menu())
    await state.set_state(ClashOfClansForm.obmen)
@router.message(StateFilter(ClashOfClansForm.obmen))
async def form_obmen(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
        return
    if message.text not in ["✅ HA", "❌ YO'Q"]:
        await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_yes_no_menu())
        return
    await state.update_data(obmen=message.text)
    await message.answer(
"🔖 QO‘SHIMCHA MA'LUMOT KIRITASIZMI?\n\n"
"❗️AGAR E'LONINGIZGA QO‘SHIMCHA TUSHUNTIRISH YOKI MUHIM MA'LUMOT QO‘SHMOQCHI BO‘LSANGIZ — BU YERGA YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📝 AKKAUNTDA QO‘SHIMCHA QAHRAMONLAR BOR\n"
"— 📝 OBMEN FAQAT MAXSUS SHAXSLARGA\n"
"— 📝 SOTILGANIDAN KEYIN QAYTARIB OLINMAYDI\n\n"
"✅ AGAR YO‘Q BO‘LSA, 'YO‘Q' DEB YUBORING!"
, 
        reply_markup=get_back_menu()
    )
    await state.set_state(ClashOfClansForm.qoshimcha)
@router.message(StateFilter(ClashOfClansForm.qoshimcha))
async def form_qoshimcha(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
        return
    await state.update_data(qoshimcha=message.text)
    await message.answer(
"📧 ULANGAN SERVISNI KIRITING\n\n"
"❗️BU BO‘LIMDA QANDAY SERVISLAR ULANGANINI KO‘RSATISHINGIZ ZARUR.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📱 SUPERCELL ID\n"
"— 🎮 GOOGLE PLAY\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇"
, 
        reply_markup=get_account_type_menu()
    )
    await state.set_state(ClashOfClansForm.ulang)
@router.message(ClashOfClansForm.ulang)
async def form_ulang(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
        return
    if message.text not in ["📱 SUPERCELL ID", "🎮 GOOGLE PLAY"]:
        await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_account_type_menu())
        return
    await state.update_data(ulang=message.text)
    await message.answer(
"💸 NARXINI KIRITING\n\n"
"❗️ILTIMOS, AKAUNT UCHUN QO‘YMOQCHI BO‘LGAN NARXNI TO‘LIQ YOZING.\n"
"SO‘MDA MIQDOR KO‘RSATILISHI SHART!\n\n"
"🔰 MISOL UCHUN:\n"
"— 💰 30 000 SO‘M\n"
"— 💰 75 000 SO‘M\n"
"— 💰 150 000 SO‘M\n\n"
"✅ AGAR BEPUL BO‘LSA, 'TEKIN' DEB YOZING!"
, reply_markup=get_back_menu())
    await state.set_state(ClashOfClansForm.narx)
@router.message(StateFilter(ClashOfClansForm.narx))
async def form_narx(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
        return
    await state.update_data(narx=message.text)
    await message.answer(
"💳 TO‘LOV TURINI KIRITING\n\n"
"❗️ILTIMOS, QABUL QILADIGAN TO‘LOV USULINI ANIQ KO‘RSATING. (BIR NECHTASINI HAM YAZSA BO‘LADI)\n\n"
"🔰 MISOL UCHUN:\n"
"— 💳 KARTA\n"
"— 💵 NAQD\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇"
,reply_markup=get_payment_menu())
    await state.set_state(ClashOfClansForm.tolov)
@router.message(StateFilter(ClashOfClansForm.tolov))
async def form_tolov(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
        return
    if message.text not in ["💳 KARTA", "💵 NAXT"]:
        await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_payment_menu())
        return
    await state.update_data(tolov=message.text)
    await message.answer(
 "🏠 MANZILINGIZNI KIRITING\n\n"
"❗️MANZIL — TO‘LOV YOKI UCHRASHUV UCHUN MUHIM BO‘LISHI MUMKIN. ILTIMOS, ANIQ YOKI UMUMIY MANZIL YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏘️ TOSHKENT SHAHRIDA\n"
"— 📍 ANDIJON VILOYATI, ASAKA\n"
"— 🗺️ FAQAT ONLINE SAVDO\n\n"
"✅ AGAR HOZIRCHA AHAMIYATLI BO‘LMASA, 'YO‘Q' DEB YOZISHINGIZ MUMKIN!"
, reply_markup=get_back_menu())
    await state.set_state(ClashOfClansForm.manzil)
@router.message(StateFilter(ClashOfClansForm.manzil))
async def form_manzil(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
        return
    
    await state.update_data(manzil=message.text)
    await message.answer(
"📩 TELEGRAM USERNAMEYINGIZNI KIRITING\n\n"
"❗️AGAR SOTUVCHI YOKI ADMIN SIZ BILAN BOG‘LANISHI KERAK BO‘LSA, USERNAME ORQALI ALOQA QILADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— @USERNAME\n"
"— @SAYYAXuz\n"
"— YO'Q\n\n"
"✅ AGAR USERNAME YO‘Q BO‘LSA 'YO‘Q' DEB YOZING!"
, 
        reply_markup=get_back_menu()
    )
    await state.set_state(ClashOfClansForm.telegram)
@router.message(StateFilter(ClashOfClansForm.telegram))
async def form_telegram(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
        return
    await state.update_data(telegram=message.text)
    await message.answer(
"📞 TELEFON RAQAMINGIZNI KIRITING\n\n"
"❗️AGAR USERNAME BO‘LMASA YOKI TELEFON ORQALI BOG‘LANISHNI HOHLASANGIZ, RAQAMINGIZNI TO‘LIQ KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— +998 90 XXX XX XX\n"
"— +998 99 XXX XX XX\n\n"
"✅ ILTIMOS, XALQARO FORMATDA YOZING: '+998' BILAN BOSHLANSIN!"
,reply_markup=get_back_menu())
    await state.set_state(ClashOfClansForm.nomer)
@router.message(StateFilter(ClashOfClansForm.nomer))
async def form_nomer(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
        return
    
    await state.update_data(nomer=message.text)
    await state.update_data(screenshots=[])  # Rasmlar ro'yxatini boshlash
    await message.answer(
        "📸 ILTIMOS, AKKAUNTINGIZNI RASMINI YUBORING (MAX 10 TA).\n"
        "HAMMASINI 1 TADA YUBORING MSOL 10 TASINI 1 TA QILIB. \n TUGAGACH '✅ RASMNI YUBORISH ' TUGMASINI BOSING.",
        reply_markup=get_finish_photos_menu()
    )
    await state.set_state(ClashOfClansForm.screenshots)
@router.message(StateFilter(ClashOfClansForm.screenshots), F.content_type == ContentType.PHOTO)
async def collect_screenshots(message: Message, state: FSMContext):
    data = await state.get_data()
    screenshots = data.get('screenshots', [])
    
    if len(screenshots) >= 10:
        await message.answer("❌ MAX 10 TA RASM YUKLASH MUMKUN!")
        return
    
    photo_id = message.photo[-1].file_id
    screenshots.append(photo_id)
    await state.update_data(screenshots=screenshots)
    await message.answer(f"✅ RASM QABUL QILINDI. JAMI: {len(screenshots)}/10")
@router.message(StateFilter(ClashOfClansForm.screenshots), F.text == "✅ RASMNI YUBORISH")
async def finish_screenshots(message: Message, state: FSMContext):
    data = await state.get_data()
    screenshots = data.get('screenshots', [])
    
    if not screenshots:
        await message.answer("❌ KAMIDA BITTA RASM YUKLASHINGIZ KERAK!")
        return
    
    payment_text = f"""
💳 <b>E'LON BERISH UCHUN TO‘LOV</b>

📥 <b>KARTA RAQAMI:</b> <code>{PAYMENT_CARD}</code>
👤 <b>KARTA EGASI:</b> <b>{PAYMENT_HOLDER}</b>
📱 <b>KARTAGA ULANGAN:</b> <b>{PAYMENTS_NUMBER}</b>
💰 <b>TO‘LOV MIQDORI:</b> <b>{PAYMENT_AMOUNT} SO‘M</b>

📋 <i>KARTA RAQAMINI NUSXA OLISH UCHUN USTIGA BOSING</i>

✅ <i>TO‘LOVNI AMALGA OSHIRGACH, CHEKNI YUBORING.</i>
"""
    
    await message.answer(payment_text,parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
    await message.answer("📃 <b>TO‘LOV CHEKINI (SKRINSHOTINI) YUBORING:</b>", parse_mode="HTML")
    await state.set_state(ClashOfClansForm.payment_screenshot)
@router.message(StateFilter(ClashOfClansForm.payment_screenshot), F.content_type == ContentType.PHOTO)
async def receive_payment_screenshot(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        payment_screenshot = message.photo[-1].file_id
        user_id = message.from_user.id
        username = message.from_user.username or "USERNAME YOQ"
        full_name = message.from_user.full_name
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        screenshots = data.get("screenshots", [])

        post_text = f"""
🇺🇿AKKAUNT SOTILADI💰 #A

🏠 RATUSHA:{data['ratusha']}
🏆 KUBIK:{data['kubik']}
🦹 SKIN:{data['skin']}
🎫 GOLD PASS:{data['gold_pass']}
🔖 QOSHIMCHA:{data['qoshimcha']}
♻️ OBMEN:{data['obmen']}

📧#ULANGAN:{data['ulang']}

💸#NARX:{data['narx']}
💳#TOLOV:{data['tolov']}
🏠#MANZIL:{data['manzil']}
❌ bekordan bekor bezovta qimelar
📩#TELEGRAM: {data['telegram']}
📞#NOMER: {data['nomer']}
➖➖➖➖➖➖➖➖➖➖➖➖➖
MASHKALARGA ALDANISHNI XOXLAMASANG ADMIN ORQALI SAVDO QIL..✔️
🤝SAVDO GURUH @SAVDO_GURUH_UZB
➖➖➖➖➖➖➖➖➖➖➖➖➖
🔰KANALIMIZ🌐
@CLASH_OF_CLANS_AKKAUNT_SAVDO_UZB


📄ELON UCHUN @SAYYAX_ELON
😎GARANT UCHUN @SAYYAX_GARANT
💎DANAT UCHUN @SAYYAX_DANAT"""

        payment_info = f"""
💳 <b>YANGI TO‘LOV MA'LUMOTI</b>

👤 <b>FOYDALANUVCHI:</b> <a href='tg://user?id={user_id}'>{full_name}</a>
🆔 <b>USER ID:</b> <code>{user_id}</code>
📱 <b>USERNAME:</b> @{username if username else 'USERNAME YO‘Q'}
⏰ <b>TO‘LOV VAQTI:</b> {current_time}
💰 <b>TO‘LOV MIQDORI:</b> <b>{PAYMENT_AMOUNT} SO‘M</b>
"""

        # Callback tugmalari
        admin_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Tastiqlash", callback_data=f"confirm_post_{user_id}_clash"),
                InlineKeyboardButton(text="❌ Bekor qilish", callback_data=f"cancel_post_{user_id}_clash")
            ]
        ])

        # Medialar
        media_group = [
            InputMediaPhoto(media=photo_id, caption=post_text if i == 0 else None)
            for i, photo_id in enumerate(screenshots)
        ]

        # Adminga yuborish
        await bot.send_media_group(chat_id=ADMIN_ID, media=media_group)
        await bot.send_photo(chat_id=ADMIN_ID, photo=payment_screenshot, caption=payment_info, reply_markup=admin_keyboard,parse_mode="HTML")

        # Callback uchun saqlash
        pending_posts[user_id] = {
            "post_text": post_text,
            "screenshots": screenshots
        }

        # Userga xabar
        await message.answer("✅ TOLOV CHEKI QABUL QILINDI VA ADMINGA YUBORILDI. TEZ ORADA JAVOB OLASIZ.", reply_markup=get_game_menu())
        await state.clear()
        await state.set_state(GameSelection.waiting_for_game)

    except Exception as e:
        await message.answer(f"❌ XATOLIK: {e}")

# BRAWL START
@router.message(BrawlStarsForm.kubik)
async def form_kubik(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(kubik=message.text)
   await message.answer(
"🥷 BRAWLERLAR SONINI KIRITING\n\n"
"❗️AKKAUNTDA NECHTA BRAWLER BORLIGINI KO‘RSATING. ILTIMOS, ANIQ SON KIRITING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 54 TA BRAWLER\n"
"— 62 TA BRAWLER\n"
"— 38 TA BRAWLER\n\n"
"✅ ILTIMOS, FAQAT SONINI VA 'TA' YOZING (MASALAN: 62 TA)"
, reply_markup=get_back_menu())
   await state.set_state(BrawlStarsForm.brawler)
@router.message(BrawlStarsForm.brawler)
async def form_brawler(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(brawler=message.text)
   await message.answer(
"🏆 LEGENDAR BRAWLERLAR SONINI KIRITING\n\n"
"❗️AKKAUNTDA NECHTA LEGENDARNY BRAWLER BORLIGINI KIRITING. ILTIMOS, FAQAT SON YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 1 TA LEGENDAR\n"
"— 3 TA LEGENDAR\n"
"— 5 TA LEGENDAR\n\n"
"✅ AGAR LEGENDARNY BRAWLER BO‘LMASA, '0' DEB YOZING!"
, reply_markup=get_back_menu())
   await state.set_state(BrawlStarsForm.legendarni)
@router.message(BrawlStarsForm.legendarni)
async def form_legendarni(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(legendarni=message.text)
   await message.answer(
"🦹 SKINLARNI KIRITING\n\n"
"❗️AKKAUNTDA MAVJUD SKINLARNI SANAB YOZING YOKI UMUMIY SONINI KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— GOLD MECHA BO, PHOENIX CROW, HEROINE BIBI\n"
"— 17 TA SKIN\n"
"— KO‘PCHILIGI RARE VA EPIC SKINLAR\n\n"
"✅ AGAR HECH QANDAY SKIN BO‘LMASA, 'YO‘Q' DEB YOZING!"
, reply_markup=get_back_menu())
   await state.set_state(BrawlStarsForm.skin)
@router.message(BrawlStarsForm.skin)
async def form_skin(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(skin=message.text)
   await message.answer(
"🎫 BRAWL PASS MA'LUMOTINI KIRITING\n\n"
"❗️AKKAUNTINGIZDA BRAWL PASS BORMI YOKI YO‘QLIGINI KO‘RSATING. ILTIMOS, ANIQ YOKI SODDA JAVOB YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— BOR\n"
"— YO‘Q\n"
"— OLDIN BOR EDI\n"
"— 5 MAROTABA OLGANMAN\n\n"
"✅ AGAR HECH QACHON OLMAGAN BO‘LSANGIZ, 'YO‘Q' DEB YOZING!"
, reply_markup=get_back_menu())
   await state.set_state(BrawlStarsForm.brawl_pass)
@router.message(BrawlStarsForm.brawl_pass)
async def form_brawl_pass(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(brawl_pass=message.text)
   await message.answer(
"♻️ OBMEN BORMI?\n\n"
"❗️AGAR OBMEN (ALMASHTIRUV) MUMKIN BO‘LSA, QUYIDAGI SHAKLLARDAN BIRINI YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— ✅ HA, OBMEN BOR\n"
"— ❌ YO‘Q, FAQAT SOTILADI\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_yes_no_menu())
   await state.set_state(BrawlStarsForm.obmen)
@router.message(BrawlStarsForm.obmen)
async def form_obmen(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   if message.text not in ["✅ HA", "❌ YO'Q"]:
    await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_yes_no_menu())
    return
   await state.update_data(obmen=message.text)
   await message.answer(
"🔖 QO‘SHIMCHA MA'LUMOT KIRITASIZMI?\n\n"
"❗️AGAR E'LONINGIZGA QO‘SHIMCHA TUSHUNTIRISH YOKI MUHIM MA'LUMOT QO‘SHMOQCHI BO‘LSANGIZ — BU YERGA YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📝 AKKAUNTDA QO‘SHIMCHA QAHRAMONLAR BOR\n"
"— 📝 OBMEN FAQAT MAXSUS SHAXSLARGA\n"
"— 📝 SOTILGANIDAN KEYIN QAYTARIB OLINMAYDI\n\n"
"✅ AGAR YO‘Q BO‘LSA, 'YO‘Q' DEB YUBORING!", reply_markup=get_back_menu())
   await state.set_state(BrawlStarsForm.qoshimcha)
@router.message(BrawlStarsForm.qoshimcha)
async def form_qoshimcha(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(qoshimcha=message.text)
   await message.answer(
"📧 ULANGAN SERVISNI KIRITING\n\n"
"❗️BU BO‘LIMDA QANDAY SERVISLAR ULANGANINI KO‘RSATISHINGIZ ZARUR.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📱 SUPERCELL ID\n"
"— 🎮 GOOGLE PLAY\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_account_type_menu())
   await state.set_state(BrawlStarsForm.ulang)
@router.message(BrawlStarsForm.ulang)
async def form_ulang(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   if message.text not in ["📱 SUPERCELL ID", "🎮 GOOGLE PLAY"]:
    await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_account_type_menu())
    return
   await state.update_data(ulang=message.text)
   await message.answer(
"💸 NARXINI KIRITING\n\n"
"❗️ILTIMOS, AKAUNT UCHUN QO‘YMOQCHI BO‘LGAN NARXNI TO‘LIQ YOZING.\n"
"SO‘MDA MIQDOR KO‘RSATILISHI SHART!\n\n"
"🔰 MISOL UCHUN:\n"
"— 💰 30 000 SO‘M\n"
"— 💰 75 000 SO‘M\n"
"— 💰 150 000 SO‘M\n\n"
"✅ AGAR BEPUL BO‘LSA, 'TEKIN' DEB YOZING!", reply_markup=get_back_menu())
   await state.set_state(BrawlStarsForm.narx)
@router.message(BrawlStarsForm.narx)
async def form_narx(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(narx=message.text)
   await message.answer(
"💳 TO‘LOV TURINI KIRITING\n\n"
"❗️ILTIMOS, QABUL QILADIGAN TO‘LOV USULINI ANIQ KO‘RSATING. (BIR NECHTASINI HAM YAZSA BO‘LADI)\n\n"
"🔰 MISOL UCHUN:\n"
"— 💳 KARTA\n"
"— 💵 NAQD\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_payment_menu())
   await state.set_state(BrawlStarsForm.tolov)
@router.message(BrawlStarsForm.tolov)
async def form_tolov(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   if message.text not in ["💳 KARTA", "💵 NAXT"]:
    await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_payment_menu())
    return
   await state.update_data(tolov=message.text)
   await message.answer(
"🏠 MANZILINGIZNI KIRITING\n\n"
"❗️MANZIL — TO‘LOV YOKI UCHRASHUV UCHUN MUHIM BO‘LISHI MUMKIN. ILTIMOS, ANIQ YOKI UMUMIY MANZIL YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏘️ TOSHKENT SHAHRIDA\n"
"— 📍 ANDIJON VILOYATI, ASAKA\n"
"— 🗺️ FAQAT ONLINE SAVDO\n\n"
"✅ AGAR HOZIRCHA AHAMIYATLI BO‘LMASA, 'YO‘Q' DEB YOZISHINGIZ MUMKIN!", reply_markup=get_back_menu())
   await state.set_state(BrawlStarsForm.manzil)
@router.message(BrawlStarsForm.manzil)
async def form_manzil(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(manzil=message.text)
   await message.answer(
"📩 TELEGRAM USERNAMEYINGIZNI KIRITING\n\n"
"❗️AGAR SOTUVCHI YOKI ADMIN SIZ BILAN BOG‘LANISHI KERAK BO‘LSA, USERNAME ORQALI ALOQA QILADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— @USERNAME\n"
"— @SAYYAXuz\n"
"— YO'Q\n\n"
"✅ AGAR USERNAME YO‘Q BO‘LSA 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
   await state.set_state(BrawlStarsForm.telegram)
@router.message(BrawlStarsForm.telegram)
async def form_telegram(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(telegram=message.text)
   await message.answer(
"📞 TELEFON RAQAMINGIZNI KIRITING\n\n"
"❗️AGAR USERNAME BO‘LMASA YOKI TELEFON ORQALI BOG‘LANISHNI HOHLASANGIZ, RAQAMINGIZNI TO‘LIQ KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— +998 90 XXX XX XX\n"
"— +998 99 XXX XX XX\n\n"
"✅ ILTIMOS, XALQARO FORMATDA YOZING: '+998' BILAN BOSHLANSIN!", reply_markup=get_back_menu())
   await state.set_state(BrawlStarsForm.nomer)
@router.message(BrawlStarsForm.nomer)
async def form_nomer(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(nomer=message.text, screenshots=[])
   await message.answer("📸 ILTIMOS, AKKAUNTINGIZNI RASMINI YUBORING (MAX 10 ta).\n'Tugagach ✅ RASMNI YUBORISH' tugmasini bosing.", reply_markup=get_finish_photos_menu())
   await state.set_state(BrawlStarsForm.screenshots)
@router.message(F.photo, BrawlStarsForm.screenshots)
async def collect_screenshots(message: Message, state: FSMContext):
   data = await state.get_data()
   screenshots = data.get('screenshots', [])
   if len(screenshots) >= 10:
    await message.answer("❌ MAX 10 TA RASM YUKLASH MUMKUN!")
    return
   photo_id = message.photo[-1].file_id
   screenshots.append(photo_id)
   await state.update_data(screenshots=screenshots)
   await message.answer(f"✅ RASM QABUL QILINDI. JAMI: {len(screenshots)}/10")
@router.message(F.text == "✅ RASMNI YUBORISH", BrawlStarsForm.screenshots)
async def finish_screenshots(message: Message, state: FSMContext):
   data = await state.get_data()
   screenshots = data.get('screenshots', [])
   if not screenshots:
    await message.answer("❌ KAMIDA BITTA RASM YUKLASHINGIZ KERAK!")
    return

   payment_text = f"""
💳 <b>E'LON BERISH UCHUN TO‘LOV</b>

📥 <b>KARTA RAQAMI:</b> <code>{PAYMENT_CARD}</code>
👤 <b>KARTA EGASI:</b> <b>{PAYMENT_HOLDER}</b>
📱 <b>KARTAGA ULANGAN:</b> <b>{PAYMENTS_NUMBER}</b>
💰 <b>TO‘LOV MIQDORI:</b> <b>{PAYMENT_AMOUNT} SO‘M</b>

📋 <i>KARTA RAQAMINI NUSXA OLISH UCHUN USTIGA BOSING</i>

✅ <i>TO‘LOVNI AMALGA OSHIRGACH, CHEKNI YUBORING.</i>
"""
   await message.answer(payment_text,parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
   await message.answer("📃 <b>TO‘LOV CHEKINI (SKRINSHOTINI) YUBORING:</b>", parse_mode="HTML")
   await state.set_state(BrawlStarsForm.payment_screenshot)
@router.message(F.photo, BrawlStarsForm.payment_screenshot)
async def receive_payment_screenshot(message: Message, state: FSMContext):
   data = await state.get_data()
   payment_screenshot = message.photo[-1].file_id
   user_id = message.from_user.id
   username = message.from_user.username or "USERNAME YOQ"
   full_name = message.from_user.full_name
   current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

   post_text = f"""
🇺🇿AKKAUNT SOTILADI💰#B
🏆 KUBIK:{data['kubik']}
🥷 BRAWLER:{data['brawler']}
🦹 SKIN:{data['skin']}
🌟 LEGENDARNI:{data['legendarni']}
🎫 BRWAL PASS:{data['brawl_pass']}
🔖 QOSHIMCHA:{data['qoshimcha']}
♻️ OBMEN:{data['obmen']}

📧#ULANGAN:{data['ulang']}

💸#NARXI:{data['narx']}
💳#TOLOV:{data['tolov']}
🏠#MANZIL:{data['manzil']}
❌ bekordan bekor bezovta qimelar
📩#TELEGRAM:{data['telegram']}
📞#NOMER:{data['nomer']}
➖➖➖➖➖➖➖➖➖➖➖➖➖
MASHKALARGA ALDANISHNI XOXLAMASANG ADMIN ORQALI SAVDO QIL..✔️
🤝SAVDO GURUH @SAVDO_GURUH_UZB
➖➖➖➖➖➖➖➖➖➖➖➖➖
🔰KANALIMIZ🌐
@BRAWL_STARS_AKKAUNT_SAVDO_UZB


📄ELON UCHUN @SAYYAX_ELON
😎GARANT UCHUN @SAYYAX_GARANT
💎DANAT UCHUN @SAYYAX_DANAT"""

   payment_info = f"""
💳 <b>YANGI TO‘LOV MA'LUMOTI</b>

👤 <b>FOYDALANUVCHI:</b> <a href='tg://user?id={user_id}'>{full_name}</a>
🆔 <b>USER ID:</b> <code>{user_id}</code>
📱 <b>USERNAME:</b> @{username if username else 'USERNAME YO‘Q'}
⏰ <b>TO‘LOV VAQTI:</b> {current_time}
💰 <b>TO‘LOV MIQDORI:</b> <b>{PAYMENT_AMOUNT} SO‘M</b>
"""

   admin_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Tastiqlash", callback_data=f"confirm_post_{user_id}_brawl"),
            InlineKeyboardButton(text="❌ Bekor qilish", callback_data=f"cancel_post_{user_id}_brawl")
        ]
    ])

   media_group = [InputMediaPhoto(media=p, caption=post_text if i == 0 else None) for i, p in enumerate(data['screenshots'])]

   await bot.send_media_group(chat_id=ADMIN_ID, media=media_group)
   await bot.send_photo(chat_id=ADMIN_ID, photo=payment_screenshot, caption=payment_info, reply_markup=admin_keyboard,parse_mode="HTML")

   pending_posts[user_id] = {'post_text': post_text, 'screenshots': data['screenshots']}
   await message.answer("✅ TOLOV CHEKINI VA E'LON ADMINGA YUBORILDI. TEZ ORADA JAVOB OLASIZ.", reply_markup=get_game_menu())
   await state.clear()
   await state.set_state(GameSelection.waiting_for_game)
# PUBG MOBILE
@router.message(PubgMobileForm.lvl)
async def form_lvl(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(lvl=message.text)
   await message.answer(
"🔫 PROKACHKALARNI KIRITING\n\n"
"❗️PUBG AKKAUNTINGIZDA QANCHA PROKACHKA (YA’NI KO‘TARILGAN SKINLAR, LEVELLI QUROLLAR, UC-ORQALI OCHILGAN NARSA) BORLIGINI KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— M416 MAX\n"
"— DP28 4-DARAJA\n"
"— 3 TA PROKACHKA BOR\n"
"— YO‘Q\n\n"
"✅ AGAR HECH QANDAY PROKACHKA BO‘LMASA, 'YO‘Q' DEB YOZING!"

, reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.prokachka)
@router.message(PubgMobileForm.prokachka)
async def form_prokachka(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(prokachka=message.text)
   await message.answer(
"🪄 KILCHAT BO‘LGANLAR SONINI KIRITING\n\n"
"❗️AKKAUNTINGIZDA NECHTA BRAWLER TO‘LIQ KILCHAT (YA’NI MAKSIMAL DARAJADA OCHILGAN) EKANINI KO‘RSATING. ILTIMOS, SONDA YOZING YOKI QISQACHA TUSHUNTIRING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 7 TA KILCHAT\n"
"— HAMMASI KILCHAT QILINGAN\n"
"— YO'Q\n\n"
"✅ AGAR HECH QANDAY KILCHAT BO‘LMASA, '0' DEB YOZING YOKI 'YO‘Q' DEB BELGILANG!"
, reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.kilchat)
@router.message(PubgMobileForm.kilchat)
async def form_kilchat(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(kilchat=message.text)
   await message.answer(
"🦹 X-SUITLAR SONINI KIRITING\n\n"
"❗️PUBG AKKAUNTINGIZDA NECHTA X-SUIT (YA’NI MAXSUS EFFEKTLI KOSTYUMLAR) BORLIGINI KO‘RSATING. ILTIMOS, FAQAT SON YOZING YOKI NOMLARINI SANAB CHIQING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 2 TA X-SUIT\n"
"— PHARAOH VA MECHA X-SUIT\n"
"— YO'Q\n\n"
"✅ AGAR HECH QANDAY X-SUIT BO‘LMASA, '0' YOKI 'YO‘Q' DEB YOZING!"
, reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.xsuit)
@router.message(PubgMobileForm.xsuit)
async def form_xsuit(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(xsuit=message.text)
   await message.answer(
"🧛 ULTIMATELAR SONINI KIRITING\n\n"
"❗️AKKAUNTINGIZDA NECHTA ULTIMATE KO‘RINISH (YA’NI ENG QIMMAT VA EFFEKTI BOR KOSTYUMLAR) BORLIGINI YOZING. ILTIMOS, SONDA YOKI NOMLARDA KIRITING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 1 TA ULTIMATE\n"
"— 3 TA BOR: BLOOD RAVEN, INFERNO RIDER, SILVER TITAN\n"
"— YO‘Q\n\n"
"✅ AGAR HECH QANDAY ULTIMATE BO‘LMASA, '0' YOKI 'YO‘Q' DEB YOZING!"
, reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.ultimate)
@router.message(PubgMobileForm.ultimate)
async def form_ultimate(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(ultimate=message.text)
   await message.answer(
"🥷 MIFIKLAR SONINI KIRITING\n\n"
"❗️PUBG AKKAUNTINGIZDA NECHTA MIFIK KO‘RINISH (YA’NI QIZIL RAMKALI KOSTYUMLAR, QIMMAT SKINLAR) BORLIGINI KO‘RSATING. ILTIMOS, SONDA YOKI NOMLARDA YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 7 TA MIFIK\n"
"— 3 TA: BLOOD RAVEN, CYCLOPS, FLAME LORD\n"
"— YO‘Q\n\n"
"✅ AGAR MIFIK YO‘Q BO‘LSA, '0' YOKI 'YO‘Q' DEB YOZING!"
, reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.mifik)
@router.message(PubgMobileForm.mifik)
async def form_mifik(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(mifik=message.text)
   await message.answer(
"🏎 SPORTCARLAR SONINI KIRITING\n\n"
"❗️PUBG AKKAUNTINGIZDA NECHTA SPORTCAR (YA’NI TESLA, KOENIGSEGG, BUGATTI, LAMBORGHINI KABI MAXSUS MASHINALAR) BORLIGINI YOZING. ILTIMOS, SONDA YOKI NOMLARDA KIRITING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 2 TA SPORTCAR\n"
"— TESLA MODEL Y VA KOENIGSEGG BOR\n"
"— YO‘Q\n\n"
"✅ AGAR SPORTCAR BO‘LMASA, '0' YOKI 'YO‘Q' DEB YOZING!"
, reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.sportcar)
@router.message(PubgMobileForm.sportcar)
async def form_sportcar(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(sportcar=message.text)
   await message.answer(
"⚜️ ROYAL PASSLAR SONINI KIRITING\n\n"
"❗️PUBG AKKAUNTINGIZDA NECHTA ROYAL PASS OLGANLIGINGIZNI KO‘RSATING. ILTIMOS, SONDA YOKI QISQACHA TUSHUNTIRIB YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 5 TA ROYAL PASS\n"
"— 10-MAVSUMDAN 25-GACHA BOR\n"
"— YO'Q\n\n"
"✅ AGAR HECH QACHON ROYAL PASS OLMAGAN BO‘LSANGIZ, '0' YOKI 'YO‘Q' DEB YOZING!"
, reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.royal_pass)
@router.message(PubgMobileForm.royal_pass)
async def form_royal_pass(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(royal_pass=message.text)
   await message.answer(
"♻️ OBMEN BORMI?\n\n"
"❗️AGAR OBMEN (ALMASHTIRUV) MUMKIN BO‘LSA, QUYIDAGI SHAKLLARDAN BIRINI YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— ✅ HA, OBMEN BOR\n"
"— ❌ YO‘Q, FAQAT SOTILADI\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_yes_no_menu())
   await state.set_state(PubgMobileForm.obmen)
@router.message(PubgMobileForm.obmen)
async def form_obmen(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   if message.text not in ["✅ HA", "❌ YO'Q"]:
    await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_yes_no_menu())
    return
   await state.update_data(obmen=message.text)
   await message.answer(
"🔖 QO‘SHIMCHA MA'LUMOT KIRITASIZMI?\n\n"
"❗️AGAR E'LONINGIZGA QO‘SHIMCHA TUSHUNTIRISH YOKI MUHIM MA'LUMOT QO‘SHMOQCHI BO‘LSANGIZ — BU YERGA YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📝 AKKAUNTDA QO‘SHIMCHA QAHRAMONLAR BOR\n"
"— 📝 OBMEN FAQAT MAXSUS SHAXSLARGA\n"
"— 📝 SOTILGANIDAN KEYIN QAYTARIB OLINMAYDI\n\n"
"✅ AGAR YO‘Q BO‘LSA, 'YO‘Q' DEB YUBORING!", reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.qoshimcha)
@router.message(PubgMobileForm.qoshimcha)
async def form_qoshimcha(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(qoshimcha=message.text)
   await message.answer("📧 ULANGAN SERVISNI KIRITING\n\n"
"❗️BU BO‘LIMDA QANDAY SERVISLAR ULANGANINI KO‘RSATISHINGIZ ZARUR.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📱 POCHTA\n"
"— 🎮 GOOGLE PLAY\n"
"— YO'Q\n\n"
"✅ AGAR HECH QANDAY ULANGAN SERVER BO‘LMASA, '0' YOKI 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.ulang)
@router.message(PubgMobileForm.ulang)
async def form_ulang(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(ulang=message.text)
   await message.answer(
"💸 NARXINI KIRITING\n\n"
"❗️ILTIMOS, AKAUNT UCHUN QO‘YMOQCHI BO‘LGAN NARXNI TO‘LIQ YOZING.\n"
"SO‘MDA MIQDOR KO‘RSATILISHI SHART!\n\n"
"🔰 MISOL UCHUN:\n"
"— 💰 30 000 SO‘M\n"
"— 💰 75 000 SO‘M\n"
"— 💰 150 000 SO‘M\n\n"
"✅ AGAR BEPUL BO‘LSA, 'TEKIN' DEB YOZING!", reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.narx)
@router.message(PubgMobileForm.narx)
async def form_narx(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(narx=message.text)
   await message.answer("💳 TO‘LOV TURINI KIRITING\n\n"
"❗️ILTIMOS, QABUL QILADIGAN TO‘LOV USULINI ANIQ KO‘RSATING. (BIR NECHTASINI HAM YAZSA BO‘LADI)\n\n"
"🔰 MISOL UCHUN:\n"
"— 💳 KARTA\n"
"— 💵 NAQD\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_payment_menu())
   await state.set_state(PubgMobileForm.tolov)
@router.message(PubgMobileForm.tolov)
async def form_tolov(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   if message.text not in ["💳 KARTA", "💵 NAXT"]:
    await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_payment_menu())
    return
   await state.update_data(tolov=message.text)
   await message.answer(
"🏠 MANZILINGIZNI KIRITING\n\n"
"❗️MANZIL — TO‘LOV YOKI UCHRASHUV UCHUN MUHIM BO‘LISHI MUMKIN. ILTIMOS, ANIQ YOKI UMUMIY MANZIL YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏘️ TOSHKENT SHAHRIDA\n"
"— 📍 ANDIJON VILOYATI, ASAKA\n"
"— 🗺️ FAQAT ONLINE SAVDO\n\n"
"✅ AGAR HOZIRCHA AHAMIYATLI BO‘LMASA, 'YO‘Q' DEB YOZISHINGIZ MUMKIN!", reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.manzil)
@router.message(PubgMobileForm.manzil)
async def form_manzil(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(manzil=message.text)
   await message.answer(
"📩 TELEGRAM USERNAMEYINGIZNI KIRITING\n\n"
"❗️AGAR SOTUVCHI YOKI ADMIN SIZ BILAN BOG‘LANISHI KERAK BO‘LSA, USERNAME ORQALI ALOQA QILADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— @USERNAME\n"
"— @SAYYAXuz\n"
"— YO'Q\n\n"
"✅ AGAR USERNAME YO‘Q BO‘LSA 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.telegram)
@router.message(PubgMobileForm.telegram)
async def form_telegram(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(telegram=message.text)
   await message.answer(
"📞 TELEFON RAQAMINGIZNI KIRITING\n\n"
"❗️AGAR USERNAME BO‘LMASA YOKI TELEFON ORQALI BOG‘LANISHNI HOHLASANGIZ, RAQAMINGIZNI TO‘LIQ KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— +998 90 XXX XX XX\n"
"— +998 99 XXX XX XX\n\n"
"✅ ILTIMOS, XALQARO FORMATDA YOZING: '+998' BILAN BOSHLANSIN!", reply_markup=get_back_menu())
   await state.set_state(PubgMobileForm.nomer)
@router.message(StateFilter(PubgMobileForm.nomer))
async def form_nomer(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
        return
    
    await state.update_data(nomer=message.text)
    await state.update_data(screenshots=[])  # Rasmlar ro'yxatini boshlash
    await message.answer(
        "📸 ILTIMOS, AKKAUNTINGIZNI RASMINI YUBORING (MAX 10 TA).\n"
        "HAMMASINI 1 TADA YUBORING MSOL 10 TASINI 1 TA QILIB. \n TUGAGACH '✅ RASMNI YUBORISH ' TUGMASINI BOSING.",
        reply_markup=get_finish_photos_menu()
    )
    await state.set_state(PubgMobileForm.screenshots)
@router.message(StateFilter(PubgMobileForm.screenshots), F.content_type == ContentType.PHOTO)
async def collect_screenshots(message: Message, state: FSMContext):
    data = await state.get_data()
    screenshots = data.get('screenshots', [])
    
    if len(screenshots) >= 10:
        await message.answer("❌ MAX 10 TA RASM YUKLASH MUMKUN!")
        return
    
    photo_id = message.photo[-1].file_id
    screenshots.append(photo_id)
    await state.update_data(screenshots=screenshots)
    await message.answer(f"✅ RASM QABUL QILINDI. JAMI: {len(screenshots)}/10")
@router.message(StateFilter(PubgMobileForm.screenshots), F.text == "✅ RASMNI YUBORISH")
async def finish_screenshots(message: Message, state: FSMContext):
    data = await state.get_data()
    screenshots = data.get('screenshots', [])
    
    if not screenshots:
        await message.answer("❌ KAMIDA BITTA RASM YUKLASHINGIZ KERAK!")
        return
    
    payment_text = f"""
💳 <b>E'LON BERISH UCHUN TO‘LOV</b>

📥 <b>KARTA RAQAMI:</b> <code>{PAYMENT_CARD}</code>
👤 <b>KARTA EGASI:</b> <b>{PAYMENT_HOLDER}</b>
📱 <b>KARTAGA ULANGAN:</b> <b>{PAYMENTS_NUMBER}</b>
💰 <b>TO‘LOV MIQDORI:</b> <b>{PAYMENT_AMOUNT} SO‘M</b>

📋 <i>KARTA RAQAMINI NUSXA OLISH UCHUN USTIGA BOSING</i>

✅ <i>TO‘LOVNI AMALGA OSHIRGACH, CHEKNI YUBORING.</i>
"""
    
    await message.answer(payment_text,parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
    await message.answer("📃 <b>TO‘LOV CHEKINI (SKRINSHOTINI) YUBORING:</b>", parse_mode="HTML")
    await state.set_state(PubgMobileForm.payment_screenshot)
@router.message(StateFilter(PubgMobileForm.payment_screenshot), F.content_type == ContentType.PHOTO)
async def receive_payment_screenshot(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        payment_screenshot = message.photo[-1].file_id
        user_id = message.from_user.id
        username = message.from_user.username or "USERNAME YOQ"
        full_name = message.from_user.full_name
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        screenshots = data.get("screenshots", [])

        post_text = f"""
🇺🇿AKKAUNT SOTILADI💰 #D

〽️ LVL:{data['lvl']}
🔫 PROKACHKA:{data['prokachka']}
🪄 KILCHAT:{data['kilchat']}
🦹 X-SUIT:{data['xsuit']}
🧛 ULTIMATE:{data['ultimate']}
🥷 MIFIK:{data['mifik']}
🏎 SPORTCAR:{data['sportcar']}
⚜️ ROYAL PASS:{data['royal_pass']}
🔖 QOSHIMCHA:{data['qoshimcha']}
♻️ OBMEN:{data['obmen']}

📧#ULANGAN:{data['ulang']}

💸#NARX:{data['narx']}
💳#TOLOV:{data['tolov']}
🏠#MANZIL:{data['manzil']}
📩#TELEGRAM:{data['telegram']}
📞#NOMER:{data['nomer']}
➖➖➖➖➖➖➖➖➖➖➖➖➖
MASHKALARGA ALDANISHNI XOXLAMASANG ADMIN ORQALI SAVDO QIL..✔️
🤝 SAVDO GURUH @SAVDO_GURUH_UZB
➖➖➖➖➖➖➖➖➖➖➖➖➖
🔰KANALIMIZ🌐
@PUBG_MOBILE_AKKAUNT_SAVDO_UZ


📄ELON UCHUN @SAYYAX_ELON
😎GARANT UCHUN @SAYYAX_GARANT
💎DANAT UCHUN @SAYYAX_DANAT"""

        payment_info = f"""
💳 <b>YANGI TO‘LOV MA'LUMOTI</b>

👤 <b>FOYDALANUVCHI:</b> <a href='tg://user?id={user_id}'>{full_name}</a>
🆔 <b>USER ID:</b> <code>{user_id}</code>
📱 <b>USERNAME:</b> @{username if username else 'USERNAME YO‘Q'}
⏰ <b>TO‘LOV VAQTI:</b> {current_time}
💰 <b>TO‘LOV MIQDORI:</b> <b>{PAYMENT_AMOUNT} SO‘M</b>
"""

        # Callback tugmalari
        admin_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Tastiqlash", callback_data=f"confirm_post_{user_id}_pubg"),
                InlineKeyboardButton(text="❌ Bekor qilish", callback_data=f"cancel_post_{user_id}_pubg")
            ]
        ])

        # Medialar
        media_group = [
            InputMediaPhoto(media=photo_id, caption=post_text if i == 0 else None)
            for i, photo_id in enumerate(screenshots)
        ]

        # Adminga yuborish
        await bot.send_media_group(chat_id=ADMIN_ID, media=media_group)
        await bot.send_photo(chat_id=ADMIN_ID, photo=payment_screenshot, caption=payment_info, reply_markup=admin_keyboard,parse_mode="HTML")

        # Callback uchun saqlash
        pending_posts[user_id] = {
            "post_text": post_text,
            "screenshots": screenshots
        }

        # Userga xabar
        await message.answer("✅ TOLOV CHEKI QABUL QILINDI VA ADMINGA YUBORILDI. TEZ ORADA JAVOB OLASIZ.", reply_markup=get_game_menu())
        await state.clear()
        await state.set_state(GameSelection.waiting_for_game)

    except Exception as e:
        await message.answer(f"❌ XATOLIK: {e}")

# EFOOTBALL
@router.message(EfootballForm.sila)
async def form_sila(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(sila=message.text)
   await message.answer(
"🦸‍♂️ EPICLAR SONINI KIRITING\n\n"
"❗️EFOOTBALL AKKAUNTINGIZDA NECHTA EPIC O‘YINCHI BORLIGINI KO‘RSATING. ILTIMOS, FAQAT SON YOKI NOMLARDA KIRITING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 4 TA EPIC\n"
"— EPIC: MESSI, BECKHAM, BATISTUTA, ZANETTI\n"
"— EPIC YO‘Q\n\n"
"✅ AGAR HECH QANDAY EPIC BO‘LMASA, '0' YOKI 'YO‘Q' DEB YOZING!"
, reply_markup=get_back_menu())
   await state.set_state(EfootballForm.epic)
@router.message(EfootballForm.epic)
async def form_epic(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(epic=message.text)
   await message.answer(
"💰 COIN MIQDORINI KIRITING\n\n"
"❗️EFOOTBALL AKKAUNTINGIZDA HOZIRDA NECHTA COIN BORLIGINI YOZING. ILTIMOS, FAQAT SON KIRITING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 500 COIN\n"
"— 1250 TA\n"
"— 0 COIN\n\n"
"✅ AGAR COIN BO‘LMASA, '0' YOKI 'YO‘Q' DEB YOZING!"
, reply_markup=get_back_menu())
   await state.set_state(EfootballForm.coin)
@router.message(EfootballForm.coin)
async def form_coin(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(coin=message.text)
   await message.answer(
"♻️ OBMEN BORMI?\n\n"
"❗️AGAR OBMEN (ALMASHTIRUV) MUMKIN BO‘LSA, QUYIDAGI SHAKLLARDAN BIRINI YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— ✅ HA, OBMEN BOR\n"
"— ❌ YO‘Q, FAQAT SOTILADI\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_yes_no_menu())
   await state.set_state(EfootballForm.obmen)
@router.message(EfootballForm.obmen)
async def form_obmen(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   if message.text not in ["✅ HA", "❌ YO'Q"]:
    await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_yes_no_menu())
    return
   await state.update_data(obmen=message.text)
   await message.answer(
"🔖 QO‘SHIMCHA MA'LUMOT KIRITASIZMI?\n\n"
"❗️AGAR E'LONINGIZGA QO‘SHIMCHA TUSHUNTIRISH YOKI MUHIM MA'LUMOT QO‘SHMOQCHI BO‘LSANGIZ — BU YERGA YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📝 AKKAUNTDA QO‘SHIMCHA QAHRAMONLAR BOR\n"
"— 📝 OBMEN FAQAT MAXSUS SHAXSLARGA\n"
"— 📝 SOTILGANIDAN KEYIN QAYTARIB OLINMAYDI\n\n"
"✅ AGAR YO‘Q BO‘LSA, 'YO‘Q' DEB YUBORING!", reply_markup=get_back_menu())
   await state.set_state(EfootballForm.qoshimcha)
@router.message(EfootballForm.qoshimcha)
async def form_qoshimcha(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(qoshimcha=message.text)
   await message.answer(
"📧 ULANGAN SERVISNI KIRITING\n\n"
"❗️BU BO‘LIMDA QANDAY SERVISLAR ULANGANINI KO‘RSATISHINGIZ ZARUR.\n\n"
"🔰 MISOL UCHUN:\n"
"— 📱 KONAMI ID\n"
"— 🎮 GOOGLE PLAY\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_account_type_menu2())
   await state.set_state(EfootballForm.ulang)
@router.message(EfootballForm.ulang)
async def form_ulang(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   if message.text not in ["📱 KONAMI ID", "🎮 GOOGLE PLAY"]:
    await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_account_type_menu2())
    return
   await state.update_data(ulang=message.text)
   await message.answer(
"💸 NARXINI KIRITING\n\n"
"❗️ILTIMOS, AKAUNT UCHUN QO‘YMOQCHI BO‘LGAN NARXNI TO‘LIQ YOZING.\n"
"SO‘MDA MIQDOR KO‘RSATILISHI SHART!\n\n"
"🔰 MISOL UCHUN:\n"
"— 💰 30 000 SO‘M\n"
"— 💰 75 000 SO‘M\n"
"— 💰 150 000 SO‘M\n\n"
"✅ AGAR BEPUL BO‘LSA, 'TEKIN' DEB YOZING!", reply_markup=get_back_menu())
   await state.set_state(EfootballForm.narx)
@router.message(EfootballForm.narx)
async def form_narx(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(narx=message.text)
   await message.answer(
"💳 TO‘LOV TURINI KIRITING\n\n"
"❗️ILTIMOS, QABUL QILADIGAN TO‘LOV USULINI ANIQ KO‘RSATING. (BIR NECHTASINI HAM YAZSA BO‘LADI)\n\n"
"🔰 MISOL UCHUN:\n"
"— 💳 KARTA\n"
"— 💵 NAQD\n\n"
"⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_payment_menu())
   await state.set_state(EfootballForm.tolov)
@router.message(EfootballForm.tolov)
async def form_tolov(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   if message.text not in ["💳 KARTA", "💵 NAXT"]:
    await message.answer("⌨️ PASDAGI MENYUDAN BO‘LIMNI TANLANG VA DAVOM ETAMIZ! 👇", reply_markup=get_payment_menu())
    return
   await state.update_data(tolov=message.text)
   await message.answer(
"🏠 MANZILINGIZNI KIRITING\n\n"
"❗️MANZIL — TO‘LOV YOKI UCHRASHUV UCHUN MUHIM BO‘LISHI MUMKIN. ILTIMOS, ANIQ YOKI UMUMIY MANZIL YOZING.\n\n"
"🔰 MISOL UCHUN:\n"
"— 🏘️ TOSHKENT SHAHRIDA\n"
"— 📍 ANDIJON VILOYATI, ASAKA\n"
"— 🗺️ FAQAT ONLINE SAVDO\n\n"
"✅ AGAR HOZIRCHA AHAMIYATLI BO‘LMASA, 'YO‘Q' DEB YOZISHINGIZ MUMKIN!", reply_markup=get_back_menu())
   await state.set_state(EfootballForm.manzil)
@router.message(EfootballForm.manzil)
async def form_manzil(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(manzil=message.text)
   await message.answer(
"📩 TELEGRAM USERNAMEYINGIZNI KIRITING\n\n"
"❗️AGAR SOTUVCHI YOKI ADMIN SIZ BILAN BOG‘LANISHI KERAK BO‘LSA, USERNAME ORQALI ALOQA QILADI.\n\n"
"🔰 MISOL UCHUN:\n"
"— @USERNAME\n"
"— @SAYYAXuz\n"
"— YO'Q\n\n"
"✅ AGAR USERNAME YO‘Q BO‘LSA 'YO‘Q' DEB YOZING!", reply_markup=get_back_menu())
   await state.set_state(EfootballForm.telegram)
@router.message(EfootballForm.telegram)
async def form_telegram(message: Message, state: FSMContext):
   if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
    return
   await state.update_data(telegram=message.text)
   await message.answer(
"📞 TELEFON RAQAMINGIZNI KIRITING\n\n"
"❗️AGAR USERNAME BO‘LMASA YOKI TELEFON ORQALI BOG‘LANISHNI HOHLASANGIZ, RAQAMINGIZNI TO‘LIQ KO‘RSATING.\n\n"
"🔰 MISOL UCHUN:\n"
"— +998 90 XXX XX XX\n"
"— +998 99 XXX XX XX\n\n"
"✅ ILTIMOS, XALQARO FORMATDA YOZING: '+998' BILAN BOSHLANSIN!", reply_markup=get_back_menu())
   await state.set_state(EfootballForm.nomer)
@router.message(StateFilter(EfootballForm.nomer))
async def form_nomer(message: Message, state: FSMContext):
    if message.text in ["🔙 ORQAGA", "🚩 BOSH SAHIFAGA"]:
        return
    
    await state.update_data(nomer=message.text)
    await state.update_data(screenshots=[])  # Rasmlar ro'yxatini boshlash
    await message.answer(
        "📸 ILTIMOS, AKKAUNTINGIZNI RASMINI YUBORING (MAX 10 TA).\n"
        "HAMMASINI 1 TADA YUBORING MSOL 10 TASINI 1 TA QILIB. \n TUGAGACH '✅ RASMNI YUBORISH ' TUGMASINI BOSING.",
        reply_markup=get_finish_photos_menu()
    )
    await state.set_state(EfootballForm.screenshots)@router.message(StateFilter(EfootballForm.screenshots), F.content_type == ContentType.PHOTO)
@router.message(StateFilter(EfootballForm.screenshots), F.content_type == ContentType.PHOTO)
async def collect_screenshots(message: Message, state: FSMContext):
    data = await state.get_data()
    screenshots = data.get('screenshots', [])
    
    if len(screenshots) >= 10:
        await message.answer("❌ MAX 10 TA RASM YUKLASH MUMKUN!")
        return
    
    photo_id = message.photo[-1].file_id
    screenshots.append(photo_id)
    await state.update_data(screenshots=screenshots)
    await message.answer(f"✅ RASM QABUL QILINDI. JAMI: {len(screenshots)}/10")
@router.message(StateFilter(EfootballForm.screenshots), F.text == "✅ RASMNI YUBORISH")
async def finish_screenshots(message: Message, state: FSMContext):
    data = await state.get_data()
    screenshots = data.get('screenshots', [])
    
    if not screenshots:
        await message.answer("❌ KAMIDA BITTA RASM YUKLASHINGIZ KERAK!")
        return

    payment_text = f"""
💳 <b>E'LON BERISH UCHUN TO‘LOV</b>

📥 <b>KARTA RAQAMI:</b> <code>{PAYMENT_CARD}</code>
👤 <b>KARTA EGASI:</b> <b>{PAYMENT_HOLDER}</b>
📱 <b>KARTAGA ULANGAN:</b> <b>{PAYMENTS_NUMBER}</b>
💰 <b>TO‘LOV MIQDORI:</b> <b>{PAYMENT_AMOUNT} SO‘M</b>

📋 <i>KARTA RAQAMINI NUSXA OLISH UCHUN USTIGA BOSING</i>

✅ <i>TO‘LOVNI AMALGA OSHIRGACH, CHEKNI YUBORING.</i>
"""
    
    await message.answer(payment_text,parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
    await message.answer("📃 <b>TO‘LOV CHEKINI (SKRINSHOTINI) YUBORING:</b>", parse_mode="HTML")
    await state.set_state(EfootballForm.payment_screenshot)
@router.message(StateFilter(EfootballForm.payment_screenshot), F.content_type == ContentType.PHOTO)
async def receive_payment_screenshot(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        payment_screenshot = message.photo[-1].file_id
        user_id = message.from_user.id
        username = message.from_user.username or "USERNAME YOQ"
        full_name = message.from_user.full_name
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        screenshots = data.get("screenshots", [])

        post_text = f"""
🇺🇿EFOOTBALL AKKAUNT SOTILADI💰#E

⚡️ SILA:{data.get('sila')}
🦸 EPIC:{data.get('epic')}
💰 COIN:{data.get('coin')}
♻️ OBMEN:{data.get('obmen')}
🔖 QO‘SHIMCHA:{data.get('qoshimcha')}

📧#ULANGAN SERVIS:{data.get('ulang')}

💸#NARX:{data.get('narx')}
💳#TO‘LOV:{data.get('tolov')}
🏠#MANZIL:{data.get('manzil')}
📩#TELEGRAM:{data.get('telegram')}
📞#NOMER:{data.get('nomer')}

📧#ULANGAN: {data['ulang']}

💸#NARX: {data['narx']}
💳#TOLOV: {data['tolov']}
🏠#MANZIL: {data['manzil']}
❌ bekordan bekor bezovta qimelar
📩#TELEGRAM: {data['telegram']}
📞#NOMER: {data['nomer']}
➖➖➖➖➖➖➖➖➖➖➖➖➖
MASHKALARGA ALDANISHNI XOXLAMASANG ADMIN ORQALI SAVDO QIL..✔️
🤝SAVDO GURUH @SAVDO_GURUH_UZB
➖➖➖➖➖➖➖➖➖➖➖➖➖
🔰KANALIMIZ🌐
@EFOOTBALL_AKKAUNT_SAVDO_UZB


📄ELON UCHUN @SAYYAX_ELON
😎GARANT UCHUN @SAYYAX_GARANT
💎DANAT UCHUN @SAYYAX_DANAT"""

        payment_info = f"""
💳 <b>YANGI TO‘LOV MA'LUMOTI</b>

👤 <b>FOYDALANUVCHI:</b> <a href='tg://user?id={user_id}'>{full_name}</a>
🆔 <b>USER ID:</b> <code>{user_id}</code>
📱 <b>USERNAME:</b> @{username if username else 'USERNAME YO‘Q'}
⏰ <b>TO‘LOV VAQTI:</b> {current_time}
💰 <b>TO‘LOV MIQDORI:</b> <b>{PAYMENT_AMOUNT} SO‘M</b>
"""

        # Callback tugmalari
        admin_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Tastiqlash", callback_data=f"confirm_post_{user_id}_ef"),
                InlineKeyboardButton(text="❌ Bekor qilish", callback_data=f"cancel_post_{user_id}_ef")
            ]
        ])

        # Medialar
        media_group = [
            InputMediaPhoto(media=photo_id, caption=post_text if i == 0 else None)
            for i, photo_id in enumerate(screenshots)
        ]

        # Adminga yuborish
        await bot.send_media_group(chat_id=ADMIN_ID, media=media_group)
        await bot.send_photo(chat_id=ADMIN_ID, photo=payment_screenshot, caption=payment_info, reply_markup=admin_keyboard,parse_mode="HTML")

        # Callback uchun saqlash
        pending_posts[user_id] = {
            "post_text": post_text,
            "screenshots": screenshots
        }

        # Userga xabar
        await message.answer("✅ TOLOV CHEKI QABUL QILINDI VA ADMINGA YUBORILDI. TEZ ORADA JAVOB OLASIZ.", reply_markup=get_game_menu())
        await state.clear()
        await state.set_state(GameSelection.waiting_for_game)

    except Exception as e:
        await message.answer(f"❌ XATOLIK: {e}")
# Adminning qarorini handle qilish
@router.callback_query(F.data.startswith("confirm_post_") | F.data.startswith("cancel_post_"))
async def handle_admin_decision(callback_query: CallbackQuery):
    if callback_query.from_user.id != ADMIN_ID:
        await callback_query.answer("❌ SIZGA RUHSAT YO'Q!")
        return

    try:
        data_parts = callback_query.data.split('_')
        action = data_parts[0]  # confirm yoki cancel
        user_id = int(data_parts[2])
        game = data_parts[3]  # clash yoki brawl

        if game == "clash":
            channel_id = CLASH_OF_CLANS_ID
        elif game == "brawl":
            channel_id = BRAWL_STARS_ID
        elif game == "pubg":
            channel_id = PUBG_MOBILE_ID
        elif game == "ef":
            channel_id = EFOOTBALL_ID
        else:
            await callback_query.answer("❌ NOMA'LUM O'YIN TUR!")
            return

        if action == 'confirm':
            if user_id in pending_posts:
                post_data = pending_posts[user_id]
                media_group = [
                    InputMediaPhoto(media=p, caption=post_data['post_text'] if i == 0 else None)
                    for i, p in enumerate(post_data['screenshots'])
                ]
                await bot.send_media_group(chat_id=channel_id, media=media_group)
                del pending_posts[user_id]

            await bot.send_message(user_id, "🎉 E'LONINGIZ KANALGA YUBORILDI.", reply_markup=get_game_menu())
            await callback_query.message.edit_reply_markup()
            await callback_query.message.reply("✅ KANALGA YUBORILDI.")

        elif action == 'cancel':
            if user_id in pending_posts:
                del pending_posts[user_id]
            await bot.send_message(user_id, "❌ E'LONINGIZ RAD ETILDI.", reply_markup=get_game_menu())
            await callback_query.message.edit_reply_markup()
            await callback_query.message.reply("❌ RAD ETILDI.")

        await callback_query.answer()

    except Exception as e:
        await callback_query.message.reply(f"❌ CALLBACK XATOLIK: {e}")
# Barcha boshqa xabarlarni handle qilish
@router.message()
async def handle_any_message(message: Message, state: FSMContext):
    current_state = await state.get_state()

    # Tugmalarning matni
    valid_buttons = ["⚔️ CLASH OF CLANS", "💫 BRAWL STARS", "🔫 PUBG MOBILE","⚽ EFOOTBALL"]

    if current_state is None and message.text not in valid_buttons:
        await message.answer("QUYIDAGI TUGMANI BOSING:", reply_markup=get_game_menu())
# Asosiy funksiya
async def main():
    # Bot va dispatcher yaratish
    bot = Bot(token=API_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Routerni qo'shish
    dp.include_router(router)
    
    # Botni ishga tushirish haqida xabar
    await bot.send_message(ADMIN_ID, "🤖 BOT ISHGA TUSHDI!")
    
    # Pollingni boshlash
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())