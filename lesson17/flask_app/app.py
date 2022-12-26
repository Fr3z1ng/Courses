from flask import Flask
from app1.views import app1


def create_app():
    """
    Создание приложение Flask
    """
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    app.register_blueprint(app1)
    return app


if __name__ == '__main__':
    create_app().run() # Запуск приложения Flask
