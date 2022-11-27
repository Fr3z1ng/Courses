"""
3. Откройте файл «unsorted_names.txt» содержащий имена студентов.
Прочитайте данные, отсортируйте их и запишите в новый файл «sorted_names.txt» (каждое имя начинается с новой строки
_______
Aaron
Adrian
…..
Wiley
________
"""
with open("unsorted_names.txt", mode="r") as file:
    src = file.readlines()
src.sort()
sorted_name = []
for i in src:
    sorted_name.append(i)
print(sorted_name)
with open("sorted_names.txt", mode="w") as file:
    for item in sorted_name:
        file.writelines(item.strip("\n") + "\n")
