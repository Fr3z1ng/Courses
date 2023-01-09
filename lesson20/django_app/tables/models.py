from django.db import models
from .validations import validate_login, validate_email


class User(models.Model):
    "Модель User"
    id = models.IntegerField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    login = models.TextField(validators=[validate_login])  # Валидация логина не меньше 6 символов
    email = models.TextField(validators=[validate_email])  # Валидация почты
    register = models.TextField(max_length=10)

    def __str__(self):
        return f"Имя:{self.first_name}/Фамилия:{self.last_name}"  # Переопределяю вывод модели User


class Category(models.Model):
    """
    Модель Category
    """
    category_id = models.IntegerField(primary_key=True)
    category_title = models.TextField()

    def __str__(self):
        return f"Название: {self.category_title}" # Переопределяю вывод модели Category


class Post(models.Model):
    """
    Модель Post
    """
    title = models.TextField()
    data_created = models.TextField(max_length=10)
    content = models.TextField(max_length=140)
    post_author_id = models.ForeignKey(User, on_delete=models.CASCADE) # При удалении пользователя удаляется все посты связанные с пользователем
    post_category_id = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL) # При удалении категории устанавливается в постах NULL вместо категории

    def __str__(self):
        return f"Название:{self.title}/Дата создания: {self.data_created}/{self.post_category_id}"#  Переопределяю вывод модели Post
