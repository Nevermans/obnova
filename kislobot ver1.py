import subprocess
import telebot
import datetime
from telebot import types
import requests
import io
bot = telebot.TeleBot("5830917962:AAF14OkxWo3L_ypw2-SQpE5eP13ZA_5KEMA")

# Сохранение логов
def save_message(username, text):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("messages.txt", "a", encoding='utf-8') as file:
        file.write(f"{now} {username} {text}\n")

# Стартовое меню
@bot.message_handler(commands=['start'])
def start(message):
    # get the user_id from the message
    user_id = str(message.from_user.id)

    # read the user_id's from the users.txt file
    with open("users.txt", "r") as file:
        users = file.readlines()

    # check if the user_id is already in the file
    if user_id + "\n" not in users:
        # add the user_id to the users.txt file
        with open("users.txt", "a") as file:
            file.write(user_id + "\n")
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%A1%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BC%D0%B5%D0%BD%D1%8E/%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82%D1%81%D1%82%D0%B2%D0%B8%D0%B5.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Описание функционала  💬')
    item2 = types.KeyboardButton('Главное меню ➡️')
    markup0.add(item1, item2)
    bot.send_message(message.chat.id, text)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup0)

@bot.message_handler(func=lambda message: message.text == "Описание функционала  💬")
def funk(message):
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%A1%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BC%D0%B5%D0%BD%D1%8E/%D0%9E%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D0%B0.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    markup000 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2 = types.KeyboardButton('Главное меню ➡️')
    markup000.add(item2)
    bot.send_message(message.chat.id, text)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup000)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

# Главное меню
@bot.message_handler(func=lambda message: message.text == "Главное меню ➡️")
def main(message):
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%A1%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BC%D0%B5%D0%BD%D1%8E/%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D0%BE%D0%B5%20%D0%BC%D0%B5%D0%BD%D1%8E.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('Игротека  🤹  ➡️')
    item2 = types.KeyboardButton('Для вожатых 🧙‍♂️ ➡️')
    item3 = types.KeyboardButton('Для выступлений 💃 🔐')
    item4 = types.KeyboardButton('Интерактивная ШВМ  👨‍💻   🔒')
    item5 = types.KeyboardButton('Для лагерей и СПО  💼 ➡️')
    item6 = types.KeyboardButton('О проекте   💡  ➡️')
    item7 = types.KeyboardButton('Предложить идею 📋')
    item8 = types.KeyboardButton('Знакомство с ботом  ⬅️')
    item9 = types.KeyboardButton('Оставить отзыв ✍')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item9)
    markup.add(item8)
    bot.send_message(message.chat.id, text)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)
    
# Обработчи кнопки Игротека
@bot.message_handler(func=lambda message: message.text == "Игротека  🤹  ➡️")
def game(message):
    markup8 = types.ReplyKeyboardMarkup(row_width=2)
    bth1 = types.KeyboardButton('Готовые блоки игр 🧙‍♂️')
    bth2 = types.KeyboardButton('Ледоколы ❄️')
    bth3 = types.KeyboardButton('Тактилки 👐')
    bth4 = types.KeyboardButton('На знакомство 👋')
    bth5 = types.KeyboardButton('Пятиминутки ⏰')
    bth6 = types.KeyboardButton('Прочее 🌈')
    bth7 = types.KeyboardButton('Предложить игру  📝')
    bth8 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markup8.add(bth1, bth2, bth3, bth4, bth5, bth6, bth7, bth8)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup8)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)
    
# Обработчик кнопки Готовые блоки
@bot.message_handler(func=lambda message: message.text == "Готовые блоки игр 🧙‍♂️")
def game(message):
    markup8 = types.ReplyKeyboardMarkup(row_width=2)
    bth1 = types.KeyboardButton('Блок игр на знакомство')
    bth2 = types.KeyboardButton('Подборка для младших')
    bth3 = types.KeyboardButton('Подборка для средних')
    bth4 = types.KeyboardButton('Подборка для старших')
    bth5 = types.KeyboardButton('Назад ⬅️')
    bth6 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markup8.add(bth1, bth2, bth3, bth4, bth5, bth6)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup8)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

# Обработчки кнопки Главное меню
@bot.message_handler(func=lambda message: message.text == "В главное меню  ⬅️⬅️")
def main(message):
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%A1%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BC%D0%B5%D0%BD%D1%8E/%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D0%BE%D0%B5%20%D0%BC%D0%B5%D0%BD%D1%8E.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('Игротека  🤹  ➡️')
    item2 = types.KeyboardButton('Для вожатых 🧙‍♂️ ➡️')
    item3 = types.KeyboardButton('Для выступлений 💃 🔐')
    item4 = types.KeyboardButton('Интерактивная ШВМ  👨‍💻   🔒')
    item5 = types.KeyboardButton('Для лагерей и СПО  💼 ➡️')
    item6 = types.KeyboardButton('О проекте   💡  ➡️')
    item7 = types.KeyboardButton('Предложить идею 📋')
    item8 = types.KeyboardButton('Знакомство с ботом  ⬅️')
    item9 = types.KeyboardButton('Оставить отзыв ✍')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item9)
    markup.add(item8)
    bot.send_message(message.chat.id, text)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

# Обработчик кнопки Прочее
@bot.message_handler(func=lambda message: message.text == "Прочее 🌈")
def prochee(message):
    markup3 = types.ReplyKeyboardMarkup(row_width=2)
    bth1 = types.KeyboardButton('На выявление лидера 🙋‍♀️')
    bth2 = types.KeyboardButton('С залом 🎤')
    bth3 = types.KeyboardButton('Подвижная 🏃')
    bth4 = types.KeyboardButton('Игры-розыгрыши 🤡')
    bth5 = types.KeyboardButton('Головоломка 🤓')
    bth6 = types.KeyboardButton('Данетки 🤔')
    bth7 = types.KeyboardButton('На пляже 🏖️')
    bth8 = types.KeyboardButton('Игры народов мира 🇰🇬')
    bth9 = types.KeyboardButton('Предложить игру  📝')
    bth10 = types.KeyboardButton('Назад ⬅️')
    bth11 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markup3.add(bth1, bth2, bth3, bth4, bth5, bth6, bth7, bth8, bth9, bth10, bth11)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup3)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

