def print_data(data):
    str = ''
    if len(data) > 0:
        str = str + "id".center(5) + "Фамилия".center(20) + "Имя".center(10) + "Класс".center(6) + "Статус".center(6)\
           + "Ряд".center(4) + "Парта".center(6)\
           + "Город".center(15) + "Улица".center(15) + "Дом".center(6) + "Квартира".center(4) + "Примечание".center(20)
        str = str + "-"*120
        for item in data:
            str = str + item[0].center(5) + item[1].center(20) + item[2].center(10) + item[3].center(6) + item[4].center(6)\
           + item[5].center(4) + item[6].center(6)\
           + item[7].center(15) + item[8].center(15) + item[9].center(6) + item[10].center(4) + item[11].center(20)
    else:
        str = str + "\n"
        str = str + "*"*100 + "\nСправочник пуст!\n" + "*"*100
        str = str + "\n"
    return str