def sum_numbers_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

            total_sum = 0
            current_number = ''

            # Проходим по каждому символу в файле
            for char in content:
                if char.isdigit():
                    # Если символ - цифра, добавляем к текущему числу
                    current_number += char
                else:
                    # Если символ не цифра, добавляем текущее число к сумме
                    if current_number:
                        total_sum += int(current_number)
                        current_number = ''

            # Добавляем последнее число, если файл заканчивается цифрой
            if current_number:
                total_sum += int(current_number)

            return total_sum

    except FileNotFoundError:
        print(f"❌ Ошибка: Файл '{filename}' не найден!")
        return None
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        return None


# Основная программа
filename = 'nubers.txt'
result = sum_numbers_in_file(filename)

if result is not None:
    print(f"📊 Сумма всех чисел в файле '{filename}': {result}")