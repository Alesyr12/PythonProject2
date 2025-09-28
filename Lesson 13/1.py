def fibonacci_generator():
    """
    Генераторная функция для бесконечной последовательности чисел Фибоначчи
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main():
    """
    Основная функция программы
    """
    try:
        # Получаем номер числа от пользователя
        n = int(input("Введите номер числа Фибоначчи, до которого нужно выводить последовательность: "))

        if n <= 0:
            print("Пожалуйста, введите положительное число.")
            return

        print(f"Последовательность Фибоначчи до {n}-го числа:")

        # Создаем генератор
        fib_gen = fibonacci_generator()

        # Выводим последовательность
        for i, fib_number in enumerate(fib_gen):
            if i >= n:  # Останавливаемся после n-го числа
                break
            print(f"F({i}) = {fib_number}")

    except ValueError:
        print("Ошибка: пожалуйста, введите целое число.")


def main_with_next():
  
    try:
        n = int(input("Введите номер числа Фибоначчи, до которого нужно выводить последовательность: "))

        if n <= 0:
            print("Пожалуйста, введите положительное число.")
            return

        print(f"Последовательность Фибоначчи до {n}-го числа:")

        fib_gen = fibonacci_generator()

        for i in range(n):
            fib_number = next(fib_gen)
            print(f"F({i}) = {fib_number}")

    except ValueError:
        print("Ошибка: пожалуйста, введите целое число.")


if __name__ == "__main__":
    main()