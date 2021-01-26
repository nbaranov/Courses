import telebot
from config import TOKEN, values
from extensions import APIException, Exchage

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы конвертировать валюту введите сообщение в формате:\n\n\
<имя/тикер валюты цену которой хотите узнать>\n\
<имя/тикер валюты в которой надо узнать цену первой валюты>\n\
<количество первой валюты>\n\n\
Например: Доллар Рубль 20\n\
\t\tили USD RUB 20\n\n\
Введите команду /values чтобы посмотреть доступные валюты'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = 'Доступные валюты:\n'
    for key in values.keys():
        text = text + f'{key}\t{values[key]}\n'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def echo_test(message: telebot.types.Message):
    user_input = message.text.split(' ')
    try:    
        if len(user_input) < 2:
            raise APIException('Недостаточно параметров.\nВведите /help чтобы посмотреть подсказку.')
            
        elif len(user_input) == 2:
            base, quote = user_input
            amount = '1'
        else:
            base, quote, amount = user_input[:3]
        text = Exchage.get_price(base, quote, amount)
    except APIException as error:
        bot.reply_to(message, error)
    except Exception as error:
        bot.reply_to(message, f'Не удалось обработать команду\n{error}')
    else:
        bot.reply_to(message, text)

bot.polling()