# Обработчик кнопки Назад в игротеке/прочем и готовые блоки игр
@bot.message_handler(func=lambda message: message.text == "Назад ⬅️")
def back(message):
    markup2 = types.ReplyKeyboardMarkup(row_width=2)
    bth1 = types.KeyboardButton('Готовые блоки игр 🧙‍♂️')
    bth2 = types.KeyboardButton('Ледоколы ❄️')
    bth3 = types.KeyboardButton('Тактилки 👐')
    bth4 = types.KeyboardButton('На знакомство 👋')
    bth5 = types.KeyboardButton('Пятиминутки ⏰')
    bth6 = types.KeyboardButton('Прочее 🌈')
    bth7 = types.KeyboardButton('Предложить игру  📝')
    bth8 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markup2.add(bth1, bth2, bth3, bth4, bth5, bth6, bth7, bth8)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup2)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)   

# Обработчик кнопки Для вожатых
@bot.message_handler(func=lambda message: message.text == "Для вожатых 🧙‍♂️ ➡️")
def dliavojatih(message):
    markup4 = types.ReplyKeyboardMarkup(row_width=2)
    bth1 = types.KeyboardButton('КТД 🤝 🔐')
    bth2 = types.KeyboardButton('Легенды 🕯️ ➡️')
    bth3 = types.KeyboardButton('Кричалки 💥 ➡️')
    bth4 = types.KeyboardButton('Лагерные песни  🎶 🔐')
    bth5 = types.KeyboardButton('ЭВК 🔗 ➡️')
    bth6 = types.KeyboardButton('Что делать в ситуации ❓  ➡️')
    bth7 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markup4.add(bth1, bth2, bth3, bth4, bth5, bth6, bth7)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup4)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

# Обработчик кнопки Для выступлений
@bot.message_handler(func=lambda message: message.text == "Для выступлений 💃 🔐")
def dliavojatih(message):
    markup5 = types.ReplyKeyboardMarkup(row_width=2)
    bth1 = types.KeyboardButton('Сценки 🎭 🔒')
    bth2 = types.KeyboardButton('Танцы  💃 🔒')
    bth3 = types.KeyboardButton('Корпоративы  👯 🔒')
    bth4 = types.KeyboardButton('Прочее  💙 🔒')
    bth5 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markup5.add(bth1, bth2, bth3, bth4, bth5)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup5)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

# Обработчик кнопки Интерактивная ШВМ
@bot.message_handler(func=lambda message: message.text == "Интерактивная ШВМ  👨‍💻   🔒")
def dliavojatih(message):
    bot.send_message(message.chat.id, "No data...")
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)   

# Обработчик кнопки Для лагерей СПО (Доделать)
@bot.message_handler(func=lambda message: message.text == "Для лагерей и СПО  💼 ➡️")
def prochee(message):
    markup6 = types.ReplyKeyboardMarkup(row_width=2)
    bth1 = types.KeyboardButton('Доска объявлений 📋  ➡️')
    bth2 = types.KeyboardButton('Предложить объявление  📩  ➡️')
    bth3 = types.KeyboardButton('Связаться с нами  💬')
    bth4 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markup6.add(bth1, bth2, bth3, bth4)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup6)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

# Обработчик кнопки О проекте
@bot.message_handler(func=lambda message: message.text == "О проекте   💡  ➡️")
def prochee(message):
    markup7 = types.ReplyKeyboardMarkup(row_width=2)
    bth1 = types.KeyboardButton('Дорожная карта проекта  ✈️  ➡️')
    bth2 = types.KeyboardButton('Оставить отзыв  👍  ➡️')
    bth3 = types.KeyboardButton('Предложить материал  📃  ➡️')
    bth4 = types.KeyboardButton('Связаться с нами  💬')
    bth5 = types.KeyboardButton('Поддержать проект  💰')
    bth6 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markup7.add(bth1, bth2, bth3, bth4, bth5, bth6)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup7)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

# Обработчик кнопки Знакомство с ботом
@bot.message_handler(func=lambda message: message.text == "Знакомство с ботом  ⬅️")
def prochee(message):
    markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Описание функционала  💬')
    item2 = types.KeyboardButton('Главное меню ➡️')
    markup0.add(item1, item2)
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup0)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

