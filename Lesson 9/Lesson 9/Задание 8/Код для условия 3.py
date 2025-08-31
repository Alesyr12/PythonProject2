import json


def add_employee_simple():
    """
    Простая функция для добавления сотрудника
    """
    print("Добавление нового сотрудника")
    print("---------------------------")

    # Создаем словарь для сотрудника
    new_employee = {}

    # Запрашиваем данные
    new_employee['name'] = input("Введите Имя и Фамилию: ")
    new_employee['birthday'] = input("Введите дату рождения: ")
    new_employee['height'] = input("Введите рост: ")
    new_employee['weight'] = input("Введите вес: ")
    new_employee['car'] = input("Введите наличие машины (True or False): ")
    new_employee['languages'] = input("Введите язык программирования: ")
    # Читаем существующий файл
    try:
        with open('employees.json', 'r', encoding='utf-8') as f:
            employees = json.load(f)
    except:
        # Если файла нет или он пустой, создаем новый список
        employees = []

    # Добавляем нового сотрудника
    employees.append(new_employee)

    # Сохраняем обратно
    with open('employees.json', 'w', encoding='utf-8') as f:
        json.dump(employees, f, ensure_ascii=False, indent=2)

    print("Сотрудник добавлен!")


# Запускаем
add_employee_simple()