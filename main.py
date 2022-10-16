import requests
import telebot


# import config

token = '5758992104:AAHgXCJ3ybtfwNLiKlCT2-RjUfahFK16yUU'
bot = telebot.TeleBot(token)


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет!')
# bot.polling()
#

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот, который умеет опрашивать по сети заданные адреса".format(
                         message.from_user))
    bot.send_message(message.chat.id,
                     text="Отправь мне адрес ".format(
                         message.from_user))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        response = requests.get(message.text)
        if response.status_code == 200:
            bot.send_message(message.from_user.id, 'Success!')
        # elif (response.status_code > 399) and (response.status_code < 600):
        #     bot.send_message(message.from_user.id, 'Not Found.')
    except Exception:
        bot.send_message(message.from_user.id, "Not Found 2")


bot.polling(none_stop=True, interval=0)
