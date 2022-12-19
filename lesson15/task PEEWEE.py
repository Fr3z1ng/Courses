from peewee import *

titles = input('Введите альбом: ')


def database_info(titles: str) -> list:
    """
    Функция подключается к БД и выводит все треки введенного альбома
    """
    conn = SqliteDatabase('chinook.db') # подключение к БД
    cursor = conn.cursor() # для перехода по записям
    cursor.execute(f"SELECT Name FROM tracks WHERE AlbumID = (SELECT AlbumID FROM albums WHERE Title = '{titles}')")
    result = cursor.fetchall() # заносим в переменную все совпадения
    conn.close()
    return result


print(database_info(titles))