@bot.message_handler(func=lambda message: message.text == "Предложить идею 📋")
def handle_offer(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Предложить идею 📋', callback_data='offer')
    item2 = types.InlineKeyboardButton(text= 'Отмена ⬅️', callback_data='cancel_offer')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(chat_id=message.chat.id, text='Отлично! Нажмите кнопку "Предложить идею 📋" или нажмите на кнопку "Отмена ⬅️" если передумали писать предложение', reply_markup=markup)

    
IDStatus = {}
@bot.callback_query_handler(func=lambda call: call.data == 'offer')
def handle_offer_callback(call):
    IDStatusop[call.from_user.id] = False
    IDStatuso[call.from_user.username] = False
    IDStatus[call.from_user.username] = True
    bot.send_message(call.message.chat.id, 'Просто напишите свою идею в чат и мы её обязательно рассмотрим!')

@bot.message_handler(func=lambda message: message.text != "Предложить идею 📋" and IDStatus.get(message.from_user.username, False))
def handle_offer_message(message):
    username = message.from_user.username
    user_message = message.text
    with open('Идеи и предложения.txt', 'a', encoding='utf-8') as f:
        f.write(username + '\n' + user_message + '\n\n\n')
    IDStatus[message.from_user.username] = False
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('Игротека  🤹  ➡️')
    item2 = types.KeyboardButton('Для вожатых 🧙‍♂️ ➡️')
    item3 = types.KeyboardButton('Для выступлений 💃 🔐')
    item4 = types.KeyboardButton('Интерактивная ШВМ  👨‍💻   🔒')
    item5 = types.KeyboardButton('Для лагерей и СПО  💼 ➡️')
    item6 = types.KeyboardButton('О проекте   💡  ➡️')
    item7 = types.KeyboardButton('Предложить идею 📋')
    item8 = types.KeyboardButton('Знакомство с ботом  ⬅️')
    item9 = types.KeyboardButton('Оставить отзыв ✍')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item9)
    markup.add(item8)
    bot.send_message(message.chat.id, "Спасибо за предложение, мы рассмотрим его в ближайшее время!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'cancel_offer')
def handle_cancel_offer_callback(call):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('Игротека  🤹  ➡️')
    item2 = types.KeyboardButton('Для вожатых 🧙‍♂️ ➡️')
    item3 = types.KeyboardButton('Для выступлений 💃 🔐')
    item4 = types.KeyboardButton('Интерактивная ШВМ  👨‍💻   🔒')
    item5 = types.KeyboardButton('Для лагерей и СПО  💼 ➡️')
    item6 = types.KeyboardButton('О проекте   💡  ➡️')
    item7 = types.KeyboardButton('Предложить идею 📋')
    item8 = types.KeyboardButton('Знакомство с ботом  ⬅️')
    item9 = types.KeyboardButton('Оставить отзыв ✍')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item9)
    markup.add(item8)
    bot.send_message(call.message.chat.id, 'Вы отменили функцию предложение и идеи, можете дальше пользоваться ботом', reply_markup=markup)
    IDStatus[call.from_user.username] = False


@bot.message_handler(func=lambda message: message.text == "Оставить отзыв ✍")
def handle_offer(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Оставить отзыв ✍', callback_data='offero')
    item2 = types.InlineKeyboardButton(text= 'Отмена ⬅️', callback_data='cancel_offero')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(chat_id=message.chat.id, text='Отлично! Нажмите кнопку "Оставить отзыв ✍" или нажмите на кнопку "Отмена ⬅️" если передумали писать отзыв', reply_markup=markup)

    
IDStatuso = {}

@bot.callback_query_handler(func=lambda call: call.data == 'offero')
def handle_offer_callback(call):
    IDStatusop[call.from_user.id] = False
    IDStatus[call.from_user.username] = False
    IDStatuso[call.from_user.username] = True
    bot.send_message(call.message.chat.id, 'Просто напишите свой отзыв в чат и мы его увидим!')

@bot.message_handler(func=lambda message: message.text != "Оставить отзыв ✍" and IDStatuso.get(message.from_user.username, False))
def handle_offer_message(message):
    username = message.from_user.username
    user_message = message.text
    with open('Отзывы.txt', 'a', encoding='utf-8') as f:
        f.write(username + '\n' + user_message + '\n\n\n')
    IDStatus[message.from_user.username] = False
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('Игротека  🤹  ➡️')
    item2 = types.KeyboardButton('Для вожатых 🧙‍♂️ ➡️')
    item3 = types.KeyboardButton('Для выступлений 💃 🔐')
    item4 = types.KeyboardButton('Интерактивная ШВМ  👨‍💻   🔒')
    item5 = types.KeyboardButton('Для лагерей и СПО  💼 ➡️')
    item6 = types.KeyboardButton('О проекте   💡  ➡️')
    item7 = types.KeyboardButton('Предложить идею 📋')
    item8 = types.KeyboardButton('Знакомство с ботом  ⬅️')
    item9 = types.KeyboardButton('Оставить отзыв ✍')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item9)
    markup.add(item8)
    bot.send_message(message.chat.id, "Спасибо за отзыв, мы рады получать обратную связь!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'cancel_offero')
def handle_cancel_offer_callback(call):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('Игротека  🤹  ➡️')
    item2 = types.KeyboardButton('Для вожатых 🧙‍♂️ ➡️')
    item3 = types.KeyboardButton('Для выступлений 💃 🔐')
    item4 = types.KeyboardButton('Интерактивная ШВМ  👨‍💻   🔒')
    item5 = types.KeyboardButton('Для лагерей и СПО  💼 ➡️')
    item6 = types.KeyboardButton('О проекте   💡  ➡️')
    item7 = types.KeyboardButton('Предложить идею 📋')
    item8 = types.KeyboardButton('Знакомство с ботом  ⬅️')
    item9 = types.KeyboardButton('Оставить отзыв ✍')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item9)
    markup.add(item8)
    bot.send_message(call.message.chat.id, 'Вы отменили функцию Отзывов, можете дальше пользоваться ботом', reply_markup=markup)
    IDStatuso[call.from_user.username] = False

@bot.message_handler(func=lambda message: message.text == "Ледоколы ❄️")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextl2')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9B%D0%B5%D0%B4%D0%BE%D0%BA%D0%BE%D0%BB%D1%8B1.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "Ледоколы страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)    

