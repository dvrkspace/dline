import telebot

bot = telebot.TeleBot('943862443:AAGJGrMorC-XAvCuMqBLYMoMJQ1Aa1-HGu0')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Web Technology')
keyboard1.row('English [Sholokhova]')
keyboard1.row('Discrete Math')
keyboard1.row('Database')
keyboard1.row('Software Development')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'web technology':
        bot.send_message(message.chat.id, 'Понедельник, 21 Сентябрь 2020, 00:02 | Laboratory work1_for_IT2CCO-2001 ')
    elif message.text.lower() == 'english':
        bot.send_message(message.chat.id, 'Прощай, создатель')


    print(message)

bot.polling()
