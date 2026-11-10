import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# --- SOZLAMALAR ---
TOKEN = "8682447931:AAH2aBrYJV8yk2-NSrBubLRDFFLNrSu9vk4"
WEB_APP_URL = "https://futquiz-nu.vercel.app/"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Mini App ochuvchi tugma yaratish
    keyboard = InlineKeyboardMarkup()
    web_app = WebAppInfo(WEB_APP_URL)
    button = InlineKeyboardButton(text="⚽️ O'ynash", web_app=web_app)
    keyboard.add(button)
    
    msg = (
        "⚽️ **Pro Futbol Quiz** botiga xush kelibsiz!\n\n"
        "Bilimingizni sinovdan o'tkazish, reytingda qatnashish va sovrinlar yutib olish uchun quyidagi tugmani bosing:"
    )
    
    bot.send_message(
        message.chat.id, 
        msg, 
        reply_markup=keyboard, 
        parse_mode="Markdown"
    )

print("Bot zo'r ishlayapti va xabarlarni kutmoqda...")
bot.infinity_polling()