@bot.callback_query_handler(func=lambda call: call.data == 'nextl2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backl1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextl3')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9B%D0%B5%D0%B4%D0%BE%D0%BA%D0%BE%D0%BB%D1%8B2.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Ледоколы страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'igr')
def main(call):
    markup8 = types.ReplyKeyboardMarkup(row_width=2)
    bth1 = types.KeyboardButton('Готовые блоки игр 🧙‍♂️')
    bth2 = types.KeyboardButton('Ледоколы ❄️')
    bth3 = types.KeyboardButton('Тактилки 👐')
    bth4 = types.KeyboardButton('На знакомство 👋')
    bth5 = types.KeyboardButton('Пятиминутки ⏰')
    bth6 = types.KeyboardButton('Прочее 🌈')
    bth7 = types.KeyboardButton('Предложить игру  📝')
    bth8 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markup8.add(bth1, bth2, bth3, bth4, bth5, bth6, bth7, bth8)
    bot.send_message(call.message.chat.id, "Выберите пункт меню:", reply_markup=markup8)


@bot.callback_query_handler(func=lambda call: call.data == 'backl1')
def main(call):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextl2')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9B%D0%B5%D0%B4%D0%BE%D0%BA%D0%BE%D0%BB%D1%8B1.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Ледоколы страница 1", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl1)


@bot.callback_query_handler(func=lambda call: call.data == 'nextl3')
def igrled(call):
    keyboardl3 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backl2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextl4')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl3.add(item1,item2)
    keyboardl3.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9B%D0%B5%D0%B4%D0%BE%D0%BA%D0%BE%D0%BB%D1%8B3.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Ледоколы страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl3)


@bot.callback_query_handler(func=lambda call: call.data == 'backl2')
def main(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backl1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextl3')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9B%D0%B5%D0%B4%D0%BE%D0%BA%D0%BE%D0%BB%D1%8B2.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Ледоколы страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextl4')
def igrled(call):
    keyboardl3 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backl3')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl3.add(item1)
    keyboardl3.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9B%D0%B5%D0%B4%D0%BE%D0%BA%D0%BE%D0%BB%D1%8B4.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Ледоколы страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl3)


@bot.callback_query_handler(func=lambda call: call.data == 'backl3')
def igrled(call):
    keyboardl3 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backl2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextl4')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl3.add(item1,item2)
    keyboardl3.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9B%D0%B5%D0%B4%D0%BE%D0%BA%D0%BE%D0%BB%D1%8B3.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Ледоколы страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl3)


@bot.message_handler(func=lambda message: message.text == "Тактилки 👐")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextt2')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A2%D0%B0%D0%BA%D1%82%D0%B8%D0%BB%D0%BA%D0%B81.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "Тактилки страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)


@bot.callback_query_handler(func=lambda call: call.data == 'nextt2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backt1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextt3')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A2%D0%B0%D0%BA%D1%82%D0%B8%D0%BB%D0%BA%D0%B82.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Тактилки страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backt1')
def igrled(call):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextt2')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A2%D0%B0%D0%BA%D1%82%D0%B8%D0%BB%D0%BA%D0%B81.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Тактилки страница 1", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl1)


@bot.callback_query_handler(func=lambda call: call.data == 'nextt3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backt2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextt4')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A2%D0%B0%D0%BA%D1%82%D0%B8%D0%BB%D0%BA%D0%B83.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Тактилки страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backt2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backt1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextt3')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A2%D0%B0%D0%BA%D1%82%D0%B8%D0%BB%D0%BA%D0%B82.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Тактилки страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextt4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backt3')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextt5')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A2%D0%B0%D0%BA%D1%82%D0%B8%D0%BB%D0%BA%D0%B84.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Тактилки страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backt3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backt2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextt4')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A2%D0%B0%D0%BA%D1%82%D0%B8%D0%BB%D0%BA%D0%B83.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Тактилки страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextt5')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backt4')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A2%D0%B0%D0%BA%D1%82%D0%B8%D0%BB%D0%BA%D0%B85.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Тактилки страница 5", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backt4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backt3')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextt5')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A2%D0%B0%D0%BA%D1%82%D0%B8%D0%BB%D0%BA%D0%B84.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Тактилки страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.message_handler(func=lambda message: message.text == "На знакомство 👋")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextz2')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE1.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "Знакомства страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)


@bot.callback_query_handler(func=lambda call: call.data == 'nextz2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backz1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextz3')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE2.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Знакомства страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backz1')
def igrled(call):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextz2')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE1.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Знакомства страница 1", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl1)


@bot.callback_query_handler(func=lambda call: call.data == 'nextz3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backz2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextz4')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE3.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Знакомства страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backz2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backz1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextz3')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE2.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Знакомства страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextz4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backz3')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextz5')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE4.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Знакомства страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backz3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backz2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextz4')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE3.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Знакомства страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextz5')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backz4')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE5.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Знакомства страница 5", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backz4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backz3')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextz5')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE4.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Знакомства страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.message_handler(func=lambda message: message.text == "Пятиминутки ⏰")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextp2')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D1%8F%D1%82%D0%B8%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D0%BA%D0%B81.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "Пятиминутки страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)


@bot.callback_query_handler(func=lambda call: call.data == 'nextp2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backp1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextp3')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D1%8F%D1%82%D0%B8%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D0%BA%D0%B82.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Пятиминутки страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backp1')
def igrled(call):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextp2')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D1%8F%D1%82%D0%B8%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D0%BA%D0%B81.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Пятиминутки страница 1", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl1)


