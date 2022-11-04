def calculations(a: int, b: int, c: str) -> float:
    """По выбору пользователем операции,происходит определенный подсчет"""
    if c == "+":
        return float(a + b)
    elif c == "-":
        return float(a - b)
    elif c == "*":
        return float(a * b)
    elif c == "//":
        return float(a // b)
    elif c == "%":
        return float(a % b)
    elif c == "**":
        return float(a ** b)
    else:
        return "Введен неправильный символ"


a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
c = input("Введите операцию,которую желаете сделать (+, - , * , // , % , **)")
print(calculations(a, b, c))
