"""
2. Создать скрипт который получает от пользователя 4 строки с данными (данные произвольные)
Создать файл и записать в него первые 2 строки (после данной операции закрыть файл)
Преобразовать оставшиеся 2 строки в строки в верхнем регистре и добавить их в созданный файл
В итоговом файле должно быть 4 строки каждая из которых оканчивается символом « | » и начинается с новой строки
"""
a = "Привет"
b = "Саша"
c = "это"
d = 'python'
with open("task_8_2.txt", mode="w") as file:
    data = [a, b]
    for line in data:
        file.write(line + "|\n")
with open("task_8_2.txt", mode="a") as file:
    data = [c, d]
    for line in data:
        file.write(f"{line.title()}" + "|\n")
"""
Только не понял нужно записывать что бы 2 строки должны быть в верхнем регистер или нет
"""