@bot.callback_query_handler(func=lambda call: call.data == 'nextp3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backp2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextp4')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D1%8F%D1%82%D0%B8%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D0%BA%D0%B83.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Пятиминутки страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backp2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backp1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextp3')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D1%8F%D1%82%D0%B8%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D0%BA%D0%B82.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Пятиминутки страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextp4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backp3')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextp5')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D1%8F%D1%82%D0%B8%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D0%BA%D0%B84.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Пятиминутки страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backp3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backp2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextp4')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D1%8F%D1%82%D0%B8%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D0%BA%D0%B83.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Пятиминутки страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextp5')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backp4')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextp6')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D1%8F%D1%82%D0%B8%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D0%BA%D0%B85.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Пятиминутки страница 5", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backp4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backp3')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextp5')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D1%8F%D1%82%D0%B8%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D0%BA%D0%B84.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Пятиминутки страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'nextp6')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backp5')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D1%8F%D1%82%D0%B8%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D0%BA%D0%B86.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Пятиминутки страница 6", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backp5')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backp4')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextp6')
    item3 = types.InlineKeyboardButton(text='К игротеке ⬅️', callback_data='igr')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D1%8F%D1%82%D0%B8%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D0%BA%D0%B85.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Пятиминутки страница 5", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.message_handler(func=lambda message: message.text == "На выявление лидера 🙋‍♀️")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item3 = types.InlineKeyboardButton(text='К прочему ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%B2%D1%8B%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BB%D0%B8%D0%B4%D0%B5%D1%80%D0%B01.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "На лидера страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)


@bot.callback_query_handler(func=lambda call: call.data == 'proch')
def prochee(call):
    markup3 = types.ReplyKeyboardMarkup(row_width=2)
    bth1 = types.KeyboardButton('На выявление лидера 🙋‍♀️')
    bth2 = types.KeyboardButton('С залом 🎤')
    bth3 = types.KeyboardButton('Подвижная 🏃')
    bth4 = types.KeyboardButton('Игры-розыгрыши 🤡')
    bth5 = types.KeyboardButton('Головоломка 🤓')
    bth6 = types.KeyboardButton('Данетки 🤔')
    bth7 = types.KeyboardButton('На пляже 🏖️')
    bth8 = types.KeyboardButton('Игры народов мира 🇰🇬')
    bth9 = types.KeyboardButton('Предложить игру  📝')
    bth10 = types.KeyboardButton('Назад ⬅️')
    bth11 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markup3.add(bth1, bth2, bth3, bth4, bth5, bth6, bth7, bth8, bth9, bth10, bth11)
    bot.send_message(call.message.chat.id, "Выберите пункт меню:", reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == "С залом 🎤")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextzl2')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A1%20%D0%B7%D0%B0%D0%BB%D0%BE%D0%BC1.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "С залом страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

@bot.callback_query_handler(func=lambda call: call.data == 'nextzl2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backzl1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextzl3')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A1%20%D0%B7%D0%B0%D0%BB%D0%BE%D0%BC2.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "С залом страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backzl1')
def igrled(call):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextzl2')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A1%20%D0%B7%D0%B0%D0%BB%D0%BE%D0%BC1.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "С залом страница 1", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl1)


@bot.callback_query_handler(func=lambda call: call.data == 'nextzl3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backzl2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextzl4')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A1%20%D0%B7%D0%B0%D0%BB%D0%BE%D0%BC3.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "С залом страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backzl2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backzl1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextzl3')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A1%20%D0%B7%D0%B0%D0%BB%D0%BE%D0%BC2.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "С залом страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextzl4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backzl3')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextzl5')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A1%20%D0%B7%D0%B0%D0%BB%D0%BE%D0%BC4.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "С залом страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backzl3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backzl2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextzl4')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A1%20%D0%B7%D0%B0%D0%BB%D0%BE%D0%BC3.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "С залом страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextzl5')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backzl4')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextzl6')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A1%20%D0%B7%D0%B0%D0%BB%D0%BE%D0%BC5.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "С залом страница 5", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backzl4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backzl3')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextzl5')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A1%20%D0%B7%D0%B0%D0%BB%D0%BE%D0%BC4.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "С залом страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextzl6')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backzl5')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A1%20%D0%B7%D0%B0%D0%BB%D0%BE%D0%BC6.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "С залом страница 6", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backzl5')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backzl4')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextzl6')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%A1%20%D0%B7%D0%B0%D0%BB%D0%BE%D0%BC5.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "С залом страница 5", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.message_handler(func=lambda message: message.text == "Подвижная 🏃")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextpd2')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%BD%D1%8B%D0%B51.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "Подвижная страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

@bot.callback_query_handler(func=lambda call: call.data == 'nextpd2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backpd1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextpd3')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%BD%D1%8B%D0%B52.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Подвижная страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backpd1')
def igrled(call):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextpd2')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%BD%D1%8B%D0%B51.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Подвижная страница 1", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl1)


@bot.callback_query_handler(func=lambda call: call.data == 'nextpd3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backpd2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextpd4')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%BD%D1%8B%D0%B53.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Подвижная страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backpd2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backpd1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextpd3')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%BD%D1%8B%D0%B52.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Подвижная страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextpd4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backpd3')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%BD%D1%8B%D0%B54.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Подвижная страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backpd3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backpd2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextpd4')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9F%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%BD%D1%8B%D0%B53.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Подвижная страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.message_handler(func=lambda message: message.text == "Данетки 🤔")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextdn2')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%94%D0%B0%D0%BD%D0%B5%D1%82%D0%BA%D0%B81.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "Данетки страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

@bot.callback_query_handler(func=lambda call: call.data == 'nextdn2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backdn1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextdn3')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%94%D0%B0%D0%BD%D0%B5%D1%82%D0%BA%D0%B82.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Данетки страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backdn1')
def igrled(call):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextdn2')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%94%D0%B0%D0%BD%D0%B5%D1%82%D0%BA%D0%B81.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Данетки страница 1", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl1)


