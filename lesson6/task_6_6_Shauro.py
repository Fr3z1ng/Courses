"""
6. Создайте функцию которая работает так же как str.split() метод (естественно, без использования str.split())
"""
s = "I,love,Python"
# sep = input("Введите разделитель: ")
list_1 = []
for i in s:
    list_1.append(i.replace(",", " "))

print(list_1)

# s = s.split(",")
# print(s)

# def split_func(s: str, sep: str):
#     s = s.replace(" ", sep)
#     print(s)
#
#
# split_func(s, sep)
