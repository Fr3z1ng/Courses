a = input("Введите строку: ")
b = input("Введите символ,который желаете искать в строке")
start = -1
count = 0
while True:
    start = a.find(b, start + 1)
    if start == -1:
        break
    else:
        count += 1
print("Вхождений в строке символа:", count)
