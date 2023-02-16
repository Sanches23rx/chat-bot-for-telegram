from re import S
import string
import telebot
from telebot import types
from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot("5727198024:AAHzxiWY4fcMzOhRX3YLUlqY8FdMzuN8vJc")

a = int(0)
aa = int(0)
b = int(0)
c = int(0)
ga = []
gb = []
gc = []
login = []
password = []

#@bot.send_message(message.chat.id, text="Здравствуйте, {0.first_name} напишите start")

@bot.message_handler(commands=['start']) #Начальное меню
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Посмотреть расписание")
    btn2 = types.KeyboardButton("Записаться на урок")
    btn3 = types.KeyboardButton("Отменить запись")
    btn4 = types.KeyboardButton("Авторизация")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Здравствуйте, {0.first_name}! Я виртуальный помощник для записи на занятия\nВыберите что необходимо сделать".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text']) #Запись
def func(message):
    if(message.text == "Посмотреть расписание"):
        bot.send_message(message.chat.id, text="Вот тебе готовое расписание\n")
        global a
        global b
        global c
        if a == 1:
            bot.send_message(message.chat.id, text="10:00 - Занято❌\n")
        else:
            bot.send_message(message.chat.id, text="10:00 - Свободно✅\n")
        if b == 1:
            bot.send_message(message.chat.id, text="11:00 - Занято❌\n")
        else:
            bot.send_message(message.chat.id, text="11:00 - Свободно✅\n")
        if c == 1:
            bot.send_message(message.chat.id, text="12:00 - Занято❌\n")
        else:
            bot.send_message(message.chat.id, text="12:00 - Свободно✅\n")

    elif(message.text == "Записаться на урок"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("10:00")
        btn2 = types.KeyboardButton("11:00")
        btn3 = types.KeyboardButton("12:00")
        back1 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back1)
        bot.send_message(message.chat.id, text="Выберете подходящее время", reply_markup=markup)
    elif(message.text == "Отменить запись"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butn1 = types.KeyboardButton("10-00")
        butn2 = types.KeyboardButton("11-00")
        butn3 = types.KeyboardButton("12-00")
        back1 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(butn1, butn2, butn3, back1)
        bot.send_message(message.chat.id, text="Выберете время для отмены записи", reply_markup=markup)
    
    elif(message.text == "10:00"):
        if a == 0:
            bot.send_message(message.chat.id, text="Записал на 10:00, Напишите Фамилию и Имя")
            bot.send_message(488838956, text="Записались на 10:00")
        else:
            bot.send_message(message.chat.id, text="Время занято")
        a = 1
    
    elif(message.text == "10-00"):
        if a == 1:
            bot.send_message(message.chat.id, text="Отменил на 10:00, Напишите Фамилию и Имя")
            bot.send_message(488838956, text="Отменились на 10:00")
        else:
            bot.send_message(message.chat.id, text="Время свободно")
        a = 0

    elif (message.text == "11:00"):
        if b == 0:
            bot.send_message(message.chat.id, text="Записал на 11:00, Напишите Фамилию и Имя")
            bot.send_message(488838956, text="Записались на 11:00")
        else:
            bot.send_message(message.chat.id, text="Время занято")
        b = 1

    elif(message.text == "11-00"):
        if b == 1:
            bot.send_message(message.chat.id, text="Отменил на 11:00, Напишите Фамилию и Имя")
            bot.send_message(488838956, text="Отменились на 11:00")
        else:
            bot.send_message(message.chat.id, text="Время свободно")
        b = 0

    elif message.text == "12:00":
        if c == 0:
            bot.send_message(message.chat.id, text="Записал на 12:00, Напишите Фамилию и Имя")
            bot.send_message(488838956, text="Записались на 12:00")
        else:
            bot.send_message(message.chat.id, text="Время занято")
        c = 1

    elif(message.text == "12-00"):
        if c == 1:
            bot.send_message(message.chat.id, text="Отменил на 12:00, Напишите Фамилию и Имя")
            bot.send_message(488838956, text="Отменились на 12:00")
        else:
            bot.send_message(message.chat.id, text="Время свободно")
        c = 0

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Посмотреть расписание")
        button2 = types.KeyboardButton("Записаться на урок")
        button3 = types.KeyboardButton("Отменить запись")
        button4 = types.KeyboardButton("Авторизация")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif(message.text == "Авторизация"): #?????
        global login
        global password
        bot.send_message(message.chat.id, text="Введите ФИО")
        bot.register_next_step_handler(message.chat.id)
        if message.text in login: #Идентификация
            bot.send_message(message.chat.id, text="Введите пароль") 
            if message.text in password: #Аутентификация
                bot.send_message(message.chat.id, text="Вы успешно вошли в систему✅")
            else:
                bot.send_message(message.chat.id, text="Попробуйте еще раз")
        else:
            bot.send_message(message.chat.id, text="Пожалуйста зарегестрируйтесь")

    elif(message.text == "admin"):
        bot.send_photo(message.chat.id, photo = ("https://s0.rbk.ru/v6_top_pics/media/img/0/10/756372136012100.jpg"))
    
    else:
        bot.send_message(message.chat.id, text="Если выбрали своё время то\nНапишите Имя\nЕсли написали Имя - на этом всё\n\nДля создания новой записи нажмите /start")
        global ga
        global gb
        global gc
        if message.text in ga:
            #bot.send_message(message.chat.id, text="команда выполнена")
            ga.remove(message.text)
            bot.send_message(488838956, message.text)
            print(ga)
        else:
            ga.append(message.text)
            bot.send_message(488838956, message.text)
            print(ga, "ga")
        if message.text in gb:
            #bot.send_message(message.chat.id, text="команда выполнена")
            gb.remove(message.text)
            bot.send_message(488838956, message.text)
            print(gb)
        else:
            gb.append(message.text)
            bot.send_message(488838956, message.text)
            print(gb, "gb")
        if message.text in gc:
            #bot.send_message(message.chat.id, text="команда выполнена")
            gc.remove(message.text)
            bot.send_message(488838956, message.text)
            print(gc)
        else:
            gc.append(message.text)
            bot.send_message(488838956, message.text)
            print(gc, "gc")

bot.polling(none_stop=True)
