import csv


def find_employee_with_table():
  
    print("🔍 Поиск сотрудника по имени")
    print("=" * 50)

    search_name = input("Введите имя для поиска: ").strip().lower()

    try:
        with open('employees.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            employees = list(reader)

        # Фильтруем по имени
        results = [emp for emp in employees if emp['name'].lower() == search_name]

        if results:
            print(f"\n✅ Найдено: {len(results)} сотрудник(ов)")
            print("=" * 50)

            # Выводим в виде простой таблицы
            headers = list(results[0].keys())

            # Заголовок таблицы
            header_line = " | ".join(f"{h:15}" for h in headers)
            print(header_line)
            print("-" * len(header_line))

            # Данные
            for emp in results:
                row_line = " | ".join(f"{str(emp[h]):15}" for h in headers)
                print(row_line)

        else:
            print(f"\n❌ Сотрудники с именем '{search_name}' не найдены")

    except FileNotFoundError:
        print("❌ Файл не найден")
    except Exception as e:
        print(f"❌ Ошибка: {e}")


find_employee_with_table()