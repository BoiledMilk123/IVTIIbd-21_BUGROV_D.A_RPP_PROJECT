from datetime import datetime
import csv
from pathlib import Path

def count_files(path):
    try:
        p = Path(path)
        files = [f for f in p.iterdir() if f.is_file()]
        return len(files)
    except FileNotFoundError:
        print(f"Директория {path} не найдена.")
        return 0

def read_csv(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data_list = []
            for row in csv_reader:
                data_list.append(row)
            return data_list
    except FileNotFoundError:
        print(f"Файл {path} не найден.")
        return []

def load_clients_and_transactions(csv_path):
    data = read_csv(csv_path)
    clients = {}
    for row in data:
        name = row['ФИО']
        date_time_str = row['дата и время']
        transaction_type = row['тип обращения']
        if name not in clients:
            clients[name] = Client(name)
        client = clients[name]
        if transaction_type == "депозит":
            transaction = Deposit(client, date_time_str)
        elif transaction_type == "кредит":
            transaction = Credit(client, date_time_str)
        else:
            raise ValueError(f"Неверный тип обращения: {transaction_type}")
        client.add_transaction(transaction)
    return list(clients.values())



class Client:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def __iter__(self):
        return iter(self.transactions)

    def __getitem__(self, index):
        return self.transactions[index]

    def __repr__(self):
        return f"Клиент({self.name})"

    def transactions_by_date(self):
        for transaction in sorted(self.transactions, key = lambda x: x.date_time_str):
            yield transaction

    @staticmethod
    def from_names(names_list):
        return [Client(name) for name in names_list]

class Transaction:
    ALLOWED_TYPES = ["депозит", "кредит"]

    def __init__(self, client, date_time_str, transaction_type):
        self.client = client
        self.date_time_str = date_time_str
        self.transaction_type = transaction_type

    def __setattr__(self, name, value):
        if name == "transaction_type" and value not in self.ALLOWED_TYPES:
            raise ValueError(f"Неверный тип транзакции '{value}'")
        super().__setattr__(name, value)

    def __repr__(self):
        return f"Транзакция({self.client.name}, {self.date_time_str}, {self.transaction_type})"

class Deposit(Transaction):
    def __init__(self,client, date_time_str):
        super().__init__(client, date_time_str, "депозит")

class Credit(Transaction):
    def __init__(self,client, date_time_str):
        super().__init__(client, date_time_str, "кредит")

def sort_clients_by_name(clients):
    return sorted(clients, key=lambda c: c.name)

def filter_transactions_by_date(client, date_str):
    date_format = "%Y-%m-%d %H:%M"
    filter_date = datetime.strptime(date_str, date_format)
    return [trans for trans in client.transactions
            if datetime.strptime(trans.date_time_str, date_format) > filter_date]



if __name__ == "__main__":
    # Создаем клиентов
    client1 = Client("Сидоров Сидор Сидорович")
    client2 = Client("Алексей Алексеевич Алексеев")

    # Создаем транзакции с использованием дочерних классов
    deposit1 = Deposit(client1, "2023-10-03 12:00")
    credit1 = Credit(client2, "2023-10-04 15:00")

    # Добавляем транзакции к клиентам
    client1.add_transaction(deposit1)
    client2.add_transaction(credit1)

    # Выводим транзакции клиента 1
    print(f"Транзакции клиента {client1.name}:")
    for trans in client1:
        print(trans)  # Вывод: Транзакция(Сидоров Сидор Сидорович, 2023-10-03 12:00, депозит)

    # Выводим транзакции клиента 2
    print(f"\nТранзакции клиента {client2.name}:")
    for trans in client2:
        print(trans)  # Вывод: Транзакция(Алексей Алексеевич Алексеев, 2023-10-04 15:00, кредит)

    # Используем генератор для вывода транзакций по дате для клиента 1
    print("\nТранзакции клиента 1 по дате:")
    for trans in client1.transactions_by_date():
        print(trans)

    csv_path = "C:\\Users\\Mi\\PycharmProjects\\PythonProject\\data.csv"
    clients = load_clients_and_transactions(csv_path)

    for client in clients:
        print(f"Клиент: {client.name}")
        for transaction in client.transactions:
            print(f"  {transaction}")