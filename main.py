from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup
from telegram import ReplyKeyboardMarkup
language=['🇺🇿 O‘zbek tili 🎓']
def start(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    user_username = update.message.from_user.username

   
    reply_key = [
        ['🇷🇺 Русский язык', '🇺🇿 O‘zbek tili 🎓', '🇬🇧 English language']
    ]
    key = ReplyKeyboardMarkup(reply_key, resize_keyboard=True)
    if language[0] == '🇺🇿 O‘zbek tili 🎓':
       msg = (
        "👋 Salom! Botimizga xush kelibsiz.\n"
        "📅 Dars jadvalini bilish uchun sinf nomini ayting "
        "yoki tilni almashtirish uchun tugmalardan birini tanlang."
      )
    elif language[0] == '🇬🇧 English language':
       msg = (
        "👋 Hello! Welcome to our bot.\n"
        "📅 Please tell me your class name to know the schedule, "
        "or select one of the buttons to change the language."
    )
    elif language[0] == '🇷🇺 Русский язык':
       msg = (
        "👋 Привет! Добро пожаловать в наш бот.\n"
        "📅 Скажите название класса, чтобы узнать расписание, "
        "или выберите одну из кнопок, чтобы сменить язык."
    )
    else:
       msg = "Iltimos, tilni tanlang."





    if user_username:
        update.message.reply_text(
            f"👋  @{user_username}! {msg}",
            reply_markup=key
        )
    else:
        update.message.reply_text(
            f"👋  {first_name}! {msg}",
            reply_markup=key
        )
def choose_language(update,context):

    global language
    text=update.message.text
    language[0]=text
   
    if language[0] == '🇺🇿 O‘zbek tili 🎓':
           update.message.reply_text("✅ Siz tilingizni o‘zbek tiliga almashtirdingiz. 📅 Dars jadvalini bilish uchun sinf nomini ayting.")
    elif language[0] == '🇬🇧 English language':
       update.message.reply_text("✅ You have switched your language to English. 📅 Please tell me your class name to know the schedule.")
    else:
        update.message.reply_text("✅ Вы сменили язык на русский. 📅 Скажите название класса, чтобы узнать расписание.")

    
       






updater = Updater('8409915189:AAHJncmzMRpkYIvQocHSYlKNSCFFqkuHigk', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(
    Filters.regex(r'^(🇷🇺 Русский язык|🇺🇿 O‘zbek tili 🎓|🇬🇧 English language)$'),
    choose_language))

updater.start_polling()
updater.idle()