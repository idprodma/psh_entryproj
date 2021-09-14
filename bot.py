import telebot
from telebot import types
import google_funcs

TOKEN = open('token.txt', 'r').read()
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Получить список студентов с пропусками"))
    bot.send_message(chat_id=message.chat.id,
                     text="Выберите действие",
                     reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def send_help_message(message):
    bot.send_message(chat_id=message.chat.id,
                     text="Бот выдает список студентов с пропусками.\n" +
                          "Для его получения нажмите кнопку на клавиатуре")


@bot.message_handler(commands=['getdata'])
@bot.message_handler(func=lambda msg: msg.text=="Получить список студентов с пропусками")
def send_list(message):
    data = google_funcs.get_data()
    msg_string = ""
    for record in data:
        msg_string += "ФИО: " + record[0] + "\nEmail: " + record[1]
        msg_string += "\nПропуски:\n"
        for item in record[2:len(record)]:
            msg_string += item + "\n"
        msg_string += "\n\n"
    bot.send_message(chat_id=message.chat.id,
                     text=msg_string)


def make_choose_timespend_keyboard():
    keyboard = types.InlineKeyboardMarkup()



bot.polling()
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(types.KeyboardButton("Получить список студентов с пропусками"))
keyboard.row()
while True:
    pass
