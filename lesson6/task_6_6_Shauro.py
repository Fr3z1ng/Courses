"""
6. Создайте функцию которая работает так же как str.split() метод (естественно, без использования str.split())
"""
s = "I,love,Python"
sep = input("Введите разделитель: ")


def split_func(s: str, sep: str):
    """
    функция - замена методу split()
    """
    split_value = []
    word = ''
    for c in s:
        if c == sep:
            split_value.append(word)
            word = ''
        else:
            word += c
    if word:
        split_value.append(word)
    return split_value


print(split_func(s, sep))
