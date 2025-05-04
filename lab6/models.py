# models.py: Отделяет логику базы данных (модели Client и Transaction) от остального кода. Это упрощает поддержку и повторное использование.
from peewee import Model, CharField, ForeignKeyField, SqliteDatabase

# Подключение к базе данных SQLite
db = SqliteDatabase('C:\\Users\\Mi\\PycharmProjects\\IVTIIbd-21_BUGROV_D.A_RPP_PROJECT\\lab6\\bank.db')

# Модель клиента
class Client(Model):
    name = CharField()  # Поле для имени клиента

    class Meta:
        database = db  # Связь модели с базой данных

# Модель транзакции
class Transaction(Model):
    client = ForeignKeyField(Client, backref='transactions')  # Внешний ключ на клиента
    date_time_str = CharField()  # Дата и время в виде строки
    transaction_type = CharField()  # Тип транзакции (например, "депозит" или "кредит")

    class Meta:
       database = db  # Связь модели с базой данных