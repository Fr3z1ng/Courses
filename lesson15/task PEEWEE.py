from peewee import *

# titles = input('Введите альбом: ')

# def database_info(titles: str) -> list:
#     """
#     Функция подключается к БД и выводит все треки введенного альбома
#     """
#     conn = SqliteDatabase('chinook.db') # подключение к БД
#     cursor = conn.cursor() # для перехода по записям
#     cursor.execute(f"SELECT Name FROM tracks WHERE AlbumID = (SELECT AlbumID FROM albums WHERE Title = '{titles}')")
#     result = cursor.fetchall() # заносим в переменную все совпадения
#     conn.close()
#     return result
db = SqliteDatabase('chinook.db')


class BaseModel(Model):
    class Meta:
        database = db


class Albums(BaseModel):
    title = CharField(column_name='Title')
    album_id = AutoField(column_name='AlbumID')

    class Meta:
        table_name = 'albums'


class Track(BaseModel):
    name = CharField(column_name='Name')
    album_id = AutoField(column_name='AlbumID')

    class Meta:
        table_name = 'tracks'


def get(album_name_from_input):
    with db as database:
        tracks = Track.select().where(Track.album_id == Albums.select().where(Albums.title == album_name_from_input))
        print(tracks)
    return tracks


print([track.name for track in list(get('A-Sides'))])