@bot.callback_query_handler(func=lambda call: call.data == 'nextdn3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backdn2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextdn4')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%94%D0%B0%D0%BD%D0%B5%D1%82%D0%BA%D0%B83.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Данетки страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backdn2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backdn1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextdn3')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%94%D0%B0%D0%BD%D0%B5%D1%82%D0%BA%D0%B82.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Данетки страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextdn4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backdn3')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%94%D0%B0%D0%BD%D0%B5%D1%82%D0%BA%D0%B84.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Данетки страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backdn3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backdn2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextdn4')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%94%D0%B0%D0%BD%D0%B5%D1%82%D0%BA%D0%B83.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Данетки страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.message_handler(func=lambda message: message.text == "На пляже 🏖️")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnp2')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%BF%D0%BB%D1%8F%D0%B6%D0%B51.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "На пляже страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

@bot.callback_query_handler(func=lambda call: call.data == 'nextnp2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnp1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnp3')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%BF%D0%BB%D1%8F%D0%B6%D0%B52.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "На пляже страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backnp1')
def igrled(call):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnp2')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%BF%D0%BB%D1%8F%D0%B6%D0%B51.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "На пляже страница 1", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl1)


@bot.callback_query_handler(func=lambda call: call.data == 'nextnp3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnp2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnp4')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%BF%D0%BB%D1%8F%D0%B6%D0%B53.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "На пляже страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backnp2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnp1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnp3')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%BF%D0%BB%D1%8F%D0%B6%D0%B52.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "На пляже страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextnp4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnp3')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnp5')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%BF%D0%BB%D1%8F%D0%B6%D0%B54.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "На пляже страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backnp3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnp2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnp4')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%BF%D0%BB%D1%8F%D0%B6%D0%B53.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "На пляже страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextnp5')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnp4')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnp6')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%BF%D0%BB%D1%8F%D0%B6%D0%B55.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "На пляже страница 5", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backnp4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnp3')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnp5')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%BF%D0%BB%D1%8F%D0%B6%D0%B54.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "На пляже страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'nextnp6')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnp5')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%BF%D0%BB%D1%8F%D0%B6%D0%B56.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "На пляже страница 6", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backnp5')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnp4')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnp6')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%9D%D0%B0%20%D0%BF%D0%BB%D1%8F%D0%B6%D0%B55.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "На пляже страница 5", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.message_handler(func=lambda message: message.text == "Игры народов мира 🇰🇬")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnm2')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%98%D0%B3%D1%80%D1%8B%20%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BE%D0%B21.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "Игры народов мира страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

@bot.callback_query_handler(func=lambda call: call.data == 'nextnm2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnm1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnm3')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%98%D0%B3%D1%80%D1%8B%20%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BE%D0%B22.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Игры народов мира страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backnm1')
def igrled(call):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnm2')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%98%D0%B3%D1%80%D1%8B%20%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BE%D0%B21.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Игры народов мира страница 1", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl1)


@bot.callback_query_handler(func=lambda call: call.data == 'nextnm3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnm2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnm4')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%98%D0%B3%D1%80%D1%8B%20%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BE%D0%B23.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Игры народов мира страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backnm2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnm1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnm3')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%98%D0%B3%D1%80%D1%8B%20%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BE%D0%B22.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Игры народов мира страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextnm4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnm3')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnm5')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%98%D0%B3%D1%80%D1%8B%20%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BE%D0%B24.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Игры народов мира страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backnm3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnm2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnm4')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%98%D0%B3%D1%80%D1%8B%20%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BE%D0%B23.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Игры народов мира страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextnm5')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnm4')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnm6')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%98%D0%B3%D1%80%D1%8B%20%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BE%D0%B25.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Игры народов мира страница 5", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backnm4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnm3')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnm5')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%98%D0%B3%D1%80%D1%8B%20%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BE%D0%B24.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Игры народов мира страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'nextnm6')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnm5')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%98%D0%B3%D1%80%D1%8B%20%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BE%D0%B26.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Игры народов мира страница 6", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backnm5')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnm4')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextnm6')
    item3 = types.InlineKeyboardButton(text='К прочим ⬅️', callback_data='proch')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%98%D0%B3%D1%80%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B1%D0%BE%D1%82%D0%B0/%D0%98%D0%B3%D1%80%D1%8B%20%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BE%D0%B25.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Игры народов мира страница 5", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.message_handler(func=lambda message: message.text == "Легенды 🕯️ ➡️")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextleg2')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%9B%D0%B5%D0%B3%D0%B5%D0%BD%D0%B4%D1%8B1.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "Легенды страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

@bot.callback_query_handler(func=lambda call: call.data == 'nextleg2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backleg1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextleg3')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%9B%D0%B5%D0%B3%D0%B5%D0%BD%D0%B4%D1%8B2.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Легенды страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backleg1')
def igrled(call):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextleg2')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%9B%D0%B5%D0%B3%D0%B5%D0%BD%D0%B4%D1%8B1.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Легенды страница 1", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl1)


@bot.callback_query_handler(func=lambda call: call.data == 'nextleg3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backnm2')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%9B%D0%B5%D0%B3%D0%B5%D0%BD%D0%B4%D1%8B3.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Легенды страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backleg2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backleg1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextleg3')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%9B%D0%B5%D0%B3%D0%B5%D0%BD%D0%B4%D1%8B2.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Легенды страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'vog')
def prochee(call):
    markup4 = types.ReplyKeyboardMarkup(row_width=2)
    bth1 = types.KeyboardButton('КТД 🤝 🔐')
    bth2 = types.KeyboardButton('Легенды 🕯️ ➡️')
    bth3 = types.KeyboardButton('Кричалки 💥 ➡️')
    bth4 = types.KeyboardButton('Лагерные песни  🎶 🔐')
    bth5 = types.KeyboardButton('ЭВК 🔗 ➡️')
    bth6 = types.KeyboardButton('Что делать в ситуации ❓  ➡️')
    bth7 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markup4.add(bth1, bth2, bth3, bth4, bth5, bth6, bth7)
    bot.send_message(call.message.chat.id, "Выберите пункт меню:", reply_markup=markup4)



