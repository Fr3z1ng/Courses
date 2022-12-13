"""
1. Создайте генераторную функцию которая в качестве аргумента принимать путь к файлу «unsorted_names.txt» и букву английского алфавита, открывает файл по данному пути и генерирует последовательность из имен начинающихся на указанную букву
names_with_letter = names_gen(«unsorted_names.txt», «A»)
next(names_with_letter)
Amelia
next(names_with_letter)
Adrienne
или
for name in names_with_letter:
	print(i, end=““)
Amelia
Adrienne

"""
path = "names.txt"
letter = input("Enter letter: ")


def names_with_letter(path, letter):
    """
    генератор для чтения файла и который выводит все файлы начинающийся на введенный символ
    """
    with open(path, mode="r") as file:
        for line in file:
            if line.startswith(letter.upper()):
                yield line


for i in names_with_letter(path, letter):
    print(i)
