"""
4. Имеется строка, содержащая имена через запятую «Tim,John,Sally,Trevor,Harry» и соответствующий именам кортеж содержащий возраст (12,34,24,57,18)
Создать новый словарь, который будет иметь следующую структуру
Ключ — сгенерированое шестизначное число, значения — словарь который состоит из 2 ключей «name» и «age» с соответствующими значениями из строки с именами и кортежа с возрастами, например
{
	'127492': {
			'name': 'Tim',
			'age': 12
		},
	'538956': {
		…..
}
Сохранить итоговый словарь в виде json файла
"""
import random
import json

name = "Tim", "John", "Sally", "Trevor", "Harry"
age = (12, 34, 24, 57, 16)
keys = random.randint(99999, 999999)
zipped = dict(zip(name, age))
with open("/home/fr3zing/python/Courses/Courses/lesson8/task_8_4.json", mode="w") as file:
    js = {keys}
    js_name_value = {"name": age}
    js.update(js_name_value)
    json.dump(js, file, indent=4)