@bot.message_handler(func=lambda message: message.text == "Кричалки 💥 ➡️")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextk2')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%9A%D1%80%D0%B8%D1%87%D0%B0%D0%BB%D0%BA%D0%B81.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "Кричалки страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)

@bot.callback_query_handler(func=lambda call: call.data == 'nextk2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backk1')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%9A%D1%80%D0%B8%D1%87%D0%B0%D0%BB%D0%BA%D0%B82.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Кричалки страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)



@bot.callback_query_handler(func=lambda call: call.data == 'backk1')
def igrled(call):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextk2')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%9A%D1%80%D0%B8%D1%87%D0%B0%D0%BB%D0%BA%D0%B81.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "Кричалки страница 1", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl1)


@bot.message_handler(func=lambda message: message.text == "ЭВК 🔗 ➡️")
def igrled(message):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextj2')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%AD%D0%92%D0%9A1.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(message.chat.id, "ЭВК страница 1", reply_markup=markupi)
    bot.send_message(message.chat.id, text, reply_markup=keyboardl1)
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)


@bot.callback_query_handler(func=lambda call: call.data == 'nextj2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backj1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextj3')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%AD%D0%92%D0%9A2.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "ЭВК страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backj1')
def igrled(call):
    keyboardl1 = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextj2')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl1.add(item2)
    keyboardl1.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%AD%D0%92%D0%9A1.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "ЭВК страница 1", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl1)


@bot.callback_query_handler(func=lambda call: call.data == 'nextj3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backj2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextj4')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%AD%D0%92%D0%9A3.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "ЭВК страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backj2')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backj1')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextj3')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%AD%D0%92%D0%9A2.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "ЭВК страница 2", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'nextj4')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backj3')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%AD%D0%92%D0%9A4.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "ЭВК страница 4", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)


@bot.callback_query_handler(func=lambda call: call.data == 'backj3')
def igrled(call):
    keyboardl2 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='backj2')
    item2 = types.InlineKeyboardButton(text='Далее ➡️', callback_data='nextj4')
    item3 = types.InlineKeyboardButton(text='Для вожатых ⬅️', callback_data='vog')
    markupi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bth1 = types.KeyboardButton('В главное меню  ⬅️⬅️')
    markupi.add(bth1)
    keyboardl2.add(item1,item2)
    keyboardl2.add(item3)
    url = 'https://raw.githubusercontent.com/Nevermans/kislo/main/%D0%94%D0%BB%D1%8F%20%D0%B2%D0%BE%D0%B6%D0%B0%D1%82%D1%8B%D1%85/%D0%AD%D0%92%D0%9A3.txt'
    response = requests.get(url)
    file = io.StringIO(response.text)
    text = file.read()
    bot.send_message(call.message.chat.id, "ЭВК страница 3", reply_markup=markupi)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboardl2)














allowed_users = []
with open("allowed_users.txt", "r") as file:
    for line in file:
        allowed_users.append(line.strip())
        print(allowed_users)

# Меню админисмтратора
@bot.message_handler(func=lambda message: message.text == "!!!")
def prochee(message):
 if message.from_user.username in allowed_users:
    keyboard = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Выключение', callback_data='turn_off')
    item2 = types.InlineKeyboardButton(text='Включение', callback_data='turn_on')
    item3 = types.InlineKeyboardButton(text='Оповещение', callback_data='opov')
    item4 = types.InlineKeyboardButton(text='Перезагрузка', callback_data='reload_bot')
    item5 = types.InlineKeyboardButton(text='Логи', callback_data='send_logs')
    item6 = types.InlineKeyboardButton(text='Предложения пользователей', callback_data='predlojenia')
    item7 = types.InlineKeyboardButton(text='Отзывы', callback_data='report')
    keyboard.add(item1,item4, item2)
    keyboard.add(item5)
    keyboard.add(item7,item6)
    keyboard.add(item3)
    markup00 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup00.add()
    bot.send_message(message.chat.id, text='Вы вошли в панель администратора.', reply_markup=markup00)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=keyboard)
 else:
        bot.send_message(message.chat.id, "You do not have permission to access this menu.")
        save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text) 


#Обработчики меню админа, кнопка Главное меню
@bot.callback_query_handler(func=lambda call: call.data == 'gm')
def main(call):
 if call.from_user.username in allowed_users:
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('Игротека  🤹  ➡️')
    item2 = types.KeyboardButton('Для вожатых 🧙‍♂️ ➡️')
    item3 = types.KeyboardButton('Для выступлений 💃 🔐')
    item4 = types.KeyboardButton('Интерактивная ШВМ  👨‍💻   🔒')
    item5 = types.KeyboardButton('Для лагерей и СПО  💼 ➡️')
    item6 = types.KeyboardButton('О проекте   💡  ➡️')
    item7 = types.KeyboardButton('Материалы на проверке 🔬 🔒')
    item8 = types.KeyboardButton('Знакомство с ботом  ⬅️')
    item9 = types.KeyboardButton('Оставить отзыв ✍')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item9)
    markup.add(item8)
    bot.send_message(call.message.chat.id, "Выберите пункт меню:", reply_markup=markup)
    exit()
 else:
        bot.send_message(call.message.chat.id, "You do not have permission to access this menu.")


# Обработчик меню админа, Выключение
@bot.callback_query_handler(func=lambda call: call.data == "turn_off")
def turn_off(call):
 if call.from_user.username in allowed_users:
    bot.answer_callback_query(callback_query_id=call.id, text="Бот выключен")
    bot.stop_polling()
    subprocess.run(["python3", "turn_on.py"])   
 else:
        bot.send_message(call.message.chat.id, "You do not have permission to access this menu.")


