import json
import csv


def save_json_to_csv(json_filename, csv_filename):
    """
    Сохраняет данные из JSON в CSV файл
    Работает с любым количеством данных
    """
    try:
        # Читаем JSON файл
        print(f"Читаем файл: {json_filename}")
        with open(json_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        print(f"Успешно прочитали JSON")

        # Проверяем тип данных
        if isinstance(data, dict):
            # Если один объект - делаем список из одного элемента
            data = [data]
            print("Обнаружен один объект, преобразуем в список")
        elif not isinstance(data, list):
            print("Ошибка: данные должны быть списком или словарем")
            return False

        # Проверяем что есть данные
        if len(data) == 0:
            print("Файл пустой")
            return False

        print(f"Найдено записей: {len(data)}")

        # Получаем все уникальные заголовки из всех записей
        all_headers = set()
        for item in data:
            if isinstance(item, dict):
                all_headers.update(item.keys())

        headers = list(all_headers)
        print(f"Обнаружено полей: {len(headers)}")
        print(f"Поля: {', '.join(headers)}")

        # Записываем в CSV
        print(f"Записываем в CSV: {csv_filename}")
        with open(csv_filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)

            # Заголовки
            writer.writeheader()
            print("Заголовки записаны")

            # Данные
            count = 0
            for item in data:
                if isinstance(item, dict):
                    writer.writerow(item)
                    count += 1

            print(f"Записали записей: {count}")

        print("✅ Готово! CSV файл создан")
        return True

    except FileNotFoundError:
        print(f"❌ Ошибка: Файл {json_filename} не найден")
        return False
    except json.JSONDecodeError:
        print("❌ Ошибка: Файл не в формате JSON")
        return False
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        return False


# Пример использования
if __name__ == "__main__":
    # Конвертируем
    success = save_json_to_csv("employees.json", "employees.csv")

    if success:
        print("🎉 Программа завершилась успешно!")
    else:
        print("😞 Программа завершилась с ошибкой")