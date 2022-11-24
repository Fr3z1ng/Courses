"""
5. Открыть файл из п.4. Создать функцию ('transform_to_csv') которая будет выполнять следующее:
каждую запись в json файле функция будет преобразовывать в строку с данными
в виде name,age,id (например, Tim,12,127492) и сохранять все данные в виде csv файла
Путь к json файлу и имя сохраняемого csv файла должно запрашиваться у пользователя
"""
import json
import csv

json_name = input("Введите имя файла JSON(если же он находится в вашей корневой папке, то просто название: ")
with open(f"{json_name}.json", mode="r") as file:
    json_string = json.load(file)


def transform_to_csv(json_string: str):
    """
    Функция принимают JSON файл и делает преобразование в CSV файл
    """
    names = [] #список для записи имен
    ages = [] #список для записи возраста
    id_s = [] #список для записи ключей
    for key, value in json_string.items():
        id_s.append(key)
        for first, second in value.items():
            if first == "name": # проверяем если значение равно "name" добавляем имя в список имен
                names.append(second)
            else:
                ages.append(second) # если не равно значение "name" добавляем возраст в список возраста

    obj_list = list(zip(names, ages, id_s)) # объединяем все в кортеж для удобства записи
    csv_name = input('Введите название CSV файла в который желаете сохранить данные:')
    with open(f"{csv_name}.csv", mode="w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(["name", "age", "id"]) # создаем заголовки
        for i in obj_list:
            csv_writer.writerow(list(i)) # добавляем под каждым заголовком нужную информацию


if __name__ == '__main__':
    transform_to_csv(json_string)
