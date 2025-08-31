import json


def main():
    # Пробуем открыть файл с данными
    try:
        with open('employees.json', 'r', encoding='utf-8') as file:
            people = json.load(file)
    except FileNotFoundError:
        print("Файл employees.json не найден!")
        return
    except:
        print("Какая-то ошибка с файлом!")
        return

    # Спросим у пользователя год
    year_input = input("Введите год рождения для поиска: ")

    # Проверим, что ввели число
    if not year_input.isdigit():
        print("Надо ввести число!")
        return

    year = int(year_input)

    # Будем собирать подходящих людей
    good_people = []
    all_heights = 0
    count = 0

    # Перебираем всех сотрудников
    for person in people:
        # Проверяем, есть ли у человека день рождения и рост
        if 'birthday' in person and 'height' in person:
            # Получаем дату рождения
            birthday_str = person['birthday']

            # Пробуем понять дату (формат DD.MM.YYYY)
            if '.' in birthday_str:
                parts = birthday_str.split('.')
                if len(parts) == 3 and parts[2].isdigit():
                    birth_year = int(parts[2])

                    # Проверяем год рождения
                    if birth_year < year:
                        good_people.append(person)
                        all_heights += person['height']
                        count += 1
                else:
                    print(f"Странная дата у {person['name']}: {birthday_str}")
            else:
                print(f"Непонятная дата у {person['name']}: {birthday_str}")

    # Если нашли людей
    if count > 0:
        # Считаем средний рост
        average_height = all_heights / count

        print(f"\nНашлось {count} человек, родившихся до {year} года:")
        print("\nСписок:")

        for i, person in enumerate(good_people, 1):
            print(f"{i}. {person['name']}")
            print(f"   День рождения: {person['birthday']}")
            print(f"   Рост: {person['height']} см")
            print(f"   Вес: {person['weight']} кг")
            print(f"   Машина: {'есть' if person['car'] else 'нет'}")
            print(f"   Языки: {', '.join(person['languages'])}")
            print()
    else:
        print(f"\nНе нашлось людей, родившихся до {year} года")

    print(f"Их средний рост: {average_height:.1f} см")

# Запускаем программу
if __name__ == "__main__":
    main()