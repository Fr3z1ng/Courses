"""
*4. Создайте программу которая генерирует случайное число в интервале от 1 до 100 и предлагает пользователю угадать это число.
 В случает ввода от пользователя инструкции «stop», завершает работу и выводит загаданное число
для генерации случайного числа используйте метод randint модуля random
"""
from random import randint


def random_game() -> None:
    """
    Проходит валидация на попадание пользователем в нужное число
    """
    n = randint(0, 10)
    while True:
        guess = input("Введите число или команду 'stop': ")
        if guess.lower() == "stop":
            print(f"Users say 'stop'")
            break
        elif n > int(guess):
            print(f"Your number less")
        elif n < int(guess):
            print(f"Your number greater")
        elif n == int(guess):
            print(f"Your guess number, Congratulations")
            break


random_game()
