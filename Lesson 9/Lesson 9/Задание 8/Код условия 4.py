import csv
import os


def add_employee_smart():
    """
    Умное добавление сотрудника с чтением существующих заголовков
    """
    print("🎯 Добавление сотрудника в CSV")
    print("=" * 40)

    filename = "employees.csv"

    # Проверяем существует ли файл и читаем заголовки
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = next(reader, None)
                print(f"📋 Обнаружены поля: {headers}")
        except:
            headers = ['name', 'birthday', 'height', 'weight', 'car', 'languages']
    else:
        headers = ['name', 'birthday', 'height', 'weight', 'car', 'languages']
        print("📋 Будет создан новый файл")

    # Ввод данных
    print("\n📝 Введите данные:")
    print("-" * 25)

    employee_data = {}
    for field in headers:
        value = input(f"{field}: ").strip()
        employee_data[field] = value

    # Сохранение
    try:
        with open(filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)

            # Если файл пустой, пишем заголовки
            if os.path.getsize(filename) == 0:
                writer.writeheader()

            # Пишем данные
            writer.writerow(employee_data)

        print(f"✅ Сотрудник добавлен в {filename}")

    except Exception as e:
        print(f"❌ Ошибка: {e}")


add_employee_smart()