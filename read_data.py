# модуль экспорта данных 
import json
def read_data():
    lst_name = []
    with open('name.json', 'r') as file:
        all = json.load(file)
        for line in all:
            temp = list(line.values())
            lst_name.append(temp)
        print(lst_name)
    lst_adress = []
    with open('adress.json', 'r') as file:
        all = json.load(file)
        for line in all:
            temp = list(line.values())
            lst_adress.append(temp)
        print(lst_adress)

    lst_class = []
    with open('class.json', 'r') as file:
        all = json.load(file)
        for line in all:
            temp = list(line.values())
            lst_class.append(temp)
        print(lst_class)

    lst = []
    for i in range(len(lst_name)):
        lst.append([str(lst_name[i][0]), str(lst_name[i][1]), str(lst_name[i][2]), str(lst_name[i][3]), str(lst_name[i][4]), \
            str(lst_class[i][1]), str(lst_class[i][2]), \
            str(lst_adress[i][1]), str(lst_adress[i][2]), str(lst_adress[i][3]), str(lst_adress[i][4]), str(lst_adress[i][5])])
    return lst



