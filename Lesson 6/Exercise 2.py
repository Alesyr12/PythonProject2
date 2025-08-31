
# Функция для рекурсивного метода
def decimal_to_binary_recursive(n):
    if n <= 0:
        return "0" if n == 0 \
            else ""
    return decimal_to_binary_recursive(n // 2) + str(n % 2)

# Пользователь сам вводит число
try:
    num = int(input("Введите число в десятичной системе: "))
    # Число пользователя проходит через вышеуказанную функцию
    recursive_result = decimal_to_binary_recursive(num)
    print(f"Число в двоичной системе: {recursive_result if recursive_result else '0'}")

# Если пользователь ввел дробно число - выводим ошибку
except ValueError:
    print("Неверно! Нужно ввести целое число.")