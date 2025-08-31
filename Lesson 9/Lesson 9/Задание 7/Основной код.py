# Очень простой шифр Цезаря
# Без функций, все в main

# Пытаемся открыть файл
try:
    file = open("text.txt", "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
except:
    print("Не могу найти файл text.txt!")
    exit()

print("Начинаем шифрование...")
print("=" * 30)

# Создаем список для результата
result_lines = []

# Обрабатываем каждую строку
line_number = 1
for line in lines:
    original = line.strip()
    encrypted = ""
    shift = line_number  # Сдвиг = номер строки

    # Обрабатываем каждый символ в строке
    for char in original:
        if 'A' <= char <= 'Z':  # Большая буква
            # Сдвигаем и учитываем, что после Z идет A
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted += new_char
        elif 'a' <= char <= 'z':  # Маленькая буква
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted += new_char
        else:
            # Не буква - оставляем как есть
            encrypted += char

    # Добавляем в результат
    result_lines.append(encrypted)

    # Показываем процесс
    print(f"Строка {line_number}:")
    print(f"Сдвиг: {shift}")
    print(f"Было:  {original}")
    print(f"Стало: {encrypted}")
    print("-" * 20)

    line_number += 1

# Записываем результат
try:
    output_file = open("result.txt", "w", encoding="utf-8")
    for line in result_lines:
        output_file.write(line + "\n")
    output_file.close()
    print("Успешно! Результат в result.txt")
except:
    print("Ошибка при записи файла!")