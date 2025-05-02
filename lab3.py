import csv
from pathlib import Path
from datetime import datetime

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
        with open(path, 'r', encoding= 'utf-8') as file:
            csv_reader = csv.DictReader(file)
            data_list = []
            for row in csv_reader:
                data_list.append(row)
            return data_list
    except FileNotFoundError:
        print(f"Файл {path} не найден.")
        return []

def sort_by_num(data):
    return sorted(data, key=lambda x: int(x['№']))

def sort_by_name(data):
    return sorted(data, key=lambda x: x['ФИО'])

def filter_by_date(data, date_str):
    date_format = "%Y-%m-%d %H:%M"
    filter_date = datetime.strptime(date_str, date_format)
    return [record for record in data if datetime.strptime(record['дата и время'], date_format) > filter_date]

def save_csv(file_path, data):
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

def add_record(data, new_record):
    data.append(new_record)
    return data

directory = "C:\\Users\\Mi\\PycharmProjects\\PythonProject"
file_count = count_files(directory)
print(f"Количество файлов в директории: {file_count}")
path = directory + "\\data.csv"
print(read_csv(path))
bank_users_list = read_csv(path)

print(sort_by_num(bank_users_list))
print(sort_by_name(bank_users_list))
print(filter_by_date(bank_users_list, "2023-10-03 12:00"))

new_record = {
    '№': '3',
    'ФИО': 'Викторов Виктор Викторович',
    'дата и время': '2020-10-03 12:00',
    'тип обращения': 'кредит'
}
bank_users_list = add_record(bank_users_list, new_record)
save_csv(path, bank_users_list)

