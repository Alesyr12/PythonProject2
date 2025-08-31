import json


def load_data():
    try:
        with open('employees.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        print("Ошибка загрузки файла!")
        return []


def filter_by_language():
    people = load_data()
    if not people:
        return

    language = input("Введите язык программирования: ").strip()
    if not language:
        print("Язык не может быть пустым!")
        return

    found_people = []
    for person in people:
        if 'languages' in person:
            for lang in person['languages']:
                if lang.lower() == language.lower():
                    found_people.append(person)
                    break

    if found_people:
        print(f"\nНашлось {len(found_people)} человек, владеющих {language}:")
        for i, person in enumerate(found_people, 1):
            print(f"{i}. {person['name']} - {', '.join(person['languages'])}")
    else:
        print(f"Не нашлось людей, владеющих {language}")


def filter_by_year():
    people = load_data()
    if not people:
        return

    year_input = input("Введите год рождения для поиска: ")
    if not year_input.isdigit():
        print("Надо ввести число!")
        return

    year = int(year_input)
    good_people = []
    all_heights = 0

    for person in people:
        if 'birthday' in person and 'height' in person:
            birthday_str = person['birthday']
            if '.' in birthday_str:
                parts = birthday_str.split('.')
                if len(parts) == 3 and parts[2].isdigit():
                    birth_year = int(parts[2])
                    if birth_year < year:
                        good_people.append(person)
                        all_heights += person['height']

    if good_people:
        average_height = all_heights / len(good_people)
        print(f"\nНашлось {len(good_people)} человек, родившихся до {year} года:")
        print(f"Средний рост: {average_height:.1f} см")
        for i, person in enumerate(good_people, 1):
            print(f"{i}. {person['name']} - {person['birthday']} - рост: {person['height']} см")
    else:
        print(f"Не нашлось людей, родившихся до {year} года")


def show_all():
    people = load_data()
    if not people:
        return

    print(f"\nВсего сотрудников: {len(people)}")
    for i, person in enumerate(people, 1):
        print(f"{i}. {person['name']}")
        print(f"   ДР: {person['birthday']}, Рост: {person['height']} см")
        print(f"   Вес: {person['weight']} кг, Машина: {'есть' if person['car'] else 'нет'}")
        print(f"   Языки: {', '.join(person['languages'])}")
        print()


def main():
    # Приветствие
    welcome_text = """
    ┌──────────────────────────────────────────────────────────────┐
    │    💻 Здравствуйте, Вас приветствует сервис по найму         │
    │       специалистов в области программирования 💻             │
    └──────────────────────────────────────────────────────────────┘
    """
    print(welcome_text)
    # Дальше идет основное меню...
    while True:
        print("\nМЕНЮ:")
        print("1. Найти по языку программирования")
        print("2. Найти по году рождения")
        print("3. Показать всех сотрудников")
        print("4. Выйти")

        choice = input("Выберите действие: ")
        # ... остальной код

        choice = input("Выберите действие (1-4): ").strip()

        if choice == "1":
            filter_by_language()
        elif choice == "2":
            filter_by_year()
        elif choice == "3":
            show_all()
        elif choice == "4":
            goodbye_text = """
╔══════════════════════════════════════════════╗
║           🎉 До свидания! 🎉                 ║
║      Спасибо за использование сервиса!       ║
╚══════════════════════════════════════════════╝
"""
            print(goodbye_text)
            break
        else:
            print("Неправильный выбор! Введите число от 1 до 4")

        # Пауза перед следующим меню
        input("\nНажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    main()