a = "красный,белый,черный,красный,зеленый,черный"
# a = input("Введите последовательность цветов:")
a = sorted(set(a.split(",")))
print(a)