@bot.callback_query_handler(func=lambda call: call.data == 'reload_bot')
def reload_bot_handler(call):
 if call.from_user.username in allowed_users:
    bot.stop_polling()
    subprocess.run(["python3", "kislobotver1.py"])
    bot.answer_callback_query(call.id, text='Бот перезагружен')
 else:
        bot.send_message(call.message.chat.id, "You do not have permission to access this menu.")


import time
@bot.callback_query_handler(func=lambda call: call.data == 'send_logs')
def reload_bot_handler(call):
 if call.from_user.username in allowed_users:
    subprocess.run(["python3", "logs.py"])
    time.sleep(3)
    with open("logs.txt", "r", encoding='utf-8') as file:
        file_contents = file.read()
        bot.send_document(call.message.chat.id, open("messages.txt", "rb"))
        bot.send_document(call.message.chat.id, open("logs.txt", "rb"))
        bot.send_message(call.message.chat.id, file_contents)
 else:
        bot.send_message(call.message.chat.id, "You do not have permission to access this menu.")


@bot.callback_query_handler(func=lambda call: call.data == 'predlojenia')
def reload_bot_handler(call):
 if call.from_user.username in allowed_users:
    bot.send_document(call.message.chat.id, open("Идеи и предложения.txt", "rb"))
 else:
        bot.send_message(call.message.chat.id, "You do not have permission to access this menu.")
        

@bot.callback_query_handler(func=lambda call: call.data == 'report')
def reload_bot_handler(call):
 if call.from_user.username in allowed_users:
    bot.send_document(call.message.chat.id, open("Отзывы.txt", "rb"))
 else:
        bot.send_message(call.message.chat.id, "You do not have permission to access this menu.")



@bot.callback_query_handler(func=lambda call: call.data == 'opov')
def handle_offer(call):
 if call.from_user.username in allowed_users:
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Написать оповещение ✍', callback_data='offerop')
    item2 = types.InlineKeyboardButton(text= 'Отправить оповещение 📩', callback_data='sendop')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(call.message.chat.id, text='Нажмите кнопку "Написать оповещение ✍" если хотите написать оповещение всем или кнопку "Отправить оповещение 📩" если вы его уже написали', reply_markup=markup)
 else:
        bot.send_message(call.message.chat.id, "You do not have permission to access this menu.")

IDStatusop = {}

@bot.callback_query_handler(func=lambda call: call.data == 'offerop')
def handle_offer_callback(call):
 if call.from_user.username in allowed_users:
    IDStatuso[call.from_user.username] = False
    IDStatus[call.from_user.username] = False
    IDStatusop[call.from_user.id] = True
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel_offerop')
    markup.add(item1)
    bot.send_message(call.message.chat.id, 'Напишите в чат оповещение', reply_markup=markup)
 else:
        bot.send_message(call.message.chat.id, "You do not have permission to access this menu.")

    
@bot.message_handler(func=lambda message: message.text and IDStatusop.get(message.from_user.id, False))
def handle_message_for_op(message):
 if message.from_user.username in allowed_users:
    user_message = message.text
    filename = 'Оповещение.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        pass
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(user_message + '\n')
    IDStatusop[message.from_user.username] = False
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Отложить 🕗', callback_data='wait')
    item2 = types.InlineKeyboardButton(text='Отправить оповещение 📩', callback_data='sendop')
    item3 = types.InlineKeyboardButton(text='Переписать оповещение ✍', callback_data='offerop')
    markup.add(item1)
    markup.add(item3)
    markup.add(item2)
    with open(filename, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    bot.send_message(message.chat.id, text="Вы написали оповещение:\n" + file_contents, reply_markup=markup)
 else:
        bot.send_message(message.chat.id, "You do not have permission to access this menu.")

@bot.callback_query_handler(func=lambda call: call.data == 'cancel_offerop')
def handle_cancel_offer_callback(call):
 if call.from_user.username in allowed_users:
    bot.send_message(call.message.chat.id, 'Вы больше не пишете')
    IDStatusop[call.from_user.id] = False
 else:
        bot.send_message(call.message.chat.id, "You do not have permission to access this menu.")

@bot.callback_query_handler(func=lambda call: call.data == 'sendop')
def handle_cancel_offer_callback(call):
 if call.from_user.username in allowed_users:
    # read the user_ids from the file "users.txt"
    with open("users.txt") as f:
        user_ids = [int(line.strip()) for line in f]

    # read the message from the file "Оповещение.txt"
    with open("Оповещение.txt", encoding='utf-8') as f:
        message = f.read()

    # iterate over all user_ids and send the message
    for user_id in user_ids:
        bot.send_message(chat_id=user_id, text=message)
    bot.send_message(call.message.chat.id, "Вы отправили оповещение всем")
 else:
        bot.send_message(call.message.chat.id, "You do not have permission to access this menu.")

@bot.callback_query_handler(func=lambda call: call.data == 'wait')
def handle_cancel_offer_callback(call):
 if call.from_user.username in allowed_users:
    bot.send_message(call.message.chat.id, 'Оповещение отложено, что бы отправить его нажмите кнопку "Отправить оповещение 📩" в любой момент ')
    IDStatusop[call.from_user.id] = False
 else:
        bot.send_message(call.message.chat.id, "You do not have permission to access this menu.")


# @bot.message_handler(commands=['send_photo'])
# def send_photo(message):
#     # Open the image file
#     file = open("image.png", "rb")
#     # Send the image
#     bot.send_photo(chat_id=message.chat.id, photo=file)

# Обработчик всех сообщений которые не имеют функций
@bot.message_handler(func=lambda message: message.text)
def nodata(message):
    bot.send_message(message.chat.id, "No data..." )
    save_and_echo(message)
def save_and_echo(message):
    save_message(message.from_user.username, message.text)    
bot.polling()