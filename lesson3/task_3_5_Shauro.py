a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")
b = b[::-1]
c = a[1:-1] + b[1:-1]
print(c)