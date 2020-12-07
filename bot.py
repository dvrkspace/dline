import telebot

bot = telebot.TeleBot('943862443:AAGJGrMorC-XAvCuMqBLYMoMJQ1Aa1-HGu0')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('The bustle of my city')
keyboard1.row('The beginning of the end')
keyboard1.row('The adventures of Tom Sawyer')
keyboard1.row('Dark Tower')
keyboard1.row('Harry Potter')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome!', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'the bustle of my city':
        bot.send_message(message.chat.id, 'Nurmakhanov Arnur - The bustle of my city \n\n https://vk.com/public181444950')
    elif message.text.lower() == 'the beginning of the end':
        bot.send_message(message.chat.id, 'Darkhan Makhanbetov - The beginning of the end \n\n https://vk.com/d9rkhan')
    elif message.text.lower() == 'the adventures of tom sawyer':
        bot.send_message(message.chat.id, 'Mark Twain - The adventures of Tom Sawyer \n\n https://en.wikipedia.org/wiki/The_Adventures_of_Tom_Sawyer')
    elif message.text.lower() == 'dark tower':
        bot.send_message(message.chat.id, 'Stephen King - Dark Tower \n\n https://en.wikipedia.org/wiki/The_Dark_Tower_(series)')
    elif message.text.lower() == 'harry potter':
         bot.send_message(message.chat.id,'Joanne Rowling - Harry Potter \n\n https://en.wikipedia.org/wiki/Harry_Potter_(character)')


    print(message)

bot.polling()
