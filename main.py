import telebot
from read_data import *
from print_data import *
from push_data import *
from search_data import *
from write_data import count_data
#import logger as log
import json
from telebot import types
dct_uc = dict()
dct_ad = dict()
dct_cl = dict()
bot = telebot.TeleBot('5717359870:AAGXGSbIuGJ4pgWkJkTkbhuzLQqZmGqUzC8')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        msg = "Что желаем сделать:\n\
        1 - получить всю информацию о учениках;\n\
        2 - добавить ученика;\n\
        3 - поиск ученика;\n\
        4 - выход."
        bot.send_message(message.from_user.id, msg)
        bot.register_next_step_handler(message, get_number); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')

def get_number(message):
    global ch
    ch = message.text
    if ch == '1':
        data = read_data()
        str = print_data(data)
        bot.send_message(message.from_user.id, str)
    elif ch == '2':
        #push_data()
        global dct_uc
       
        Id = count_data("name.json")
        
        dct_uc["id"] = Id  
        bot.send_message(message.from_user.id, 'Введите Фамилию: ')
        bot.register_next_step_handler(message, get_surname)
    elif ch == '3':
        bot.send_message(message.from_user.id, 'Введите данные для поиска: ')
        bot.register_next_step_handler(message, get_info)
                 
        #start()
    elif ch == '4':
        bot.send_message(message.from_user.id, 'Сеанс окончен, до свидания!')
    else:
        bot.send_message(message.from_user.id, 'Введите корректную цифру!')
        start()
    #bot.send_message(message.from_user.id, 'Введите второе число')
    #bot.register_next_step_handler(message, get_value_b);


def get_info(message):
    info = message.text
    data = read_data()
    item = search_data(info, data)
    if item != None:
        str = print_data(item)
        bot.send_message(message.from_user.id, str)
    else:
        bot.send_message(message.from_user.id, "Данные не обнаружены")       
def get_surname(message):
    global dct_uc
    dct_uc["surname"] = message.text
    bot.send_message(message.from_user.id, 'Введите Имя: ')
    bot.register_next_step_handler(message, get_name)
def get_name(message):
    global dct_uc
    dct_uc["name"] = message.text
    bot.send_message(message.from_user.id, 'Введите класс: ')
    bot.register_next_step_handler(message, get_class)
def get_class(message):
    global dct_uc
    dct_uc["class"] = message.text
    bot.send_message(message.from_user.id, 'Введите статус: ')
    bot.register_next_step_handler(message, get_status)  
def get_status(message):
    global dct_uc
    dct_uc["status"] = message.text
    bot.send_message(message.from_user.id, 'Введите город: ')
    bot.register_next_step_handler(message, get_city)      
def get_city(message):
    global dct_ad
    Id = count_data("name.json") 
    dct_ad["id"] = Id     
    dct_ad["city"] = message.text
    bot.send_message(message.from_user.id, 'Введите улицу: ')
    bot.register_next_step_handler(message, get_street)    
def get_street(message):
    global dct_ad
    dct_ad["street"] = message.text
    bot.send_message(message.from_user.id, 'Введите дом: ')
    bot.register_next_step_handler(message, get_house) 
def get_house(message):
    global dct_ad
    dct_ad["house"] = message.text
    bot.send_message(message.from_user.id, 'Введите квартиру: ')
    bot.register_next_step_handler(message, get_apartament) 
def get_apartament(message):
    global dct_ad
    dct_ad["apartament"] = message.text
    bot.send_message(message.from_user.id, 'Введите примечание: ')
    bot.register_next_step_handler(message, get_other) 
def get_other(message):
    global dct_ad
    dct_ad["other"] = message.text
    bot.send_message(message.from_user.id, 'Введите ряд: ')
    bot.register_next_step_handler(message, get_row) 
def get_row(message):
    global dct_cl
    Id = count_data("name.json") 
    dct_cl["id"] = Id     
    dct_cl["row"] = message.text
    bot.send_message(message.from_user.id, 'Введите номер парты: ')
    bot.register_next_step_handler(message, get_col)  
def get_col(message):
    global dct_cl
    Id = count_data("name.json") 
    dct_cl["id"] = Id     
    dct_cl["col"] = message.text
    write_data(dct_uc, "name.json")
    write_data(dct_ad, "adress.json")
    write_data(dct_cl, "class.json")
    bot.send_message(message.from_user.id, 'Ученик сохранен в базу')
    #bot.register_next_step_handler(message, get_col)     

print('server start')
bot.polling()