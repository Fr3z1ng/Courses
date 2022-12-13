"""
2) Создайте класс Validator который позволяет проводить проверку данных пользователя при регистрации передаваемых в виде кортежа (login, password, email)
В данном классе реализовать метод validate(user_data), который позволяет проверить передаваемый кортеж по правилам:
login — не менее 6 символов
password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)
email — присутствует символ @, оканчивается . и 2 символами (.by)
Валидация каждого элемента в кортеже производится отдельным методом для каждого элемента (validate_email, validate_login, validate_password)
в которых в случае непрохождения валидации вызывается ошибка (InvalidPassword, InvalidLogin, InvalidEmail), при соответствии — возвращается значение True.
 В методе validate необходимо предусмотреть обработку этих ошибок и в случае их наличия — вызвать ошибку ValidationError.
"""
import re
import string

"""
пытался сделать валидацию пароля через регулярные выражения,но не вышло
# password = "sashaSHuauro#"
# pattern = r"[a-zA-Z0-9#]"


# if string.punctuation in password:
#     print("Лучший")
"""


class InvalidLogin(Exception):
    pass


class InvalidPassword(Exception):
    pass


class InvalidEmail(Exception):
    pass


class Validation(Exception):
    pass


class Validator:
    """
    Класс принимает логин,пароль,email и делает валидацию этих аргументов
    """

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def validate_email(self):
        """
        Метод делает валидацию на проверку email
        """
        if "@" in self.email and self.email.endswith(".by") or self.email.endswith(".ru"):
            return True
        else:
            raise InvalidEmail

    def validate_login(self):
        """
        Метод делает валидацию на проверку логина
        """
        if len(self.login) > 6:
            return True
        else:
            raise InvalidLogin

    def validate_password(self):
        """
        Метод делает валидацию на проверку пароля
        """
        if len(self.password) < 8 or len(set(self.password) & set(string.ascii_lowercase)) < 1 or len(
                set(self.password) & set(string.ascii_uppercase)) < 1 or len(
            set(self.password) & set(string.punctuation)) < 1:
            raise InvalidPassword
        else:
            return True

    def validation(self):
        """
        Метод принимает другие методы и если в них случаются ошибки обрабатывает их и выводит собственную ошибку
        """
        try:
            self.validate_email()
            self.validate_login()
            self.validate_password()
        except (InvalidLogin, InvalidPassword, InvalidEmail):
            raise Validation


valid_1 = Validator("Sasha123", "sashaShauro#", "sobaka@mail.by")
valid_1.validation()
