import os
import telebot

# === CONFIG ===
BOT_TOKEN = os.getenv("BOT_TOKEN")  # токен загружается из переменных среды
GROUP_ID = -1003398324556

bot = telebot.TeleBot(BOT_TOKEN)

categories = {
    "Промокод": "https://t.me/marketappru/19",
    "Недвижимость": "https://t.me/marketappru/18",
    "Авто": "https://t.me/marketappru/16",
    "Работа": "https://t.me/marketappru/15",
    "Вакансии": "https://t.me/marketappru/14",
    "Услуги": "https://t.me/marketappru/13",
    "Одежда и обувь": "https://t.me/marketappru/12",
    "Детские товары": "https://t.me/marketappru/11",
    "Техника": "https://t.me/marketappru/10",
    "Мебель": "https://t.me/marketappru/9",
    "Животные": "https://t.me/marketappru/8",
    "Ищу / Куплю": "https://t.me/marketappru/6",
    "Бесплатно": "https://t.me/marketappru/5",
    "Поставщики ОПТ (Stars)": "https://t.me/marketappru/4",
    "Другое": "https://t.me/marketappru/3"
}

@bot.message_handler(commands=['start'])
def start(message):
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for c in categories:
        kb.add(c)
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=kb)

@bot.message_handler(func=lambda m: m.text in categories)
def open_category(message):
    bot.send_message(message.chat.id, categories[message.text])

print("Bot running...")
bot.infinity_polling()
