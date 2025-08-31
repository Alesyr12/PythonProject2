import re


def load_stop_words(filename):
    """Загружает запрещенные слова из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            stop_words = content.split()
        return stop_words
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


def censor_text(text, stop_words):
    """Заменяет запрещенные слова в тексте на звездочки"""
    if not stop_words:
        return text

    # Создаем регулярное выражение для поиска всех запрещенных слов
    # Игнорируем регистр и ищем слова целиком
    pattern = r'\b(' + '|'.join(re.escape(word) for word in stop_words) + r')\b'

    def replace_with_stars(match):
        word = match.group(0)
        return '*' * len(word)

    # Заменяем все вхождения (с игнорированием регистра)
    censored_text = re.sub(pattern, replace_with_stars, text, flags=re.IGNORECASE)
    return censored_text


def main():
    # Загружаем запрещенные слова
    stop_words = load_stop_words('Задание 4\Стоп-слова.txt')
    if not stop_words:
        print("Не удалось загрузить запрещенные слова. Программа завершена.")
        return

    print("Запрещенные слова:", stop_words)

    # Получаем имя файла от пользователя
    input_filename = input("Введите имя текстового файла для обработки: ")

    try:
        # Читаем текст из файла
        with open(input_filename, 'r', encoding='utf-8') as file:
            text = file.read()

        print("\nИсходный текст:")
        print(text)
        print("\n" + "=" * 50)

        # Цензурируем текст
        censored_text = censor_text(text, stop_words)

        print("Цензурированный текст:")
        print(censored_text)

        # Сохраняем результат в файл (опционально)
        save_option = input("\nСохранить результат в файл? (y/n): ").lower()
        if save_option == 'y':
            output_filename = input("Введите имя выходного файла: ")
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(censored_text)
            print(f"Результат сохранен в файл: {output_filename}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_filename}' не найден.")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")


if __name__ == "__main__":
    main()