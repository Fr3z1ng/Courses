s = input("Введите строку:")
s = s.lower().strip()
s = s.capitalize()
part_1 = s[:s.rfind(" ") + 1]
part_2 = s[s.rfind(" ") + 1:]
part_2 = part_2.capitalize()
answer = part_1 + part_2
print(answer)

