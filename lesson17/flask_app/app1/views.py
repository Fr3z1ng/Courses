from flask import Blueprint, render_template
from datetime import datetime
import requests

app1 = Blueprint('app1', __name__)


@app1.route('/times')
def times():
    """
    Передача реального времени,но не понял в интернете в каком формате точно выводить,куча информации было
    """
    current_times = datetime.now().date()
    return f"<h3><font color=green> {str(current_times)} </font></h3>"


@app1.route('/quote')
def quote():
    """
    Вывод цитаты Кани Веста,сделал без скобок,так как бесили меня
    """
    src = requests.get('https://api.kanye.rest')
    return f"<h3><font color=red> {src.text[1:-1]} </font></h3>"
# Пробовал подключать шаблоны,но как-то с выводом информации немного не задалось
