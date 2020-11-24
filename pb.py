import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('дед мороз.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("ДЕЛА: Что ты сейчас делаешь?")
    item2 = types.KeyboardButton("ГДЕ ЖИВУ: Ты правда живешь на Северном полюсе?")
    item3 = types.KeyboardButton("СЛАДОСТИ: Ты любишь сладости?")
    item4 = types.KeyboardButton("МУЛЬТИКИ: Ты любишь смотреть мультики?")
    item5 = types.KeyboardButton("ПОДАРОК: Что бы ты попросил на Новый год?")
    item6 = types.KeyboardButton("ИГРЫ: Ты любишь играть?")
    item7 = types.KeyboardButton("ИГРУШКА: Какая твоя любимая игрушка?")
    item8 = types.KeyboardButton("ОДНА НОЧЬ: Как ты успеваешь развести всем подарки за одну ночь?")
    item9 = types.KeyboardButton("ВНЕШНОСТЬ: Как ты выглядишь?")
    item10 = types.KeyboardButton("ТЕЛЕФОН: У тебя есть телефон?")
    item11 = types.KeyboardButton("ВЫХОДНЫЕ: Что ты делаешь, когда не нужно доставлять подарки?")
    item12 = types.KeyboardButton("ЖАРА: А ты можешь растаять?")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

    bot.send_message(message.chat.id, "Привет! Я – Дед Мороз🎅! \n Надеюсь, что письмо для меня уже готово💌.\nТы можешь задать мне вопросы. Выбирай внизу, что ты хочешь у меня узнать. Давай знакомиться!".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
        if message.text == "ДЕЛА: Что ты сейчас делаешь?":
            bot.send_message(message.chat.id, 'Прямо сейчас разговариваю с тобой 😉 \nА до этого я спал. Ведь я очень люблю поспать😴')

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data='good')
            item2 = types.InlineKeyboardButton("Нет", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'А ты любишь поспать?', reply_markup=markup)

        elif message.text == "ГДЕ ЖИВУ: Ты правда живешь на Северном полюсе?":
            sti = open('Домик.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Да! Тут холодно, часто идет снег🌨и его очень много❄️Но я не замерзаю, потому что у меня очень теплая шуба😊')

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data='good1')
            item2 = types.InlineKeyboardButton("Нет", callback_data='bad1')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'А ты всегда тепло одеваешься, когда холодно?', reply_markup=markup)

        elif message.text == "СЛАДОСТИ: Ты любишь сладости?":
            bot.send_message(message.chat.id, 'Конечно! Особенно леденцы🍭 и мороженое 🍧. Но приходится себя ограничивать, а то зубы могут испортиться… Это бывает сложно, но я очень стараюсь! ')
        elif message.text == "МУЛЬТИКИ: Ты любишь смотреть мультики?":
            bot.send_message(message.chat.id, 'Да, я люблю смотреть мультики, но только недолго⌛️. Если смотреть их долго, могут глаза испортиться👀, так что я смотрю мультики редко и только самые лучшие 🤩.')

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data='good2')
            item2 = types.InlineKeyboardButton("Нет", callback_data='bad2')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'А ты много смотришь мультики?', reply_markup=markup)

        elif message.text == "ПОДАРОК: Что бы ты попросил на Новый год?":
            bot.send_message(message.chat.id, 'Я не задумывался об этом… Наверное, я бы попросил цветы🌼🌺🌸, потому что из-за снега и холода я очень редко их вижу. А еще я очень люблю детские поделки ✂️🎨.')
        elif message.text == "ИГРЫ: Ты любишь играть?":
            bot.send_message(message.chat.id, 'Конечно! Больше всего я люблю радовать детей, спать и играть! А еще лепить снеговиков ⛄️.')

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data='good3')
            item2 = types.InlineKeyboardButton("Нет", callback_data='bad3')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'А ты любишь играть?', reply_markup=markup)

        elif message.text == "ИГРУШКА: Какая твоя любимая игрушка?":
            sti = open('Олень.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Моя любимая игрушка – олененок 🦌. Он такой мягкий! Я очень люблю его обнимать.')

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data='good4')
            item2 = types.InlineKeyboardButton("Нет", callback_data='bad4')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'А у тебя есть любимая игрушка?', reply_markup=markup)

        elif message.text == "ОДНА НОЧЬ: Как ты успеваешь развести всем подарки за одну ночь?":
            sti = open('Сани.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'С помощью моих волшебных оленей, которые поднимают мои сани в небо\n🦌 🦌 🦌 🛷\nМы быстро летим по небу и каждому ребенку доставляем подарок, который он хотел 🎁.  А чтобы не запутаться, какой подарок подарить, у меня есть очень большой список 📋. За много лет работы я еще ни разу не ошибся!')
        elif message.text == "ВНЕШНОСТЬ: Как ты выглядишь?":
            sti = open('одежда.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'У меня белая борода. Я часто хожу в своей шубе и колпачке. Иногда я надеваю красные теплые штаны. А на ногах у меня всегда валенки или теплые сапоги. Ну и конечно, у меня есть очки 👓.')
        elif message.text == "ТЕЛЕФОН: У тебя есть телефон?":
            bot.send_message(message.chat.id, 'Да, у меня есть телефон 📞. Если бы у меня его не было, я бы не смог общаться с детьми! Но использую я его только для общения 🗣.')
        elif message.text == "ВЫХОДНЫЕ: Что ты делаешь, когда не нужно доставлять подарки?":
            bot.send_message(message.chat.id, 'Даже не в Новогоднюю ночь у меня очень много работы! Я общаюсь с детьми, читаю письма и отвечаю на них 💌, добавляю все пожелания детей в список 📋. И, конечно, слежу за производством подарков. А когда у меня есть свободное время, я играю или сплю 😴.')
        elif message.text == "ЖАРА: А ты можешь растаять?":
            bot.send_message(message.chat.id, 'Нет, я не могу растаять, но могу заболеть от жары… Я привык к холоду❄️, поэтому жара ☀️ для меня опасна. Из-за этого я всегда нахожусь у себя дома🏠, на северном полюсе, и только в новогоднюю ночь лечу развозить подарки.')
        else:
            bot.send_message(message.chat.id,"Прости, я не знаю, что ответить...")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Мы с тобой похожи 😉')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Повезло😊. Это значит, что у тебя больше времени на что-то интересное!')
            elif call.data == 'good1':
                bot.send_message(call.message.chat.id, 'Молодец 👏!')
            elif call.data == 'bad1':
                bot.send_message(call.message.chat.id, 'Обязательно одевайся тепло, чтобы не простудиться ☕️!')
            elif call.data == 'good2':
                bot.send_message(call.message.chat.id, 'Постарайся, пожалуйста, смотреть их поменьше🙏.')
            elif call.data == 'bad2':
                bot.send_message(call.message.chat.id, 'Молодец 👏!')
            elif call.data == 'good3':
                bot.send_message(call.message.chat.id, 'Здорово! Веселье – это замечательно😜!')
            elif call.data == 'bad3':
                bot.send_message(call.message.chat.id, 'Наверное ты еще просто не нашел свою любимую игру😉.')
            elif call.data == 'good4':
                bot.send_message(call.message.chat.id, 'Прекрасно! 😍 Береги её!')
            elif call.data == 'bad4':
                bot.send_message(call.message.chat.id, 'Значит, еще появится (даже если ты думаешь, что уже слишком взрослый для этого 😊)')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                                  reply_markup=None)


    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)