def encrypt(text, shift=3):
    """
    text - наш текст на английском языке, который мы шифруем
    shift - реализует метод шифра Цезаря (происходит сдвиг на 3 символа в право)
    """
    encrypted = []
    for char in text:
        if char.isalpha():
            # Определяем базу для верхнего или нижнего регистра
            base = ord('A') if char.isupper() else ord('a')
            # Происходит вычисление новых символов уже со сдвигом на 3 в право
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted.append(new_char)
        else:
            # Символы не входящие в алфафит остаются без зменений позиции
            encrypted.append(char)
    return ''.join(encrypted)


def decrypt(text, shift=3):
    """
    text - текст, который будем расшифровывать
    shift - тут происходит уже расшифровка шифром Цезаря (сдвигаемся на 3 символа влево)
    """
    return encrypt(text, -shift)


# Окна для ввода текста нашим пользователем
print("*" * 79)
print("ВАС ПРИВЕСТВУЕТ СЕРВИС ПО ШИФРОВАНИЯ И ДЕШИФРОВАНИЮ")
print("*" * 79)

if __name__ == "__main__":
    print("Выберите действие:")
    print("1 - Зашифровать сообщение")
    print("2 - Расшифровать сообщение")

    choice = input("Ваш выбор (1 или 2): ")
    text = input("Введите сообщение: ")

    if choice == '1':
        result = encrypt(text)
        print("Зашифрованное сообщение:", result)
    elif choice == '2':
        result = decrypt(text)
        print("Расшифрованное сообщение:", result)
    else:
        print("Некорректный выбор")