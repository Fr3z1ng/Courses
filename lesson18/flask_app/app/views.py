from flask import Blueprint, render_template, request, abort
import requests
from .validation import Validator, Validation  # добавление задания 13.3

app1 = Blueprint('app1', __name__)


@app1.route('/quote')
def quote():
    """
    Вывод цитаты Кани Веста взависимости от введенных данных, /quote&number=3 - выводит 3 цитаты и т.д.
    """
    quotes = None  # определил переменную для определения есть ли передача цитат или нет
    for value in dict(request.args).values():
        quotes = value
    some_list = []  # пустой список по которому буду проходить в Jinja что бы показывать определенное кол-во цитат
    if quotes is None:  # если не приходит ни одна цитата,то по условию вывести одну цитату
        src = requests.get('https://api.kanye.rest')
        for value in src.json().values():
            some_list.append(value)
        return render_template("index.html", some_list=some_list)
    elif int(quotes) > 0:  # если цитаты все таки есть,то посчитать их кол-во для вывода определенного кол-ва цитат
        i = 1
        while i <= int(quotes):  # использую цикл while,что бы запрашивать каждый раз новую цитату
            src = requests.get('https://api.kanye.rest')
            for value in src.json().values():
                some_list.append(value)
            i += 1
        return render_template("index.html", some_list=some_list)


@app1.route('/register', methods=["POST", "GET"])
def register():
    username = None
    password = None
    email = None
    if request.method == 'POST':  # проверяю является ли данный запрос POST
        src = dict(request.form)  # забираю введенные данные пользователя в форме
        for key, value in src.items():  # присваиваю переменным их значения для валидации введенных данных
            if key == 'username':
                username = value
            elif key == 'password':
                password = value
            elif key == 'email':
                email = value
        validator_1 = Validator(username, password, email)  # создаю объект из 13.3 домашнего задания
        try:
            if validator_1.validation():  # если проходит валидацию до вызываю код 405,что персональные данные отработаны
                abort(405)
        except Validation:  # если не прошли валидацию вывожу код 406,что валидация не пройдена
            abort(
                406)  # без подключеня render_template, код 406 выводился в f-строке,но когда приходит ошбика в except, то в Jinja код 406 не срабатывает и сразу выкидывает ошибку
    return render_template('register.html')


@app1.errorhandler(405)
def valid_accept(error):
    """
    Обработка кода 405
    """
    return render_template('error405.html')


@app1.errorhandler(406)
def valid_error(error):
    """
    Обработка кода 406
    """
    return f"Valid_error"
