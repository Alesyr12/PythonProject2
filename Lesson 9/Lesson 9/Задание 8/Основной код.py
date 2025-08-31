import json
import csv


# Простая конвертация без сложных проверок
def simple_json_to_csv():
    # Читаем JSON
    try:
        with open('employees.json', 'r') as f:
            data = json.load(f)
        print("JSON файл прочитан")
    except:
        print("Не могу прочитать JSON файл")
        return

    # Проверяем что данные есть
    if not data:
        print("Нет данных")
        return

    # Предполагаем что данные это список словарей
    if type(data) is list:
        # Берем ключи из первого элемента
        keys = data[0].keys()
    else:
        print("Данные должны быть списком")
        return

    # Создаем CSV
    try:
        with open('output.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)

            # Пишем заголовки
            writer.writeheader()

            # Пишем все строки
            for item in data:
                writer.writerow(item)

        print("CSV файл создан!")

    except:
        print("Ошибка при создании CSV")


# Запускаем
simple_json_to_csv()

