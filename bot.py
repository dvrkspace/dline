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
    bot.send_message(message.chat.id, 'Доброго времени суток!', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Web Technology':
        bot.send_message(message.chat.id , 'Понедельник, 21 Сентябрь 2020, 00:02 | Laboratory work1_for_IT2CCO-2001 ')
    elif message.text.lower() == 'English [Sholokhova]':
        bot.send_message(message.chat.id ,'English Понедельник 21 September 2020, 00:02 | Hometask. N WB. Unit 6 p. 38 Задание \n\n English Четверг, 24 Сентябрь 2020, 00:02 | Glossary ')
    elif message.text.lower() == 'Discrete Math':
        bot.send_message(message.chat.id, 'Discrete Math 22 сентября до 15:00 | exercise №3')

    elif message.text.lower() == 'Database':
        bot.send_message(message.chat.id, 'Database Среда 23 сентября 2020, 00:02 | Course Work 1, 2')
    

    elif message.text.lower() == 'Software Development':
        bot.send_message(message.chat.id, 'Software development Суббота 27 September 2020, 23:55 | lab 2 \n\n Software development Воскресенье, 4 Октябрь 2020, 23:55 | lab 3')
    
    print(message)
    
    
bot.polling()
                                            
