def simple_cyclic_generator():
    """
    Генераторная функция специально для последовательности 1-2-3
    """
    sequence = [1, 2, 3]
    index = 0
    while True:
        yield sequence[index]
        index = (index + 1) % 3  # 3 - длина последовательности


def main_simple():
    """
    Упрощенная версия основной функции
    """
    try:
        count = int(input("Введите количество чисел для вывода: "))

        if count <= 0:
            print("Пожалуйста, введите положительное число.")
            return

        print(f"Циклическая последовательность 1-2-3 из {count} чисел:")

        gen = simple_cyclic_generator()

        for i in range(count):
            print(next(gen), end="")
            if i < count - 1:
                print("-", end="")
        print()

    except ValueError:
        print("Ошибка: пожалуйста, введите целое число.")


main_simple()