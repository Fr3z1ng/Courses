"""
1) Создайте интерактивный калькулятор.
Пользовательский ввод представляет собой формулу, состоящую из числа, оператора (+,-,*,/,**) и другого числа, разделенных пробелом (например, 1 + 1). Проверьте input по следующим правилам:
1. Если входные данные не состоят из 3 действительных элементов, вызовите InputFormulaError, которая является пользовательским исключением.
2. Если первый и третий элемент не являются действительными числами — выводится ошибка InputNumberError.
3. Если второй элемент не соответствует поддерживаемым операторам — выводится ошибка InputOperatorError.
Если ввод верен, выполните вычисление и выведите результат (в случае возникновения ошибки при вычислении — также выводим ее). Затем пользователю предлагается ввести новый ввод и так далее, пока пользователь не введет quit.

Взаимодействие может выглядеть так:
1 + 1
Вывод: 2.0
3,2 - 1,5
Вывод: 1.70
quit
"""


class InputFormulaError(Exception):
    pass


class InputNumberError(Exception):
    pass


class InputOperatorError(Exception):
    pass


while True:
    values = input("Введите данные в виде (1 + 1) с любым операторам (+,-,*,/,**):").lower()
    storage_operand = ["*", "+", "-", "/", "**"]
    storage = values.split(" ")
    try:
        if len(storage) > 3:
            raise InputFormulaError
        elif values == "quit":
            break
        elif isinstance(storage[0], None | bool) or isinstance(storage[2], None | bool):
            raise InputNumberError
        elif storage[1] not in storage_operand:
            raise InputOperatorError
    except InputOperatorError as error:
        print(f"Произошла ошибка попробуйте еще раз или напишите 'quit' ")
    except InputFormulaError as error:
        print(f"Произошла ошибка попробуйте еще раз или напишите 'quit' ")
    except InputNumberError as error:
        print(f"Произошла ошибка попробуйте еще раз или напишите 'quit' ")


    def calculator(storage: list) -> float | InputFormulaError | InputNumberError | InputOperatorError:

        first = float(storage[0])
        second = float(storage[2])
        if storage[1] == "+":
            return first + second
        elif storage[1] == "-":
            return first - second
        elif storage[1] == "**":
            return first ** second
        elif storage[1] == "/":
            return first / second
        elif storage[1] == "*":
            return first * second


    print(calculator(storage))
