from write_data import count_data
Id = count_data("name.json")
def input_data_uch():
    dct = dict()
     
    dct["id"] = Id     
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["class"] = input('Введите Класс: ')
    dct["status"] = input('Введите Статус: ')
    return dct

def input_data_adr():
    dct = dict()
    #Id = count_data("name.json") 
    dct["id"] = Id     
    dct["city"] = input('Введите Город: ')
    dct["street"] = input('Введите Улица: ')
    dct["house"] = input('Введите Дом: ')
    dct["apartament"] = input('Введите Квартира: ')
    dct["other"] = input('Введите Примечание: ')
    return dct

def input_data_cl():
    dct = dict()
    #Id = count_data("name.json") 
    dct["id"] = Id     
    dct["row"] = input('Введите Ряд: ')
    dct["col"] = input('Введите Номер парты: ')
    return dct