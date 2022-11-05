str_1 = "Саша"
str_2 = "Паша"
str_3 = "Даша"
"""
Ответ на второе условие все три условия ниже
"""
set_1 = set(str_1)
set_2 = set(str_2)
set_3 = set(str_3)

answer_1 = set_1 & set_2 & set_3
print("Ответ на первое условие", answer_1)
answer_2 = (set_1 ^ set_2) | (set_2 ^ set_3)
print("Ответ на третье условие", answer_2)
