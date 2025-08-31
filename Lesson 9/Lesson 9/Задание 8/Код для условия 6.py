import json
import os


def load_employees_from_json(file_path):
    """
    Загружает данные сотрудников из JSON-файла.

    Args:
        file_path (str): Путь к JSON-файлу

    Returns:
        list: Список сотрудников или пустой список при ошибке
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            employees = json.load(file)
        return employees
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Файл '{file_path}' содержит некорректный JSON.")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при чтении файла: {e}")
        return []


def filter_by_language(employees_list, programming_language):
    """
    Фильтрует список сотрудников по заданному языку программирования.

    Args:
        employees_list (list): Список словарей с данными сотрудников.
        programming_language (str): Язык программирования для фильтрации.

    Returns:
        list: Список сотрудников, владеющих указанным языком.
    """
    if not employees_list:
        return []

    filtered_employees = []
    language_lower = programming_language.lower()

    for employee in employees_list:
        # Проверяем, есть ли ключ 'languages' в словаре сотрудника
        if "languages" in employee and isinstance(employee["languages"], list):
            employee_languages_lower = [lang.lower() for lang in employee["languages"]]
            if language_lower in employee_languages_lower:
                filtered_employees.append(employee)

    return filtered_employees


def display_results(employees, programming_language):
    """
    Выводит результаты поиска в удобном формате.

    Args:
        employees (list): Список найденных сотрудников
        programming_language (str): Язык, по которому проводился поиск
    """
    if not employees:
        print(f"\nНет сотрудников, владеющих языком '{programming_language}'.")
        return

    print(f"\nСотрудники, владеющие языком '{programming_language}':")
    print("-" * 60)

    for i, employee in enumerate(employees, 1):
        print(f"{i}. {employee['name']}")
        print(f"   Владеет: {', '.join(employee['languages'])}")
        print()


def main():
    # Путь к JSON-файлу (можно изменить на нужный)
    json_file_path = "employees.json"

    # Загрузка данных из JSON
    employees = load_employees_from_json(json_file_path)

    if not employees:
        print("Не удалось загрузить данные сотрудников. Программа завершена.")
        return

    print("Данные сотрудников успешно загружены из файла.")
    print(f"Всего сотрудников в базе: {len(employees)}")
    print()

    # Запрос языка у пользователя
    target_language = input("Введите язык программирования для поиска: ").strip()

    # Проверка на пустой ввод
    if not target_language:
        print("Вы не ввели язык программирования.")
        return

    # Вызов функции фильтрации
    result = filter_by_language(employees, target_language)

    # Вывод результатов
    display_results(result, target_language)


# Запуск программы
if __name__ == "__main__":
    main()